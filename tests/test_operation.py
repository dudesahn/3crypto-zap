import brownie
from brownie import Contract
import pytest
import math


def test_operation(chain, accounts, token, zap, whale, newToken):

    ## zap to the new vault after approving
    starting_old_balance = token.balanceOf(whale)
    print(
        "Starting v1 triCrypto vault token balance of whale:",
        starting_old_balance / 1e18,
    )
    token.approve(zap, 2 ** 256 - 1, {"from": whale})
    zap.migrate_to_new_vault({"from": whale})

    final_new_balance = newToken.balanceOf(whale)
    final_old_balance = token.balanceOf(whale)

    print("Ending v1 triCrypto vault token balance of whale:", final_old_balance / 1e18)
    print("Ending v2 triCrypto vault token balance of whale:", final_new_balance / 1e18)

    # Make sure we don't have any old yToken left and have a positive balance of the new one
    assert final_new_balance > 0
    assert final_old_balance == 0

    # Make sure we have about the same amount of underlying within 1%
    underlying_original = token.pricePerShare() * starting_old_balance / 1e18
    underlying_new = newToken.pricePerShare() * final_new_balance / 1e18

    print("Underlying balance of v1 vault token:", underlying_original / 1e18)
    print("Underlying balance of v2 vault token:", underlying_new / 1e18)

    assert math.isclose(
        underlying_new, underlying_original, abs_tol=underlying_original * 0.01
    )
