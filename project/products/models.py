from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    category_text = models.CharField(max_length=128)

    def __str__(self):
        return self.category_text


class Brand(models.Model):
    brand_text = models.CharField(max_length=128)

    def __str__(self):
        return self.brand_text


class Product(models.Model):
    product_text = models.CharField(max_length=128)
    description = RichTextUploadingField()
    price = models.IntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    IN_STOCK = '??? / In Stock'
    OUT_OF_STOCK = '??? / Out of stock'
    NEED_TO_CONFIRM = '??? / Need to confirm'
    INVENTORY_STATUS = (
        (IN_STOCK, 'In Stock'),
        (OUT_OF_STOCK, 'Out Of Stock'),
        (NEED_TO_CONFIRM, 'Need To Confirm'),
    )

    inventory_status = models.CharField(
        max_length=128,
        choices=INVENTORY_STATUS,
        default=IN_STOCK,
    )

    def __str__(self):
        return self.product_text

    def __unicode__(self):
        return u"{}".format(self.your_field)


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
