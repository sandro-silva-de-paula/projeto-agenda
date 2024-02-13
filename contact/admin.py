from django.contrib import admin
from contact import models


@admin.register(models.Category)
class CategorytAdmin(admin.ModelAdmin):
    list_display = 'name',


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'first_name', "last_name", 'phone', 'show',
    list_editable = 'show',
    ordering = '-id',
    list_filter = 'created_date', 'category'
    search_fields = 'first_name', "last_name",
    list_per_page = 50
    list_max_show_all = 200
    list_display_links = 'first_name', "last_name",
