import maya.cmds as cmds
from functools import partial
from dwpicker.pyside import QtCore, QtWidgets

from dwpicker.commands import (
    CommandsEditor, MenuCommandsEditor, GlobalCommandsEditor)
from dwpicker.qtutils import VALIGNS, HALIGNS
from dwpicker.designer.stackeditor import StackEditor
from dwpicker.designer.layer import VisibilityLayersEditor
from dwpicker.designer.patheditor import PathEditor
from dwpicker.stack import ORIENTATIONS
from dwpicker.widgets import (
    BoolCombo, BrowseEdit, ColorEdit, ChildrenWidget, IntEdit, FloatEdit,
    LayerEdit, TextEdit, Title, WidgetToggler, ZoomsLockedEditor)


LEFT_CELL_WIDTH = 90
SHAPE_TYPES = 'square', 'round', 'rounded_rect', 'custom'
SPACES = 'world', 'screen'
ANCHORS = 'top_left', 'top_right', 'bottom_left', 'bottom_right'


class AttributeEditor(QtWidgets.QWidget):
    imageModified = QtCore.Signal()
    optionSet = QtCore.Signal(str, object)
    optionsSet = QtCore.Signal(dict, bool)  # all options, affect rect
    selectLayerContent = QtCore.Signal(str)
    panelDoubleClicked = QtCore.Signal(int)

    def __init__(self, document, display_options, parent=None):
        super(AttributeEditor, self).__init__(parent)
        self.document = document

        self.generals = GeneralSettings(self.document, display_options)
        self.generals.panelDoubleClicked.connect(self.panel_double_clicked)
        mtd = self.selectLayerContent.emit
        self.generals.layers.selectLayerContent.connect(mtd)

        self.shape = ShapeSettings()
        self.shape.optionSet.connect(self.optionSet.emit)
        self.shape.optionsSet.connect(self.optionsSet.emit)
        self.shape_toggler = WidgetToggler('Shape', self.shape)

        self.image = ImageSettings()
        self.image.optionSet.connect(self.image_modified)
        self.image_toggler = WidgetToggler('Image', self.image)

        self.appearence = AppearenceSettings()
        self.appearence.optionSet.connect(self.optionSet.emit)
        self.appearence_toggler = WidgetToggler('Appearence', self.appearence)

        self.text = TextSettings()
        self.text.optionSet.connect(self.optionSet.emit)
        self.text_toggler = WidgetToggler('Text', self.text)

        self.action = ActionSettings(document, display_options)
        self.action.optionSet.connect(self.optionSet.emit)
        self.action_toggler = WidgetToggler('Action', self.action)

        self.widget = QtWidgets.QWidget()
        self.layout = QtWidgets.QVBoxLayout(self.widget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.layout.addWidget(self.shape_toggler)
        self.layout.addWidget(self.shape)
        self.layout.addWidget(self.image_toggler)
        self.layout.addWidget(self.image)
        self.layout.addWidget(self.appearence_toggler)
        self.layout.addWidget(self.appearence)
        self.layout.addWidget(self.text_toggler)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.action_toggler)
        self.layout.addWidget(self.action)
        self.layout.addStretch(1)

        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setWidget(self.widget)

        self.tab = QtWidgets.QTabWidget()
        self.tab.addTab(self.scroll_area, 'Shapes')
        self.tab.addTab(self.generals, 'Picker')

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addWidget(self.tab)

        self.setFixedWidth(self.sizeHint().width() * 1.05)

    def panel_double_clicked(self, panel):
        self.panelDoubleClicked.emit(panel - 1)

    def set_options(self, options):
        self.blockSignals(True)
        self.shape.set_options(options)
        self.image.set_options(options)
        self.appearence.set_options(options)
        self.text.set_options(options)
        self.action.set_options(options)
        self.blockSignals(False)

    def image_modified(self, option, value):
        self.optionSet.emit(option, value)
        self.imageModified.emit()


