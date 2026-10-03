# Water Pump Automation Script

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from user_stubs import water_pump as self

from water_pump import WaterPumpController

pump = WaterPumpController(self)
pump.run()

