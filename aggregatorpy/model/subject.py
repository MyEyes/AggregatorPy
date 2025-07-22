from .submittable import APISubmittable

class Subject(APISubmittable):
    def __init__(self, aggregator, name, hash, parent, properties, tags):
        super().__init__(aggregator, "/api/subject/create")
        self.name = name
        self.hash = hash
        self._setParent(parent)
        self.properties = properties
        self.tags = tags
        self._convertProperties()
        self._convertTags()

    def _convertTags(self):
        tagIds = [tag.get_id() for tag in self.tags]
        self.tagIds = tagIds

    def _convertProperties(self):
        propertyIds = [prop.get_id() for prop in self.properties]
        self.propertyIds = propertyIds

    def _setParent(self, parent):
        if parent is None:
            self.parentId = -1
        elif isinstance(parent, Subject):
            self.parentId = parent.get_id()
        elif isinstance(parent, int):
            self.parentId = parent
        else:
            raise TypeError(f"Unexpected type of parent: { type(parent) }")

    def to_dict(self):
        return {
            "id": self._id,
            "name": self.name,
            "hash": self.hash,
            "parentId": self.parentId,
            "properties": self.propertyIds,
            "tags": self.tagIds
        }