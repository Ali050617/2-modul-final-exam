from django.contrib import admin
from .models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'head_department', 'email', 'phone_number', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'email', 'phone_number')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('-created_at',)
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'head_department', 'description', 'location')
        }),
        ('Contact Details', {
            'fields': ('email', 'phone_number')
        }),
        ('Status & Metadata', {
            'fields': ('status', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
