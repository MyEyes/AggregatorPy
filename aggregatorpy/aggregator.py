import requests
import platform
from base64 import b64encode
from .model.scan import Scan
from .model.subject import Subject
from .model.tool import Tool
from .model.tag import Tag
from .model.api_response import APIResponse

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
        try:
            return APIResponse(resp.json())
        except requests.exceptions.JSONDecodeError:
            raise Exception(f"Server response had unexpected format:\nReq:\n{json}\nResp:\n{resp.text}")

    def reauthenticate(self):
        resp = self.postRequest("/api/auth/tokens", {}, self.user, self.passwd)
        if resp.error:
            print("Error authenticating:", resp.error)
            return False
        self.token = resp.token
        if not self.token:
            print("Error: authentication token empty")
            return False
        return True

    def startScan(self, tool, hard_hash, arguments):
        if not self.token:
            self.reauthenticate()
        scan = Scan(self, tool, hard_hash, arguments)
        scan.submit()
        if scan.get_id() == -1:
            raise Exception("Scan didn't start for some reason")
        return scan

    #Returns True when the request is done, false when it should be retried
    def checkErrorAndReauthenticate(self, resp):
        err = resp.error
        if err:
            if err == "401":
                return not self.reauthenticate() #Only retry if succesfully authenticated
            return True
        return True

    def stopScan(self, scan):
        for _ in range(2):
            resp = self.postRequest("/api/scan/stop", scan.to_dict())
            if not self.checkErrorAndReauthenticate(resp):
                continue
            if resp.error:
                print("Couldn't stop scan. Error:", resp.error)
                return False
            return True