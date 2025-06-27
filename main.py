import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QThread
from ui.monitor_ui import Ui_MainWindow
from worker import SystemMonitoring, SpeedTest  # импортируем SpeedTest


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Подключаем кнопку к обработчику
        self.ui.start_test_B.clicked.connect(self.speed_test)

        # Поток и объект для мониторинга
        self.thread = QThread()
        self.worker = SystemMonitoring()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.stats_ready.connect(self.update_system_monitoring)
        self.thread.start()

        # Здесь будем хранить поток и воркер для спидтеста
        self.speed_thread = None
        self.speed_worker = None


    def update_system_monitoring(self, stats):
        self.ui.cpu_L.setText(f"{stats['CPU']}")
        self.ui.ram_L.setText(f"{stats['RAM']}")
        self.ui.disk_L.setText(f"{stats['Disk']}")
        self.ui.gpu_L.setText(f"{stats['GPU']}")
        self.ui.network_L.setText(f"{stats['Network']}")


    def speed_test(self):
        # Отключаем кнопку, чтобы нельзя было запустить тест повторно
        self.ui.start_test_B.setEnabled(False)

        # Создаём новый поток и объект SpeedTest
        self.speed_thread = QThread()
        self.speed_worker = SpeedTest()
        self.speed_worker.moveToThread(self.speed_thread)

        # Подключаем запуск и сигнал результата
        self.speed_thread.started.connect(self.speed_worker.run)
        self.speed_worker.stats_ready.connect(self.update_speed_network)

        # По завершении работы - останавливаем поток
        self.speed_worker.stats_ready.connect(self.speed_thread.quit)

        # Очистка объектов после завершения потока
        self.speed_thread.finished.connect(self.speed_worker.deleteLater)
        self.speed_thread.finished.connect(self.speed_thread.deleteLater)

        # Разблокируем кнопку после окончания теста
        self.speed_thread.finished.connect(lambda: self.ui.start_test_B.setEnabled(True))

        # Запускаем поток
        self.speed_thread.start()


    def update_speed_network(self, stats):
        # Обрабатываем результат спидтеста — выводим в UI или консоль
        self.ui.Download_L.setText(f"{stats.get('Download')}")
        self.ui.Upload_L.setText(f"{stats.get('Upload')}")
        self.ui.Ping_L.setText(f"{stats.get('Ping')}")
        self.ui.start_test_B.setEnabled(True)


    def closeEvent(self, event):
        self.worker.stop()
        self.thread.quit()
        self.thread.wait()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
