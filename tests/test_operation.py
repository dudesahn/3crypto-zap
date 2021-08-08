import brownie
from brownie import Contract
import pytest


def test_operation(
    chain, accounts, token, zap, whale, newToken
):

    ## zap to the new vault after approving
    starting_old_balance = token.balanceOf(whale)
    print("Starting v1 triCrypto vault token balance of whale:", starting_old_balance/1e18)
    token.approve(zap, 2 ** 256 - 1, {"from": whale})
    zap.migrate_to_new_vault({"from": whale})
    
    final_new_balance = newToken.balanceOf(whale)
    final_old_balance = token.balanceOf(whale)

    print("Ending v1 triCrypto vault token balance of whale:", final_old_balance/1e18)
    print("Ending v2 triCrypto vault token balance of whale:", final_new_balance/1e18)

    assert final_new_balance > 0
    assert final_old_balance == 0
