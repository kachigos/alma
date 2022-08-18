from django.contrib import admin
from .models import *

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Rating)
admin.site.register(Favorite)
admin.site.register(Like)
