from django import forms
from payment.models import BillingAddress
from order.models import Order

class BillingAddressForm(forms.ModelForm):
     class Meta:
        model=BillingAddress
        fields=['first_name','last_name','country','address_one','address_two','city','zipcode','phone_number']
   
class PaymentForms(forms.ModelForm):
   class Meta:
      model=Order
      fields=['payment_method']