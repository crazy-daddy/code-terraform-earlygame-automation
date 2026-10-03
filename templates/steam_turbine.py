# Steam Turbine Automation Script

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from user_stubs import turbine as self

from steam_turbine import SteamTurbineController

turbine = SteamTurbineController(self)
turbine.run()

