from django.contrib import admin
from users.models import Member


# Register your models here.
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'cms_id')

    def username(self, member):
        return member.user.username
    
    def email(self, member):
        return member.user.email
