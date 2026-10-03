from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from user_stubs import oxygen_sensor as self

raw_val = self.get_value()
print(f"Raw oxygen sensor value: {raw_val}")
res = self.calibrate(raw_val * 100)
print("Oxygen sensor calibrate result:", res.status, res.message)

