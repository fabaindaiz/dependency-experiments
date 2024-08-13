from src.dependencies.resolver.errors import raise_dependency_error
from src.dependencies.resolver.utils import provider_is_resolved

def resolve_dependency_layers(unresolved_providers):
    resolved_layers = []

    while unresolved_providers:
        new_layer = [
            provider
            for provider in unresolved_providers
            if provider_is_resolved(provider, resolved_layers)
        ]

        if not new_layer:
            raise_dependency_error(unresolved_providers, resolved_layers)
        
        resolved_layers.append(new_layer)

        unresolved_providers = [
            provider
            for provider in unresolved_providers
            if provider not in new_layer
        ]

    return resolved_layers