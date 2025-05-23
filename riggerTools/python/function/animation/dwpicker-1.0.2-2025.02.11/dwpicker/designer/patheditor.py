import os
import json
from copy import deepcopy
from functools import partial

from dwpicker.pyside import QtWidgets, QtCore, QtGui
from maya import cmds

from dwpicker.geometry import (
    distance, get_global_rect, grow_rect, path_symmetry)
from dwpicker.qtutils import icon
from dwpicker.interactionmanager import InteractionManager
from dwpicker.interactive import SelectionSquare, Manipulator
from dwpicker.optionvar import (
    LAST_OPEN_DIRECTORY, SHAPE_PATH_ROTATION_STEP_ANGLE, save_optionvar)
from dwpicker.painting import (
    draw_selection_square, draw_manipulator, draw_tangents,
    draw_world_coordinates)
from dwpicker.path import get_open_directory
from dwpicker.qtutils import get_cursor
from dwpicker.selection import get_selection_mode
from dwpicker.shapepath import (
    offset_tangent, offset_path, auto_tangent, create_polygon_path,
    rotate_path)
from dwpicker.transform import (
    Transform, resize_path_with_reference, resize_rect_with_direction)
from dwpicker.viewport import ViewportMapper


class PathEditor(QtWidgets.QWidget):
    pathEdited = QtCore.Signal()

    def __init__(self, parent=None):
        super(PathEditor, self).__init__(parent)
        self.setWindowTitle('Shape path editor')
        self.buffer_path = None
        self.rotate_center = None

        self.canvas = PathEditorCanvas()
        self.canvas.pathEdited.connect(self.pathEdited.emit)

        export_path = QtWidgets.QAction(icon('save.png'), 'Export path', self)
        export_path.triggered.connect(self.export_path)

        import_path = QtWidgets.QAction(icon('open.png'), 'Import path', self)
        import_path.triggered.connect(self.import_path)

        delete = QtWidgets.QAction(icon('delete.png'), 'Delete vertex', self)
        delete.triggered.connect(self.canvas.delete)

        smooth_tangent = QtWidgets.QAction(
            icon('tangent.png'), 'Smooth tangents', self)
        smooth_tangent.triggered.connect(self.canvas.smooth_tangents)

        break_tangent = QtWidgets.QAction(
            icon('tangentbreak.png'), 'Break tangents', self)
        break_tangent.triggered.connect(self.canvas.break_tangents)

        hsymmetry = QtWidgets.QAction(
            icon('h_symmetry.png'), 'Mirror horizontally', self)
        hsymmetry.triggered.connect(partial(self.canvas.symmetry, True))

        vsymmetry = QtWidgets.QAction(
            icon('v_symmetry.png'), 'Mirror vertically', self)
        vsymmetry.triggered.connect(partial(self.canvas.symmetry, False))

        center_path = QtWidgets.QAction(
            icon('frame.png'), 'Center path', self)
        center_path.triggered.connect(partial(self.canvas.center_path))
        center_path_button = QtWidgets.QToolButton()
        center_path_button.setDefaultAction(center_path)

        self.angle = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.angle.setMinimum(0)
        self.angle.setMaximum(360)
        self.angle.sliderPressed.connect(self.start_rotate)
        self.angle.sliderReleased.connect(self.end_rotate)
        self.angle.valueChanged.connect(self.rotate)

        self.angle_step = QtWidgets.QSpinBox()
        self.angle_step.setToolTip('Step')
        self.angle_step.setMinimum(0)
        self.angle_step.setMaximum(90)
        value = cmds.optionVar(query=SHAPE_PATH_ROTATION_STEP_ANGLE)
        self.angle_step.setValue(value)
        function = partial(save_optionvar, SHAPE_PATH_ROTATION_STEP_ANGLE)
        self.angle_step.valueChanged.connect(function)

        polygon = QtWidgets.QAction(
            icon('polygon.png'), 'Create Polygon', self)
        polygon.triggered.connect(self.create_polygon)

        toggle = QtWidgets.QAction(icon('dock.png'), 'Dock/Undock', self)
        toggle.triggered.connect(self.toggle_flag)

        self.toolbar = QtWidgets.QToolBar()
        self.toolbar.setIconSize(QtCore.QSize(18, 18))
        self.toolbar.addAction(import_path)
        self.toolbar.addAction(export_path)
        self.toolbar.addSeparator()
        self.toolbar.addAction(polygon)
        self.toolbar.addAction(delete)
        self.toolbar.addSeparator()
        self.toolbar.addAction(smooth_tangent)
        self.toolbar.addAction(break_tangent)
        self.toolbar.addSeparator()
        self.toolbar.addAction(hsymmetry)
        self.toolbar.addAction(vsymmetry)

        toolbar3 = QtWidgets.QHBoxLayout()
        toolbar3.setContentsMargins(0, 0, 0, 0)
        toolbar3.addWidget(center_path_button)
        toolbar3.addStretch()
        toolbar3.addWidget(QtWidgets.QLabel('Rotate: '))
        toolbar3.addWidget(self.angle)
        toolbar3.addWidget(self.angle_step)

        self.toolbar2 = QtWidgets.QToolBar()
        self.toolbar2.setIconSize(QtCore.QSize(18, 18))
        self.toolbar2.addAction(toggle)

        toolbars = QtWidgets.QHBoxLayout()
        toolbars.setContentsMargins(0, 0, 0, 0)
        toolbars.addWidget(self.toolbar)
        toolbars.addStretch()
        toolbars.addWidget(self.toolbar2)

        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addLayout(toolbars)
        layout.addWidget(self.canvas)
        layout.addLayout(toolbar3)

    def export_path(self):
        directory = get_open_directory()
        filename = QtWidgets.QFileDialog.getSaveFileName(
            self, 'Export shape', directory, '*.dws')
        if not filename[0]:
            return
        save_optionvar(LAST_OPEN_DIRECTORY, os.path.dirname(filename[0]))
        with open(filename[0], 'w') as f:
            json.dump(self.canvas.path, f, indent=2)

    def import_path(self):
        directory = get_open_directory()
        filename = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Import shape', directory, '*.dws')
        if not filename[0]:
            return
        save_optionvar(LAST_OPEN_DIRECTORY, os.path.dirname(filename[0]))
        with open(filename[0], 'r') as f:
            path = json.load(f)
        self.canvas.set_path(path)
        self.pathEdited.emit()

    def start_rotate(self):
        self.buffer_path = deepcopy(self.canvas.path)
        if not self.canvas.selection:
            self.rotate_center = (0, 0)
        elif len(self.canvas.selection) == 1:
            index = self.canvas.selection[0]
            self.rotate_center = self.buffer_path[index]['point']
        else:
            point = self.canvas.manipulator.rect.center()
            self.rotate_center = point.toTuple()

    def end_rotate(self):
        self.buffer_path = None
        self.rotate_center = None
        self.pathEdited.emit()
        self.angle.blockSignals(True)
        self.angle.setValue(0)
        self.angle.blockSignals(False)

    def rotate(self, value):
        if self.buffer_path is None:
            self.start_rotate()

        step_size = self.angle_step.value()
        value = round(value / step_size) * step_size
        if 1 < len(self.canvas.selection):
            path = deepcopy(self.buffer_path)
            points = [self.buffer_path[i] for i in self.canvas.selection]
            rotated_path = rotate_path(points, value, self.rotate_center)
            for i, point in zip(self.canvas.selection, rotated_path):
                path[i] = point
        else:
            path = rotate_path(self.buffer_path, value, self.rotate_center)
        if path is None:
            return

        self.canvas.path = path
        if self.canvas.selection:
            points = [
                QtCore.QPointF(*path[i]['point'])
                for i in self.canvas.selection]
            self.canvas.update_manipulator_rect(points)
        self.canvas.update()

    def create_polygon(self):
        edges, result = QtWidgets.QInputDialog.getInt(
            self, 'Polygon', 'Number of edges', value=3, minValue=3,
            maxValue=25)
        if not result:
            return

        path = create_polygon_path(radius=45, n=edges)
        self.canvas.set_path(path)
        self.pathEdited.emit()

    def toggle_flag(self):
        point = self.mapToGlobal(self.rect().topLeft())
        state = not self.windowFlags() & QtCore.Qt.Tool
        self.setWindowFlag(QtCore.Qt.Tool, state)
        self.show()
        if state:
            self.resize(400, 400)
            self.move(point)
        self.canvas.focus()

    def set_options(self, options):
        if options is None:
            self.canvas.set_path(None)
            return
        self.canvas.set_path(options['shape.path'] or [])

    def path(self):
        return self.canvas.path

    def path_rect(self):
        return get_global_rect(
            [QtCore.QPointF(*p['point']) for p in self.canvas.path])


