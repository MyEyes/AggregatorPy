class Tool:
    def __init__(self, name, soft_hash, hash, version, description):
        self.name = name
        self.soft_match_hash = soft_hash
        self.hard_match_hash = hash
        self.version = version
        self.description = description

    def toDict(self):
        return {
            "name": self.name,
            "soft_match_hash": self.soft_match_hash,
            "hard_match_hash": self.hard_match_hash,
            "version": self.version,
            "description": self.description
        }