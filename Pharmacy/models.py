from django.db import models
from django.contrib.auth.models import User
# from email.policy import default
from tkinter import CASCADE


# Create your models here.
class Admin(models.Model):
    #Admin_Phone_Number = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

class User_Profile(models.Model):
    User_Phone_Number = models.IntegerField(primary_key=True)
    User_Name = models.CharField(max_length=100)
    User_Password = models.CharField(max_length=100)

class Bill(models.Model):
    Bill_id = models.CharField(primary_key=True,max_length=50)
    Total_Amount = models.FloatField()
    Date = models.DateField()
    Time = models.TimeField()
    Address = models.CharField(max_length=200)
    Profile = models.CharField(max_length=50) #this one


class Drugs(models.Model):
    Drug_ID = models.CharField(primary_key=True,max_length=50)
    Drug_Name = models.CharField(max_length=100)
    Drug_Details = models.CharField(max_length=200)
    Drug_Link = models.URLField(max_length=200) #this one

class Employee(models.Model):
    Employee_Phone_Number = models.IntegerField(primary_key=True)
    Employee_Password = models.CharField(max_length=100)


class Order(models.Model):
    Order_ID = models.CharField(primary_key=True,max_length=50)
    Drug_ID = models.ForeignKey(Drugs,on_delete=models.CASCADE)
    Order_Amount = models.FloatField()
    Bill_id = models.ForeignKey(Bill,on_delete=models.CASCADE)
    Order_Profile = models.CharField(max_length=200) #this one

class Pre_Book(models.Model):
    ID = models.CharField(primary_key=True,max_length=50)
    User_Phone_Number = models.ForeignKey(User_Profile,on_delete=models.CASCADE)
    Drug_ID = models.ForeignKey(Drugs,on_delete=models.CASCADE)

class Sell(models.Model):
    Sell_ID = models.CharField(primary_key=True,max_length=50)
    Drug_ID = models.ForeignKey(Drugs,on_delete=models.CASCADE)
    
class Storage(models.Model):
    Storage_ID = models.CharField(primary_key=True,max_length=50)
    Drug_ID = models.ForeignKey(Drugs, on_delete=models.CASCADE)
    Storage_Amount = models.IntegerField()

class Availability(models.Model):
    drug_name = models.CharField(primary_key=True, max_length=100)
    drug_group = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    availability = models.CharField(max_length=100)
    
class EmployeePanel(models.Model):
    username = models.CharField(primary_key=True,max_length=100)
    password = models.CharField(max_length=50)
    number = models.IntegerField()
    address = models.CharField(max_length=100)

class InventoryPanel(models.Model):
    drug_name = models.CharField(primary_key=True,max_length=100)
    drug_group = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.CharField(max_length=10)

class Sales(models.Model):
    total_sale = models.CharField(max_length=100)
    monthly_sale = models.CharField(max_length=100)

# class User(models.Model):
#     User_Id = models.CharField(primary_key=True,max_length=50)
#     User_Password = models.CharField(max_length=100)
#     User_Name = models.CharField(max_length=100)
#     User_First_Name = models.CharField(max_length=50)
#     User_Last_Name = models.CharField(max_length=50)
#     User_Email = models.CharField(max_length=100)




