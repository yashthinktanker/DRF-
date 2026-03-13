from django.db import models



class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Model_name(models.Model):
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,related_name='model_name')
    modelname = models.CharField(max_length=100)
    color = models.CharField(max_length=10,default="black")

    def __str__(self):
        return self.modelname