class PathEditorCanvas(QtWidgets.QWidget):
    pathEdited = QtCore.Signal()

    def __init__(self, parent=None):
        super(PathEditorCanvas, self).__init__(parent)
        self.viewportmapper = ViewportMapper()
        self.viewportmapper.viewsize = self.size()
        self.selection_square = SelectionSquare()
        self.manipulator = Manipulator(self.viewportmapper)
        self.transform = Transform()
        self.selection = PointSelection()
        self.interaction_manager = InteractionManager()
        self.setMouseTracking(True)
        self.path = []

    def sizeHint(self):
        return QtCore.QSize(300, 200)

    def mousePressEvent(self, event):
        if not self.path:
            return

        cursor = self.viewportmapper.to_units_coords(get_cursor(self))
        self.transform.direction = self.manipulator.get_direction(event.pos())
        self.current_action = self.get_action()
        if self.current_action and self.current_action[0] == 'move point':
            self.selection.set([self.current_action[1]])
            self.update_manipulator_rect()
        if self.manipulator.rect is not None:
            self.transform.set_rect(self.manipulator.rect)
            self.transform.reference_rect = QtCore.QRectF(self.manipulator.rect)
            self.transform.set_reference_point(cursor)

        has_shape_hovered = bool(self.current_action)
        self.interaction_manager.update(
            event, pressed=True,
            has_shape_hovered=has_shape_hovered,
            dragging=has_shape_hovered)
        self.selection_square.clicked(cursor)
        self.update()

    def get_action(self):
        if not self.path:
            return

        cursor = self.viewportmapper.to_units_coords(get_cursor(self))
        if self.manipulator.rect and self.manipulator.rect.contains(cursor):
            return 'move points', None
        direction = self.manipulator.get_direction(get_cursor(self))
        if direction:
            return 'resize points', direction
        tolerance = self.viewportmapper.to_units(5)
        for i, data in enumerate(self.path):
            point = QtCore.QPointF(*data['point'])
            if distance(point, cursor) < tolerance:
                return 'move point', i
            if data['tangent_in']:
                point = QtCore.QPointF(*data['tangent_in'])
                if distance(point, cursor) < tolerance:
                    return 'move in', i
            if data['tangent_out']:
                point = QtCore.QPointF(*data['tangent_out'])
                if distance(point, cursor) < tolerance:
                    return 'move out', i
        index = is_point_on_path_edge(self.path, cursor, tolerance)
        if index is not None:
            return 'create point', index

    def mouseMoveEvent(self, event):
        if not self.path:
            return

        cursor = self.viewportmapper.to_units_coords(get_cursor(self)).toPoint()
        if self.interaction_manager.mode == InteractionManager.NAVIGATION:
            offset = self.interaction_manager.mouse_offset(event.pos())
            if offset is not None:
                origin = self.viewportmapper.origin - offset
                self.viewportmapper.origin = origin

        elif self.interaction_manager.mode == InteractionManager.SELECTION:
            self.selection_square.handle(cursor)

        elif self.interaction_manager.mode == InteractionManager.DRAGGING:
            if not self.current_action:
                return self.update()

            offset = self.interaction_manager.mouse_offset(event.pos())
            if not offset:
                return self.update()

            offset = QtCore.QPointF(
                self.viewportmapper.to_units(offset.x()),
                self.viewportmapper.to_units(offset.y()))

            if self.current_action[0] == 'move points':
                offset_path(self.path, offset, self.selection)
                self.update_manipulator_rect()

            elif self.current_action[0] == 'resize points':
                resize_rect_with_direction(
                    self.transform.rect, cursor,
                    self.transform.direction)
                path = (
                    [self.path[i] for i in self.selection] if
                    self.selection else self.path)
                resize_path_with_reference(
                    path,
                    self.transform.reference_rect,
                    self.transform.rect)
                rect = self.transform.rect
                self.transform.reference_rect.setTopLeft(rect.topLeft())
                self.transform.reference_rect.setSize(rect.size())
                self.manipulator.set_rect(self.transform.rect)

            elif self.current_action[0] == 'move point':
                offset_path(self.path, offset, [self.current_action[1]])

            elif self.current_action and self.current_action[0] == 'move in':
                move_tangent(
                    point=self.path[self.current_action[1]],
                    tangent_in_moved=True,
                    offset=offset,
                    lock=not self.interaction_manager.ctrl_pressed)

            elif self.current_action[0] == 'move out':
                move_tangent(
                    point=self.path[self.current_action[1]],
                    tangent_in_moved=False,
                    offset=offset,
                    lock=not self.interaction_manager.ctrl_pressed)

            elif self.current_action[0] == 'create point':
                self.interaction_manager.mouse_offset(event.pos())
                point = {
                    'point': [cursor.x(), cursor.y()],
                    'tangent_in': None,
                    'tangent_out': None}
                index = self.current_action[1] + 1
                self.path.insert(index, point)
                self.autotangent(index)
                self.current_action = 'move point', index
                self.selection.set([index])
                self.update_manipulator_rect()

        self.update()

    def move_point(self, i, offset):
        self.path[i]['point'][0] += offset.x()
        self.path[i]['point'][1] += offset.y()
        point = self.path[i]['tangent_in']
        if point:
            point[0] += offset.x()
            point[1] += offset.y()
        point = self.path[i]['tangent_out']
        if point:
            point[0] += offset.x()
            point[1] += offset.y()

    def mouseReleaseEvent(self, event):
        if not self.path:
            return

        if self.current_action:
            self.pathEdited.emit()

        if self.interaction_manager.mode == InteractionManager.SELECTION:
            self.select()

        self.selection_square.release()
        self.interaction_manager.update(
            event, pressed=False, has_shape_hovered=False, dragging=False)
        self.update()

    def select(self):
        shift = self.interaction_manager.shift_pressed
        ctrl = self.interaction_manager.ctrl_pressed
        self.selection.mode = get_selection_mode(shift=shift, ctrl=ctrl)
        rect = self.selection_square.rect
        points = []
        indexes = []
        for i, p in enumerate(self.path):
            point = QtCore.QPointF(*p['point'])
            if rect.contains(point):
                indexes.append(i)
                points.append(point)
        self.selection.set(indexes)
        self.update_manipulator_rect()

    def update_manipulator_rect(self, points=None):
        if points is None:
            points = [
                QtCore.QPointF(*self.path[i]['point'])
                for i in self.selection]
        if len(points) < 2:
            self.manipulator.set_rect(None)
            return

        rect = get_global_rect(points)
        rect.setHeight(max(rect.height(), .5))
        rect.setWidth(max(rect.width(), .5))
        self.manipulator.set_rect(rect)

    def wheelEvent(self, event):
        # To center the zoom on the mouse, we save a reference mouse position
        # and compare the offset after zoom computation.
        factor = .25 if event.angleDelta().y() > 0 else -.25
        self.zoom(factor, event.pos())
        self.update()

    def resizeEvent(self, event):
        self.viewportmapper.viewsize = self.size()
        size = (event.size() - event.oldSize()) / 2
        offset = QtCore.QPointF(size.width(), size.height())
        self.viewportmapper.origin -= offset
        self.update()

    def zoom(self, factor, reference):
        abspoint = self.viewportmapper.to_units_coords(reference)
        if factor > 0:
            self.viewportmapper.zoomin(abs(factor))
        else:
            self.viewportmapper.zoomout(abs(factor))
        relcursor = self.viewportmapper.to_viewport_coords(abspoint)
        vector = relcursor - reference
        self.viewportmapper.origin = self.viewportmapper.origin + vector

    def paintEvent(self, event):
        if not self.path:
            return

        try:
            painter = QtGui.QPainter(self)
            painter.setPen(QtGui.QPen())
            color = QtGui.QColor('black')
            color.setAlpha(50)
            painter.setBrush(color)
            rect = QtCore.QRect(
                0, 0, self.rect().width() - 1, self.rect().height() - 1)
            painter.drawRect(rect)
            draw_world_coordinates(
                painter, self.rect(), QtGui.QColor('#282828'),
                self.viewportmapper)
            painter.setBrush(QtGui.QBrush())
            draw_shape_path(
                painter, self.path, self.selection, self.viewportmapper)
            draw_tangents(painter, self.path, self.viewportmapper)
            if self.selection_square.rect:
                draw_selection_square(
                    painter, self.selection_square.rect, self.viewportmapper)

            conditions = (
                self.manipulator.rect is not None and
                all(self.manipulator.viewport_handlers()))

            if conditions:
                draw_manipulator(
                    painter, self.manipulator,
                    get_cursor(self), self.viewportmapper)

        finally:
            painter.end()

    def center_path(self):
        qpath = path_to_qpath(self.path, ViewportMapper())
        center = qpath.boundingRect().center()
        offset_path(self.path, -center)
        self.pathEdited.emit()
        self.update_manipulator_rect()
        self.update()

    def delete(self):
        if len(self.path) - len(self.selection) < 3:
            return QtWidgets.QMessageBox.critical(
                self, 'Error', 'Shape must at least contains 3 control points')

        for i in sorted(self.selection, reverse=True):
            del self.path[i]
        self.selection.clear()
        self.update_manipulator_rect()
        self.pathEdited.emit()
        self.update()

    def break_tangents(self):
        for i in self.selection:
            self.path[i]['tangent_in'] = None
            self.path[i]['tangent_out'] = None
        self.pathEdited.emit()
        self.update()

    def smooth_tangents(self):
        if not self.selection:
            return

        for i in self.selection:
            self.autotangent(i)
        self.update()
        self.pathEdited.emit()

    def autotangent(self, i):
        point = self.path[i]['point']
        next_index = i + 1 if i < (len(self.path) - 1) else 0
        next_point = self.path[next_index]['point']
        previous_point = self.path[i - 1]['point']
        tan_in, tan_out = auto_tangent(point, previous_point, next_point)
        self.path[i]['tangent_in'] = tan_in
        self.path[i]['tangent_out'] = tan_out

    def set_path(self, path):
        self.path = path
        self.selection.clear()
        self.manipulator.set_rect(None)
        self.focus()

    def focus(self):
        if not self.path:
            self.update()
            return
        points = [QtCore.QPointF(*p['point']) for p in self.path]
        rect = get_global_rect(points)
        self.viewportmapper.focus(grow_rect(rect, 15))
        self.update()

    def symmetry(self, horizontal=True):
        path = (
            [self.path[i] for i in self.selection] if
            self.selection else self.path)

        if self.manipulator.rect:
            center = self.manipulator.rect.center()
        else:
            points = [QtCore.QPointF(*p['point']) for p in self.path]
            rect = get_global_rect(points)
            center = rect.center()

        path_symmetry(path, center, horizontal=horizontal)
        self.pathEdited.emit()
        self.update()


