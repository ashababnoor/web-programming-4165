from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Type(models.Model):
    type_name = models.CharField(max_length=256)

class Status(models.Model):
    status_name = models.CharField(max_length=256)
    status_notes = models.TextField()

class Categories(models.Model):
    category_name = models.CharField(max_length=256)
    category_description = models.TextField()
    category_type = models.CharField(max_length=256)

class Contacts(models.Model):
    contact_name = models.CharField(max_length=256)
    type_id = models.ForeignKey(Type, on_delete=models.CASCADE)

class Projects(models.Model):
    project_name = models.CharField(max_length=256)
    project_description = models.TextField()
    project_start_date = models.DateField(default=timezone.now)
    project_end_date = models.DateField(default=timezone.now)
    project_owner_id = models.AutoField()
    contact_id = models.ForeignKey(Contacts, on_delete=models.CASCADE)

class Project_HR(models.Model):
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    project_testimonial = models.TextField()

class Contact_Cat(models.Model):
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    contact_id = models.ForeignKey(Contacts, on_delete=models.CASCADE)
    project_hr_id = models.ForeignKey(Project_HR, on_delete=models.CASCADE)

class Hire_Rates(models.Model):
    hire_rate_rate = models.FloatField()
    hire_rate_period = models.TimeField()

class Equipment(models.Model):
    equipment_name = models.CharField(max_length=256)
    equipment_description = models.TextField()
    equipment_status_id = models.AutoField()
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE)

class Equip_Hire_Rates(models.Model):
    equipment_id = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    hire_rate_id = models.ForeignKey(Hire_Rates, on_delete=models.CASCADE)

class Project_Equipment(models.Model):
    equipment_id = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    proj_equip_booking_rate = models.FloatField()

class Equip_Cat(models.Model):
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    equipment_id = models.ForeignKey(Equipment, on_delete=models.CASCADE)

class Calender(models.Model):
    calender_date = models.DateField()
    project_hr_id = models.ForeignKey(Project_HR, on_delete=models.CASCADE)
    project_equip_id = models.ForeignKey(Project_Equipment, on_delete=models.CASCADE)
    invoice_id = models.AutoField()
    calender_date_confirmed = models.BooleanField()