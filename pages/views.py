from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import SiteSettings, HeroSection, Feature, Testimonial, PricingPlan, Page

# Create your views here.

def get_site_settings():
    """Get site settings or return None"""
    try:
        return SiteSettings.objects.first()
    except:
        return None

def home(request):
    """Homepage view"""
    site_settings = get_site_settings()
    context = {
        'hero_sections': HeroSection.objects.filter(is_active=True),
        'features': Feature.objects.filter(is_active=True)[:6],
        'testimonials': Testimonial.objects.filter(is_active=True)[:3],
        'site_settings': site_settings,
    }
    return render(request, 'pages/home.html', context)

def features(request):
    """Features page view"""
    site_settings = get_site_settings()
    context = {
        'features': Feature.objects.filter(is_active=True),
        'site_settings': site_settings,
    }
    return render(request, 'pages/features.html', context)

def pricing(request):
    """Pricing page view"""
    site_settings = get_site_settings()
    context = {
        'pricing_plans': PricingPlan.objects.filter(is_active=True),
        'site_settings': site_settings,
    }
    return render(request, 'pages/pricing.html', context)

class PageDetailView(DetailView):
    """Generic page detail view"""
    model = Page
    template_name = 'pages/page_detail.html'
    context_object_name = 'page'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_settings'] = get_site_settings()
        return context
