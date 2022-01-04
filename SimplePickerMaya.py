from PySide2 import QtWidgets, QtCore
from maya import cmds
import typing

class SelectorButton(QtWidgets.QPushButton):
    _objectName: str = ""

    def __init__(self, objectName: str, buttonLabel: str, posX: int, posY: int, sizeX: int, sizeY: int, parent: QtWidgets.QWidget):
        super().__init__(buttonLabel, parent)

        self._objectName = objectName
                
        self.setGeometry(posX, posY, sizeX, sizeY)
        self.clicked.connect(self.onButtonClicked)

        self.show()

    def onButtonClicked(self):
        if (cmds.objExists(self._objectName)):
            modifiers = QtWidgets.QApplication.keyboardModifiers()
            if modifiers == (QtCore.Qt.ControlModifier | QtCore.Qt.ShiftModifier):
                # Ctrl + Shift + Click
                cmds.select(self._objectName, add=True)
            elif modifiers == QtCore.Qt.ShiftModifier:
                # Shift + Click
                cmds.select(self._objectName, toggle=True)
            elif modifiers == QtCore.Qt.ControlModifier:
                # Ctrl + Click
                cmds.select(self._objectName, deselect=True)
            else:
                # Click
                cmds.select(self._objectName, replace=True)
        else:
            print(f"Error: Object '{self._objectName}', dose not exist!")

class SimpleMayaPicker(QtWidgets.QWidget):
    _buttons: typing.List[SelectorButton] = []
    
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SimpleMayaPicker 1.0")
        self.setGeometry(300, 50, 766, 980)

        self.show()
        
    def AddSelector(self, objectName: str, buttonLabel: str, posX: int, posY: int, sizeX: int, sizeY: int):
        newSelectorButton = SelectorButton(objectName, buttonLabel, posX, posY, sizeX, sizeY, self)
        newSelectorButton.show()
        self._buttons.append(newSelectorButton)

myPicker = SimpleMayaPicker()
myPicker.AddSelector("L_Wrist_CTRL", "lWrist", 100, 10, 50, 30)
myPicker.AddSelector("R_Wrist_CTRL", "rWrist", 100, 40, 50, 30)
