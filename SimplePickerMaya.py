from PySide2 import QtWidgets, QtCore
from maya import cmds
import typing

class SelectorButton(QtWidgets.QPushButton):
    _objectName: str = ""
    _UIScale: float = 1.0

    def __init__(self, objectName: str, buttonLabel: str, buttonColor: str, posX: int, posY: int, sizeX: int, sizeY: int, parent: QtWidgets.QWidget):
        super().__init__(buttonLabel, parent)
        self._objectName = objectName
        self.setStyleSheet(f"background-color: {buttonColor}")
        self.setGeometry(posX, posY, sizeX, sizeY)
        self.clicked.connect(self.onButtonClicked)
        self.show()

    def onButtonClicked(self):
        if (cmds.objExists(self._objectName)):
            modifiers = QtWidgets.QApplication.keyboardModifiers()
            if modifiers == (QtCore.Qt.ControlModifier | QtCore.Qt.ShiftModifier): cmds.select(self._objectName, add=True)
            elif modifiers == QtCore.Qt.ShiftModifier: cmds.select(self._objectName, toggle=True)
            elif modifiers == QtCore.Qt.ControlModifier: cmds.select(self._objectName, deselect=True)
            else: cmds.select(self._objectName, replace=True)
        else:
            print(f"Error: Object '{self._objectName}', dose not exist!")

class SimpleMayaPicker(QtWidgets.QWidget):
    _buttons: typing.List[SelectorButton] = []
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SimpleMayaPicker 1.0")
        self.setGeometry(300, 50, 766, 980)
        self.show()

    def SetUIScale(self, scale: float):
        self._UIScale = scale
        
    def AddSelector(self, objectName: str, buttonLabel: str, buttonColor: str, posX: int, posY: int, sizeX: int, sizeY: int):
        newSelectorButton = SelectorButton(objectName, buttonLabel, buttonColor, posX*self._UIScale, posY*self._UIScale, sizeX*self._UIScale, sizeY*self._UIScale, self)
        newSelectorButton.show()
        self._buttons.append(newSelectorButton)

myPicker = SimpleMayaPicker()
myPicker.SetUIScale(2)
myPicker.AddSelector("L_Wrist_CTRL", "lWrist", "red", 100, 10, 50, 30)
myPicker.AddSelector("R_Wrist_CTRL", "rWrist", "blue", 100, 50, 50, 30)