from ..utils import fetch_api_data
from .deflex_quote import DeflexQuote
from .deflex_transaction_group import DeflexTransactionGroup
import json

class DeflexOrderRouterClient:
    def __init__(self, algodUri: str, algodToken, algodPort: str, chain: str, referrerAddress: str = '', feeBps: str = '', apiKey: str = ''):
        self.algodUri = algodUri
        self.algodToken = algodToken
        self.algoPort = algodPort
        self.chain = chain
        self.referrerAddress = referrerAddress
        self.feeBps = feeBps
        self.apiKey = apiKey

    def get_fixed_input_swap_quote(self, fromASAId: int, toASAId: int, amount: int, disabledProtocols: list = [], maxGroupSize: int = 16, atomicOnly: bool = True):
        return self.get_swap_quote('fixed-input', fromASAId, toASAId, amount, disabledProtocols, maxGroupSize, atomicOnly)

    def get_fixed_output_swap_quote(self, fromASAId: int, toASAId: int, amount: int, disabledProtocols: list = [], maxGroupSize: int = 16, atomicOnly: bool = True):
        return self.get_swap_quote('fixed-output', fromASAId, toASAId, amount, disabledProtocols, maxGroupSize, atomicOnly)

    def get_swap_quote(self, type: str, fromASAId: int, toASAId: int, amount: int, disabledProtocols: list, maxGroupSize: int, atomicOnly: bool):
        apiResponse = fetch_api_data('fetchQuote', {
            'chain': self.chain,
            'algodUri': self.algodUri,
            'algodToken': json.dumps(self.algodToken) if isinstance(self.algodToken, dict) else self.algodToken,
            'algodPort': self.algoPort,
            'type': type,
            'amount': amount,
            'fromASAID': fromASAId,
            'toASAID': toASAId,
            'disabledProtocols': ",".join(disabledProtocols),
            'maxGroupSize': maxGroupSize,
            'apiKey': self.apiKey,
            'referrerAddress': self.referrerAddress,
            'feeBps': self.feeBps,
            'atomicOnly': 'true' if atomicOnly else 'false'
        })
        return DeflexQuote.from_api_response(apiResponse)

    def get_swap_quote_transactions(self, address: str, txnPayload, slippage):
        apiResponse = fetch_api_data('fetchExecuteSwapTxns', {
            'address': address,
            'txnPayloadJSON': txnPayload,
            'slippage': slippage,
            'apiKey': self.apiKey
        }, True)
        return DeflexTransactionGroup.from_api_response(apiResponse)


class DeflexOrderRouterTestnetClient(DeflexOrderRouterClient):
    def __init__(self, algodUri: str, algodToken, algodPort: str, referrerAddress: str = '', feeBps: str = '', apiKey: str = ''):
        super().__init__(algodUri, algodToken, algodPort, 'testnet', referrerAddress, feeBps, apiKey)


class DeflexOrderRouterMainnetClient(DeflexOrderRouterClient):
    def __init__(self, algodUri: str, algodToken, algodPort: str, referrerAddress: str = '', feeBps: str = '', apiKey: str = ''):
        super().__init__(algodUri, algodToken, algodPort, 'mainnet', referrerAddress, feeBps, apiKey)