class PointSelection():
    def __init__(self):
        self.elements = []
        self.mode = 'replace'

    def set(self, elements):
        if self.mode == 'add':
            if elements is None:
                return
            return self.add(elements)
        elif self.mode == 'replace':
            if elements is None:
                return self.clear()
            return self.replace(elements)
        elif self.mode == 'invert':
            if elements is None:
                return
            return self.invert(elements)
        elif self.mode == 'remove':
            if elements is None:
                return
            for element in elements:
                if element in self.elements:
                    self.remove(element)

    def replace(self, elements):
        self.elements = elements

    def add(self, elements):
        self.elements.extend([e for e in elements if e not in self])

    def remove(self, element):
        self.elements.remove(element)

    def invert(self, elements):
        for element in elements:
            if element not in self.elements:
                self.add([element])
            else:
                self.remove(element)

    def clear(self):
        self.elements = []

    def __len__(self):
        return len(self.elements)

    def __bool__(self):
        return bool(self.elements)

    __nonzero__ = __bool__

    def __getitem__(self, i):
        return self.elements[i]

    def __iter__(self):
        return self.elements.__iter__()


def path_to_qpath(path, viewportmapper):
    painter_path = QtGui.QPainterPath()
    start = QtCore.QPointF(*path[0]['point'])
    painter_path.moveTo(viewportmapper.to_viewport_coords(start))
    for i in range(len(path)):
        point = path[i]
        point2 = path[i + 1 if i + 1 < len(path) else 0]
        c1 = QtCore.QPointF(*(point['tangent_out'] or point['point']))
        c2 = QtCore.QPointF(*(point2['tangent_in'] or point2['point']))
        end = QtCore.QPointF(*point2['point'])
        painter_path.cubicTo(
            viewportmapper.to_viewport_coords(c1),
            viewportmapper.to_viewport_coords(c2),
            viewportmapper.to_viewport_coords(end))
    return painter_path


