import sys
from random import randint

from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


# class TheFloor(QWidget):
#    """
#    This "window" is a QWidget. this is the basic window so i might make this the main window later but for now it is its own window
#    """
#
#    def __init__(self):
#        super().__init__()
#        layout = QVBoxLayout()
#        self.label = QLabel("This Is the Floor, Here you will eventually find the links to different trunks")
#        layout.addWidget(self.label)
#        self.setLayout(layout)

class TrunkTemplate(QWidget):
    """
    This "window" is a QWidget. for now, it is a basic templete for trunks
    """

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("This Is a trunk, here you will eventually find links to different branches")
        layout.addWidget(self.label)
        self.setLayout(layout)


class BranchTemplate(QWidget):
    """
    This "window" is a QWidget. for now, it is the basic template for a branch
    """

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("This Is a Branch, here you will eventually find links to different Leaves")
        layout.addWidget(self.label)
        self.setLayout(layout)


class LeafTemplate(QWidget):
    """
    This "window" is a QWidget. for now, it is the basic template for a leaf
    """

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("This Is a Leaf, here you will eventually find the ending points of a string or line of thought")
        layout.addWidget(self.label)
        self.setLayout(layout)





class TheFloor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TreeNotes")
        self.setContentsMargins(10, 10, 10, 10)
        self.resize(500, 500)

        Title_label = QLabel("The Floor")

        
        self.Trunk = TrunkTemplate()
        self.Branch = BranchTemplate()
        self.Leaf = LeafTemplate()

        l = QVBoxLayout()
        
        


        l.addWidget(Title_label)


        buttonTrunk = QPushButton("Push to see a Trunk")
        buttonTrunk.clicked.connect(
            lambda checked: self.toggle_window(self.Trunk)
        )
        l.addWidget(buttonTrunk)

        buttonBranch = QPushButton("Push to see a Branch")
        buttonBranch.clicked.connect(
            lambda checked: self.toggle_window(self.Branch)
        )
        l.addWidget(buttonBranch)

        buttonLeaf = QPushButton("Push to see a Leaf")
        buttonLeaf.clicked.connect(
            lambda checked: self.toggle_window(self.Leaf)
        )
        l.addWidget(buttonLeaf)








        w = QWidget()
        w.setLayout(l)
        self.setCentralWidget(w)

    def toggle_window(self, window):
        if window.isVisible():
            window.hide()

        else:
            window.show()


app = QApplication(sys.argv)
app.setStyle("Fusion")
w = TheFloor()
w.show()

app.exec()