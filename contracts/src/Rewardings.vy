import Cards
import Inventory

initializes: Inventory

event Claimed:
    by: address
    card: Cards.Card

event Rewrote:
    old_cards: Cards.Card[128]
    new_cards: Cards.Card[128]


rewardings: public(DynArray[Cards.Card, 128])


@deploy
def __init__():
    self.rewardings.append(Cards.Card(name="Lionel Messi", power=99))
    self.rewardings.append(Cards.Card(name="Cristiano Ronaldo", power=99))
    self.rewardings.append(Cards.Card(name="Ronaldinho", power=99))
    self.rewardings.append(Cards.Card(name="Ronaldo", power=99))
    self.rewardings.append(Cards.Card(name="Pele", power=100))
    self.rewardings.append(Cards.Card(name="Maradona", power=100))
    self.rewardings.append(Cards.Card(name="Chech", power=100))

@view
@external
def all_rewardings() -> DynArray[Cards.Card, 128]:
    return self.rewardings


@external
def claim() -> Cards.Card:
    assert len(self.rewardings) > 0, "No rewardings available at the moment."
    assert len(Inventory._deck_of(msg.sender)) < 64, "User's deck must have available stock."

    claimed: Cards.Card = self.rewardings.pop()
    Inventory.add_card_to(msg.sender, claimed)

    log Claimed(by=msg.sender, card=claimed)
    return claimed


@external
def rewrite_rewards(cards: DynArray[Cards.Card, 128]):    
    self.empty_rewardings()
    self.fill_rewardings(cards)

@internal
def empty_rewardings():
    self.rewardings = empty(DynArray[Cards.Card, 128])

        
@internal
def fill_rewardings(cards: DynArray[Cards.Card, 128]):
    self.rewardings = cards
