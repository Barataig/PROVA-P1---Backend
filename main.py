""" from domain.category import Category
from domain.category_events import (
    CategoryCreated,
    CategoryUpdated,
    CategoryActivated,
    CategoryDeactivated
)
from application.event_handlers import (
    handle_category_created,
    handle_category_updated,
    handle_category_activated,
    handle_category_deactivated
)

print("=== INÍCIO DO TESTE DE CATEGORY COM EVENTOS ===\n")

# Cria a categoria
cat = Category(name="Eletrônicos", description="Produtos de tecnologia")

# Registra handlers
cat.register_handler(CategoryCreated, handle_category_created)
cat.register_handler(CategoryUpdated, handle_category_updated)
cat.register_handler(CategoryActivated, handle_category_activated)
cat.register_handler(CategoryDeactivated, handle_category_deactivated)

# Ciclo de vida
cat.update(name="Eletrônicos e Gadgets", description="Tecnologia e acessórios")
cat.deactivate()
cat.activate()

# Serialização
serialized = cat.to_dict()
print("\nCategoria serializada:", serialized)

reconstructed = Category.from_dict(serialized)
print("Categoria reconstruída:", reconstructed.to_dict())

print("\n=== FIM DO TESTE ===") """ 

from domain.category import Category
from domain.category_events import (
    CategoryCreated,
    CategoryUpdated,
    CategoryActivated,
    CategoryDeactivated
)
from application.event_handlers import (
    handle_category_created,
    handle_category_updated,
    handle_category_activated,
    handle_category_deactivated
)


def setup_handlers(category: Category):
    """Registra todos os handlers de eventos para a categoria."""
    handlers = {
        CategoryCreated: handle_category_created,
        CategoryUpdated: handle_category_updated,
        CategoryActivated: handle_category_activated,
        CategoryDeactivated: handle_category_deactivated,
    }
    for event_type, handler in handlers.items():
        category.register_handler(event_type, handler)


def print_event_table(events):
    """Imprime os eventos disparados em formato de tabela."""
    print("\n=== TABELA DE EVENTOS ===")
    print(f"{'Evento':<25} | {'ID da Categoria':<36} | {'Timestamp'}")
    print("-" * 80)
    for event in events:
        print(f"{event.__class__.__name__:<25} | {event.aggregate_id:<36} | {event.timestamp}")
    print("-" * 80)


def run_category_demo():
    """Executa todo o ciclo de vida da categoria e demonstra serialização."""
    print("\n=== INÍCIO DO TESTE DE CATEGORY COM EVENTOS ===\n")

    # Criação da categoria
    cat = Category(name="Eletrônicos", description="Produtos de tecnologia")
    setup_handlers(cat)

    # Ciclo de vida
    steps = [
        ("Atualizando categoria", lambda c: c.update(
            name="Eletrônicos e Gadgets", description="Tecnologia e acessórios")),
        ("Desativando categoria", lambda c: c.deactivate()),
        ("Ativando categoria novamente", lambda c: c.activate()),
    ]

    for description, action in steps:
        print(f"\n-- {description} --")
        action(cat)

    # Serialização
    print("\n-- Serializando categoria --")
    serialized = cat.to_dict()
    print(serialized)

    # Reconstrução
    print("\n-- Reconstruindo categoria --")
    reconstructed = Category.from_dict(serialized)
    print(reconstructed.to_dict())

    # Tabela de eventos disparados
    print_event_table(cat._raised_events)

    print("\n=== FIM DO TESTE ===\n")


if __name__ == "__main__":
    run_category_demo()

