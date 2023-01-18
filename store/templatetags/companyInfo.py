from django import template
from store.models import OurProjectInfo

register=template.Library()

@register.filter

def companyLogo(user):
    if user.is_authenticated:
        company=OurProjectInfo.objects.filter(user=user,is_active=True).order_by('-id').first()
        return company.company_logo.url
    else:
        company=OurProjectInfo.objects.filter(is_active=True).order_by('-id').first()
        return company.company_logo.url

@register.filter
def companyName(user):
    if user.is_authenticated:
        company=OurProjectInfo.objects.filter(user=user,is_active=True).order_by('-id').first()
        return company.company_name
    else:
        company=OurProjectInfo.objects.filter(is_active=True).order_by('-id').first()
        return company.company_name 

@register.filter
def companyAddress(user):
    if user.is_authenticated:
        company=OurProjectInfo.objects.filter(user=user,is_active=True).order_by('-id').first()
        return company.company_address
    else:
        company=OurProjectInfo.objects.filter(is_active=True).order_by('-id').first()
        return company.company_address
@register.filter
def aboutCompany(user):
    if user.is_authenticated:
        company=OurProjectInfo.objects.filter(user=user,is_active=True).order_by('-id').first()
        return company.about_company
    else:
        company=OurProjectInfo.objects.filter(is_active=True).order_by('-id').first()
        return company.about_company 
@register.filter
def companyEmail(user):
    if user.is_authenticated:
        company=OurProjectInfo.objects.filter(user=user,is_active=True).order_by('-id').first()
        return company.email_adddress
    else:
        company=OurProjectInfo.objects.filter(is_active=True).order_by('-id').first()
        return company.email_adddress
@register.filter
def companyPhone(user):
    if user.is_authenticated:
        company=OurProjectInfo.objects.filter(user=user,is_active=True).order_by('-id').first()
        return company.contract_number
    else:
        company=OurProjectInfo.objects.filter(is_active=True).order_by('-id').first()
        return company.contract_number

@register.filter
def facebook(user):
    if user.is_authenticated:
        company=OurProjectInfo.objects.filter(user=user,is_active=True).order_by('-id').first()
        return company.facebook
    else:
        company=OurProjectInfo.objects.filter(is_active=True).order_by('-id').first()
        return company.facebook
@register.filter
def twitter(user):
    if user.is_authenticated:
        company=OurProjectInfo.objects.filter(user=user,is_active=True).order_by('-id').first()
        return company.twitter
    else:
        company=OurProjectInfo.objects.filter(is_active=True).order_by('-id').first()
        return company.twitter
@register.filter
def youtube(user):
    if user.is_authenticated:
        company=OurProjectInfo.objects.filter(user=user,is_active=True).order_by('-id').first()
        return company.youtube
    else:
        company=OurProjectInfo.objects.filter(is_active=True).order_by('-id').first()
        return company.youtube
@register.filter
def linkedin(user):
    if user.is_authenticated:
        company=OurProjectInfo.objects.filter(user=user,is_active=True).order_by('-id').first()
        return company.linkedin
    else:
        company=OurProjectInfo.objects.filter(is_active=True).order_by('-id').first()
        return company.linkedin