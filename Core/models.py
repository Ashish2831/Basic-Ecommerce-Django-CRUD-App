from django.db import models
import os

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

    def delete(self, using=None, keep_parents=False):
        products = self.product_set.all()
        for product in products:
            product.delete()
        super().delete(using=using, keep_parents=keep_parents)


class Size(models.Model):
    category_id = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    size = models.IntegerField()

    def __str__(self):
        return str(self.size)


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category_id = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def delete(self, using=None, keep_parents=False):
        product_images = self.productimage_set.all()
        for product_image in product_images:
            product_image.delete()
        super().delete(using=using, keep_parents=keep_parents)


class ProductSize(models.Model):
    product_id = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    size_id = models.ManyToManyField(to=Size)

    def __str__(self):
        return str(self.product_id)
        

class ProductImage(models.Model):
    product_id = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    image = models.FileField(upload_to="ProductImages/", default="no_photo.jpg")

    def __str__(self):
        return str(self.product_id)

    def delete(self, using=None, keep_parents=False):
        if self.image.name != "no_photo.jpg":
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super(ProductImage, self).delete(using=using, keep_parents=keep_parents)
