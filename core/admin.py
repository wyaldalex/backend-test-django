from django.contrib import admin
from .models import Payment

# Register your models here.
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_id','customer','staff','rental','amount','payment_date')


admin.register(Payment,PaymentAdmin)
