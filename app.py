import streamlit as st
import yaml
from modules import config_apply, troubleshoot, audit
from utils.claude_parser import get_action_from_prompt

def load_devices():
    with open("configs/device_inventory.yaml") as f:
        return yaml.safe_load(f)["devices"]

st.set_page_config(page_title="🧠 MCP Assistant", layout="wide")
st.title("🧠 MCP Network Assistant (Claude + Streamlit)")

user_input = st.text_input("💬 Enter command (e.g., 'Configure OSPF')")

if user_input:
    st.markdown("## 🤖 Claude Interpretation")
    action = get_action_from_prompt(user_input)
    st.success(f"Claude interpreted action: **{action}**")

    devices = load_devices()
    st.markdown("## 🛠️ Result")

    if action == "configure":
        for device in devices:
            output = config_apply.apply_config(device, [
                "interface loopback0",
                "ip address 1.1.1.1 255.255.255.0",
                "no shut"
            ])
            st.code(output, language="bash")

    elif action == "troubleshoot":
        for device in devices:
            output = troubleshoot.troubleshoot_ospf(device)
            st.code(output, language="bash")

    elif action == "audit":
        for device in devices:
            audit.audit_config(device)
            st.success(f"{device['host']} config saved in logs/")

    else:
        st.error("❌ Could not determine valid action from Claude.")
