# Nama  : Pudael Zikri
# NIM   : F1D02310088
# Kelas : C

import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLineEdit,
    QCheckBox
)
from PySide6.QtCore import Qt


VALID_USERNAME = "admin"
VALID_PASSWORD = "12345"


class FormLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Login")
        self.setFixedWidth(320) # Mengurangi lebar jendela utama
        self.setFixedHeight(340)

        self.setStyleSheet("background-color: #f5f5f5; font-family: Arial, sans-serif;")

        css_header = """
            QLabel {
                background-color: #8e44ad;
                color: white;
                font-size: 16px;
                font-weight: bold;
                padding: 14px;
                border-radius: 8px;
                letter-spacing: 1px;
            }
        """

        css_label = "font-size: 13px; color: #333; background: transparent;"

        css_input_normal = """
            QLineEdit {
                background-color: #eaffea;
                border: 2px solid #a8e6a3;
                border-radius: 6px;
                padding: 10px 12px;
                font-size: 15px;
                color: #000000;
            }
            QLineEdit:focus { border-color: #4caf50; }
        """

        css_input_error = """
            QLineEdit {
                background-color: #ffffff;
                border: 2px solid #e74c3c;
                border-radius: 6px;
                padding: 10px 12px;
                font-size: 15px;
                color: #000000;
            }
            QLineEdit:focus { border-color: #c0392b; }
        """

        css_checkbox = """
            QCheckBox {
                font-size: 13px;
                color: #333;
                background: transparent;
            }
            QCheckBox::indicator {
                width: 14px;
                height: 14px;
                border: 1px solid #777;
                border-radius: 2px;
                background-color: white;
            }
            QCheckBox::indicator:checked {
                border-color: #333;
            }
        """

        css_btn_login = """
            QPushButton {
                background-color: #27ae60;
                color: white;
                font-size: 14px;
                font-weight: normal;
                padding: 10px 15px;
                border-radius: 6px;
                border: none;
            }
            QPushButton:hover   { background-color: #1e8449; }
            QPushButton:pressed { background-color: #196f3d; }
        """

        css_btn_reset = """
            QPushButton {
                background-color: #95a5a6;
                color: white;
                font-size: 14px;
                font-weight: normal;
                padding: 10px 15px;
                border-radius: 6px;
                border: none;
            }
            QPushButton:hover   { background-color: #7f8c8d; }
            QPushButton:pressed { background-color: #6c7a7d; }
        """

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(10)

        header = QLabel("LOGIN")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header.setStyleSheet(css_header)
        main_layout.addWidget(header)

        lbl_username = QLabel("Username:")
        lbl_username.setStyleSheet(css_label)
        main_layout.addWidget(lbl_username)

        self.input_username = QLineEdit()
        self.input_username.setPlaceholderText("Masukkan username")
        self.input_username.setStyleSheet(css_input_normal)
        main_layout.addWidget(self.input_username)

        lbl_password = QLabel("Password:")
        lbl_password.setStyleSheet(css_label)
        main_layout.addWidget(lbl_password)

        self.input_password = QLineEdit()
        self.input_password.setPlaceholderText("Masukkan password")
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)  
        self.input_password.setStyleSheet(css_input_normal)
        main_layout.addWidget(self.input_password)

        self._css_normal = css_input_normal
        self._css_error  = css_input_error

        self.chk_show_password = QCheckBox("Tampilkan Password")
        self.chk_show_password.setStyleSheet(css_checkbox)
        main_layout.addWidget(self.chk_show_password)

        # Tombol Login & Reset
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(10)

        self.btn_login = QPushButton("Login")
        self.btn_reset = QPushButton("Reset")
        self.btn_login.setStyleSheet(css_btn_login)
        self.btn_reset.setStyleSheet(css_btn_reset)

        btn_layout.addWidget(self.btn_login)
        btn_layout.addWidget(self.btn_reset)
        main_layout.addLayout(btn_layout)

        self.label_pesan = QLabel("")
        self.label_pesan.setWordWrap(True)
        self.label_pesan.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        self.label_pesan.setVisible(False)
        main_layout.addWidget(self.label_pesan)

        self.setLayout(main_layout)

        self.chk_show_password.stateChanged.connect(self.toggle_password)
        self.btn_login.clicked.connect(self.proses_login)
        self.btn_reset.clicked.connect(self.reset_form)

    def toggle_password(self, state):
        """Tampilkan atau sembunyikan karakter password sesuai status checkbox."""
        if state == Qt.CheckState.Checked.value:
            self.input_password.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.input_password.setEchoMode(QLineEdit.EchoMode.Password)

    # login
    def proses_login(self):
        """Validasi username dan password, lalu tampilkan pesan sukses atau gagal."""
        username = self.input_username.text().strip()
        password = self.input_password.text()

        if username == VALID_USERNAME and password == VALID_PASSWORD:
            # ketika login berhasil
            self.input_username.setStyleSheet(self._css_normal)
            self.input_password.setStyleSheet(self._css_normal)
            self.label_pesan.setText(f"Login berhasil! Selamat datang, {username}.")
            self.label_pesan.setStyleSheet("""
                QLabel {
                    background-color: #d4efdf;
                    border: 1px solid #27ae60;
                    border-left: 4px solid #27ae60;
                    border-radius: 6px;
                    padding: 10px 12px;
                    font-size: 13px;
                    color: #1e6e3a;
                }
            """)
        else:
            # ketika login gagal
            self.input_username.setStyleSheet(self._css_error)
            self.input_password.setStyleSheet(self._css_error)
            self.label_pesan.setText("Login gagal! Username atau password salah.")
            self.label_pesan.setStyleSheet("""
                QLabel {
                    background-color: #fde8e8;
                    border: 1px solid #e74c3c;
                    border-left: 4px solid #e74c3c;
                    border-radius: 6px;
                    padding: 10px 12px;
                    font-size: 13px;
                    color: #a93226;
                }
            """)

        self.label_pesan.setVisible(True)

    def reset_form(self):
        """Kosongkan semua input, kembalikan tampilan ke kondisi awal."""
        self.input_username.clear()
        self.input_password.clear()
        self.input_username.setStyleSheet(self._css_normal)
        self.input_password.setStyleSheet(self._css_normal)
        self.chk_show_password.setChecked(False)
        self.label_pesan.setVisible(False)
        self.label_pesan.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FormLogin()
    window.show()
    sys.exit(app.exec())