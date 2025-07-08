from .hashhelper import GetSHA256String
from .submittable import APISubmittable

class Result(APISubmittable):
    def __init__(self, aggregator, scan_id, subject_id, hardId, title, description, properties, tags):
        super().__init__(aggregator, "/api/scan/submit")
        self.hash = hardId
        self.title = title
        self.description = description
        self.scan_id = scan_id
        self.subject_id = subject_id
        self.properties = properties
        self.tags = tags
        self._convertProperties()
        self._convertTags()

    def _convertTags(self):
        self.tagIds = [tag.get_id() for tag in self.tags]
    
    def _convertProperties(self):
        self.propertyIds = [prop.get_id() for prop in self.properties]

    def to_dict(self):
        return {
            "id": self._id,
            "scan_id": self.scan_id,
            "subject_id": self.subject_id,
            "hash": self.hash,
            "title": self.title,
            "description": self.description,
            "properties": self.propertyIds,
            "tags": self.tagIds
        }