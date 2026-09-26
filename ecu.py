from fault_codes import FAULT_CODES


def diagnose(data):

    temperature = data["temperature"]
    pressure = data["pressure"]
    voltage = data["voltage"]
    rpm = data["rpm"]

    # Temperature check
    if temperature > 100:
        return "F001", FAULT_CODES["F001"]

    # Pressure checks
    if pressure < 1.5:
        return "F002", FAULT_CODES["F002"]

    if pressure > 3.5:
        return "F003", FAULT_CODES["F003"]

    # Voltage checks
    if voltage < 11:
        return "F004", FAULT_CODES["F004"]

    if voltage > 15:
        return "F005", FAULT_CODES["F005"]

    # RPM check
    if rpm > 6000:
        return "F006", FAULT_CODES["F006"]

    return "F000", FAULT_CODES["F000"]