def draw_shape_path(painter, path, selection, viewportmapper):
    painter.setPen(QtCore.Qt.gray)
    painter.drawPath(path_to_qpath(path, viewportmapper))
    rect = QtCore.QRectF(0, 0, 5, 5)
    for i, point in enumerate(path):
        center = QtCore.QPointF(*point['point'])
        rect.moveCenter(viewportmapper.to_viewport_coords(center))
        painter.setBrush(QtCore.Qt.white if i in selection else QtCore.Qt.NoBrush)
        painter.drawRect(rect)


def is_point_on_path_edge(path, cursor, tolerance=3):
    stroker = QtGui.QPainterPathStroker()
    stroker.setWidth(tolerance * 2)

    for i in range(len(path)):
        point = path[i]
        painter_path = QtGui.QPainterPath()
        painter_path.moveTo(QtCore.QPointF(*point['point']))

        point2 = path[i + 1 if i + 1 < len(path) else 0]
        c1 = QtCore.QPointF(*(point['tangent_out'] or point['point']))
        c2 = QtCore.QPointF(*(point2['tangent_in'] or point2['point']))
        end = QtCore.QPointF(*point2['point'])
        painter_path.cubicTo(c1, c2, end)

        stroke = stroker.createStroke(painter_path)
        if stroke.contains(cursor):
            return i

    return None


def move_tangent(point, tangent_in_moved, offset, lock):
    center_point = point['point']
    tangent_in = point['tangent_in' if tangent_in_moved else 'tangent_out']
    tangent_out = point['tangent_out' if tangent_in_moved else 'tangent_in']
    offset = offset.x(), offset.y()
    tangent_in, tangent_out = offset_tangent(
        tangent_in, tangent_out, center_point, offset, lock)
    point['tangent_in'if tangent_in_moved else 'tangent_out'] = tangent_in
    point['tangent_out'if tangent_in_moved else 'tangent_in'] = tangent_out


if __name__ == '__main__':
    try:
        se.close()
    except:
        pass
    from dwpicker.qtutils import maya_main_window
    se = PathEditor(maya_main_window())
    se.setWindowFlags(QtCore.Qt.Window)
    se.show()
