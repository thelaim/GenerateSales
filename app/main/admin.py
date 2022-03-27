from django.contrib import admin
from .models import Bank, Product, CategoryProduct, Order, User

admin.site.register(Product)
admin.site.register(CategoryProduct)
admin.site.register(Order)
admin.site.register(User)

@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):

        if not change: # Проверяем что запись только создаётся
            obj.token = abs(hash(obj.name)) # Присваеваем hash полю token 
    
        super(BankAdmin, self).save_model(
            request=request,
            obj=obj,
            form=form,
            change=change
        )
