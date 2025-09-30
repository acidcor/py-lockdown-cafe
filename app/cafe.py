from datetime import date

from app.errors import (OutdatedVaccineError,
                        NotWearingMaskError,
                        NotVaccinatedError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError(f"{visitor['name']} "
                                     f"have no vaccine!")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError(f"{visitor['name']}"
                                       f" vaccine is outdated!")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(f"{visitor['name']}"
                                      f" not wearing a mask!")

        return f"Welcome to {self.name}"
