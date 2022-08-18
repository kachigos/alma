from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models

from product.models import Product


class OrderManager(models.Manager):

    def has_bought_product(self, product):
        Order.objects.filter(order_items__product_id=product.id)

    def get_order_not_containing_product(self, product):
        return Order.objects.exclude(order_items__product_id=product.id).first()


class Order(models.Model):
    ORDERED = 0
    IN_TRANSIT = 1
    DELIVERED = 2

    ORDER_STATUS = (
        (ORDERED, "ordered"),
        (IN_TRANSIT, "In transit"),
        (DELIVERED, "Delivered"),
    )
    order_status = models.SmallIntegerField(choices=ORDER_STATUS, default=ORDERED)
    tracking_number = models.CharField(max_length=50)
    user = models.ForeignKey(
        # settings.AUTH_USER_MODEL, # better practice, but no intellisense in filter(), exclude , etc.
        User,  # intellisense available, at least in pycharm :)
        related_name='orders', null=True, blank=True, on_delete=models.SET_NULL,
        verbose_name='User')

    objects = OrderManager()

    def __str__(self):
        return str(self.tracking_number)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False, related_name='orders_is_in')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False, blank=False, related_name='order_items')
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    price = models.FloatField(validators=[MinValueValidator(1.0)])
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='products_bought')
    # user = models.ForeignKey(AppUser, on_delete=models.SET_NULL, related_name='order_items')

    def __str__(self):
        return self.name + self.product
