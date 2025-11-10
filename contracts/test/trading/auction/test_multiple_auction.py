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


@scenario("trading/Auction.feature", "Prevent Multiple Active Auctions")
def test_prevent_multiple_active_auctions():
    pass


@given("a seller with an active auction", target_fixture="seller_with_active_auction")
def seller_with_active_auction(trades, cards):
    seller = boa.env.generate_address()
    card = cards.card("Card B", 50)

    with boa.env.prank(seller):
        trades.auction_card(card, 5)

    auction = trades.auction_of(seller)
    assert auction.seller == seller

    return seller


@when("the seller tries to auction another card", target_fixture="try_auction_another_card")
def try_auction_another_card(
    seller_with_active_auction,
    trades,
    cards,
):
    seller = seller_with_active_auction
    card = cards.card("Card C", 30)
    old_auction = trades.auction_of(seller)

    reverted = False
    with boa.env.prank(seller):
        try:
            trades.auction_card(card, 5)
        except Exception:
            reverted = True

    return seller, old_auction, reverted


@then("the Auction should be rejected")
def auction_rejected(try_auction_another_card, trades):
    seller, old_auction, reverted = try_auction_another_card
    
    assert reverted is True
    assert trades.auction_of(seller) == old_auction