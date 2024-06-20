import azure.identity
from azure.keyvault.secrets import SecretClient

class AZAPI:
    def __init__(self, client_id, client_secret, tenant_id):
        self.credential = azure.identity.ClientSecretCredential(tenant_id, client_id, client_secret)

    def get_secrets(self, kv_name):
        client = SecretClient(vault_url=f"https://{kv_name}.vault.azure.net", credential=self.credential)

        for prop in client.list_properties_of_secrets():
            print(prop.name)

    def get_secret(self, kv_name, secret_name):
        client = SecretClient(vault_url=f"https://{kv_name}.vault.azure.net", credential=self.credential)

        secret = client.get_secret(secret_name)
        print(f"{secret.name} - {secret.value}")