from django.contrib import admin
from .models import SiteSettings, HeroSection, Feature, Testimonial, PricingPlan, Page

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['site_name']
    fieldsets = (
        ('Basic Settings', {
            'fields': ('site_name', 'site_description', 'logo', 'favicon')
        }),
        ('Footer Settings', {
            'fields': ('footer_text', 'facebook_url', 'twitter_url', 'instagram_url', 'behance_url')
        }),
    )

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    list_filter = ['is_active']
    search_fields = ['title']

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    list_filter = ['is_active']
    search_fields = ['title', 'description']

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'company', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    list_filter = ['is_active']
    search_fields = ['name', 'position', 'company']

@admin.register(PricingPlan)
class PricingPlanAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'currency', 'is_popular', 'is_active', 'order']
    list_editable = ['price', 'is_popular', 'is_active', 'order']
    list_filter = ['is_active', 'is_popular', 'currency']
    search_fields = ['name', 'description']

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_active', 'created_at']
    list_editable = ['is_active']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
