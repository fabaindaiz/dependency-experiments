from typing import Any, Callable, cast
from dependency_injector import providers
from dependency.core.container.injectable import Injectable
from dependency.core.declaration.component import Component

class Provider:
    def __init__(self,
            provided_cls: type,
            imports: list[Component],
            inject: Injectable
        ):
        self.provided_cls = provided_cls
        self.imports = imports
        self.provider = inject

    def __repr__(self) -> str:
        return self.provided_cls.__name__

def provider(
        component: type[Component],
        imports: list[type[Component]] = [],
        provider: type[providers.Provider[Any]] = providers.Singleton
    ) -> Callable[[type], Provider]:
    def wrap(cls: type) -> Provider:
        _component = cast(Component, component)
        _imports = cast(list[Component], imports)
        return Provider(
            provided_cls=cls,
            imports=_imports,
            inject=Injectable(
                inject_name=_component.base_cls.__name__,
                inject_cls=_component.__class__,
                provided_cls=cls,
                provider_cls=provider
            )
        )
    return wrap