from django.db import models



class product(models.Model):
  name = models.CharField(max_length=200, verbose_name="Наименование")
  cost = models.IntegerField(verbose_name="Стоимость")
  description = models.CharField(max_length=200 , verbose_name="Описание")
  count = models.IntegerField(verbose_name="Количетво")
  dod =  models.DateField(auto_now=True, verbose_name="Дата поставки")
  pic = models.ImageField(upload_to="myapp/static/img", blank=True)
  cat = models.ForeignKey("cat", on_delete=models.CASCADE, blank=True, null=True, default=1)
  def __str__(self):
    return self.name

# Create your models here.



class cat(models.Model):
  category_name = models.CharField(max_length=200)
  category_description = models.CharField(max_length=2000)

  def __str__(self):
    return self.category_name
  




class Animal(models.Model):
  name = models.CharField(max_length=100)
  sound = models.CharField(max_length=100)
  def speak(self, a):
    return a**2 #f'The {self.name} says "{self.sound}"'
  

