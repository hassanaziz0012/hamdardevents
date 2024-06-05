from django.contrib import admin
from users.models import Member, Society


# Register your models here.
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'cms_id')

    def username(self, member):
        return member.user.username
    
    def email(self, member):
        return member.user.email


@admin.register(Society)
class SocietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'president', 'vice_president')
