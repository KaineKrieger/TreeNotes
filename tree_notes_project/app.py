import sys
import json
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


# the basic screen known as the floor which holds everything
        

class TheFloor(QWidget):
    def __init__(self):
        super().__init__()


        # sizing and spacing and layout
        self.setWindowTitle("TreeNotes")
        self.layout = QVBoxLayout(self)
        self.setContentsMargins(10, 10, 10, 10)
        self.resize(1000, 500)
       

        # Floor label
        self.Floor_label = QLabel("The Floor")
        self.Floor_label.setFont(QFont("Montserrat", 20, weight=QFont.Weight.Bold))
        self.layout.addWidget(self.Floor_label)




        # Nav widget, i have updated it to populate itself using a function

        self.treenav_widget = QTreeWidget()


        # Only 2 column for trunk titles and branch titles
        self.treenav_widget.setColumnCount(2)  
        self.treenav_widget.setHeaderLabels(["Trunks", "Branches"])
        # using the populate function
        self.populate_tree_widget()
       
        # update to change the note to the selected one
        self.treenav_widget.itemSelectionChanged.connect(self.update_note)
        self.layout.addWidget(self.treenav_widget)

        #       self.treenav_layout.addWidget(self.)


        # Notes label
        self.notes_label = QLabel("Title")
        self.notes_label.setFont(QFont("Montserrat", 15, weight=QFont.Weight.Bold))
        self.layout.addWidget(self.notes_label)




        # Notes box widget
        self.notes_layout = QVBoxLayout()
        self.Floor = QWidget()
        self.Floor_layout = QVBoxLayout(self.Floor)
        self.text_box = QTextEdit()
       
        self.Floor_layout.addWidget(self.text_box)
        self.notes_layout.addWidget(self.Floor)
        self.layout.addLayout(self.notes_layout)




        # create new turnk/branch buttons
        self.buttons_layout = QHBoxLayout()
        self.forward_button = QPushButton("New Trunk Note", clicked=self.new_trunk_note)
        self.buttons_layout.addWidget(self.forward_button)
        self.new_branch_button = QPushButton("New Branch Note", clicked=self.new_branch_note)
        self.buttons_layout.addWidget(self.new_branch_button)
        self.layout.addLayout(self.buttons_layout)


        


# gap for functions because it makes my brain feel better you can shush winika i know you don't like it



    def populate_tree_widget(self):
        # takes the data stored in the other file and populates the treewidget with it
        for trunk in data:
            item = QTreeWidgetItem([trunk])
            self.treenav_widget.addTopLevelItem(item)
            for branch in data[trunk]:
                item = QTreeWidgetItem([branch])
                trunk

# selected_items[0].addChild(item)

    def update_note(self):
        # updates the note part when changed
        selected_items = self.treenav_widget.selectedItems()
        if selected_items:
            selected_note = selected_items[0].text(0)  
            self.notes_label.setText(selected_note)
#            self.text_box.setText(data[selected_note])
            


    def new_trunk_note(self):
        # adds a new trunk to to treewidget and gives it a basic name
        new_note_title = f"New Trunk {self.treenav_widget.topLevelItemCount() + 1}"
        new_note_content = f"Content of {new_note_title}"
        item = QTreeWidgetItem([new_note_title])
        self.treenav_widget.addTopLevelItem(item)
        self.text_box.setPlainText(new_note_content)
        self.notes_label.setText(new_note_title)




    def new_branch_note(self):
        # adds a new branch to the selected trunk and gives it a basic title based on the trunk
        selected_items = self.treenav_widget.selectedItems()
        if selected_items:
            selected_note = selected_items[0].text(0)
            new_note_title = f"New Branch of '{selected_note}'"
            new_note_content = f"content of {new_note_title}"
            item = QTreeWidgetItem([new_note_title])
            selected_items[0].addChild(item)
            self.text_box.setPlainText(new_note_content)
            self.notes_label.setText(new_note_title)
            

print("hello world!")



# yk what this is i don't have to explain it (it starts the code properly)
app = QApplication(sys.argv)
window = TheFloor()
window.show()
sys.exit(app.exec())








# really huge blocks of dummy code that i didn't want to get rid of because i want to make this into the stacked layout but i really do not know how to figure it out




#    def next_note(self) -> None:
#        self.notes_layout.setCurrentIndex(
#            self.notes_layout.currentIndex() + 1
#
#        )

        # saving the current layout as a .json
#        self.save_button = QPushButton()
#        with open(a, 'C:\Users\horna733\Documents\Python Projects-Adam\Tree-Notes-Project\data.json', data) as f:
        

# class TrunkTemplate(QWidget):
#     """
#     This "window" is a QWidget. for now, it is a basic templete for trunks
#     """

#     def __init__(self):
#         super().__init__()
#         self.trunk_layout = QVBoxLayout()
#         self.label = QLabel("This Is a trunk, here you will eventually find links to different branches")

#         self.trunk_layout.addWidget(self.label)
#         self.setLayout(self.trunk_layout)


# class BranchTemplate(QWidget):
#     """
#     This "window" is a QWidget. for now, it is the basic template for a branch
#     """

#     def __init__(self):
#         super().__init__()
#         layout = QVBoxLayout()
#         self.label = QLabel("This Is a Branch, here you will eventually find links to different Leaves")
#         layout.addWidget(self.label)
#         self.setLayout(layout)





