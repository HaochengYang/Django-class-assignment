from __future__ import unicode_literals

from django.db import models

class ProductManager(models.Manager):
    def product_check(self, postdata):
        errors = []
        if not len(postdata['product_name']):
            errors.append('product name must enter')
        if not len(postdata['description']):
            errors.append('description must enter')
        if not len(postdata['price']):
            errors.append('price must enter')

        response = {}
        if errors:
            response['status'] = False
            response['errors'] = errors
        else:
            response['status'] = True
            self.create(product_name=postdata['product_name'],description=postdata['description'],price=postdata['price'])
        return response

    def product_edit(self,postdata,id):
        self.filter(id=id).update(product_name=postdata['new_product_name'], description=postdata['new_description'], price=postdata['new_price'])
# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    description =models.TextField(max_length=1000)
    price = models.IntegerField()
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    objects = ProductManager()
