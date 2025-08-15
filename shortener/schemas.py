from ninja import ModelSchema, Schema
from datetime import timedelta

from .models import Links


class LinkSchema(ModelSchema):
    expiration_time: int
    

    class Meta:
        model = Links
        fields = ['redirect_link', 'token', 'expiration_time', 'max_uniques_cliques']

    def to_model_data(self):
        return{
            "redirect_link": self.redirect_link,
            "token": self.token,
            "expiration_time": timedelta(minutes=self.expiration_time),
            "max_uniques_cliques": self.max_uniques_cliques
        }
    