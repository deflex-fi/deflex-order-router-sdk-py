from .deflex_path_element import DeflexPathElement

class DeflexRoute:

    def __init__(self, percent: int, path: list):
        self.percent = percent
        self.path = path

    @staticmethod
    def from_api_response(apiResponse):
        return DeflexRoute(
            apiResponse['percentage'],
            [DeflexPathElement.from_api_response(pathElement) for pathElement in apiResponse['path']]
        )