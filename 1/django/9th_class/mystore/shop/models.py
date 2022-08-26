from django.db import models

# Create your models here


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"{self.name}"


class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True)
    date_created = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):

    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door'),
    )

    name = models.CharField(max_length=100, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    category = models.CharField(max_length=250, null=True, choices=CATEGORY)
    description = models.TextField(max_length=1000, null=True, blank=True)
    date_created = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    tag = models.ManyToManyField(Tag)
    image = models.ImageField(
        upload_to="images/category/", max_length=300, blank=True)

    def __str__(self):
        return f"{self.name}"


class Order(models.Model):

    STATUS = (
        ('Pending', 'Pending'),
        ('Out of Delivery', 'Out of Delivery'),
        ('Delivered', 'Delivered'),
    )

    customer_id = models.ForeignKey(
        Customer, null=True, on_delete=models.SET_NULL, related_name='customer')
    product_id = models.ForeignKey(
        Product, null=True, on_delete=models.SET_NULL, related_name='product')
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return f"{self.customer_id}: {self.product_id}"
