from django.contrib import admin


from .models import Cryptocurrency2, Cryptocurrency1, Cryptocurrency23
# Register your models here.

from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser
# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('Rating',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('Rating',)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)


class Cryptocurrency1Admin(admin.ModelAdmin):
    list_display = ('name', 'usd_price',)


admin.site.register(Cryptocurrency1, Cryptocurrency1Admin)


class Cryptocurrency2Admin(admin.ModelAdmin):
    list_display = ('response_data', 'datetime_moified')


admin.site.register(Cryptocurrency2, Cryptocurrency2Admin)


class Cryptocurrency23Admin(admin.ModelAdmin):
    list_display = ('response_datA', 'datetime_moified')


admin.site.register(Cryptocurrency23, Cryptocurrency23Admin)


