from django.contrib import admin
from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'position', 'employment_type', 'status', 'created_at')
    list_filter = ('employment_type', 'status', 'department', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number', 'position')
    prepopulated_fields = {'slug': ('first_name', 'last_name')}
    ordering = ('-created_at',)
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'slug', 'email', 'phone_number', 'address', 'image')
        }),
        ('Employment Details', {
            'fields': ('position', 'qualification', 'employment_type', 'department', 'subjects', 'join_date', 'status')
        }),
        ('Status & Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    filter_horizontal = ('subjects',)
    readonly_fields = ('created_at', 'updated_at')