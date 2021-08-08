import pytest
from brownie import config
from brownie import Contract


@pytest.fixture
def gov(accounts):
    yield accounts.at("0xFEB4acf3df3cDEA7399794D0869ef76A6EfAff52", force=True)


@pytest.fixture
def user(accounts):
    yield accounts[0]


@pytest.fixture
def rewards(accounts):
    yield accounts[1]


@pytest.fixture
def guardian(accounts):
    yield accounts[2]


@pytest.fixture
def management(accounts):
    yield accounts[3]


@pytest.fixture
def strategist(accounts):
    yield accounts[4]


@pytest.fixture
def keeper(accounts):
    yield accounts[5]


@pytest.fixture
def token():
    token_address = "0x3D980E50508CFd41a13837A60149927a11c03731"  # this should be the address of the ERC-20 used by the zap (triCrypto)
    yield Contract(token_address)


@pytest.fixture
def newToken():
    token_address = (
        "0xE537B5cc158EB71037D4125BDD7538421981E6AA"  # this is our new vault address
    )
    yield Contract(token_address)


@pytest.fixture(scope="module")
def whale(accounts):
    # Totally in it for the tech
    # Update this with a large holder of your want token (largest EOA holder of triCrypto vault token)
    whale = accounts.at("0x718f06A344bfeCf6664D8d329a14dc9Bb8Ff2246", force=True)
    yield whale


@pytest.fixture
def zap(gov, tricrypto_migrator):
    zap = gov.deploy(tricrypto_migrator)
    yield zap
