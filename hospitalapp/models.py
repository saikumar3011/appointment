from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):

    """ This class contains details of Patient"""

    id = models.IntegerField(primary_key=True)
    patient_name = models.CharField(max_length=50)
    age = models.CharField(max_length=100,null=True,blank=True)
    gender = models.CharField(max_length=50,null=True,blank=True)
    email = models.CharField(max_length=100,null=True,blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.patient_name

class Doctor(models.Model):

    """ This class contains details of Doctor"""

    doctor_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.doctor_name

class Appointment(models.Model):

	""" This class contains details of patient , Doctor details using ForeignKey's
          and date_appoinment,reason details"""

	doctor 			 = models.ForeignKey(Doctor, on_delete = models.CASCADE,null=True, blank=True)
	patient 		 = models.ForeignKey(Patient,on_delete=models.CASCADE,null=True, blank=True)	
	reason 			 = models.CharField(max_length=50,null=True,blank=True)
	date_appointment = models.DateField(null=True,blank=True)


    


