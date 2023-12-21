from django.db import models


class User(models.Model):
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=25)
    creat_date = models.DateField()
    last_date = models.DateField()


class Notification(models.Model):
    user_id = models.IntegerField()
    notification_type = models.CharField(max_length=50)
    notification_text = models.CharField(max_length=50)


class Financial_Movement(models.Model):
    FM_id = models.IntegerField()
    user_id = models.IntegerField()
    use_user_id = models.IntegerField()
    discription = models.TextField()
    method = models.CharField(max_length=100)
    data_time = models.DateTimeField()
    reference = models.CharField(max_length=100)
    admin_configration = models.BooleanField()
    im_port = models.DecimalField(max_digits=5, decimal_places=2)
    export = models.DecimalField(max_digits=5, decimal_places=2)
    img = models.ImageField()


class Comparison(models.Model):
    Comparison_id = models.IntegerField()
    property_id = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=100)


class Photo_Property(models.Model):
    Photo_Property_id = models.IntegerField()
    property_id = models.IntegerField()
    description = models.CharField(max_length=100)
    path = models.CharField(max_length=100)


class Favorite(models.Model):
    favorite_id = models.IntegerField()
    property_id = models.IntegerField()
    user_id = models.IntegerField()
    status = models.CharField(max_length=100)


class ADS(models.Model):
    ADS_id = models.IntegerField()
    property_id = models.IntegerField()
    user_id = models.IntegerField()


class Photo_ADS(models.Model):
    Photo_ADS_id = models.IntegerField()
    photADS_id = models.IntegerField()
    description = models.CharField(max_length=100)
    path = models.CharField(max_length=100)


class Evaluation(models.Model):
    evaluation_id = models.IntegerField()
    user_id = models.IntegerField()
    cus_user_id = models.IntegerField()
    rating = models.IntegerField()
    review = models.CharField(max_length=50)


class Report_Customer(models.Model):
    Report_Customer_id = models.IntegerField()
    ADS_id = models.IntegerField()
    user_id = models.IntegerField()
    report_text = models.CharField(max_length=150)
    report_type = models.CharField(max_length=100)
    report_state = models.CharField(max_length=50)
