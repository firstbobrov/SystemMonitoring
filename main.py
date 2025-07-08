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

        # Подключаем обработчики для переключения языка
        self.ui.actionEN_2.triggered.connect(self.set_english_language)
        self.ui.actionRU_2.triggered.connect(self.set_russian_language)

        # Подключаем обработчики для экспорта данных
        # self.ui.actionWord.triggered.connect(self.export_to_word)
        # self.ui.actionExcel.triggered.connect(self.export_to_excel)
        # self.ui.actiontxt.triggered.connect(self.export_to_txt)
        # self.ui.actionpdf.triggered.connect(self.export_to_pdf)
        # self.ui.actionhtml.triggered.connect(self.export_to_html)

        # Собираем данные для экспорта
        self.export_data = {
            "CPU": [],
            "RAM": [],
            "Disk": [],
            "GPU": [],
            "Network": [],
            "Download": [],
            "Upload": [],
            "Ping": [],
            "Public_IP": [],
            "Local_IP": [],
            "MAC": [],
            "Timestamp": []
        }

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


    def set_english_language(self):
        """Установка английского языка"""
        # Кнопки верхнего меню
        self.ui.file_MB.setTitle("File")
        self.ui.export_MB.setTitle("Export")
        self.ui.params_MB.setTitle("Settings")
        self.ui.lang_MB.setTitle("Language")
        self.ui.actionEN_2.setText("English")
        self.ui.actionRU_2.setText("Russian")
        # Надписи
        self.ui.publicIP_L.setText("Public IP:")
        self.ui.localIP_L.setText("Local IP:")
        self.ui.mac_L.setText("MAC address:")
        self.ui.systemmonitor_L.setText("System monitor")
        self.ui.cpu_L_2.setText("CPU:")
        self.ui.ram_L_2.setText("RAM:")
        self.ui.disk_L_2.setText("Disk:")
        self.ui.gpu_L_2.setText("GPU:")
        self.ui.network_L_2.setText("Network:")
        self.ui.networkspeed_L.setText("Network speed")
        self.ui.download_L.setText("Download:")
        self.ui.upload_L.setText("Upload:")
        self.ui.ping_L.setText("Ping:")
        # Кнопки
        self.ui.start_test_B.setText("Start test")


    def set_russian_language(self):
        """Установка русского языка"""
        # Кнопки верхнего меню
        self.ui.file_MB.setTitle("Файл")
        self.ui.export_MB.setTitle("Экспорт")
        self.ui.params_MB.setTitle("Настройки")
        self.ui.lang_MB.setTitle("Язык")
        self.ui.actionEN_2.setText("Английский")
        self.ui.actionRU_2.setText("Русский")
        # Надписи
        self.ui.publicIP_L.setText("Публичный IP:")
        self.ui.localIP_L.setText("Локальный IP:")
        self.ui.mac_L.setText("Мак адрес:")
        self.ui.systemmonitor_L.setText("Мониторинг системы")
        self.ui.cpu_L_2.setText("Процессор:")
        self.ui.ram_L_2.setText("Оперативная память:")
        self.ui.disk_L_2.setText("Диск:")
        self.ui.gpu_L_2.setText("Видеокарта:")
        self.ui.network_L_2.setText("Сеть:")
        self.ui.networkspeed_L.setText("Тест скорость сети")
        self.ui.download_L.setText("Скачивание:")
        self.ui.upload_L.setText("Загрузка:")
        self.ui.ping_L.setText("Пинг:")
        # Кнопки
        self.ui.start_test_B.setText("Начать тест")


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
        # для экспорта
        self.export_data["Public_IP"] = stats.get('Public_IP', 'N/A')
        self.export_data["Local_IP"] = stats.get('Local_IP', 'N/A')
        self.export_data["MAC"] = stats.get('Mac', 'N/A')


    def update_system_monitoring(self, stats):
        """Обновление динамической информации и графика"""
        logging_system_monitor(stats)

        # Обновляем текстовые метки
        self.ui.cpu_L.setText(f"{stats.get('CPU', 'N/A')}")
        self.ui.ram_L.setText(f"{stats.get('RAM', 'N/A')}")
        self.ui.disk_L.setText(f"{stats.get('Disk', 'N/A')}")
        self.ui.gpu_L.setText(f"{stats.get('GPU', 'N/A')}")
        self.ui.network_L.setText(f"{stats.get('Network', 'N/A')}")
        # для экспорта
        self.export_data["CPU"] = stats.get('CPU', 'N/A')
        self.export_data["RAM"] = stats.get('RAM', 'N/A')
        self.export_data["Disk"] = stats.get('Disk', 'N/A')
        self.export_data["GPU"] = stats.get('GPU', 'N/A')
        self.export_data["Network"] = stats.get('Network', 'N/A')
        self.export_data["Timestamp"] = stats.get('date_time', 'N/A')


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
        # для экспорта
        self.export_data["Download"] = stats.get('Download', 'N/A')
        self.export_data["Upload"] = stats.get('Upload', 'N/A')
        self.export_data["Ping"] = stats.get('Ping', 'N/A')
        self.export_data["Timestamp"] = stats.get('date_time', 'N/A')
        print(self.export_data)


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