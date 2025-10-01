from shared.domain_event import DomainEvent

class CategoryCreated(DomainEvent):
    pass

class CategoryUpdated(DomainEvent):
    def __init__(self, aggregate_id, timestamp=None, updated_fields=None):
        super().__init__(aggregate_id, timestamp)
        self.updated_fields = updated_fields or {}

class CategoryActivated(DomainEvent):
    pass

class CategoryDeactivated(DomainEvent):
    pass
