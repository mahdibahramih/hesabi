from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class expense(models.Model):
    text = models.CharField(max_length=50)
    user_name = models.OneToOneField(User , on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    amount = models.BigIntegerField()
    sour = models.CharField(max_length=20)
    def  __unicode__(self):
        return "{}    {}".format(self.text , self.amount)


class income(models.Model):
    text = models.CharField(max_length=50)
    user_name = models.OneToOneField(User , on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    amount = models.BigIntegerField()
    sour = models.CharField(max_length=20)
    def  __unicode__(self):
        return "{}    {}".format(self.text , self.amount)

class group(models.Model):
    name = models.CharField(max_length=50)
    discription = models.TextField()
    admin = models.OneToOneField(User , on_delete=models.CASCADE)
    status = models.CharField(max_length=10)

class group_member(models.Model):
    this_user = models.OneToOneField(User , on_delete=models.CASCADE)
    this_group = models.OneToOneField(group , on_delete=models.CASCADE)

class group_expense(models.Model):
    text = models.CharField(max_length=50)
    user_name = models.OneToOneField(User , on_delete=models.CASCADE)
    this_group = models.OneToOneField(group , on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    amount = models.BigIntegerField()
    def  __unicode__(self):
        return "{}    {}".format(self.text , self.amount)

class group_income(models.Model):
    text = models.CharField(max_length=50)
    user_name = models.OneToOneField(User , on_delete=models.CASCADE)
    this_group = models.OneToOneField(group , on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    amount = models.BigIntegerField()
    def  __unicode__(self):
        return "{}    {}".format(self.text , self.amount)
