from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Brend"
        verbose_name_plural = "Brendlar"


class Car(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    date_manufactured = models.DateField()
    count = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Avtomobil"
        verbose_name_plural = "Avtomobillar"


