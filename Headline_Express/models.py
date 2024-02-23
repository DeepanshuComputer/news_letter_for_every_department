from datetime import timedelta, timezone
from django.db import models
from datetime import *
from django.utils import timezone
from ckeditor.fields import RichTextField








# too=(
#     ('Independent','Independent'),
#     ('With Owner','With Owner'),
# )




# Create your models here.

      



class subs_info(models.Model):
    Email= models.EmailField(unique=True)
    Name =models.CharField( max_length= 50)
    def __str__(self):
        return self.Email

# https://www.lamar.edu/academics/colleges-and-departments.html
    
      
    
class department_cat(models.Model):
    main_dep= models.CharField(max_length=60, unique=True)
    main_desc= models.CharField(max_length=60)
    main_image= models.ImageField(upload_to='images/')
    def __str__(self):
            return self.main_dep


class departments(models.Model):
    dept_name = models.CharField(max_length=60, unique=True)
    main_dep = models.ForeignKey(department_cat, on_delete=models.CASCADE , default=None, null=True) 
    def __str__(self):
            return self.dept_name
    

class news(models.Model):
    news_name = models.CharField(max_length=60, unique=True)
    news_img = models.ImageField(upload_to='images/')
    news_description=RichTextField()
    dept_name=models.ForeignKey(departments, on_delete=models.CASCADE , default=None, null=True) 
    news_date=models.DateField(default=(timezone.now() + timedelta(days=1)))
    def __str__(self):
            return self.news_name
 


















