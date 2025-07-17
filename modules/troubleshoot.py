from utils.device_connector import connect_device

def troubleshoot_ospf(device):
    conn = connect_device(device)
    output = conn.send_command("show ip ospf neighbor")
    conn.disconnect()
    return output
