import time

from sensor_simulator import generate_sensor_data
from ecu import diagnose
from logger import save_data


print("=" * 50)
print(" AUTOMOTIVE SENSOR MONITORING & ECU SIMULATOR")
print("=" * 50)


try:

    while True:

        # Generate sensor data
        sensor_data = generate_sensor_data("normal")

        # ECU diagnosis
        fault_code, fault_name = diagnose(sensor_data)

        # Display data
        print("\n------------------------------------")

        print(f"Temperature : {sensor_data['temperature']} °C")
        print(f"Pressure    : {sensor_data['pressure']} bar")
        print(f"Voltage     : {sensor_data['voltage']} V")
        print(f"RPM         : {sensor_data['rpm']}")

        print(f"Fault Code  : {fault_code}")
        print(f"ECU Status  : {fault_name}")

        # Save to CSV
        save_data(
            sensor_data,
            fault_code,
            fault_name
        )

        time.sleep(2)


except KeyboardInterrupt:

    print("\nECU simulation stopped.")
















# 
# FAULTY CODE 
# import time

# from sensor_simulator import generate_sensor_data
# from ecu import diagnose
# from logger import save_data


# print("=" * 60)
# print(" AUTOMOTIVE SENSOR MONITORING & ECU SIMULATOR")
# print("=" * 60)

# # Different operating conditions
# modes = [
#     "normal",
#     "normal",
#     "normal",
#     "over_temperature",
#     "normal",
#     "low_pressure",
#     "normal",
#     "high_pressure",
#     "normal",
#     "low_voltage",
#     "normal",
#     "high_voltage",
#     "normal",
#     "over_rpm"
# ]

# try:

#     for mode in modes:

#         # Generate sensor data according to selected mode
#         sensor_data = generate_sensor_data(mode)

#         # ECU diagnosis
#         fault_code, fault_name = diagnose(sensor_data)

#         print("\n---------------------------------------------")
#         print(f"Operating Mode : {mode}")

#         print(f"Temperature    : {sensor_data['temperature']} °C")
#         print(f"Pressure       : {sensor_data['pressure']} bar")
#         print(f"Voltage        : {sensor_data['voltage']} V")
#         print(f"RPM            : {sensor_data['rpm']}")

#         print(f"Fault Code     : {fault_code}")
#         print(f"ECU Status     : {fault_name}")

#         # Save data
#         save_data(
#             sensor_data,
#             fault_code,
#             fault_name
#         )

#         time.sleep(2)

# except KeyboardInterrupt:

#     print("\nECU simulation stopped.")