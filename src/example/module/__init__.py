from dependency.core.module.provider import ProviderModule, module
from example.module.client import ClientComponent
from example.module.manager import ManagerComponent
from example.module.client.type1 import Type1Client
from example.module.manager.type1 import Type1Manager
from example.module.services import Services

@module(
    declaration=[
        ClientComponent,
        ManagerComponent
    ],
    imports=[
        Services
    ],
    bootstrap=[
        ClientComponent
    ]
)
class Plugin(ProviderModule):
    def declare_providers(self): # type: ignore
        return [
            Type1Client,
            Type1Manager
        ]