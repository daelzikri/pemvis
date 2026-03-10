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
    QMessageBox
)
from PySide6.QtCore import Qt


class KonversiSuhu(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Konversi Suhu")
        self.resize(400, 320)

        self.setStyleSheet("""
            QWidget {
                background-color: #ffffff;
                font-family: Arial, sans-serif;
            }
        """)

        css_header = """
            QLabel {
                background-color: #3a9fd8;
                color: white;
                font-size: 16px;
                font-weight: bold;
                padding: 14px;
                border-radius: 8px;
                letter-spacing: 1px;
            }
        """

        css_label = "font-size: 13px; color: #222; background: transparent;"

        css_input = """
            QLineEdit {
                background-color: #eaffea;
                border: 2px solid #a8e6a3;
                border-radius: 6px;
                padding: 10px 12px;
                font-size: 15px;
                color: #000000;
            }
            QLineEdit:focus {
                border-color: #4caf50;
            }
        """

        css_button = """
            QPushButton {
                background-color: #3498db;
                color: white;
                font-size: 14px;
                font-weight: normal;
                padding: 14px 16px;
                border-radius: 8px;
                border: none;
            }
            QPushButton:hover {
                background-color: #2178aa;
            }
            QPushButton:pressed {
                background-color: #155d87;
            }
        """

        css_result_box = """
            QWidget#resultBox {
                background-color: #d6eafb;
                border-left: 5px solid #003366;
                border-radius: 8px;
                padding: 4px;
            }
        """

        css_result_title = """
            QLabel {
                font-size: 13px;
                font-weight: bold;
                color: #1a5276;
                background: transparent;
            }
        """

        css_result_value = """
            QLabel {
                font-size: 13px;
                color: #1a3c5e;
                background: transparent;
            }
        """

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(25, 25, 25, 25)
        main_layout.setSpacing(15)

        # Header / Judul
        header = QLabel("KONVERSI SUHU")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header.setStyleSheet(css_header)
        main_layout.addWidget(header)

        # Label input
        label_input = QLabel("Masukkan Suhu (Celsius):")
        label_input.setStyleSheet(css_label)
        main_layout.addWidget(label_input)
        main_layout.addSpacing(-10) 

        # Field input
        self.input_celsius = QLineEdit()
        self.input_celsius.setPlaceholderText("Contoh: 100")
        self.input_celsius.setStyleSheet(css_input)
        main_layout.addWidget(self.input_celsius)

        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(10)

        self.btn_fahrenheit = QPushButton("Fahrenheit")
        self.btn_kelvin     = QPushButton("Kelvin")
        self.btn_reamur     = QPushButton("Reamur")

        for btn in (self.btn_fahrenheit, self.btn_kelvin, self.btn_reamur):
            btn.setStyleSheet(css_button)
            btn_layout.addWidget(btn)

        main_layout.addLayout(btn_layout)

        # Kotak hasil
        result_box = QWidget()
        result_box.setObjectName("resultBox")
        result_box.setStyleSheet(css_result_box)

        result_inner = QVBoxLayout(result_box)
        result_inner.setContentsMargins(18, 12, 18, 12)
        result_inner.setSpacing(15)

        self.label_hasil_title = QLabel("Hasil Konversi:")
        self.label_hasil_title.setStyleSheet(css_result_title)
        result_inner.addWidget(self.label_hasil_title)

        self.label_hasil = QLabel("—")
        self.label_hasil.setStyleSheet(css_result_value)
        result_inner.addWidget(self.label_hasil)

        main_layout.addWidget(result_box)

        self.setLayout(main_layout)

        self.btn_fahrenheit.clicked.connect(self.konversi_fahrenheit)
        self.btn_kelvin.clicked.connect(self.konversi_kelvin)
        self.btn_reamur.clicked.connect(self.konversi_reamur)

    def get_celsius(self):
        """
        Mengambil nilai Celsius dari input dan memvalidasinya.
        Mengembalikan float jika valid, None jika tidak valid.
        """
        teks = self.input_celsius.text().strip()
        if not teks:
            QMessageBox.warning(self, "Input Kosong", "Harap masukkan nilai suhu terlebih dahulu.")
            return None
        try:
            return float(teks)
        except ValueError:
            QMessageBox.critical(self, "Input Tidak Valid", "Input harus berupa angka.\nContoh: 100 atau -5.5")
            return None

    def konversi_fahrenheit(self):
        """Mengonversi Celsius ke Fahrenheit: F = (C × 9/5) + 32"""
        celsius = self.get_celsius()
        if celsius is None:
            return
        fahrenheit = (celsius * 9 / 5) + 32
        self.label_hasil.setText(f"{celsius} Celsius = {fahrenheit:.2f} Fahrenheit")

    def konversi_kelvin(self):
        """Mengonversi Celsius ke Kelvin: K = C + 273.15"""
        celsius = self.get_celsius()
        if celsius is None:
            return
        kelvin = celsius + 273.15
        self.label_hasil.setText(f"{celsius} Celsius = {kelvin:.2f} Kelvin")

    def konversi_reamur(self):
        """Mengonversi Celsius ke Reamur: R = C × 4/5"""
        celsius = self.get_celsius()
        if celsius is None:
            return
        reamur = celsius * 4 / 5
        self.label_hasil.setText(f"{celsius} Celsius = {reamur:.2f} Reamur")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KonversiSuhu()
    window.show()
    sys.exit(app.exec())