import psutil
import speedtest
import GPUtil


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
    """Тест скорости интернета"""
    try:
        st = speedtest.Speedtest(timeout=10)
        st.get_servers()  # This might help in some cases
        st.get_best_server()
        st.download()
        st.upload()

        download_speed = st.results.download / (10 ** 6)  # в Мбит/с
        upload_speed = st.results.upload / (10 ** 6)  # в Мбит/с

        return {
            "Download": f"{download_speed:.2f} Мбит/с",
            "Upload": f"{upload_speed:.2f} Мбит/с",
            "Ping": f"{st.results.ping:.2f} мс"
        }
    except Exception as e:
        return {"error": str(e)}


if __name__ == '__main__':
    print(get_system_stats())
    print(get_network_speed())