

struct Card:
    name: String[64]
    power: uint8

@external
@pure
def card(_name: String[64], _power: uint8) -> Card:
    return Card(name=_name, power=_power)
