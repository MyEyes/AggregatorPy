from .properties import *
from .tags import *
from ..model.submittable import APISubmittable

def set_common_aggregator(aggregator):
    for value in properties.__dict__.values():
        if isinstance(value, APISubmittable):
            value.set_aggregator(aggregator)
    for value in tags.__dict__.values():
        if isinstance(value, APISubmittable):
            value.set_aggregator(aggregator)