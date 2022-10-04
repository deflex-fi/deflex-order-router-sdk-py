from .deflex_route import DeflexRoute
from .dex_quote import DexQuote

class DeflexQuote:

    def __init__(self, quote, profitAmount, profitASAId, priceBaseline, route, quotes, requiredAppOptIns, txnPayload):
        self.quote = quote
        self.profitAmount = profitAmount
        self.profitASAId = profitASAId
        self.priceBaseline = priceBaseline
        self.route = route
        self.quotes = quotes
        self.requiredAppOptIns = requiredAppOptIns
        self.txnPayload = txnPayload

    @staticmethod
    def from_api_response(apiResponse):
        return DeflexQuote(
            apiResponse['quote'],
            apiResponse['profit']['amount'],
            apiResponse['profit']['asa']['id'],
            apiResponse['priceBaseline'],
            [DeflexRoute.from_api_response(_route) for _route in apiResponse['route']],
            [DexQuote.from_api_response(_quote) for _quote in apiResponse['quotes']],
            apiResponse['requiredAppOptIns'],
            apiResponse['txnPayload']
        )