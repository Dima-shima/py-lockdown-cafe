import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        try:
            expiration_date = visitor["vaccine"]["expiration_date"]
        except KeyError:
            raise NotVaccinatedError
        today = datetime.date.today()
        if today > expiration_date:
            raise OutdatedVaccineError("Expiration date has expired")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Must have a mask")
        return f"Welcome to {self.name}"
