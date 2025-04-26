import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class HarmonicOscillatorPlotter(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Колебания гармонические')
        self.setGeometry(100, 100, 700, 800)

        layout = QVBoxLayout()

        self.amplitude_label = QLabel('Амплитуда, м):')
        self.amplitude_input = QLineEdit()
        layout.addWidget(self.amplitude_label)
        layout.addWidget(self.amplitude_input)

        self.frequency_label = QLabel('Частота, Гц:')
        self.frequency_input = QLineEdit()
        layout.addWidget(self.frequency_label)
        layout.addWidget(self.frequency_input)

        self.phase_label = QLabel('Фаза, град:')
        self.phase_input = QLineEdit()
        layout.addWidget(self.phase_label)
        layout.addWidget(self.phase_input)

        self.plot_button = QPushButton('Построить')
        self.plot_button.clicked.connect(self.plot_harmonic_oscillation)
        layout.addWidget(self.plot_button)

        self.canvas = FigureCanvas(plt.Figure())
        layout.addWidget(self.canvas)

        self.setLayout(layout)

    def plot_harmonic_oscillation(self):
        try:
            amplitude = float(self.amplitude_input.text())
            frequency = float(self.frequency_input.text())
            phase = float(self.phase_input.text())
        except ValueError:
            return  

        phase_rad = np.radians(phase)

        t = np.linspace(0, 10, 1000) 

        x = amplitude * np.sin(2 * np.pi * frequency * t + phase_rad)

        self.canvas.figure.clear()
        ax = self.canvas.figure.add_subplot(111)
        ax.plot(t, x)
        ax.set_xlabel('время, с')
        ax.set_ylabel('смещение,м')
        ax.set_title('График')
        ax.grid()

        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HarmonicOscillatorPlotter()
    window.show()
    sys.exit(app.exec_())
