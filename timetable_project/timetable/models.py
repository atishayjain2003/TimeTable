from django.db import models
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)  # Email is unique so we can send reminders individually
    year = models.IntegerField()  # The year the student is in (e.g., 4th year)
    class_name = models.CharField(max_length=50)  # Class or batch the student belongs to

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.class_name})"


class Timetable(models.Model):
    class_name = models.CharField(max_length=50)
    year=models.IntegerField(default=1)  # e.g., "10th Grade A"
    subject = models.CharField(max_length=50)     # e.g., "Mathematics"
    teacher = models.CharField(max_length=50)     # Teacher's name
    timeslot = models.CharField(max_length=50)    # e.g., "09:00 AM - 10:00 AM"
    day_of_week = models.CharField(max_length=15) # e.g., "Monday"  
    students = models.ManyToManyField(Student, related_name="timetables")

    def __str__(self):
        return f"{self.class_name} | {self.subject} | {self.day_of_week}"

