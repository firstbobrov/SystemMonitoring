from core.file_manager import write_file_from_dict, read_json_file
from core.monitor import get_system_stats, get_network_speed
from datetime import datetime

def logging_system_monitor(dictionary):
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = read_json_file('system_monitor.json')
    dictionary['date_time'] = current_datetime
    data = [dictionary] + data
    write_file_from_dict(data, 'system_monitor.json')
    return data


def logging_network_speed(dictionary):
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = read_json_file('network_speed.json')
    dictionary['date_time'] = current_datetime
    data = [dictionary] + data
    write_file_from_dict(data, 'network_speed.json')
    return data



if __name__ == '__main__':
    monitor = get_system_stats()
    print(logging_system_monitor(monitor))
    network = get_network_speed()
    print(logging_network_speed(network))
