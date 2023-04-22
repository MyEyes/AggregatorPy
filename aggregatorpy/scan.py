class Scan:
    def __init__(self, tool_hash, scan_hash, scan_soft_hash, arguments):
        self.tool_hash = tool_hash
        self.scan_hash = scan_hash
        self.scan_soft_hash = scan_soft_hash
        self.arguments = arguments

    def toDict(self):
        return {
            "tool_hash": self.tool_hash,
            "scan_hash": self.scan_hash,
            "scan_soft_hash": self.scan_soft_hash,
            "arguments": self.arguments
        }
