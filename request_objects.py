import dataclasses

@dataclasses.dataclass
class Response:
    data: dict = None
    status: int = 200