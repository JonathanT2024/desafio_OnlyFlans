from django.contrib import admin
from web.models import Flan, Contact

# Register your models here.
class FlanAdmin(admin.ModelAdmin):
    pass

admin.site.register(Flan, FlanAdmin)


class ContacAdmin(admin.ModelAdmin):
    pass

admin.site.register(Contact, ContacAdmin)