class GeneralSettings(QtWidgets.QWidget):
    panelDoubleClicked = QtCore.Signal(int)

    def __init__(self, document, display_options, parent=None):
        super(GeneralSettings, self).__init__(parent)
        self.document = document
        self.display_options = display_options

        self.document.general_option_changed.connect(self.update_options)
        self.document.data_changed.connect(self.update_options)

        self.name = TextEdit()
        self.name.valueSet.connect(partial(self.set_general, 'name'))

        self.zoom_locked = ZoomsLockedEditor(self.document)

        self.orientation = QtWidgets.QComboBox()
        self.orientation.addItems(list(ORIENTATIONS))
        method = partial(self.set_general, 'panels.orientation')
        self.orientation.currentTextChanged.connect(method)

        self.as_sub_tab = BoolCombo()
        method = partial(self.set_general, 'panels.as_sub_tab')
        self.as_sub_tab.valueSet.connect(method)

        self.stack = StackEditor()
        self.stack.setMinimumHeight(100)
        self.stack.panelsChanged.connect(self.stack_changed)
        self.stack.panelSelected.connect(self.panel_selected)
        self.stack.panelDoubleClicked.connect(self.panelDoubleClicked.emit)

        self.layers = VisibilityLayersEditor(self.document)
        self.commands = GlobalCommandsEditor()
        method = partial(self.set_general, 'menu_commands')
        self.commands.valueSet.connect(method)

        form_layout = QtWidgets.QFormLayout()
        form_layout.setSpacing(0)
        form_layout.setContentsMargins(0, 0, 0, 0)
        form_layout.setHorizontalSpacing(5)
        form_layout.addRow('Picker Name', self.name)

        form_layout_2 = QtWidgets.QFormLayout()
        form_layout_2.setSpacing(0)
        form_layout_2.setContentsMargins(0, 0, 0, 0)
        form_layout_2.setHorizontalSpacing(5)
        form_layout_2.addRow('Columns orientation', self.orientation)
        form_layout_2.addRow('Display panels as tab', self.as_sub_tab)

        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addLayout(form_layout)
        layout.addItem(QtWidgets.QSpacerItem(0, 8))
        layout.addWidget(Title('Picker Panels'))
        layout.addLayout(form_layout_2)
        layout.addWidget(self.stack)
        layout.addItem(QtWidgets.QSpacerItem(0, 8))
        layout.addWidget(Title('Panels Zoom Locked'))
        layout.addWidget(self.zoom_locked)
        layout.addItem(QtWidgets.QSpacerItem(0, 8))
        layout.addWidget(Title('Visibility Layers'))
        layout.addWidget(self.layers)
        layout.addItem(QtWidgets.QSpacerItem(0, 8))
        layout.addWidget(Title('Global Right Click Commands'))
        layout.addWidget(self.commands)
        layout.addStretch()
        self.update_options()

    def panel_selected(self, index):
        self.display_options.current_panel = index - 1
        self.display_options.options_changed.emit()

    def stack_changed(self):
        self.set_general('panels', self.stack.data)

    def set_general(self, key, value):
        self.document.data['general'][key] = value
        self.document.general_option_changed.emit('attribute_editor', key)
        self.document.record_undo()
        if key == 'panels.orientation':
            self.stack.set_orientation(value)

    def update_options(self, *_):
        self.block_signals(True)
        options = self.document.data['general']
        self.stack.set_data(options['panels'])
        self.stack.set_orientation(options['panels.orientation'])
        self.as_sub_tab.setCurrentText(str(options['panels.as_sub_tab']))
        self.orientation.setCurrentText(options['panels.orientation'])
        self.name.setText(options['name'])
        self.commands.set_options(options)
        self.block_signals(False)

    def block_signals(self, state):
        widgets = (
            self.stack,
            self.as_sub_tab,
            self.orientation,
            self.name,
            self.commands)
        for widget in widgets:
            widget.blockSignals(state)


