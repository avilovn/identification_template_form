from fastapi import APIRouter, Request, HTTPException
from app.db.config import db

router = APIRouter()


@router.post('/create_form',
             tags=['Создание шаблона формы валидации'])
async def create_template_form(request: Request):
    try:

        data = await request.form()
        values = dict(data)
        items = values.items()

        if not items:
            raise ValueError("Входные параметры не обнаружены.")

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=500, detail="Внутренняя ошибка")

    UUID = db.insert(dict(items))
    return {"message": "Шаблон формы успешно создан", "id": UUID, "items": [items]}


