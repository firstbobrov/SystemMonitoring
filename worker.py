from PySide6.QtCore import QObject, Signal, Slot
import time
from core.monitor import get_system_stats, get_network_speed


class SystemMonitoring(QObject):
    stats_ready = Signal(dict)

    def __init__(self):
        super().__init__()
        self._running = True

    @Slot()
    def run(self):
        while self._running:
            stats = get_system_stats()
            self.stats_ready.emit(stats)
            time.sleep(1)

    def stop(self):
        self._running = False



class SpeedTest(QObject):
    stats_ready = Signal(dict)

    def __init__(self):
        super().__init__()

    @Slot()
    def run(self):
        stats = get_network_speed()
        self.stats_ready.emit(stats)
        print(stats)