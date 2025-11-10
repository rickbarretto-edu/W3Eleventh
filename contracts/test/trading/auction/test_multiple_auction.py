import boa
from boa.util.abi import Address
import pytest
from pytest_bdd import *


ZERO_ADDRESS = Address("0x0000000000000000000000000000000000000000")

@pytest.fixture
def trades():
    return boa.load("contracts/src/Trades.vy")

@pytest.fixture
def cards():
    return boa.load("contracts/src/Cards.vy")


@scenario("trading/Auction.feature", "Replacing a Dead Auction")
def test_replacing_dead_auction():
    pass

@given("a seller with a dead auction", target_fixture="seller_with_dead_auction")
def seller_with_dead_auction(trades, cards):
    seller = boa.env.generate_address()
    card = cards.card("Card D", 20)
    with boa.env.prank(seller):
        trades.auction_card(card, 5)
    return seller


@when("the seller tries to auction another card (dead)", target_fixture="try_replace_dead_auction")
def try_replace_dead_auction():
    pass


@then("the new Auction should be registered")
def new_auction_registered(try_auction_another_card, trades):
    seller, old_auction, reverted = try_auction_another_card
    assert reverted is False
    assert trades.auction_of(seller) != old_auction
