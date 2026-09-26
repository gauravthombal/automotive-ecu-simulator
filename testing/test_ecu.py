import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

from sensor_simulator import generate_sensor_data
from ecu import diagnose


tests = [
    ("Normal Operation", "normal", "F000"),
    ("Over Temperature", "over_temperature", "F001"),
    ("Low Pressure", "low_pressure", "F002"),
    ("High Pressure", "high_pressure", "F003"),
    ("Low Voltage", "low_voltage", "F004"),
    ("High Voltage", "high_voltage", "F005"),
    ("Over RPM", "over_rpm", "F006")
]


print("\nECU VALIDATION TEST")
print("=" * 60)

passed = 0

for name, mode, expected in tests:

    data = generate_sensor_data(mode)

    actual, fault = diagnose(data)

    result = "PASS" if actual == expected else "FAIL"

    if result == "PASS":
        passed += 1

    print(f"{name:<25} Expected: {expected:<5} "
          f"Actual: {actual:<5} {result}")

print("=" * 60)

print(f"Passed: {passed}/{len(tests)}")
print(f"Pass Rate: {(passed / len(tests)) * 100:.1f}%")