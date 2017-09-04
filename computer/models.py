from django.db import models

# Create your models here.

class Computer(models.Model):
    # 计算机的属性
    owner = models.CharField(max_length = 20)
    date_made = models.CharField(max_length = 20)
    company_name = models.CharField(max_length = 20)
    computer_model = models.CharField(max_length = 20)
    date_added = models.DateTimeField(auto_now_add= True)
    
    def __str__(self):
        return self.owner 
    

    
    
