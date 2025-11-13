""" Import of package needed """
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
import sys
from controller.solving_controller import SolverController
from logic.solving import QuadraticSolver
from ui.frame import SolverUI

def main():
    app = QApplication(sys.argv)
    solver = QuadraticSolver()
    controller = SolverController(solver)
    ui = SolverUI(controller)
    ui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()