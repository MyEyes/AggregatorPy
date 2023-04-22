class Subject:
    def __init__(self, name, soft_hash, hash, host, path, version):
        self.name = name
        self.soft_hash = soft_hash
        self.hash = hash
        self.host = host
        self.path = path
        self.version = version

    def toDict(self):
        return {
            "name": self.name,
            "soft_hash": self.soft_hash,
            "hash": self.hash,
            "host": self.host,
            "path": self.path,
            "version": self.version
        }