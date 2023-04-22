import requests
import platform
from base64 import b64encode
from .scan import Scan
from .subject import Subject
from .tool import Tool
class Aggregator:
    def __init__(self, base_uri, user, passwd):
        self.base_uri = base_uri
        self.user = user
        self.passwd = passwd
        self.token = None

    def postRequest(self, endpoint, json, user=None, passwd=None):
        headers = {}
        if not user or not passwd:
            headers["Authorization"] = f"Bearer {self.token}"
        else:
            auth = f"{user}:{passwd}".encode()
            headers["Authorization"] = f"Basic {b64encode(auth).decode()}"
        resp = requests.post(self.base_uri+endpoint, headers=headers, json=json)
        return resp.json()

    def reauthenticate(self):
        resp = self.postRequest("/api/auth/tokens", {}, self.user, self.passwd)
        if resp.get("error"):
            print("Error authenticating:", resp.get("error"))
            return False
        self.token = resp.get("token")
        if not self.token:
            print("Error: authentication token empty")
            return False
        return True

    def startScan(self, tool, soft_hash, hard_hash, arguments):
        if not self.token:
            self.reauthenticate()
        scan = Scan(tool.hard_match_hash, hard_hash,soft_hash, arguments)
        resp = self.postRequest("/api/scan/start", scan.toDict())
        if resp.get("error"):
            print("Error starting scan:", resp.get("error"))
            return None
        return scan

    #Returns True when the request is done, false when it should be retried
    def checkErrorAndReauthenticate(self, resp):
        err = resp.get("error")
        if err:
            if err == "401":
                return not self.reauthenticate() #Only retry if succesfully authenticated
            return True
        return True

    def stopScan(self, scan):
        for i in range(2):
            resp = self.postRequest("/api/scan/stop", scan.toDict())
            if not self.checkErrorAndReauthenticate(resp):
                continue
            if resp.get("error"):
                print("Couldn't stop scan. Error:", resp.get("error"))
                return False
            return True

    def createSubject(self, name, path, soft_hash, hard_hash, version="1.0", host=None):
        if not host:
            host = platform.node()
        subject = Subject(name, soft_hash, hard_hash, host, path, version)
        for i in range(2):
            resp = self.postRequest("/api/subject/create", subject.toDict())
            if not self.checkErrorAndReauthenticate(resp):
                continue
            if resp.get("error"):
                print("Couldn't create subject. Error:", resp.get("error"))
                return None
            return subject
        return None
        
    def submitResult(self, result):
        for i in range(2):
            resp = self.postRequest("/api/scan/submit", result.toDict())
            if not self.checkErrorAndReauthenticate(resp):
                continue
            if resp.get("error"):
                print("Couldn't submit result. Error:", resp.get("error"))
                return False
            return True
        return False

    def createTool(self, name, soft_hash, hard_hash, description, version="1.0"):
        if not self.token:
            self.reauthenticate()
        tool = Tool(name, soft_hash, hard_hash, version, description)
        resp = self.postRequest("/api/tool/register", tool.toDict())
        if resp.get("error"):
            print("Couldn't create tool. Error:", resp.get("error"))
            return None
        return tool