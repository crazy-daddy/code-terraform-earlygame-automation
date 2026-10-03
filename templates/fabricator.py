# Fabricator Automation Script

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from user_stubs import fabricator as self

from fabricator import FabricatorController

TARGET_RECIPE = "${TARGET_RECIPE:circuit}"
fabricator = FabricatorController(self, default_recipe=TARGET_RECIPE)
fabricator.run()

