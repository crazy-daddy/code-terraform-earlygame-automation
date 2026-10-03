# Thermal Cap Automation Script

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from user_stubs import thermal_cap as self

from thermal_cap import ThermalCapController

cap = ThermalCapController(self)
cap.run()

