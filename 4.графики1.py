import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class TrajectoryPlotter(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Движение')
        self.setGeometry(100, 100, 750, 600)

        layout = QVBoxLayout()

        self.initial_speed_label = QLabel('Нач скорость, м/с:')
        self.initial_speed_input = QLineEdit()
        layout.addWidget(self.initial_speed_label)
        layout.addWidget(self.initial_speed_input)

        self.angle_label = QLabel('Угол, градусы:')
        self.angle_input = QLineEdit()
        layout.addWidget(self.angle_label)
        layout.addWidget(self.angle_input)

        self.plot_button = QPushButton('траектория')
        self.plot_button.clicked.connect(self.plot_trajectory)
        layout.addWidget(self.plot_button)

        self.canvas = FigureCanvas(plt.Figure())
        layout.addWidget(self.canvas)

        self.setLayout(layout)

    def plot_trajectory(self):
        try:
            initial_speed = float(self.initial_speed_input.text())
            angle = float(self.angle_input.text())
        except ValueError:
            return
     
        angle_rad = np.radians(angle)

        g = 10
        time_of_flight = 2 * initial_speed * np.sin(angle_rad) / g
        t = np.linspace(0, time_of_flight, num=100)  

        x = initial_speed * np.cos(angle_rad) * t
        y = initial_speed * np.sin(angle_rad) * t - 0.5 * g * t*2

        self.canvas.figure.clear()
        ax = self.canvas.figure.add_subplot(111)
        ax.plot(x, y)
        ax.set_xlabel('расстояние, м)')
        ax.set_ylabel('высота,м')
        ax.set_title('Траектория полета')
        ax.grid()

        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TrajectoryPlotter()
    window.show()
    sys.exit(app.exec_())
