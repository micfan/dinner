from django.contrib import admin

from dinner.models import Provider, MenuItem, Order, OrderItem, CalendarProvider


class OrderAdmin(admin.ModelAdmin):
    list_display = ('calendar', 'user')



admin.site.register(Provider)

admin.site.register(MenuItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(CalendarProvider)
