from django.db import models

class users(models.Model):
    first_name = models.CharField(max_length= 55)
    last_name = models.CharField(max_length= 55)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add = True)

class messages(models.Model):
    user_id = models.ForeignKey(users)
    messages = models.TextField(max_length = 1000)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add = True)

class comments(models.Model):
    user_id = models.ForeignKey(users)
    messages_id = models.ForeignKey(messages)
    comment = models.TextField(max_length = 1000)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add = True)
# Create your models here.
