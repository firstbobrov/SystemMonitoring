import psutil
import requests
import speedtest
import GPUtil
import socket
from getmac import get_mac_address


def get_system_stats():
    """Сбор общей статистики системы"""
    # CPU, RAM, Disk, Network (старая логика)
    cpu_percent = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    network = psutil.net_io_counters()

    # GPU (новая часть)
    gpu_info = "Нет данных"
    try:
        gpus = GPUtil.getGPUs()
        if gpus:
            gpu = gpus[0]  # Берём первую GPU
            gpu_info = f"{gpu.load * 100:.1f}% | {gpu.temperature}°C | {gpu.memoryUsed:.1f}MB / {gpu.memoryTotal:.1f}MB"
    except:
        pass  # Если GPU нет или ошибка

    return {
        "CPU": f"{cpu_percent}%",
        "RAM": f"{ram.used / (1024 ** 3):.2f} GB / {ram.total / (1024 ** 3):.2f} GB",
        "Disk": f"{disk.used / (1024 ** 3):.2f} GB / {disk.total / (1024 ** 3):.2f} GB",
        "Network": f"Sent: {network.bytes_sent / (1024 ** 2):.2f} MB | Recv: {network.bytes_recv / (1024 ** 2):.2f} MB",
        "GPU": gpu_info  # Добавляем GPU в отчёт
    }


def get_network_speed():
    """Тест скорости интернета с обработкой ошибок"""
    try:
        st = speedtest.Speedtest(timeout=15)

        # Пробуем вручную задать сервер (если автоматический выбор не работает)
        # Пример ID сервера можно найти тут: https://www.speedtest.net/servers
        # st.get_servers([1234])  # Раскомментируйте и укажите ID сервера

        st.get_best_server()

        # Тестируем скорость
        download_speed = st.download() / (10 ** 6)  # Мбит/с
        upload_speed = st.upload() / (10 ** 6)  # Мбит/с
        ping = st.results.ping

        return {
            "Download": f"{download_speed:.2f} Мбит/с",
            "Upload": f"{upload_speed:.2f} Мбит/с",
            "Ping": f"{ping:.2f} мс",
            "Public_IP": get_public_ip(),
            "Local_IP": get_local_ip(),
            "Mac": get_mac()
        }

    except Exception as e:
        # Альтернативный замер через psutil (только локальный трафик)
        net_io = psutil.net_io_counters()
        return {
            "error": str(e),
            "local_network": f"Sent: {net_io.bytes_sent / (1024 ** 2):.2f} MB | Recv: {net_io.bytes_recv / (1024 ** 2):.2f} MB"
        }


def get_local_ip():
    """Получает локальный IP-адрес компьютера"""
    try:
        # Создаём временный сокет для определения IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # Подключаемся к публичному DNS (Google)
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception as e:
        return f"Ошибка: {str(e)}"


def get_public_ip():
    """Получает публичный IP-адрес через внешний сервис"""
    try:
        response = requests.get("https://api.ipify.org?format=json", timeout=5)
        return response.json()["ip"]
    except Exception as e:
        return f"Ошибка: {str(e)}"


def get_mac():
    return get_mac_address()


if __name__ == '__main__':
    print(get_system_stats())
    print(get_network_speed())
    print("Локальный IP:", get_local_ip())
    print("Публичный IP:", get_public_ip())
    print("Мак адрес:", get_mac())