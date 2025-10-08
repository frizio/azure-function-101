import azure.functions as func
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import os
import logging

app = func.FunctionApp()

@app.route(route="welcome", auth_level=func.AuthLevel.ANONYMOUS)
def listSecrets(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Function triggered to list Key Vault secrets.')

    keyvault_name = "expriviaaikvf2t1yi" # os.getenv("KEYVAULT_NAME")
    if not keyvault_name:
        return func.HttpResponse("Missing KEYVAULT_NAME environment variable", status_code=500)

    vault_url = f"https://{keyvault_name}.vault.azure.net/"
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=vault_url, credential=credential)

    try:
        secrets = [s.name for s in client.list_properties_of_secrets()]
        return func.HttpResponse("\n".join(secrets))
    except Exception as e:
        logging.error(f"Error accessing Key Vault: {e}")
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
