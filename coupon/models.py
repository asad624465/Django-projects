from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Coupon(models.Model):
    code=models.CharField(unique=True, max_length=15)
    valid_from=models.DateField()
    valid_to=models.DateField()
    discount=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(70)])
    active_status=models.BooleanField(default=False)
    
    class Meta:
        verbose_name="coupon Code"
    
    def __str__(self):
        return self.code
