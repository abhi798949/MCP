from utils.device_connector import connect_device

def apply_config(device, config_lines):
    conn = connect_device(device)
    output = conn.send_config_set(config_lines)
    conn.disconnect()
    return output
