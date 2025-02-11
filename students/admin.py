from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'grade', 'status', 'created_at')
    list_filter = ('grade', 'gender', 'status', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
    prepopulated_fields = {'slug': ('first_name', 'last_name')}
    ordering = ('-created_at',)
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'slug', 'birth_date', 'gender', 'email', 'phone_number', 'image')
        }),
        ('School Details', {
            'fields': ('grade', 'group', 'status')
        }),
        ('Guardian Information', {
            'fields': ('guardian_name', 'guardian_phone', 'guardian_email')
        }),
        ('Address', {
            'fields': ('address',)
        }),
        ('Status & Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at', 'updated_at')

