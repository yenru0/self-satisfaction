from PySide2.QtWidgets import QApplication

import sys
import os
import json

from ui.main import Main

__version__ = "0.9"


if not os.path.exists("resources/"):
    os.makedirs("resources/")

if __name__ == "__main__":

    app = QApplication(sys.argv)

    runner = Main(json.load(open("preference.json", "r", encoding="utf-8")))
    runner.show()

    sys.exit(app.exec_())