from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QPushButton, QLabel

DEFAULT_OPEN_ARROW = "img/open_arrow.svg"
DEFAULT_CLOSE_ARROW = "img/close_arrow.svg"


class SideBar(QFrame):
    def __init__(self, parent):
        super(SideBar, self).__init__()
        self.parent = parent
        self.setParent(self.parent)
        self.setStyleSheet("background-color: white; max-width: 309px; min-width: 309px; background: #323639;")

        self.is_hidden = True
        self.setVisible(False)

        self.open_arrow_icon = QIcon(DEFAULT_OPEN_ARROW)
        self.closed_arrow_icon = QIcon(DEFAULT_CLOSE_ARROW)

        self.display_button = QPushButton()
        self.display_button.setParent(self.parent)
        self.display_button.setIcon(self.open_arrow_icon)
        self.display_button.setStyleSheet("background: #323639;border: none;border-top-left-radius: 8px; "
                                          "border-bottom-left-radius: 8px;max-width:30px;min-width: 30px;max-height: "
                                          "80px;min-height: 80px;")

        hello_label = QLabel("Sidebar")
        hello_label.setStyleSheet("font-size: 30px; color: white;")

        hello_layout = QHBoxLayout()
        hello_layout.setContentsMargins(0,0,0,0)
        hello_layout.setSpacing(0)
        hello_layout.addWidget(hello_label)
        hello_label.setAlignment(Qt.AlignCenter)

        #SIDEBAR LAYOUT
        self.setLayout(QVBoxLayout())
        self.layout().setSpacing(0)
        self.layout().setContentsMargins(20, 20, 20, 20)
        self.layout().addLayout(hello_layout)
        self.layout().addStretch()

        self.parent.resized.connect(self.parent_resized_event)
        self.display_button.clicked.connect(self.display_button_clicked)

    def set_open_icon(self, path):
        self.open_arrow_icon = QIcon(path)

    def set_closed_icon(self, path):
        self.closed_arrow_icon = QIcon(path)

    def display_button_clicked(self):
        if self.is_hidden:
            self.setVisible(True)
            self.display_button.setIcon(self.closed_arrow_icon)
        else:
            self.setVisible(False)
            self.display_button.setIcon(self.open_arrow_icon)

        self.is_hidden = not self.is_hidden
        self.display_button_update()

    def parent_resized_event(self):
        self.move(self.parent.width() - self.width(), 0)
        self.setFixedHeight(self.parent.height())

        self.display_button_update()

    def display_button_update(self):
        if not self.is_hidden:
            self.display_button.move(self.parent.width() - self.width() - self.display_button.width(), self.height()/2 - self.display_button.height()/2)
        else:
            self.display_button.move(self.parent.width() - self.display_button.width(), self.height()/2 - self.display_button.height()/2)