class ShapeSettings(QtWidgets.QWidget):
    optionSet = QtCore.Signal(str, object)
    optionsSet = QtCore.Signal(dict, bool)  # all options, affect rect

    def __init__(self, parent=None):
        super(ShapeSettings, self).__init__(parent)
        self.id_ = QtWidgets.QLineEdit()
        self.id_.setReadOnly(True)

        self.shape = QtWidgets.QComboBox()
        self.shape.addItems(SHAPE_TYPES)
        self.shape.currentIndexChanged.connect(self.shape_changed)
        self.path_editor = PathEditor(self)
        self.path_editor.pathEdited.connect(self.path_edited)
        self.path_editor.setVisible(False)
        self.path_editor.setEnabled(False)

        self.panel = QtWidgets.QLineEdit()
        self.panel.setReadOnly(True)
        self.layer = LayerEdit()
        method = partial(self.optionSet.emit, 'visibility_layer')
        self.layer.valueSet.connect(method)

        self.background = BoolCombo()
        method = partial(self.optionSet.emit, 'background')
        self.background.valueSet.connect(method)

        self.ignored_by_focus = BoolCombo()
        method = partial(self.optionSet.emit, 'shape.ignored_by_focus')
        self.ignored_by_focus.valueSet.connect(method)

        self.space = QtWidgets.QComboBox()
        self.space.addItems(SPACES)
        self.space.currentIndexChanged.connect(self.space_changed)

        self.anchor = QtWidgets.QComboBox()
        self.anchor.addItems(ANCHORS)
        method = partial(self.optionSet.emit, 'shape.anchor')
        self.anchor.currentTextChanged.connect(method)

        self.left = IntEdit()
        method = partial(self.optionSet.emit, 'shape.left')
        self.left.valueSet.connect(method)
        self.top = IntEdit()
        method = partial(self.optionSet.emit, 'shape.top')
        self.top.valueSet.connect(method)
        self.width = IntEdit(minimum=0)
        method = partial(self.optionSet.emit, 'shape.width')
        self.width.valueSet.connect(method)
        self.height = IntEdit(minimum=0)
        method = partial(self.optionSet.emit, 'shape.height')
        self.height.valueSet.connect(method)
        self.cornersx = IntEdit(minimum=0)
        method = partial(self.optionSet.emit, 'shape.cornersx')
        self.cornersx.valueSet.connect(method)
        self.cornersy = IntEdit(minimum=0)
        method = partial(self.optionSet.emit, 'shape.cornersy')
        self.cornersy.valueSet.connect(method)

        layout1 = QtWidgets.QFormLayout()
        layout1.setSpacing(0)
        layout1.setContentsMargins(0, 0, 0, 0)
        layout1.setHorizontalSpacing(5)
        layout1.addRow('Id', self.id_)
        layout1.addItem(QtWidgets.QSpacerItem(0, 8))
        layout1.addRow(Title('Display'))
        layout1.addRow('Panel number', self.panel)
        layout1.addRow('Visibility layer', self.layer)
        layout1.addRow('Background', self.background)
        layout1.addRow('Ignored by focus', self.ignored_by_focus)
        layout1.addRow('Shape', self.shape)

        layout2 = QtWidgets.QVBoxLayout()
        layout2.setSpacing(0)
        layout2.setContentsMargins(0, 0, 0, 0)
        layout2.addWidget(self.path_editor)

        layout3 = QtWidgets.QFormLayout()
        layout3.addItem(QtWidgets.QSpacerItem(0, 8))
        layout3.addRow(Title('Space'))
        layout3.addRow('space', self.space)
        layout3.addRow('anchor', self.anchor)
        layout3.addItem(QtWidgets.QSpacerItem(0, 8))
        layout3.addRow(Title('Dimensions'))
        layout3.addRow('left', self.left)
        layout3.addRow('top', self.top)
        layout3.addRow('width', self.width)
        layout3.addRow('height', self.height)
        layout3.addRow('roundness x', self.cornersx)
        layout3.addRow('roundness y', self.cornersy)
        layout3.addItem(QtWidgets.QSpacerItem(0, 8))

        layout = QtWidgets.QVBoxLayout(self)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addLayout(layout1)
        layout.addLayout(layout2)
        layout.addLayout(layout3)

        for label in self.findChildren(QtWidgets.QLabel):
            alignment = QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter
            if not isinstance(label, Title):
                label.setAlignment(alignment)
                label.setFixedWidth(LEFT_CELL_WIDTH)

    def path_edited(self):
        if self.shape.currentText() != 'custom':
            return
        self.optionSet.emit('shape.path', self.path_editor.path())

    def shape_changed(self, _):
        self.path_editor.setEnabled(self.shape.currentText() == 'custom')
        self.path_editor.setVisible(self.shape.currentText() == 'custom')
        self.height.setEnabled(self.shape.currentText() != 'custom')
        self.width.setEnabled(self.shape.currentText() != 'custom')
        self.optionSet.emit('shape', self.shape.currentText())
        self.path_editor.canvas.focus()

    def space_changed(self, index):
        self.anchor.setEnabled(bool(index))
        self.optionSet.emit('shape.space', self.space.currentText())

    def set_options(self, options):
        values = list({option['id'] for option in options})
        value = str(values[0]) if len(values) == 1 else '...'
        self.id_.setText(value)

        values = list({option['background'] for option in options})
        value = str(values[0]) if len(values) == 1 else None
        self.background.setCurrentText(value)

        values = list({option['shape.ignored_by_focus'] for option in options})
        value = str(values[0]) if len(values) == 1 else None
        self.ignored_by_focus.setCurrentText(value)

        values = list({option['panel'] for option in options})
        value = values[0] if len(values) == 1 else '' if not values else '...'
        self.panel.setText(str(value + 1 if isinstance(value, int) else value))

        values = list({option['shape.space'] for option in options})
        value = values[0] if len(values) == 1 else '' if not values else '...'
        self.space.setCurrentText(value)

        values = list({option['shape.anchor'] for option in options})
        value = values[0] if len(values) == 1 else '' if not values else '...'
        self.anchor.setCurrentText(value)
        self.anchor.setEnabled(self.space.currentText() == 'screen')

        values = list({option['visibility_layer'] for option in options})
        value = values[0] if len(values) == 1 else '' if not values else '...'
        self.layer.set_layer(value)

        values = list({option['shape'] for option in options})
        value = values[0] if len(values) == 1 else '...'
        self.shape.blockSignals(True)
        self.shape.setCurrentText(value)
        self.shape.blockSignals(False)
        self.height.setEnabled('custom' not in values)
        self.width.setEnabled('custom' not in values)

        if len(options) == 1:
            self.path_editor.setEnabled(options[0]['shape'] == 'custom')
            self.path_editor.setVisible(options[0]['shape'] == 'custom')
            self.path_editor.set_options(options[0])
        else:
            self.path_editor.setEnabled(False)
            self.path_editor.setVisible(False)
            self.path_editor.set_options(None)

        values = list({int(round((option['shape.left']))) for option in options})
        value = str(values[0]) if len(values) == 1 else None
        self.left.setText(value)

        values = list({option['shape.top'] for option in options})
        value = str(values[0]) if len(values) == 1 else None
        self.top.setText(value)

        values = list({option['shape.width'] for option in options})
        value = str(values[0]) if len(values) == 1 else None
        self.width.setText(value)

        values = list({option['shape.height'] for option in options})
        value = str(values[0]) if len(values) == 1 else None
        self.height.setText(value)

        values = list({option['shape.cornersx'] for option in options})
        value = str(values[0]) if len(values) == 1 else None
        self.cornersx.setText(value)

        values = list({option['shape.cornersy'] for option in options})
        value = str(values[0]) if len(values) == 1 else None
        self.cornersy.setText(value)


