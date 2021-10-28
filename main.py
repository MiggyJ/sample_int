from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

#* Import Submodules
from apps.visitor_management.app import app as vms

from template import views

app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')

#* Mount Submodules 
app.mount('/vms', vms)

@app.get('/login')
def login(req: Request):
    return views.TemplateResponse('login.html',{
        'request': req
    })

@app.get('/admin')
def login(req: Request):
    return views.TemplateResponse('admin.html',{
        'request': req
    })

@app.get('/')
def index(req: Request):
    return views.TemplateResponse('index.html',{
        'request': req
    })