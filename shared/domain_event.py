from datetime import datetime
from abc import ABC

class DomainEvent(ABC):
    def __init__(self, aggregate_id: str, timestamp: datetime = None):
        self.aggregate_id = aggregate_id
        self.timestamp = timestamp or datetime.utcnow()

    def __repr__(self):
        return f"<{self.__class__.__name__} aggregate_id={self.aggregate_id} timestamp={self.timestamp}>"
