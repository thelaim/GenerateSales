from django.contrib import admin
from .models import Bank, Product, CategoryProduct

admin.site.register(Product)
admin.site.register(CategoryProduct)

@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):

        if not change: # Проверяем что запись только создаётся
            obj.token = abs(hash(obj.name)) # Присваеваем полю автор текущего пользователя
    
        super(BankAdmin, self).save_model(
            request=request,
            obj=obj,
            form=form,
            change=change
        )
