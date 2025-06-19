import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer
from ui.monitor_ui import Ui_MainWindow
from core.monitor import get_system_stats


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.monitor = {}

        # Таймер для обновления данных
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_data)
        self.timer.start(1000)

    def update_data(self):
        """Обновляет системные показатели"""
        self.monitor = get_system_stats()
        print(1)
        stats = self.monitor
        self.ui.cpu_L.setText(f"{stats['CPU']}")
        self.ui.ram_L.setText(f"{stats['RAM']}")
        self.ui.disk_L.setText(f"{stats['Disk']}")
        self.ui.gpu_L.setText(f"{stats['GPU']}")
        self.ui.network_L.setText(f"{stats['Network']}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())