class ImageSettings(QtWidgets.QWidget):
    optionSet = QtCore.Signal(str, object)

    def __init__(self, parent=None):
        super(ImageSettings, self).__init__(parent)
        self.path = BrowseEdit()
        self.path.valueSet.connect(partial(self.optionSet.emit, 'image.path'))

        self.fit = BoolCombo(True)
        self.fit.valueSet.connect(partial(self.optionSet.emit, 'image.fit'))

        self.ratio = BoolCombo(True)
        method = partial(self.optionSet.emit, 'image.ratio')
        self.ratio.valueSet.connect(method)

        self.width = FloatEdit(minimum=0)
        method = partial(self.optionSet.emit, 'image.width')
        self.width.valueSet.connect(method)

        self.height = FloatEdit(minimum=0)
        method = partial(self.optionSet.emit, 'image.height')
        self.height.valueSet.connect(method)

        self.layout = QtWidgets.QFormLayout(self)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setHorizontalSpacing(5)
        self.layout.addRow('Path', self.path)
        self.layout.addRow('Fit to shape', self.fit)
        self.layout.addRow('Preserve ratio', self.ratio)
        self.layout.addRow('Width', self.width)
        self.layout.addRow('Height', self.height)
        self.layout.addItem(QtWidgets.QSpacerItem(0, 8))

        for label in self.findChildren(QtWidgets.QLabel):
            alignment = QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter
            if not isinstance(label, Title):
                label.setAlignment(alignment)
                label.setFixedWidth(LEFT_CELL_WIDTH)

    def set_options(self, options):
        values = list({option['image.path'] for option in options})
        value = str(values[0]) if len(values) == 1 else None
        self.path.set_value(value)

        values = list({option['image.fit'] for option in options})
        value = str(values[0]) if len(values) == 1 else None
        self.fit.setCurrentText(value)

        values = list({option['image.ratio'] for option in options})
        value = str(values[0]) if len(values) == 1 else None
        self.ratio.setCurrentText(value)

        values = list({option['image.width'] for option in options})
        value = str(values[0]) if len(values) == 1 else None
        self.width.setText(value)

        values = list({option['image.height'] for option in options})
        value = str(values[0]) if len(values) == 1 else None
        self.height.setText(value)


