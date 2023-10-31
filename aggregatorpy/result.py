from .hashhelper import GetSHA256String

class Result:
    def __init__(self, scanHash, subjectHash, softId, hardId, risk, title, description, tags):
        self.hash = hardId
        self.soft_hash = softId
        self.risk = risk
        self.title = title
        self.description = description
        self.scan_hash = scanHash
        self.subject_hash = subjectHash
        self.tags = tags
        self._convertTags()

    def _convertTags(self):
        tagIds = [tag.id for tag in self.tags]
        self.tags = tagIds

    def toDict(self):
        return {
            "scan_hash": self.scan_hash,
            "subject_hash": self.subject_hash,
            "hash": self.hash,
            "soft_hash": self.soft_hash,
            "risk": self.risk,
            "title": self.title,
            "description": self.description,
            "tags": self.tags
        }