from django.db import models

# Create your models here.
class User(models.Model):
 user_id= models.IntegerField()
 user_name= models.CharField(max_length=50)
 phone=models.CharField()
 password=models.CharField()
 email=models.CharField(max_length=25)
 creat_date=models.DateField()
 last_date=models.DateField()

 class Notification(models.Model):
    user_id = models.IntegerField()
    notification_type = models.CharField(max_length=50)
    notification_text = models.CharField()
    
 class Financial_Movement(models.Model):
     FM_id = models.IntegerField()
     user_id =models.IntegerField()
     use_user_id = models.IntegerField()
     discription = models.CharField() 
     method = models.CharField()
     data_time = models.DateTimeField()
     reference = models.CharField()
     admin_configration = models.BooleanField()
     im_port =models.DecimalField(max_digits=5, decimal_places=2)
     export = models.DecimalField(max_digits=5, decimal_places=2)
     img = models.ImageField()

class Comparison(models.Model):
   Comparison_id = models.IntegerField()
   property_id =models.IntegerField()
   price=models.DecimalField(max_digits=5, decimal_places=2)
   location=models.CharField() 
   description=models.CharField(max_length=100) 

class Photo_Property(models.Model):
   Photo_Property_id = models.IntegerField()
   property_id = models.IntegerField()
   description=models.CharField(max_length=100)
   path=models.CharField()

class Favorite(models.Model):
   favorite_id = models.IntegerField()
   property_id =  models.IntegerField()
   user_id = models.IntegerField()
   status =models.CharField()   

class ADS(models.Model):
   ADS_id= models.IntegerField()
   property_id= models.IntegerField()
   user_id= models.IntegerField()

class Photo_ADS(models.Model):
   Photo_ADS_id= models.IntegerField()
   photADS_id= models.IntegerField()
   description=models.CharField(max_length=100)
   path=models.CharField()

class Evaluation(models.Model):
   evaluation_id= models.IntegerField()
   user_id= models.IntegerField()
   cus_user_id= models.IntegerField()
   rating= models.IntegerField()
   review=models.CharField()

class Report_Customer(models.Model):
   Report_Customer_id= models.IntegerField()
   ADS_id= models.IntegerField()
   user_id= models.IntegerField()
   report_text=models.CharField()
   report_type=models.CharField()
   report_state=models.CharField()
