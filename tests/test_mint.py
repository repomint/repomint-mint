# import base58
# from cryptography.fernet import Fernet

from solana.account import Account

# from solana.rpc.api import Client

# from metaplex.api.metaplex_api import MetaplexAPI


def test_metaplex_mint() -> None:
    account = Account()
    assert account
