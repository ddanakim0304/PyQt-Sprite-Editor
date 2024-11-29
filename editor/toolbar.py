from PyQt5.QtWidgets import QToolBar, QAction
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPainter

class ToolBar(QToolBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_tools()
        
    def init_tools(self):
        # Pen tool
        self.pen_action = QAction("Pen", self)  # Store as instance variable
        self.pen_action.setCheckable(True)
        self.pen_action.setChecked(True)
        self.pen_action.triggered.connect(self.set_pen_mode)
        self.addAction(self.pen_action)
        
        # Eraser tool
        self.eraser_action = QAction("Eraser", self)  # Store as instance variable
        self.eraser_action.setCheckable(True)
        self.eraser_action.triggered.connect(self.set_eraser_mode)
        self.addAction(self.eraser_action)
        
        # Add separator
        self.addSeparator()
        
        # Clear canvas action
        clear_action = QAction("Clear", self)
        clear_action.triggered.connect(self.parent().canvas.clear_canvas)
        self.addAction(clear_action)
            
    def set_eraser_mode(self):
        self.pen_action.setChecked(False)
        self.eraser_action.setChecked(True)
        self.parent().canvas.pen_color = QColor(255, 255, 255, 0)
        # Set composition mode for erasing
        self.parent().canvas.composition_mode = QPainter.CompositionMode_Clear
        
        
    def set_pen_mode(self):
        self.eraser_action.setChecked(False)
        self.pen_action.setChecked(True)
        self.parent().canvas.pen_color = Qt.black
        # Reset composition mode for normal drawing
        self.parent().canvas.composition_mode = QPainter.CompositionMode_SourceOver