class AppearenceSettings(QtWidgets.QWidget):
    optionSet = QtCore.Signal(str, object)

    def __init__(self, parent=None):
        super(AppearenceSettings, self).__init__(parent)

        self.border = BoolCombo(True)
        method = partial(self.optionSet.emit, 'border')
        self.border.valueSet.connect(method)

        self.borderwidth_normal = FloatEdit(minimum=0.0)
        method = partial(self.optionSet.emit, 'borderwidth.normal')
        self.borderwidth_normal.valueSet.connect(method)

        self.borderwidth_hovered = FloatEdit(minimum=0.0)
        method = partial(self.optionSet.emit, 'borderwidth.hovered')
        self.borderwidth_hovered.valueSet.connect(method)

        self.borderwidth_clicked = FloatEdit(minimum=0.0)
        method = partial(self.optionSet.emit, 'borderwidth.clicked')
        self.borderwidth_clicked.valueSet.connect(method)

        self.bordercolor_normal = ColorEdit()
        method = partial(self.optionSet.emit, 'bordercolor.normal')
        self.bordercolor_normal.valueSet.connect(method)

        self.bordercolor_hovered = ColorEdit()
        method = partial(self.optionSet.emit, 'bordercolor.hovered')
        self.bordercolor_hovered.valueSet.connect(method)

        self.bordercolor_clicked = ColorEdit()
        method = partial(self.optionSet.emit, 'bordercolor.clicked')
        self.bordercolor_clicked.valueSet.connect(method)

        self.bordercolor_transparency = IntEdit(minimum=0, maximum=255)
        method = partial(self.optionSet.emit, 'bordercolor.transparency')
        self.bordercolor_transparency.valueSet.connect(method)

        self.backgroundcolor_normal = ColorEdit()
        method = partial(self.optionSet.emit, 'bgcolor.normal')
        self.backgroundcolor_normal.valueSet.connect(method)

        self.backgroundcolor_hovered = ColorEdit()
        method = partial(self.optionSet.emit, 'bgcolor.hovered')
        self.backgroundcolor_hovered.valueSet.connect(method)

        self.backgroundcolor_clicked = ColorEdit()
        method = partial(self.optionSet.emit, 'bgcolor.clicked')
        self.backgroundcolor_clicked.valueSet.connect(method)

        self.backgroundcolor_transparency = IntEdit(minimum=0, maximum=255)
        method = partial(self.optionSet.emit, 'bgcolor.transparency')
        self.backgroundcolor_transparency.valueSet.connect(method)

        self.layout = QtWidgets.QFormLayout(self)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setHorizontalSpacing(5)
        self.layout.addRow('border visible', self.border)
        self.layout.addItem(QtWidgets.QSpacerItem(0, 8))
        self.layout.addRow(Title('Border width (pxf)'))
        self.layout.addRow('normal', self.borderwidth_normal)
        self.layout.addRow('hovered', self.borderwidth_hovered)
        self.layout.addRow('clicked', self.borderwidth_clicked)
        self.layout.addItem(QtWidgets.QSpacerItem(0, 8))
        self.layout.addRow(Title('Border color'))
        self.layout.addRow('normal', self.bordercolor_normal)
        self.layout.addRow('hovered', self.bordercolor_hovered)
        self.layout.addRow('clicked', self.bordercolor_clicked)
        self.layout.addRow('transparency', self.bordercolor_transparency)
        self.layout.addItem(QtWidgets.QSpacerItem(0, 8))
        self.layout.addRow(Title('Background color'))
        self.layout.addRow('normal', self.backgroundcolor_normal)
        self.layout.addRow('hovered', self.backgroundcolor_hovered)
        self.layout.addRow('clicked', self.backgroundcolor_clicked)
        self.layout.addRow('transparency', self.backgroundcolor_transparency)
        self.layout.addItem(QtWidgets.QSpacerItem(0, 8))

        for label in self.findChildren(QtWidgets.QLabel):
            alignment = QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter
            if not isinstance(label, Title):
                label.setAlignment(alignment)
                label.setFixedWidth(LEFT_CELL_WIDTH)

    def set_options(self, options):
        values = list({option['border'] for option in options})
        value = str(values[0]) if len(values) == 1 else None
        self.border.setCurrentText(value)

        values = list({option['borderwidth.normal'] for option in options})
        value = str(values[0]) if len(values) == 1 else None
        self.borderwidth_normal.setText(value)

        values = list({option['borderwidth.hovered'] for option in options})
        value = str(values[0]) if len(values) == 1 else None
        self.borderwidth_hovered.setText(value)

        values = list({option['borderwidth.clicked'] for option in options})
        value = str(values[0]) if len(values) == 1 else None
        self.borderwidth_clicked.setText(value)

        values = list({option['bordercolor.normal'] for option in options})
        value = str(values[0]) if len(values) == 1 else None
        self.bordercolor_normal.set_color(value)

        values = list({option['bordercolor.hovered'] for option in options})
        value = str(values[0]) if len(values) == 1 else None
        self.bordercolor_hovered.set_color(value)

        values = list({option['bordercolor.clicked'] for option in options})
        value = str(values[0]) if len(values) == 1 else None
        self.bordercolor_clicked.set_color(value)

        values = list({option['bordercolor.transparency'] for option in options})
        value = str(values[0]) if len(values) == 1 else None
        self.bordercolor_transparency.setText(value)

        values = list({option['bgcolor.normal'] for option in options})
        value = str(values[0]) if len(values) == 1 else None
        self.backgroundcolor_normal.set_color(value)

        values = list({option['bgcolor.hovered'] for option in options})
        value = str(values[0]) if len(values) == 1 else None
        self.backgroundcolor_hovered.set_color(value)

        values = list({option['bgcolor.clicked'] for option in options})
        value = str(values[0]) if len(values) == 1 else None
        self.backgroundcolor_clicked.set_color(value)

        values = list({option['bgcolor.transparency'] for option in options})
        value = str(values[0]) if len(values) == 1 else None
        self.backgroundcolor_transparency.setText(value)


