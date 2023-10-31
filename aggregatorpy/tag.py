from .hashhelper import GetSHA256String

class Tag:
    def __init__(self, shortname, name, description, color="gray", special=None):
        self.shortname = shortname
        self.name = name
        self.description = description
        self.color = color
        self.special = special
        self.id = -1

    def toDict(self):
        return {
            "shortname": self.shortname,
            "name": self.name,
            "description": self.description,
            "color": self.color,
            "special": self.special
        }