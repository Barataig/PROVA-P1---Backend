📝 Prova P1 – Entidade Category com Eventos de Domínio
Contexto

Este projeto implementa a entidade de domínio Category com funcionalidades típicas de sistemas reais, seguindo princípios de Domain-Driven Design (DDD).

Objetivos principais:


Serializar e reconstruir objetos (to_dict / from_dict)

Implementar Eventos de Domínio com handlers
------------------------------------------------------------------------------------------------------------------------
Funcionalidades Implementadas ------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
1️⃣ Entidade Category

Criação e validação de atributos (name, description)

Atualização de atributos (update) com registro de evento CategoryUpdated

Ativação (activate) e desativação (deactivate) com eventos correspondentes

Serialização (to_dict) e reconstrução (from_dict)
------------------------------------------------------------------------------------------------------------------------
2️⃣ Eventos de Domínio --------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------

Base abstrata DomainEvent

Eventos específicos:

        CategoryCreated

        CategoryUpdated

        CategoryActivated

        CategoryDeactivated

Cada evento registra aggregate_id e timestamp

CategoryUpdated inclui os campos alterados
------------------------------------------------------------------------------------------------------------------------
3️⃣ Event Dispatcher e Handlers -----------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
EventDispatcher registra e dispara eventos para handlers específicos

Handlers implementados:

        handle_category_created

        handle_category_updated 

        handle_category_activated

        handle_category_deactivated

Ciclo de Vida e Exemplo de Uso
        from domain.category import Category
        from application.event_handlers import *

# Criar categoria
cat = Category(name="Eletrônicos", description="Produtos de tecnologia")

# Registrar handlers
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
reconstructed = Category.from_dict(serialized)
------------------------------------------------------------------------------------------------------------------------
Saída esperada (exemplo):

[HANDLER] Categoria criada com ID=... em ...
[HANDLER] Categoria ... atualizada em ... Campos: {...}
[HANDLER] Categoria ... foi desativada em ...
[HANDLER] Categoria ... foi ativada em ...
Categoria serializada: {...}
Categoria reconstruída: {...}
------------------------------------------------------------------------------------------------------------------------

Resumo Teórico – Parte 2
------------------------------------------------------------------------------------------------------------------------
@staticmethod

Método que não depende da instância ou da classe

Ex.: _validate_name() para validar nomes de categorias
------------------------------------------------------------------------------------------------------------------------
Dataclasses

Reduz boilerplate para criar classes (__init__, __repr__, __eq__)

Ex.: Category foi implementada como @dataclass
------------------------------------------------------------------------------------------------------------------------
Eventos de Domínio

Representam mudanças importantes no estado da entidade

Ex.: CategoryCreated, CategoryUpdated, CategoryActivated, CategoryDeactivated
------------------------------------------------------------------------------------------------------------------------
Decoradores

@classmethod usado em from_dict() para criar instância a partir de um dicionário

@staticmethod usado em _validate_name() para validação sem depender da instância
------------------------------------------------------------------------------------------------------------------------
DDD (Domain-Driven Design)

Separação clara entre entidade (Category), eventos e handlers

Mantém ciclo de vida previsível e rastreável

Facilita extensibilidade e organização do código
------------------------------------------------------------------------------------------------------------------------
Estrutura de Arquivos
├── domain/
│   ├── category.py                         # Entidade Category com serialização e eventos
│   ├── category_events.py                  # Eventos específicos da Category
│   └── domain_event.py                     # Classe base DomainEvent
├── shared/
│   └── eventdispatcher.py                  # Dispatcher de eventos e registro de handlers
├── application/
│   └── event_handlers.py                   # Handlers de eventos (funções de callback)
├── main.py                                 # Script de teste: ciclo de vida + serialização + eventos
└── README.md                               # Este arquivo
------------------------------------------------------------------------------------------------------------------------
Como Executar

Certifique-se de ter Python ≥3.9

Executar o script principal:

python main.py

------------------------------------------------------------------------------------------------------------------------
Observar:

Eventos disparados e mensagens dos handlers

Categoria serializada e reconstruída