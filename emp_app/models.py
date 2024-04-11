from django.db import models

class Department(models.Model):
    name=models.CharField(max_length=50,null=False)
    location=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Role(models.Model):
    name=models.CharField(max_length=50,null=False)
    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name=models.CharField(max_length=50,null=False)
    last_name=models.CharField(max_length=50)
    dept=models.ForeignKey(Department,on_delete=models.CASCADE) #Foreign Key
    salary=models.IntegerField(default=0)
    bonus=models.IntegerField(default=0)
    role=models.ForeignKey(Role,on_delete=models.CASCADE) #Forein Key
    phone=models.IntegerField(default=0,max_length=10)
    hire_date=models.DateField()
    
    def __str__(self):
        return "%s %s %s"%(self.first_name,self.last_name,self.phone)
   
