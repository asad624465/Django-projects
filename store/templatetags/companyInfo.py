from django import template
from store.models import OurProjectInfo

register=template.Library()

@register.filter

def companyLogo(request):
    if request:
        company=OurProjectInfo.objects.filter(is_active=True).order_by('-id').first()
        return company.company_logo.url

@register.filter
def companyName(request):
    if request:
        company=OurProjectInfo.objects.filter(is_active=True).order_by('-id').first()
        return company.company_name

@register.filter
def companyAddress(request):
    if request:
        company=OurProjectInfo.objects.filter(is_active=True).order_by('-id').first()
        return company.company_address

@register.filter
def aboutCompany(request):
    if request:
        company=OurProjectInfo.objects.filter(is_active=True).order_by('-id').first()
        return company.about_company

@register.filter
def companyEmail(request):
    if request:
        company=OurProjectInfo.objects.filter(is_active=True).order_by('-id').first()
        return company.email_adddress

@register.filter
def companyPhone(request):
    if request:
        company=OurProjectInfo.objects.filter(is_active=True).order_by('-id').first()
        return company.contract_number

@register.filter
def facebook(request):
    if request:
        company=OurProjectInfo.objects.filter(is_active=True).order_by('-id').first()
        return company.facebook

@register.filter
def twitter(request):
    if request:
        company=OurProjectInfo.objects.filter(is_active=True).order_by('-id').first()
        return company.twitter

@register.filter
def youtube(request):
    if request:
        company=OurProjectInfo.objects.filter(is_active=True).order_by('-id').first()
        return company.youtube

@register.filter
def linkedin(request):
    if request:
        company=OurProjectInfo.objects.filter(is_active=True).order_by('-id').first()
        return company.linkedin