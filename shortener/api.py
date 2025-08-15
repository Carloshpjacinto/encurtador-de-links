from ninja import Router

from .models import Links
from .schemas import LinkSchema

shortener_router = Router()


@shortener_router.get('create/', response={200: LinkSchema, 409: dict})
def create(request, link_schema: LinkSchema):
    data = link_schema.to_model_data()

    token = data['token']

    if token and Links.objects.filter(token=token).exists():
        return 409, {'error': 'Token já existe, use outro'}
    
    link = Links(**data)
    link.save()

    return 200, link
