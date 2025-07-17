from utils.device_connector import connect_device

def audit_config(device):
    conn = connect_device(device)
    config = conn.send_command("show running-config")
    conn.disconnect()
    with open(f"logs/{device['host']}_audit.txt", "w") as f:
        f.write(config)
