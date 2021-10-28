from fastapi import FastAPI, Request

#* Import Module-Specific Templates
from apps.visitor_management.template import views
app = FastAPI()

#* Routes (router files can also be applied)
@app.get('/')
def index(request: Request):
    return views.TemplateResponse('index.html',{
        'request': request,
    })