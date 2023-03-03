# Copyright 2020 by Kurt Rathjen. All Rights Reserved.
#
# This library is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Lesser General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or 
# (at your option) any later version. This library is distributed in the 
# hope that it will be useful, but WITHOUT ANY WARRANTY; without even the 
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
# See the GNU Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library. If not, see <http://www.gnu.org/licenses/>.

from studiovendor.Qt import QtWidgets

from .groupitem import GroupItem


class ItemDelegate(QtWidgets.QStyledItemDelegate):

    def __init__(self):
        """
        This class is used to display data for the items in a ItemsWidget.
        """
        QtWidgets.QStyledItemDelegate.__init__(self)

        self._itemsWidget = None

    def itemsWidget(self):
        """
        Return the ItemsWidget that contains the item delegate.

        :rtype: studioqt.ItemsWidget
        """
        return self._itemsWidget

    def setItemsWidget(self, itemsWidget):
        """
        Set the ItemsWidget for the delegate.

        :type itemsWidget: studioqt.ItemsWidget
        :rtype: None
        """
        self._itemsWidget = itemsWidget

    def sizeHint(self, option, index):
        """
        Return the size for the given index.

        :type option: QtWidgets.QStyleOptionViewItem
        :type index: QtCore.QModelIndex
        :rtype: QtCore.QSize
        """
        #This will be called for each row.
        item = self.itemsWidget().itemFromIndex(index)

        if isinstance(item, GroupItem):
            return item.sizeHint()

        return self.itemsWidget().itemSizeHint(index)

    def paint(self, painter, option, index):
        """
        Paint performs low-level painting for the given model index.

        :type painter:  QtWidgets.QPainter
        :type option: QtWidgets.QStyleOptionViewItem
        :type index: QtCore.QModelIndex
        :rtype: None
        """
        item = self.itemsWidget().itemFromIndex(index)
        item.paint(painter, option, index)
