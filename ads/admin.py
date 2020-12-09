from django.contrib import admin
from django.apps import apps

# from .models import AdTypes, Book, Category, Condition, PriceType, Price, Ad




models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass

# admin.site.register(AdTypes)
# admin.site.register(Book)
# admin.site.register(Category)
# admin.site.register(Condition)
# admin.site.register(PriceType)
# admin.site.register(Price)
# admin.site.register(Ad)
