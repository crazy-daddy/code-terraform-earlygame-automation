# Xenogenetics Survey Contract Solver

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from user_stubs import xenogenetics as self

c = self.contract
earth_set = set(c.earth_ref)
alien_list = [sample for sample in c.samples if sample not in earth_set]

transmitter = get_component("transmitter")
transmitter.connect("earth")
res = transmitter.transmit(c.id, alien_list)
print(f"Xenogenetics result: {res.status} - {res.message}")

