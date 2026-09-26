import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Automotive ECU Monitor",
    layout="wide"
)

st.title("🚗 Automotive Sensor Monitoring & ECU")

try:

    df = pd.read_csv("data/sensor_data.csv")

    latest = df.iloc[-1]

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Temperature",
        f"{latest['temperature']} °C"
    )

    col2.metric(
        "Pressure",
        f"{latest['pressure']} bar"
    )

    col3.metric(
        "Voltage",
        f"{latest['voltage']} V"
    )

    col4.metric(
        "RPM",
        int(latest["rpm"])
    )

    st.divider()

    if latest["fault_code"] == "F000":

        st.success("ECU STATUS: NORMAL")

    else:

        st.error(
            f"FAULT: {latest['fault']} "
            f"({latest['fault_code']})"
        )

    st.subheader("Temperature Trend")

    st.line_chart(
        df["temperature"]
    )

    st.subheader("RPM Trend")

    st.line_chart(
        df["rpm"]
    )

    st.subheader("Voltage Trend")

    st.line_chart(
        df["voltage"]
    )

    st.subheader("Fault History")

    fault_df = df[df["fault_code"] != "F000"]

    st.dataframe(
        fault_df.tail(20),
        use_container_width=True
    )

except FileNotFoundError:

    st.warning(
        "No sensor data found. Run main.py first."
    )