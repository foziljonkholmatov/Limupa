from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ContactModel(BaseModel):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    subject = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)


    def __str__(self):
        return  f"{self.name} | {self.email}"

    class Meta:
        verbose_name ='contact'
        verbose_name_plural = 'contacts'