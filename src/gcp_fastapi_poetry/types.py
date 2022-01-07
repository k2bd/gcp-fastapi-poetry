from fastapi_camelcase import CamelModel


class ExampleResponse(CamelModel):
    """
    A person, place, or thing to say hello to
    """

    #: Some value of the example response
    response_value: str
