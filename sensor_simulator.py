import random


def generate_sensor_data(mode="normal"):

    if mode == "normal":

        temperature = random.uniform(25, 80)
        pressure = random.uniform(1.8, 3.2)
        voltage = random.uniform(12, 14.5)
        rpm = random.randint(1000, 5000)

    elif mode == "over_temperature":

        temperature = random.uniform(101, 120)
        pressure = random.uniform(1.8, 3.2)
        voltage = random.uniform(12, 14.5)
        rpm = random.randint(1000, 5000)

    elif mode == "low_pressure":

        temperature = random.uniform(25, 80)
        pressure = random.uniform(0.5, 1.4)
        voltage = random.uniform(12, 14.5)
        rpm = random.randint(1000, 5000)

    elif mode == "high_pressure":

        temperature = random.uniform(25, 80)
        pressure = random.uniform(3.6, 5.0)
        voltage = random.uniform(12, 14.5)
        rpm = random.randint(1000, 5000)

    elif mode == "low_voltage":

        temperature = random.uniform(25, 80)
        pressure = random.uniform(1.8, 3.2)
        voltage = random.uniform(8, 10.9)
        rpm = random.randint(1000, 5000)

    elif mode == "high_voltage":

        temperature = random.uniform(25, 80)
        pressure = random.uniform(1.8, 3.2)
        voltage = random.uniform(15.1, 17)
        rpm = random.randint(1000, 5000)

    elif mode == "over_rpm":

        temperature = random.uniform(25, 80)
        pressure = random.uniform(1.8, 3.2)
        voltage = random.uniform(12, 14.5)
        rpm = random.randint(6001, 7500)

    return {
        "temperature": round(temperature, 2),
        "pressure": round(pressure, 2),
        "voltage": round(voltage, 2),
        "rpm": rpm
    }