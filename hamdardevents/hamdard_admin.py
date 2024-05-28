from django.contrib import admin
from django.contrib.admin.apps import AdminConfig


class HamdardAdminSite(admin.AdminSite):
    site_header = "Hamdard Events Admin"
    site_title = "Hamdard Events Admin"


class HamdardAdminConfig(AdminConfig):
    default_site = 'hamdardevents.hamdard_admin.HamdardAdminSite'
