# Relay Hack Contract Solver

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from user_stubs import relay_hack as self

c = self.contract
lock = c.lock
code = [0] * lock.tumblers
for t in range(lock.tumblers):
    for val in range(lock.range):
        candidate = list(code)
        candidate[t] = val
        if lock.intercept(candidate)[t]:
            code[t] = val
            break

transmitter = get_component("transmitter")
transmitter.connect("earth")
res = transmitter.transmit(c.id, code)
print(f"Relay Hack result: {res.status} - {res.message}")

