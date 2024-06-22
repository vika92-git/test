from django.contrib import admin
from myapp.models import product, cat


class myProd(admin.ModelAdmin):
  list_display=["name","cost","description","count","dod"]
  


admin.site.register(product, myProd)


admin.site.register(cat)

# Register your models here.
