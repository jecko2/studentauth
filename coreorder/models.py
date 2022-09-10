from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import pre_save

from coreorder.store.assignmentstore import SUBJECT_TYPE, ACC_LEVEL



User = get_user_model()

# Create your models here.
class InitialCalOrder(models.Model):
    student = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    )
    subject = models.CharField(choices=SUBJECT_TYPE, max_length=50)
    accademic_level = models.CharField(choices=ACC_LEVEL, max_length=10)
    price = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    pages = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)



    class Meta:
        verbose_name = _("InitialCal")
        verbose_name_plural = _("InitialCals")
        get_latest_by = ['created_at']

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse("InitialCal_detail", kwargs={"pk": self.pk})
    
    
    def get_price(self):
        return self.price


# presave the price by number of pages
@receiver(pre_save, sender=InitialCalOrder)
def save_price_with_pages(sender, instance, *args, **kwargs):
    instance.price = instance.pages * 2.7
    # instance.save()