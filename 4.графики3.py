import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class WaveInterferencePlotter(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Интерференция')
        self.setGeometry(100, 100, 650, 600)

        layout = QVBoxLayout()

        self.amplitude1_label = QLabel('Амплитуда 1,м:')
        self.amplitude1_input = QLineEdit()
        layout.addWidget(self.amplitude1_label)
        layout.addWidget(self.amplitude1_input)

        self.frequency1_label = QLabel('Частота 1,Гц):')
        self.frequency1_input = QLineEdit()
        layout.addWidget(self.frequency1_label)
        layout.addWidget(self.frequency1_input)

        self.phase1_label = QLabel('Фаза 1,градусы:')
        self.phase1_input = QLineEdit()
        layout.addWidget(self.phase1_label)
        layout.addWidget(self.phase1_input)

        self.amplitude2_label = QLabel('Амплитуда 2, м:')
        self.amplitude2_input = QLineEdit()
        layout.addWidget(self.amplitude2_label)
        layout.addWidget(self.amplitude2_input)

        self.frequency2_label = QLabel('Частота 2,Гц:')
        self.frequency2_input = QLineEdit()
        layout.addWidget(self.frequency2_label)
        layout.addWidget(self.frequency2_input)

        self.phase2_label = QLabel('Фаза 2,градусы:')
        self.phase2_input = QLineEdit()
        layout.addWidget(self.phase2_label)
        layout.addWidget(self.phase2_input)

        self.plot_button = QPushButton('интерференция')
        self.plot_button.clicked.connect(self.plot_interference)
        layout.addWidget(self.plot_button)

        self.canvas = FigureCanvas(plt.Figure())
        layout.addWidget(self.canvas)

        self.setLayout(layout)

    def plot_interference(self):
        try:
            A1 = float(self.amplitude1_input.text())
            f1 = float(self.frequency1_input.text())
            phi1 = float(self.phase1_input.text())
            A2 = float(self.amplitude2_input.text())
            f2 = float(self.frequency2_input.text())
            phi2 = float(self.phase2_input.text())
        except ValueError:
            return  

        phi1_rad = np.radians(phi1)
        phi2_rad = np.radians(phi2)

        t = np.linspace(0, 10, 1000)  

        wave1 = A1 * np.sin(2 * np.pi * f1 * t + phi1_rad)
        wave2 = A2 * np.sin(2 * np.pi * f2 * t + phi2_rad)
        resultant_wave = wave1 + wave2

        self.canvas.figure.clear()
        ax = self.canvas.figure.add_subplot(111)
        ax.plot(t, wave1, label='Волна 1', color='red')
        ax.plot(t, wave2, label='Волна 2', color='orange')
        ax.plot(t, resultant_wave, label='Результирующая', color='green')
        ax.set_xlabel('время, с')
        ax.set_ylabel('смещение, м')
        ax.set_title('Интерференция двух гармонических волн')
        ax.grid()
        ax.legend()

        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WaveInterferencePlotter()
    window.show()
    sys.exit(app.exec_())
