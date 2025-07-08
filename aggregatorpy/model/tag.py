from .hashhelper import GetSHA256String
from .submittable import APISubmittable

class Tag(APISubmittable):
    def __init__(self, aggregator, shortname, name, description, color="gray"):
        super().__init__(aggregator, "/api/tag/register")
        self.shortname = shortname
        self.name = name
        self.description = description
        self.color = color

    def to_dict(self):
        return {
            "shortname": self.shortname,
            "name": self.name,
            "description": self.description,
            "color": self.color
        }