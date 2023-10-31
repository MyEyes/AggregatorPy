class Subject:
    def __init__(self, name, soft_hash, hash, parentId, path, version, tags):
        self.name = name
        self.soft_hash = soft_hash
        self.hash = hash
        self.parentId = parentId
        self.path = path
        self.version = version
        self.tags = tags
        self._convertTags()
        self._convertParent()
        self.id = -1

    def _convertTags(self):
        tagIds = [tag.id for tag in self.tags]
        self.tags = tagIds

    def _convertParent(self):
        if isinstance(self.parentId, Subject):
            self.parentId = self.parentId.id

    def toDict(self):
        return {
            "name": self.name,
            "soft_hash": self.soft_hash,
            "hash": self.hash,
            "parentId": self.parentId,
            "path": self.path,
            "version": self.version,
            "tags": self.tags
        }