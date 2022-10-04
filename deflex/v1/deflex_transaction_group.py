from .deflex_transaction import DeflexTransaction

class DeflexTransactionGroup:

    def __init__(self, txns: list):
        self.txns = txns

    @staticmethod
    def from_api_response(apiResponse):
        return DeflexTransactionGroup([DeflexTransaction.from_api_response(txn) for txn in apiResponse['txns']])