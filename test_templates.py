#!/usr/bin/env python
"""
Template testing script for Cronos Django CMS
This script tests if all templates can be rendered without errors.
"""

import os
import sys
import django
from django.conf import settings
from django.template.loader import render_to_string

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cronos_project.settings')
django.setup()

def test_template(template_name, context_data=None):
    """Test if a template can be rendered"""
    try:
        if context_data is None:
            context_data = {}
        
        # Try to render the template
        rendered = render_to_string(template_name, context_data)
        print(f"✅ {template_name} - Rendered successfully")
        return True
    except Exception as e:
        print(f"❌ {template_name} - Error: {str(e)}")
        return False

def main():
    """Test all templates"""
    print("🔍 Testing Cronos Django CMS Templates")
    print("=" * 50)
    
    # Test base template
    test_template('base.html', {
        'site_settings': None
    })
    
    # Test home template
    test_template('pages/home.html', {
        'hero_sections': [],
        'features': [],
        'testimonials': [],
        'site_settings': None
    })
    
    # Test features template
    test_template('pages/features.html', {
        'features': [],
        'site_settings': None
    })
    
    # Test pricing template
    test_template('pages/pricing.html', {
        'pricing_plans': [],
        'site_settings': None
    })
    
    # Test contact template
    test_template('contact/contact.html', {
        'form': None,
        'contact_info': None,
        'site_settings': None
    })
    
    print("\n🎉 Template testing completed!")
    print("If you see ✅ marks, your templates are working correctly.")
    print("If you see ❌ marks, there are actual template errors to fix.")

if __name__ == '__main__':
    main() 