class ActionSettings(QtWidgets.QWidget):
    optionSet = QtCore.Signal(str, object)

    def __init__(self, document, display_options, parent=None):
        super(ActionSettings, self).__init__(parent)
        self._targets = QtWidgets.QLineEdit()
        self._targets.returnPressed.connect(self.targets_changed)

        self._add_targets = QtWidgets.QPushButton('Add')
        self._add_targets.released.connect(self.call_add_targets)
        self._add_targets.setToolTip('Add selected objects')
        self._add_targets.setFocusPolicy(QtCore.Qt.NoFocus)

        self._remove_targets = QtWidgets.QPushButton('Remove')
        self._remove_targets.released.connect(self.call_remove_targets)
        self._remove_targets.setToolTip('Remove selected objects')
        self._remove_targets.setFocusPolicy(QtCore.Qt.NoFocus)

        self._replace_targets = QtWidgets.QPushButton('Replace')
        self._replace_targets.clicked.connect(self.call_replace_targets)
        self._replace_targets.setToolTip('Replace target by current selection')
        self._replace_targets.setFocusPolicy(QtCore.Qt.NoFocus)

        self._clear_targets = QtWidgets.QPushButton('Clear')
        self._clear_targets.clicked.connect(self.call_clear_targets)
        self._clear_targets.setToolTip('Clear shape targets')
        self._clear_targets.setFocusPolicy(QtCore.Qt.NoFocus)

        _targets = QtWidgets.QWidget()
        self._targets_layout = QtWidgets.QHBoxLayout(_targets)
        self._targets_layout.setContentsMargins(0, 0, 0, 0)
        self._targets_layout.setSpacing(2)
        self._targets_layout.addStretch()
        self._targets_layout.addWidget(self._add_targets)
        self._targets_layout.addWidget(self._remove_targets)
        self._targets_layout.addWidget(self._replace_targets)
        self._targets_layout.addWidget(self._clear_targets)

        self._commands = CommandsEditor()
        method = partial(self.optionSet.emit, 'action.commands')
        self._commands.valueSet.connect(method)

        self._menu = MenuCommandsEditor()
        method = partial(self.optionSet.emit, 'action.menu_commands')
        self._menu.valueSet.connect(method)

        self.select_one_shape_label = QtWidgets.QLabel('Select only one shape')
        self.children = ChildrenWidget(document, display_options)
        method = partial(self.optionSet.emit, 'children')
        self.children.children_changed.connect(method)

        form = QtWidgets.QFormLayout()
        form.setSpacing(0)
        form.setContentsMargins(0, 0, 0, 0)
        form.setHorizontalSpacing(5)
        form.addRow(Title('Selection'))
        form.addRow('Targets', self._targets)
        form.addWidget(_targets)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.layout.addLayout(form)
        self.layout.addItem(QtWidgets.QSpacerItem(0, 8))

        for label in self.findChildren(QtWidgets.QLabel):
            alignment = QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter
            if not isinstance(label, Title):
                label.setAlignment(alignment)
                label.setFixedWidth(LEFT_CELL_WIDTH)

        self.layout.addWidget(Title('Scripts'))
        self.layout.addWidget(self._commands)
        self.layout.addItem(QtWidgets.QSpacerItem(0, 8))
        self.layout.addWidget(Title('Right Click Menu'))
        self.layout.addWidget(self._menu)
        self.layout.addItem(QtWidgets.QSpacerItem(0, 8))
        self.layout.addWidget(Title('Hierarchy'))
        self.layout.addWidget(self.select_one_shape_label)
        self.layout.addWidget(self.children)
        self.layout.addItem(QtWidgets.QSpacerItem(0, 8))

    def targets(self):
        targets = str(self._targets.text())
        try:
            return [t.strip(" ") for t in targets.split(',')]
        except ValueError:
            return []

    def call_clear_targets(self):
        self._targets.setText('')
        self.targets_changed()

    def call_add_targets(self):
        selection = cmds.ls(selection=True, flatten=True)
        if not selection:
            return

        targets = self.targets()
        edits = [item for item in selection if item not in targets]
        targets = targets if targets != [''] else []
        self._targets.setText(', '.join(targets + edits))
        self.targets_changed()

    def call_remove_targets(self):
        selection = cmds.ls(selection=True, flatten=True)
        if not selection:
            return

        targets = [item for item in self.targets() if item not in selection]
        self._targets.setText(', '.join(targets))
        self.targets_changed()

    def call_replace_targets(self):
        selection = cmds.ls(selection=True, flatten=True)
        if not selection:
            return
        self._targets.setText(', '.join(selection))
        self.targets_changed()

    def targets_changed(self):
        values = [t.strip(" ") for t in self._targets.text().split(",")]
        self.optionSet.emit('action.targets', values)

    def set_options(self, options):
        values = list({o for opt in options for o in opt['action.targets']})
        self._targets.setText(", ".join(sorted(values)))
        self._commands.set_options(options)
        self._menu.set_options(options)
        self.select_one_shape_label.setVisible(len(options) != 1)
        self.children.clear()
        if len(options) == 1:
            self.children.set_children(options[0]['children'])


