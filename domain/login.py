import dataclasses

@dataclasses.dataclass
class Login:
    email: str = ""
    password: str = ""

    @classmethod
    def from_dict(cls, obj):
        return cls(
            email = obj['email'],
            password = obj['password']
        )