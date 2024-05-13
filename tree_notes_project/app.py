import sys
from controller import data
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
    QTextEdit,
    
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
        self.resize(1000, 500)
        # the layouts
        self.layout = QVBoxLayout()
        self.notes_layout = QStackedLayout()
        self.treenav_layout = QHBoxLayout()
        self.menu_layout = QHBoxLayout()
        

        # the home screen / floor where all the information trees are connected too

        self.Floor = QWidget()
        self.Floor_layout = QVBoxLayout()

        self.Floor_label = QLabel("The Floor")
        self.Floor_label.setFont(QFont("Montserrat", 20, 1))

        self.floor_text = QTextEdit()
                

        
        self.Floor_layout.addWidget(self.Floor_label)
        self.Floor_layout.addWidget(self.floor_text)

        self.Floor.setLayout(self.Floor_layout)
        self.notes_layout.addWidget(self.Floor)
        

        # Nav widget, i actually don't know why this works properly the label part is wrong but whatever im happy
        self.treenav_widget = QTreeWidget()
        self.treenav_widget.setColumnCount(len(data))
        self.treenav_widget.setHeaderLabels(["The Floor"])
        items = []
        for key, labels in data.items():
            item = QTreeWidgetItem([key])
            for label in labels:
                text = data[key][label]
                child = QTreeWidgetItem([label, str(text)])
                item.addChild(child)
            items.append(item)

        self.treenav_widget.insertTopLevelItems(0, items)

        self.treenav_layout.addWidget(self.treenav_widget)

        

#       self.treenav_layout.addWidget(self.)
        


        self.Floor_layout.addLayout(self.treenav_layout)


        self.forward_button = QPushButton()
        self.forward_button.clicked.connect(self.next_note)
  
        
    def next_note(self) -> None:
        self.notes_layout.setCurrentIndex(
            self.notes_layout.currentIndex() + 1

        )
        



#        layout.addWidget(Title_label)


#        buttonTrunk = QPushButton("Push to see a Trunk")
#        buttonTrunk.clicked.connect(
#            lambda checked: self.toggle_window(self.Trunk)
#        )
#        self.Floor_layout.addWidget(buttonTrunk)

        # buttonBranch = QPushButton("Push to see a Branch")
        # buttonBranch.clicked.connect(
        #     lambda checked: self.toggle_window(self.Branch)
        # )
        # self.Floor_layout.addWidget(buttonBranch)









class TrunkTemplate(QWidget):
    """
    This "window" is a QWidget. for now, it is a basic templete for trunks
    """

    def __init__(self):
        super().__init__()
        self.trunk_layout = QVBoxLayout()
        self.label = QLabel("This Is a trunk, here you will eventually find links to different branches")

        self.trunk_layout.addWidget(self.label)
        self.setLayout(self.trunk_layout)


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






app = QApplication(sys.argv)
w = TheFloor()
w.show()

app.exec()