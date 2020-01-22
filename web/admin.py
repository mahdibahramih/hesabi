from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(expense)
admin.site.register(income)
admin.site.register(groupha)
admin.site.register(group_member)
admin.site.register(temporary_group_member)
admin.site.register(group_expense)
admin.site.register(group_income)
