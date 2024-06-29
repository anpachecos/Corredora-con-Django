from django.contrib import admin
from .models import Region, Comuna, TipoPropiedad, Propiedad

admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(TipoPropiedad)
admin.site.register(Propiedad)
