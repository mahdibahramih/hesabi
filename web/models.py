from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class expense(models.Model):
    text = models.CharField(max_length=50)
    user_name = models.ForeignKey(User , on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    amount = models.BigIntegerField()
    sour = models.CharField(max_length=20)
    def  __unicode__(self):
        return "{}    {}   {}".format( self.user_name ,self.text , self.amount)


class income(models.Model):
    text = models.CharField(max_length=50)
    user_name = models.ForeignKey(User , on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    amount = models.BigIntegerField()
    sour = models.CharField(max_length=20)
    def  __unicode__(self):
        return "{}    {}     {}".format(self.username , self.text , self.amount)

class groupha(models.Model):
    name = models.CharField(max_length=50)
    discription = models.TextField()
    admin = models.ForeignKey(User , on_delete=models.CASCADE)
    status = models.CharField(max_length=10)
    def  __unicode__(self):
        return "{}    {}     {}".format(self.admin , self.name , self.status)


class group_member(models.Model):
    this_user = models.ForeignKey(User , on_delete=models.CASCADE)
    this_group = models.ForeignKey(groupha , on_delete=models.CASCADE)
    def  __unicode__(self):
        return "{}    {} ".format(self.this_user , self.this_group)


class group_expense(models.Model):
    text = models.CharField(max_length=50)
    user_name = models.ForeignKey(User , on_delete=models.CASCADE)
    this_group = models.ForeignKey(groupha, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    amount = models.BigIntegerField()
    def  __unicode__(self):
        return "{}    {}     {}      {}".format( self.user_name,self.this_group ,self.text , self.amount)



class group_income(models.Model):
    text = models.CharField(max_length=50)
    user_name = models.ForeignKey(User , on_delete=models.CASCADE)
    this_group = models.ForeignKey(groupha, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    amount = models.BigIntegerField()
    def  __unicode__(self):
        return "{}    {}     {}      {}".format( self.user_name,self.this_group ,self.text , self.amount)


class temporary_group_member(models.Model):
    this_user = models.ForeignKey(User , on_delete=models.CASCADE)
    this_group = models.ForeignKey(groupha , on_delete=models.CASCADE)
    def  __unicode__(self):
        return "{}    {} ".format(self.this_user , self.this_group)
