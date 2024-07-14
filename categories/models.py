from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    image = models.ImageField(upload_to='uploads/product', blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name