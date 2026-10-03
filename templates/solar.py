# Solar Generator Automation Script

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from user_stubs import solar as self

from solar import SolarController

controller = SolarController(self)
controller.run()