class TextSettings(QtWidgets.QWidget):
    optionSet = QtCore.Signal(str, object)

    def __init__(self, parent=None):
        super(TextSettings, self).__init__(parent)
        self.text = TextEdit()
        method = partial(self.optionSet.emit, 'text.content')
        self.text.valueSet.connect(method)

        self.size = FloatEdit(minimum=0.0)
        self.size.valueSet.connect(partial(self.optionSet.emit, 'text.size'))

        self.bold = BoolCombo()
        self.bold.valueSet.connect(partial(self.optionSet.emit, 'text.bold'))

        self.italic = BoolCombo()
        method = partial(self.optionSet.emit, 'text.italic')
        self.italic.valueSet.connect(method)

        self.color = ColorEdit()
        self.color.valueSet.connect(partial(self.optionSet.emit, 'text.color'))

        self.halignement = QtWidgets.QComboBox()
        self.halignement.addItems(HALIGNS.keys())
        self.halignement.currentIndexChanged.connect(self.halign_changed)
        self.valignement = QtWidgets.QComboBox()
        self.valignement.addItems(VALIGNS.keys())
        self.valignement.currentIndexChanged.connect(self.valign_changed)

        self.layout = QtWidgets.QFormLayout(self)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setHorizontalSpacing(5)
        self.layout.addRow('Content', self.text)
        self.layout.addItem(QtWidgets.QSpacerItem(0, 8))
        self.layout.addRow(Title('Options'))
        self.layout.addRow('Size', self.size)
        self.layout.addRow('Bold', self.bold)
        self.layout.addRow('Italic', self.italic)
        self.layout.addRow('Color', self.color)
        self.layout.addItem(QtWidgets.QSpacerItem(0, 8))
        self.layout.addRow(Title('Alignement'))
        self.layout.addRow('Horizontal', self.halignement)
        self.layout.addRow('Vertical', self.valignement)
        self.layout.addItem(QtWidgets.QSpacerItem(0, 8))

        for label in self.findChildren(QtWidgets.QLabel):
            alignment = QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter
            if not isinstance(label, Title):
                label.setAlignment(alignment)
                label.setFixedWidth(LEFT_CELL_WIDTH)

    def valign_changed(self):
        self.optionSet.emit('text.valign', self.valignement.currentText())

    def halign_changed(self):
        self.optionSet.emit('text.halign', self.halignement.currentText())

    def set_options(self, options):
        values = list({option['text.content'] for option in options})
        value = str(values[0]) if len(values) == 1 else None
        self.text.setText(value)

        values = list({option['text.size'] for option in options})
        value = str(values[0]) if len(values) == 1 else None
        self.size.setText(value)

        values = list({option['text.bold'] for option in options})
        value = str(values[0]) if len(values) == 1 else None
        self.bold.setCurrentText(value)

        values = list({option['text.italic'] for option in options})
        value = str(values[0]) if len(values) == 1 else None
        self.italic.setCurrentText(value)

        values = list({option['text.color'] for option in options})
        value = str(values[0]) if len(values) == 1 else None
        self.color.set_color(value)

        values = list({option['text.halign'] for option in options})
        value = str(values[0]) if len(values) == 1 else None
        self.halignement.setCurrentText(value)

        values = list({option['text.valign'] for option in options})
        value = str(values[0]) if len(values) == 1 else None
        self.valignement.setCurrentText(value)
