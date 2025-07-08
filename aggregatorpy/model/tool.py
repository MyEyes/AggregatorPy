from .submittable import APISubmittable
class Tool(APISubmittable):
    def __init__(self, aggregator, name, soft_hash, hash, version, description):
        super().__init__(aggregator, "/api/tool/register")
        self.name = name
        self.soft_match_hash = soft_hash
        self.hard_match_hash = hash
        self.version = version
        self.description = description
        self.submitted = False

    # Small wrapper to guarantee the tool has been submitted when anything uses it
    def get_hash(self):
        if self.submitted:
            return self.hard_match_hash
        self.submit()
        self.submitted = True
        return self.hard_match_hash

    def to_dict(self):
        return {
            "name": self.name,
            "soft_match_hash": self.soft_match_hash,
            "hard_match_hash": self.hard_match_hash,
            "version": self.version,
            "description": self.description
        }