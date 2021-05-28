from django.contrib import admin
from .models import Lead , Office_Address , Residence_Address

admin.site.register(Lead)
admin.site.register(Residence_Address)
admin.site.register(Office_Address)
