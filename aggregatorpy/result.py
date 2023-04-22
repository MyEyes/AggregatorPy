from .hashhelper import GetSHA256String

class Result:
    def __init__(self, scanHash, subjectHash, softId, hardId, risk, text):
        self.hash = hardId
        self.soft_hash = softId
        self.risk = risk
        self.text = text
        self.scan_hash = scanHash
        self.subject_hash = subjectHash

    def toDict(self):
        return {
            "scan_hash": self.scan_hash,
            "subject_hash": self.subject_hash,
            "hash": self.hash,
            "soft_hash": self.soft_hash,
            "risk": self.risk,
            "text": self.text
        }