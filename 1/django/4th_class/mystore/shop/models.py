from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=250, unique=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    image = models.ImageField(
        upload_to="images/category/", width_field=300, height_field=300, max_length=300)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    category_id = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    is_active = models.BooleanField(default=False, null=True, blank=True)
    # created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, default=0)
    # updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, default=0)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.product_name
