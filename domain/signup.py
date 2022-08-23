import dataclasses

@dataclasses.dataclass
class SignUp:
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
    phone: str = ""

    @classmethod
    def from_dict(cls, obj):
        return cls(
            email = obj['email'],
            password = obj['password'],
            first_name = obj['first_name'],
            last_name = obj['last_name'],
            phone = obj['phone']
        )