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

print("\n=== FIM DO TESTE ===")
