# Supply Dock Automation Script

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from user_stubs import supply_dock as self

from supply_dock import SupplyDockController

dock = SupplyDockController(self)
dock.run()

