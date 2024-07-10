import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    user_email: str
    gender: str
    mobile_number: str
    year: str
    month: str
    day: str
    subjects: tuple
    hobbie: tuple
    picture: str
    address: str
    state: str
    city: str
