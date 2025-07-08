import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from PySide6.QtCore import QThread, Qt
from PySide6.QtCharts import QChart, QChartView, QLineSeries, QValueAxis
from PySide6.QtGui import QPainter
from ui.monitor_ui import Ui_MainWindow
from worker import SystemMonitoring, SpeedTest, StaticValue
from core.logs import logging_system_monitor, logging_network_speed


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Инициализация переменных для графика
        self.time_counter = 0
        self.max_points = 30  # Количество точек на графике (30 секунд)

        # Инициализация графика CPU (теперь после инициализации переменных)
        self.init_cpu_chart()

        # Остальная инициализация
        self.init_static_data()
        self.ui.start_test_B.clicked.connect(self.speed_test)


        # Системный мониторинг
        self.thread = QThread()
        self.worker = SystemMonitoring()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.stats_ready.connect(self.update_system_monitoring)
        self.thread.start()

        # Переменные для спидтеста
        self.speed_thread = None
        self.speed_worker = None

        self.label_design()


    def label_design(self):
        """Установка стилей на два лэйбла!!! Это необходимая мера!!!"""
        style = """
            QLabel {
                color: white;
                font: 20px;
                font-weight: bold;
            }
        """
        self.ui.systemmonitor_L.setStyleSheet(style)
        self.ui.networkspeed_L.setStyleSheet(style)


    def init_cpu_chart(self):
        """Инициализация графика загрузки CPU"""
        # Создаем график
        self.chart = QChart()
        self.chart.setTitle("CPU Usage")
        self.chart.legend().hide()

        # Оси
        self.axis_x = QValueAxis()
        self.axis_x.setRange(0, self.max_points)
        self.axis_x.setTitleText("Time (s)")

        self.axis_y = QValueAxis()
        self.axis_y.setRange(0, 100)
        self.axis_y.setTitleText("Usage (%)")

        self.chart.addAxis(self.axis_x, Qt.AlignBottom)
        self.chart.addAxis(self.axis_y, Qt.AlignLeft)

        # Линия графика
        self.series = QLineSeries()
        self.series.setName("CPU Usage")
        self.chart.addSeries(self.series)
        self.series.attachAxis(self.axis_x)
        self.series.attachAxis(self.axis_y)

        # Виджет для отображения графика
        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)

        # Настройка layout для chart_widget
        if not self.ui.chart_widget.layout():
            self.ui.chart_widget.setLayout(QVBoxLayout())

        # Очистка и добавление графика
        layout = self.ui.chart_widget.layout()
        while layout.count():
            layout.takeAt(0)
        layout.addWidget(self.chart_view)
        layout.setContentsMargins(0, 0, 0, 0)


    # ... остальные методы без изменений ...
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
        """Обновление динамической информации и графика"""
        logging_system_monitor(stats)

        # Обновляем текстовые метки
        self.ui.cpu_L.setText(f"{stats.get('CPU', 'N/A')}")
        self.ui.ram_L.setText(f"{stats.get('RAM', 'N/A')}")
        self.ui.disk_L.setText(f"{stats.get('Disk', 'N/A')}")
        self.ui.gpu_L.setText(f"{stats.get('GPU', 'N/A')}")
        self.ui.network_L.setText(f"{stats.get('Network', 'N/A')}")

        # Обновляем график CPU
        try:
            cpu_usage = float(stats.get('CPU', '0').replace('%', ''))
            self.update_cpu_chart(cpu_usage)
        except ValueError:
            pass

    def update_cpu_chart(self, cpu_usage):
        """Обновление графика загрузки CPU"""
        self.time_counter += 1

        # Добавляем новую точку
        self.series.append(self.time_counter, cpu_usage)

        # Если точек больше, чем max_points, удаляем самую старую
        if self.series.count() > self.max_points:
            self.series.remove(0)

        # Всегда показываем окно из max_points последних точек
        if self.time_counter > self.max_points:
            self.axis_x.setRange(self.time_counter - self.max_points + 1, self.time_counter)
        else:
            self.axis_x.setRange(1, self.max_points)

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