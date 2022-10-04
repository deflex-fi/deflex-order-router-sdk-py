class DexQuote:

    def __init__(self, name: str, value):
        self.name = name
        self.value = value

    @staticmethod
    def from_api_response(apiResponse):
        return DexQuote(apiResponse['name'], apiResponse['value'])