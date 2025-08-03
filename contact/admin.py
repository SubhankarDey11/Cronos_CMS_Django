from django.contrib import admin
from .models import ContactInfo, ContactSubmission

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['email', 'phone', 'is_active']
    list_editable = ['is_active']
    fieldsets = (
        ('Contact Information', {
            'fields': ('address', 'phone', 'email', 'website')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'is_read', 'created_at']
    list_editable = ['is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['created_at']
    date_hierarchy = 'created_at'
