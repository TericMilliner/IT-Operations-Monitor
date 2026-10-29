
import streamlit as st
import psutil
import pandas as pd
import time
import platform
import socket
from datetime import datetime

from network import check_connection, network_traffic
from database import create_database, save_performance, get_history

# PAGE CONFIGURATION
st.set_page_config(
    page_title="IT Operations Center",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CUSTOM DESIGN
st.markdown("""
<style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    .metric-card {
        background-color: #172337;
        padding: 22px;
        border-radius: 12px;
        border: 1px solid #30415c;
        margin-bottom: 12px;
    }

    .metric-label {
        color: #a8bdd6;
        font-size: 15px;
        margin-bottom: 8px;
    }

    .metric-value {
        color: #ffffff;
        font-size: 30px;
        font-weight: 700;
    }

    .status-good {
        color: #4ade80;
        font-weight: 600;
    }

    .status-warning {
        color: #fbbf24;
        font-weight: 600;
    }

    .status-error {
        color: #f87171;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)


# SIDEBAR
with st.sidebar:
    st.title("IT Operations Center")
    st.caption("Infrastructure Monitoring")

    st.divider()

    st.subheader("System Information")
    st.write("Operating System:", platform.system())
    st.write("OS Version:", platform.release())
    st.write("CPU Cores:", psutil.cpu_count(logical=True))

    st.divider()

    st.subheader("Monitoring")
    st.success("Monitoring Active")
    st.caption("Refresh interval: approximately 6 seconds")

    st.divider()
    st.caption("Built with Python, Streamlit & SQLite")


# COLLECT SYSTEM DATA
cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage("C:\\").percent

connection = check_connection()
traffic = network_traffic()

# DATABASE
create_database()

save_performance(
    datetime.now().isoformat(timespec="seconds"),
    cpu,
    memory,
    disk,
    connection["status"],
    connection["response_time"]
)


# DASHBOARD HEADER
st.title("IT Operations Monitoring Center")
st.caption("Real-Time System & Network Monitoring")

all_healthy = (
    cpu <= 85
    and memory <= 85
    and disk <= 90
)

if all_healthy:
    st.success("System Health: All Resources Normal")
else:
    st.warning("System Health: Attention Required")


# PERFORMANCE METRIC CARDS
st.subheader("System Performance")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">CPU Usage</div>
        <div class="metric-value">{:.1f}%</div>
    </div>
    """.format(cpu), unsafe_allow_html=True)

    st.progress(min(cpu / 100, 1.0))

with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">RAM Usage</div>
        <div class="metric-value">{:.1f}%</div>
    </div>
    """.format(memory), unsafe_allow_html=True)

    st.progress(min(memory / 100, 1.0))

with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Disk Usage</div>
        <div class="metric-value">{:.1f}%</div>
    </div>
    """.format(disk), unsafe_allow_html=True)

    st.progress(min(disk / 100, 1.0))


# RESOURCE UTILIZATION
st.subheader("Resource Utilization")

performance = pd.DataFrame({
    "Component": ["CPU", "RAM", "Disk"],
    "Usage (%)": [cpu, memory, disk]
})

st.bar_chart(
    performance.set_index("Component"),
    y="Usage (%)",
    height=250
)


# SYSTEM HEALTH DETAILS
with st.expander("View Detailed System Health"):
    if cpu > 85:
        st.error("High CPU Usage Detected")
    else:
        st.success("CPU Status: Normal")

    if memory > 85:
        st.error("High RAM Usage Detected")
    else:
        st.success("RAM Status: Normal")

    if disk > 90:
        st.warning("Disk Storage Running Low")
    else:
        st.success("Disk Status: Normal")


# NETWORK MONITORING
st.divider()
st.subheader("Network Monitoring")

net1, net2, net3, net4 = st.columns(4)

with net1:
    if connection["status"] == "Online":
        st.success("Network: Online")
    else:
        st.error("Connection Test Failed")

with net2:
    response = connection["response_time"]

    if response is not None:
        st.metric("TCP Connection Time", f"{response} ms")
    else:
        st.metric("TCP Connection Time", "N/A")

with net3:
    st.metric("Data Sent", f"{traffic['sent_mb']} MB")

with net4:
    st.metric("Data Received", f"{traffic['received_mb']} MB")


# PERFORMANCE HISTORY
st.divider()
st.subheader("Performance History")

history = get_history(100)

if history:
    history_df = pd.DataFrame(
        history,
        columns=[
            "Timestamp",
            "CPU",
            "RAM",
            "Disk",
            "Network Status",
            "Response Time"
        ]
    )

    history_df["Timestamp"] = pd.to_datetime(
        history_df["Timestamp"]
    )

    st.line_chart(
        history_df.set_index("Timestamp")[
            ["CPU", "RAM", "Disk"]
        ],
        y_label="Usage (%)"
    )

    st.subheader("Recent Performance Records")

    st.dataframe(
        history_df.iloc[::-1],
        use_container_width=True,
        hide_index=True
    )

else:
    st.info("No performance history available yet.")


# FOOTER
st.divider()

st.caption(
    "Last Updated: "
    + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
)

st.caption(
    "IT Operations Monitor | Python | Streamlit | SQLite"
)

# AUTO REFRESH
time.sleep(5)
st.rerun()
