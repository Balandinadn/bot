import sys
import numpy as np
import matplotlib.pyplot as plt

from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QMessageBox
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None):
        fig = Figure()
        self.ax = fig.add_subplot(111)
        super().__init__(fig)
        self.setParent(parent)

    def plot(self, x, y):
        self.ax.clear()
        self.ax.plot(x, y)
        self.ax.set_title('График функции')
        self.draw()


class FunctionPlotter(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('График функции')
        self.setGeometry(800, 800, 800, 800)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        input_layout = QHBoxLayout()
        input_layout.addWidget(QLabel("Функция y ="))
        self.function_input = QLineEdit("x**2")
        input_layout.addWidget(self.function_input)

        input_layout.addWidget(QLabel("X min:"))
        self.x_min_input = QLineEdit("-15")
        input_layout.addWidget(self.x_min_input)

        input_layout.addWidget(QLabel("X max:"))
        self.x_max_input = QLineEdit("15")
        input_layout.addWidget(self.x_max_input)

        self.plot_button = QPushButton("Построить график")
        self.plot_button.clicked.connect(self.plot_function)
        input_layout.addWidget(self.plot_button)

        layout.addLayout(input_layout)

        self.canvas = PlotCanvas(self)
        layout.addWidget(self.canvas)

        self.setLayout(layout)

    def plot_function(self):
        try:
            expr = self.function_input.text()
            x_min = float(self.x_min_input.text())
            x_max = float(self.x_max_input.text())

            if x_min >= x_max:
                raise ValueError("X_min должен быть меньше X_max")

            x = np.linspace(x_min, x_max, 400)
            safe_dict = {
                'x': x,
                'np': np,
                'sin': np.sin,
                'cos': np.cos,
                'exp': np.exp,
                'log': np.log,
                'sqrt': np.sqrt
            }

            y = eval(expr, {"__builtins__": {}}, safe_dict)
            self.canvas.plot(x, y)

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка построения графика:\n{e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FunctionPlotter()
    window.show()
    sys.exit(app.exec_())
