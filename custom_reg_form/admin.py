from django.contrib import admin
from .models import ExtraInfo

from django.db import models
from django.conf import settings

# Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, "AUTH_USER_MODEL", "auth.User")
from django.db.models.signals import pre_delete
from django.dispatch import receiver



@receiver(pre_delete, sender=USER_MODEL, dispatch_uid='question_delete_log')
def log_deleted_user(sender, instance, using, **kwargs):

   try:
       e = ExtraInfo.filter(user__id=instance.id).first()
       e.delete()
   except:
       pass





@admin.register(ExtraInfo)
class ExtraInfoAdmin(admin.ModelAdmin):
    readonly_fields = (
        'name',
    )

    list_display = (
        'user',
        'name',
        'email',
        'is_active',
        'eres_docente',
        'cct'
    )

    list_filter = (
        'eres_docente',
        'cct',
        'user__is_active',
    )

    search_fields = (
        'user__username',
        'user__first_name',
        'user__last_name',
        'user__email',
    )

    def is_active(self, obj):
        return obj.user.is_active

    def email(self, obj):
        return obj.user.email

    def name(self, obj):
        profile = getattr(obj.user, 'profile', None)

        if profile:
            return getattr(profile, 'name', '')

        return ''






