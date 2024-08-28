# main.py

from views.Login import Login

import sys
from PyQt5.QtWidgets import QApplication
def main():
    app = QApplication(sys.argv)

    login_window = Login()
    login_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()