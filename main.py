import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QThread
from ui.monitor_ui import Ui_MainWindow
from worker import SystemMonitoring, SpeedTest, StaticValue  # Добавляем импорт StaticValue
from core.logs import logging_system_monitor, logging_network_speed
from core.monitor import get_mac


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Запускаем воркер для статических данных (IP/MAC)
        self.init_static_data()

        # Подключаем кнопку к обработчику
        self.ui.start_test_B.clicked.connect(self.speed_test)

        # Поток и объект для мониторинга системы
        self.thread = QThread()
        self.worker = SystemMonitoring()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.stats_ready.connect(self.update_system_monitoring)
        self.thread.start()

        # Переменные для спидтеста
        self.speed_thread = None
        self.speed_worker = None



    def init_static_data(self):
        """Инициализация статических данных (IP/MAC)"""
        self.static_thread = QThread()
        self.static_worker = StaticValue()
        self.static_worker.moveToThread(self.static_thread)

        # Подключаем сигналы
        self.static_thread.started.connect(self.static_worker.run)
        self.static_worker.stats_ready.connect(self.update_static_info)
        self.static_worker.stats_ready.connect(self.static_thread.quit)

        # Очистка после завершения
        self.static_thread.finished.connect(self.static_worker.deleteLater)
        self.static_thread.finished.connect(self.static_thread.deleteLater)

        # Запускаем поток
        self.static_thread.start()

    def update_static_info(self, stats):
        """Обновление статической информации (IP/MAC)"""
        self.ui.PublicIP_L.setText(f"{stats.get('Public_IP', 'N/A')}")
        self.ui.LocalIP_L.setText(f"{stats.get('Local_IP', 'N/A')}")
        self.ui.MacAddr_L.setText(f"{stats.get('Mac', 'N/A')}")

    def update_system_monitoring(self, stats):
        """Обновление динамической информации (CPU/RAM и т.д.)"""
        logging_system_monitor(stats)
        self.ui.cpu_L.setText(f"{stats.get('CPU', 'N/A')}")
        self.ui.ram_L.setText(f"{stats.get('RAM', 'N/A')}")
        self.ui.disk_L.setText(f"{stats.get('Disk', 'N/A')}")
        self.ui.gpu_L.setText(f"{stats.get('GPU', 'N/A')}")
        self.ui.network_L.setText(f"{stats.get('Network', 'N/A')}")


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
        logging_network_speed(stats)
        self.ui.Download_L.setText(f"{stats.get('Download', 'Сервис сейчас недоступен')}")
        self.ui.Upload_L.setText(f"{stats.get('Upload', 'Сервис сейчас недоступен')}")
        self.ui.Ping_L.setText(f"{stats.get('Ping', 'Сервис сейчас недоступен')}")
        self.ui.PublicIP_L.setText(f"{stats.get('Public_IP', self.ui.PublicIP_L.text())}")
        self.ui.LocalIP_L.setText(f"{stats.get('Local_IP', self.ui.LocalIP_L.text())}")
        self.ui.MacAddr_L.setText(f"{stats.get('Mac', self.ui.MacAddr_L.text())}")
        self.ui.start_test_B.setEnabled(True)


    def closeEvent(self, event):
        """Обработчик закрытия окна"""
        self.worker.stop()
        self.thread.quit()
        self.thread.wait()
        if hasattr(self, 'static_thread') and self.static_thread.isRunning():
            self.static_thread.quit()
            self.static_thread.wait()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())