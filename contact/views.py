from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactInfo, ContactSubmission
from .forms import ContactForm
from pages.models import SiteSettings

def get_site_settings():
    """Get site settings or return None"""
    try:
        return SiteSettings.objects.first()
    except:
        return None

def contact(request):
    """Contact page view"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_submission = form.save()
            
            # Send email notification (optional)
            try:
                send_mail(
                    f'New Contact Form Submission: {contact_submission.subject}',
                    f'Name: {contact_submission.name}\nEmail: {contact_submission.email}\nMessage: {contact_submission.message}',
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.ADMIN_EMAIL] if hasattr(settings, 'ADMIN_EMAIL') else [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=True,
                )
            except:
                pass  # Email sending failed, but don't break the form submission
            
            messages.success(request, 'Thank you for your message. We will get back to you soon!')
            return redirect('contact:contact')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
        'contact_info': ContactInfo.objects.filter(is_active=True).first(),
        'site_settings': get_site_settings(),
    }
    return render(request, 'contact/contact.html', context) 