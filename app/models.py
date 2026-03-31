from django.db import models

# Create your models here.
class Gender(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name
class Acc_type(models.Model):
    name = models.CharField(max_length=15)
    def __str__(self):
        return self.name
class Relation(models.Model):
    name = models.CharField(max_length=15)
    def __str__(self):
        return self.name
class State(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name

class Acc_details(models.Model):
    acc_number = models.BigAutoField(primary_key=True)
    balance = models.BigIntegerField(default=1000)
    pin = models.CharField(default='0000')
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.BigIntegerField()
    adhar = models.PositiveIntegerField(unique='True')
    email = models.EmailField(unique='True')
    address = models.TextField()
    gender = models.ForeignKey(Gender,on_delete=models.CASCADE)
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    nomini_name = models.CharField(max_length=30)
    relation = models.ForeignKey(Relation,on_delete=models.CASCADE)
    acc_type = models.ForeignKey(Acc_type,on_delete=models.CASCADE)
