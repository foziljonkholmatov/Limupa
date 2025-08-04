from django.db import models
from django.utils.translation import gettext_lazy as _

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated_at'))

    class Meta:
        abstract = True


class ContactModel(BaseModel):
    name = models.CharField(max_length=60, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    subject = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('subject'))
    message = models.TextField(verbose_name=_('message'))
    is_read = models.BooleanField(default=False, verbose_name=_('is_read'))


    def __str__(self):
        return  f"{self.name} | {self.email}"

    class Meta:
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')