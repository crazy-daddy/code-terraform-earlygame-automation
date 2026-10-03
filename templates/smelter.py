# Smelter Automation Script

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from user_stubs import smelter as self

from smelter import SmelterController

TARGET_ORE = "${TARGET_ORE:iron_ore}"
smelter = SmelterController(self, target_ore=TARGET_ORE)
smelter.run()

