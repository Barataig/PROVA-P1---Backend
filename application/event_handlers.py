from domain.category_events import (
    CategoryCreated,
    CategoryUpdated,
    CategoryActivated,
    CategoryDeactivated
)

def handle_category_created(event: CategoryCreated):
    print(f"[HANDLER] Categoria criada com ID={event.aggregate_id} em {event.timestamp}")

def handle_category_updated(event: CategoryUpdated):
    print(f"[HANDLER] Categoria {event.aggregate_id} atualizada em {event.timestamp}. Campos: {event.updated_fields}")

def handle_category_activated(event: CategoryActivated):
    print(f"[HANDLER] Categoria {event.aggregate_id} foi ativada em {event.timestamp}")

def handle_category_deactivated(event: CategoryDeactivated):
    print(f"[HANDLER] Categoria {event.aggregate_id} foi desativada em {event.timestamp}")
