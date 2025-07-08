class APISubmittable:
    def __init__(self, aggregator, endpoint):
        self.endpoint = endpoint
        self.aggregator = aggregator
        self._id = -1

    def to_dict(self):
        raise NotImplementedError()
    
    def set_aggregator(self, aggregator):
        assert not self.aggregator or aggregator==self.aggregator, "APISubmittable.aggregator must not be changed after being set"
        self.aggregator = aggregator
    
    def get_id(self):
        if self._id == -1:
            self.submit()
        return self._id
    
    def submit(self, can_retry=True):
        result = self.aggregator.postRequest(self.endpoint, self.to_dict())
        if result.is_error():
            # If we failed because we were unauthorized and we haven't retried yet retry once
            # If we failed for some other reason or we already retried, fail immediately and raise Exception
            if result.unauthorized and can_retry:
                self.aggregator.reauthenticate()
                return self.submit(can_retry=False)
            raise Exception(f"Unexpected error while submitting: {result.error}")
        self._id = result.id