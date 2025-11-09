import pytest
import boa

@pytest.fixture
def rewardings():
    return boa.load("contracts/src/Rewardings.vy")

@pytest.fixture
def cards():
    return boa.load("contracts/src/Cards.vy")

@pytest.fixture
def sample_card(cards):
    return cards.card("CR7", 99)


def test_initial_rewards(rewardings):
    assert len(rewardings.all()) == 7


def test_rewrite_full(rewardings, sample_card):
    rewardings.rewrite_rewards([sample_card] * 128)
    assert len(rewardings.all()) == 128
