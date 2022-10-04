class DeflexPathElement:

    def __init__(self, name: str, inputASAId: int, outputASAId: int):
        self.name = name
        self.inputASAId = inputASAId
        self.outputASAId = outputASAId

    @staticmethod
    def from_api_response(apiResponse):
        return DeflexPathElement(apiResponse['name'], apiResponse['in']['id'], apiResponse['out']['id'])