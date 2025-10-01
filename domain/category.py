import uuid
from dataclasses import dataclass, field
from typing import Optional, Dict
from datetime import datetime

from domain.category_events import (
    CategoryCreated,
    CategoryUpdated,
    CategoryActivated,
    CategoryDeactivated
)

from shared.event_dispatcher import EventDispatcher

MAX_NAME = 255

@dataclass
class Category:
    name: str
    description: str = ""
    is_active: bool = True
    id: Optional[str] = field(default=None)

    def __post_init__(self):
        if not self.id:
            self.id = str(uuid.uuid4())

        self.name = self._validate_name(self.name)
        self.description = self.description or ""
        self.is_active = bool(self.is_active)

        self._dispatcher = EventDispatcher()
        self._raise_event(CategoryCreated(self.id, datetime.utcnow()))

    # ---- validações ----
    @staticmethod
    def _validate_name(name: str) -> str:
        if not isinstance(name, str):
            raise TypeError("O nome deve ser uma string")
        n = name.strip()
        if not n:
            raise ValueError("O nome é obrigatório")
        if len(n) > MAX_NAME:
            raise ValueError(f"O nome deve ter no máximo {MAX_NAME} caracteres")
        return n

    # ---- comportamentos ----
    def update(self, *, name: Optional[str] = None, description: Optional[str] = None):
        updated_fields = {}
        if name and name != self.name:
            updated_fields["name"] = (self.name, name)
            self.name = self._validate_name(name)
        if description and description != self.description:
            updated_fields["description"] = (self.description, description)
            self.description = description
        if updated_fields:
            self._raise_event(CategoryUpdated(self.id, datetime.utcnow(), updated_fields))

    def activate(self):
        if not self.is_active:
            self.is_active = True
            self._raise_event(CategoryActivated(self.id, datetime.utcnow()))

    def deactivate(self):
        if self.is_active:
            self.is_active = False
            self._raise_event(CategoryDeactivated(self.id, datetime.utcnow()))

    # ---- serialização ----
    def to_dict(self) -> Dict:
        return {
            "class_name": self.__class__.__name__,
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "is_active": self.is_active
        }

    @classmethod
    def from_dict(cls, data: Dict):
        return cls(
            id=data.get("id"),
            name=data.get("name", ""),
            description=data.get("description", ""),
            is_active=data.get("is_active", True)
        )

    # ---- eventos ----
    def _raise_event(self, event):
        # dispara para todos os handlers registrados
        self._dispatcher.dispatch(event)

    def register_handler(self, event_type, handler):
        self._dispatcher.register(event_type, handler)

    def __str__(self):
        return f"{self.name} | {self.description} ({'Ativa' if self.is_active else 'Inativa'})"