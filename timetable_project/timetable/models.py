from django.db import models

class Timetable(models.Model):
    class_name = models.CharField(max_length=50)
    year=models.IntegerField(default=1)  # e.g., "10th Grade A"
    subject = models.CharField(max_length=50)     # e.g., "Mathematics"
    teacher = models.CharField(max_length=50)     # Teacher's name
    timeslot = models.CharField(max_length=50)    # e.g., "09:00 AM - 10:00 AM"
    day_of_week = models.CharField(max_length=15) # e.g., "Monday"  

    def __str__(self):
        return f"{self.class_name} | {self.subject} | {self.day_of_week}"

