import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QStackedLayout,
    QHBoxLayout,
    QTreeWidget, 
    QTreeWidgetItem,

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



class TheFloor(QWidget):
    def __init__(self):
        super().__init__()
        # sizing and spacing
        self.setWindowTitle("TreeNotes")
        self.setContentsMargins(10, 10, 10, 10)
        self.resize(500, 500)
        # the layouts
        self.layout = QVBoxLayout()
        self.notes_layout = QStackedLayout()
        self.treenav_layout = QHBoxLayout()
        self.menu_layout = QHBoxLayout()

        # Nav widget
        self.tree_widget = QTreeWidget()

        # the home screen / floor where all the information trees are connected too

        self.Floor = QWidget()
        self.Floor_layout = QVBoxLayout()

        self.Floor_label = QLabel("The Floor")
        self.Floor_label.setFont(QFont("Montserrat", 20, 1))
        

        # adding Floor to the stacked layout
        self.Floor_layout.addWidget(self.Floor_label)
        self.Floor.setLayout(self.Floor_layout)
        self.notes_layout.addWidget(self.Floor)

        self.Trunk = TrunkTemplate()
        self.Branch = BranchTemplate()
        self.Leaf = LeafTemplate()

        layout = QVBoxLayout()
        

#        layout.addWidget(Title_label)


        buttonTrunk = QPushButton("Push to see a Trunk")
        buttonTrunk.clicked.connect(
            lambda checked: self.toggle_window(self.Trunk)
        )
        self.Floor_layout.addWidget(buttonTrunk)

        buttonBranch = QPushButton("Push to see a Branch")
        buttonBranch.clicked.connect(
            lambda checked: self.toggle_window(self.Branch)
        )
        self.Floor_layout.addWidget(buttonBranch)

        buttonLeaf = QPushButton("Push to see a Leaf")
        buttonLeaf.clicked.connect(
            lambda checked: self.toggle_window(self.Leaf)
        )
        self.Floor_layout.addWidget(buttonLeaf)


        self.setLayout(self.Floor_layout)

    def toggle_window(self, window):
        if window.isVisible():
            window.hide()

        else:
            window.show()





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





app = QApplication(sys.argv)
w = TheFloor()
w.show()

app.exec()