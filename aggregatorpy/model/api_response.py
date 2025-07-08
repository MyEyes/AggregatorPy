class APIResponse:
    def __init__(self, json):
        self.id = json.get("id") or -1
        self.error = json.get("error") or None
        self.token = json.get("token") or None
        self.unauthorized = True if self.error and self.error == "401" else False

    def is_error(self):
        return self.error is not None