from django.db import models

class DemoModel(models.Model):
    auto_field = models.AutoField(primary_key=True)
    file = models.BinaryField()
    number = models.IntegerField()
    agreed = models.BooleanField()
    name = models.CharField(max_length=50)
    published = models.DateTimeField()
    email = models.EmailField()
    ip_address = models.GenericIPAddressField()
    image = models.ImageField(upload_to='images/')
    price = models.PositiveBigIntegerField()
    slug = models.SlugField()
    time_in_day = models.TimeField()
    url = models.URLField()