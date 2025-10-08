import azure.functions as func
import os
import datetime
import json
import logging

app = func.FunctionApp()


#@app.route(route="welcome", auth_level=func.AuthLevel.ANONYMOUS)
def sayHello(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        name = os.getenv("NAME", "Mondo") 
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hola, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized hola.",
             status_code=200
        )