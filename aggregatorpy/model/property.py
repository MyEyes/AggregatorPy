from .hashhelper import GetSHA256String
from .submittable import APISubmittable

class PropertyKind(APISubmittable):
    def __init__(self, aggregator, name, description="", is_matching=False):
        super().__init__(aggregator, "/api/property/register_kind")
        self.name = name
        self.description = description
        self.is_matching = is_matching

    def create_instance(self, value):
        return Property(self.aggregator, self, value)
    
    def __call__(self, *args, **kwds):
        assert len(args) == 1, "PropertyKind() must only have one arg for the value"
        return self.create_instance(args[0])

    def to_dict(self):
        return {
            "id": self._id,
            "name": self.name,
            "description": self.description,
            "is_matching": self.is_matching
        }
    
class Property(APISubmittable):
    def __init__(self, aggregator, definition, value):
        super().__init__(aggregator, "/api/property/add")
        self.definition = definition
        if value and len(value) > 256:
            self.value = GetSHA256String(value)
        else:
            self.value = value

    def to_dict(self):
        return {
            "id": self._id,
            "kind": self.definition.get_id(),
            "value": self.value
        }