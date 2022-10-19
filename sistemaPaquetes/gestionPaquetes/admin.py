from django.contrib import admin
# Register your models here.
from gestionPaquetes.models.paquete import Paquete

from .models.account import Account
from .models.user import User

admin.site.register(User)
admin.site.register(Account)
admin.site.register(Paquete)