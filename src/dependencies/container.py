from dependency_injector import containers, providers

class Mixin:
    @classmethod
    def _wire(cls, container: containers.Container):
        return container.wire(modules=[cls])

class ServiceContainer(containers.DeclarativeContainer):
    name = providers.Object()
    depends = providers.List()
    config = providers.Configuration()
    inject = providers.Callable(containers.DeclarativeContainer)