from fastapi import APIRouter, Request
from app.schemas.ValidationSchema import field_validation
from app.db.config import db

router = APIRouter()


@router.post('/get_form',
             tags=['Получение формы валидации по параметрам'])
async def get_form_template(request: Request):
    request_data = await request.form()
    form_data = dict(request_data)

    validation_fields = {field: field_validation(value) for field, value in form_data.items()}
    composite_query = []

    for data in db.all():
        data_fields = {key: data[key] for key in data if key.startswith("field_name_")}

        if all(field in validation_fields for field in data_fields):
            composite_query.append({"name": data["name"]})

    if composite_query:
        return composite_query
    else:
        return validation_fields
