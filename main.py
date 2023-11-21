from fastapi import FastAPI
from app.api.v1.GetFormTemplateRouter import router as form_validation_router
from app.api.v1.CreateFormTemplateRouter import router as create_form_template_router
app = FastAPI()

app.include_router(form_validation_router, prefix='/v1/templates')
app.include_router(create_form_template_router, prefix='/v1/templates')
