from django.contrib import admin
from .models import Acc_details,State,Relation,Acc_type,Gender
# Register your models here.
admin.site.register(Acc_details)
admin.site.register(State)
admin.site.register(Acc_type)
admin.site.register(Relation)
admin.site.register(Gender)