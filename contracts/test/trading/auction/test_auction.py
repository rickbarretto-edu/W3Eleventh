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


@scenario("trading/Auction.feature", "Auction Cards")
def test_owner_auction_cards():
    pass


@given("a seller without any active auction", target_fixture="seller_without_active_auction")
def seller_without_active_auction(trades):
    seller = boa.env.generate_address()
    auction = trades.auction_of(seller)

    assert auction.seller == ZERO_ADDRESS
    return seller


@when("the seller auctions a card", target_fixture="auction_card")
def auction_card(seller_without_active_auction, trades, cards):
    owner = seller_without_active_auction
    card = cards.card("Card A", 99)

    with boa.env.prank(owner):
        trades.auction_card(card, 7)

    return owner


@then("the Auction should be registered.")
def auction_active_in_store(auction_card, trades):
    owner = auction_card
    auction = trades.auction_of(owner)

    assert auction.card.name == "Card A"
    assert auction.card.power == 99