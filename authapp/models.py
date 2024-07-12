from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    pnumbner=models.CharField(max_length=12)
    description=models.TextField(max_length=200)

    def __str__(self):
        return self.email

class Enrollment(models.Model) :
    fullname= models.CharField(max_length=30)
    Email=models.EmailField()
    Gender= models.CharField(max_length=10)
    PhoneNumber=models.CharField(max_length=25)
    DOB=models.CharField(max_length=10)
    SelectMembershipplan=models.CharField(max_length=200)
    SelectTrainer=models.CharField(max_length=50)
    Reference=models.CharField(max_length=50)
    Address=models.TextField()
    timeStamp=models.DateField(auto_now_add=True,blank=True)
    paymentStatus=models.CharField(max_length=50,blank=True,null=True)
    Amount=models.IntegerField(blank=True,null=True)
    DueDate=models.DateField(blank=True,null=True)



    def __str__(self):
        return self.fullname

    
class Trainer(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    phone=models.CharField(max_length=25)
    salary=models.IntegerField()
    timeStamp=models.DateField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.name

class MembershipPlan(models.Model) :
    plan=models.CharField(max_length=185)
    price=models.IntegerField()    

    def __int__(self):
        return self.id

class Gallary(models.Model) :
    tital=models.CharField(max_length=100)
    img=models.ImageField(upload_to='gallery')
    timeStamp=models.DateField(auto_now_add=True,blank=True)
    def __int__(self):
        return self.id
class Attendence(models.Model) :  
    selsectdate= models.DateField(auto_now_add=True)
    phonenumber=models.CharField(max_length=25) 
    login=models.CharField(max_length=200)
    logout=models.CharField(max_length=200)
    selectworkout=models.CharField(max_length=200)
    trainedby= models.CharField(max_length=200) 

    def __int__(self):
        return self.id
class Services(models.Model) :  
    sname=models.CharField( max_length=50)
    about=models.CharField( max_length=500)
    simg=models.ImageField(upload_to='serviceimg')
    def __int__(self):
        return self.id

class Workout(models.Model) :  
    workoutname=models.CharField( max_length=50)
    workouttype=models.CharField( max_length=50)
    weight=models.IntegerField(blank=True)
    repitaions=models.IntegerField(blank=True)
    numberofset=models.IntegerField(blank=True)
    simg=models.ImageField(upload_to='workout')
    def __int__(self):
        return self.workoutname