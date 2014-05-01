from django.contrib import admin
from django.forms import ModelForm

from suit.widgets import SuitDateWidget

from models import *

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Etapa)
