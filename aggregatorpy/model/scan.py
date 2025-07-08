from .submittable import APISubmittable

class Scan(APISubmittable):
    def __init__(self, aggregator, tool, hash, arguments):
        super().__init__(aggregator, "/api/scan/start")
        self.tool = tool
        self.hash = hash
        self.arguments = arguments
        self.submitted = False

    # Small wrapper to guarantee the scan has been submitted when anything uses it
    def get_hash(self):
        if self.submitted:
            return self.hash
        self.submit()
        self.submitted = True
        return self.hash

    # This only exists to be nice, in general Scan.get_id() would always trigger a submit before the first result is submitted anyway
    def start(self):
        self.submit()

    def stop(self):
        self.aggregator.stopScan(self)

    def to_dict(self):
        return  {
            "id": self._id,
            "tool_hash": self.tool.get_hash(),
            "scan_hash": self.hash,
            "arguments": self.arguments
        }
    
