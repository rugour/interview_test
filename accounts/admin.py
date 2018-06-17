from django.contrib import admin
from django.utils import timezone
from .models import APIUser, SearchCall
from django.utils.html import format_html

class APIUserAdmin(admin.ModelAdmin):
    """docstring for APIUserAdmin"""
    model = APIUser
    list_display = ('login', 'avatar')
    search_fields = ['added_on', 'email', 'login']

class ReportAdmin(admin.ModelAdmin):
    date_hierarchy = 'called_on'
    readonly_fields = (
        'calls_made_in_this_week',
        'calls_made_in_this_month',
        'user_added_on_day',
        'user_added_in_week',
        'user_added_in_month',
        )

    def get_readonly_fields(self, request, obj=None):
        return ('called_on', 'counter') + self.readonly_fields


    def calls_made_in_this_week(self, instance):
        c = SearchCall.objects.filter(
            called_on__gt=instance.called_on-timezone.timedelta(days=7),
            called_on__lte=instance.called_on,
            )
        total=0
        for a in c:
            total += a.counter 
        return format_html('<p>{}</>',total)

    def calls_made_in_this_month(self, instance):
        c = SearchCall.objects.filter(
            called_on__gt=instance.called_on-timezone.timedelta(days=30),
            called_on__lte=instance.called_on,
            )
        total=0
        for a in c:
            total += a.counter 
        return format_html('<p>{}</>',total)

    def user_added_on_day(self, instance):
        c = APIUser.objects.filter(
            added_on=instance.called_on
            ).count()
        return format_html('<p>{}</>',c)


    def user_added_in_week(self, instance):
        c = APIUser.objects.filter(
            added_on__gt=instance.called_on-timezone.timedelta(days=7),
            added_on__lte=instance.called_on,
            ).count()
        return format_html('<p>{}</>',c)


    def user_added_in_month(self, instance):
        c = APIUser.objects.filter(
            added_on__gt=instance.called_on-timezone.timedelta(days=30),
            added_on__lte=instance.called_on,
            ).count()
        return format_html('<p>{}</>',c)

    def has_add_permission(self, request):
        return False

admin.site.register(APIUser, APIUserAdmin)
admin.site.register(SearchCall, ReportAdmin)