from PySide6.QtWidgets import QMainWindow, QListWidgetItem, QWidget, QTextEdit, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget
from PySide6.QtGui import QFont, QIcon, QShortcut, QKeySequence
from PySide6.QtCore import Qt


import os
import glob
from datetime import datetime


class DisplayText(QWidget):
    def __init__(self):
        super().__init__()
              
        text_display_font = QFont()
        text_display_font.setPointSize(14)
        self.text_display = QTextEdit()
        self.text_display.setReadOnly(True)
        self.text_display.setFont(text_display_font)

        layout = QVBoxLayout()
        layout.addWidget(self.text_display)
        self.setLayout(layout)

    def set_text(self, text):
        self.text_display.setPlainText(text)
        self.text_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        



class TextE(QMainWindow):
    def __init__(self, parent=None):
        super(TextE, self).__init__(parent)
        current_date = datetime.now().strftime("%m.%d.%Y")
        self.setWindowTitle("Text Editor - {}".format(current_date))

        te_icon = QIcon("Images\\icon.png")
        self.setWindowIcon(te_icon)

        save_shortcut = QShortcut(QKeySequence(Qt.CTRL | Qt.Key_S), self)
        save_shortcut.activated.connect(self.save_text_to_file)
        

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        save_action = file_menu.addAction("Save")
        save_action.triggered.connect(self.save_text_to_file)
        self.setFixedSize(1000, 700)

        font = QFont()
        font.setPointSize(18)



        
        self.te = QTextEdit()
        self.te.setFont(font)
        self.setCentralWidget(self.te)

        with open("Diffnes.qss", "r") as file:
            self.te.setStyleSheet(file.read())

    def save_text_to_file(self):
        file_path =os.path.join("Saves", "{}.txt".format(self.windowTitle()[14:]))
        with open(file_path, "w", encoding="utf-8") as new_file:
            new_file.write(self.te.toPlainText())
        
class ListW(QMainWindow):
    def __init__(self):
        super().__init__()

        

        list_widget_font = QFont()
        list_widget_font.setPointSize(12)
        self.list_widget = QListWidget()
        self.list_widget.setFont(list_widget_font)
        self.list_widget.setFixedWidth(200)
        

       
        self.text_edit = TextE()
        
        self.populate_list_widget()

        self.list_widget.itemDoubleClicked.connect(self.open_file)
        self.list_widget.itemClicked.connect(self.update_display_text)

        self.display_widget = DisplayText() 

        self.list_widget.itemClicked.emit(self.list_widget.item(0)) 

        main_layout = QHBoxLayout()
        main_layout.addWidget(self.list_widget)
        main_layout.addWidget(self.display_widget)

        main_widget = QWidget()
        main_widget.setLayout(main_layout)

        self.setCentralWidget(main_widget)

        with open("Diffnes.qss", "r") as file:
            main_widget.setStyleSheet(file.read())

        
    def populate_list_widget(self):
       
        file_folder = "Saves\\"
        file_paths = glob.glob(os.path.join(file_folder, "*.txt"))
        file_paths.sort(reverse=True)

        for file in file_paths:
            list_item = QListWidgetItem(file[6:-4])
            self.list_widget.addItem(list_item)

    def update_display_text(self, item):
        file_folder = "Saves\\"
        selected_date = item.text()
        file_path = os.path.join(file_folder, "{}.txt".format(selected_date))

        with open(file_path, "r", encoding="utf-8") as file:
            file_contents = file.read()

        self.display_widget.set_text(file_contents)
        

    def open_file(self, item):
        file_folder = "Saves\\"
        selected_date = item.text()
        file_path = os.path.join(file_folder, "{}.txt".format(selected_date))
        
        
        with open(file_path, "r", encoding="utf-8") as file:
            file_contents = file.read()
            

        self.text_edit.te.setPlainText(file_contents)

        self.text_edit.setWindowTitle("Text Editor - " + selected_date)
        self.text_edit.show()


class Widget(QWidget):
    def __init__(self):
        super().__init__()
       

        with open("Diffnes.qss", "r") as file:  
            self.setStyleSheet(file.read())
        self.setWindowTitle("Journal App")
        self.setFixedSize(1280, 720)
        
        icon = QIcon("Images\\journal.png")
        self.setWindowIcon(icon)

        self.list_widget = ListW() 

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.list_widget) 
        

        button_font = QFont()
        button_font.setPointSize(13)
        main_button = QPushButton("Open Texteditor")
        main_button.setFont(button_font)
        main_button.setFixedHeight(50)
        main_button.clicked.connect(self.on_pushButton_clicked)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(main_button)
        self.setLayout(v_layout)

        with open("Diffnes.qss", "r") as file:
            main_button.setStyleSheet(file.read())
            self.list_widget.setStyleSheet(file.read())
    
    def on_pushButton_clicked(self):
        editor = TextE(self)
        editor.show()











        




