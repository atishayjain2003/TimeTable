from django.db import models

class Class(models.Model):
    name = models.CharField(max_length=50)  # e.g., "10th Grade A"

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=50)  # e.g., "Mathematics"

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=50)  # Teacher's name
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.subject.name})"


class Timeslot(models.Model):
    start_time = models.TimeField()  # e.g., "09:00 AM"
    end_time = models.TimeField()    # e.g., "10:00 AM"

    def __str__(self):
        return f"{self.start_time} - {self.end_time}"


class Timetable(models.Model):
    class_name = models.CharField(max_length=50)
    year=models.IntegerField(default=1)  # e.g., "10th Grade A"
    subject = models.CharField(max_length=50)     # e.g., "Mathematics"
    teacher = models.CharField(max_length=50)     # Teacher's name
    timeslot = models.CharField(max_length=50)    # e.g., "09:00 AM - 10:00 AM"
    day_of_week = models.CharField(max_length=15) # e.g., "Monday"  

    def __str__(self):
        return f"{self.class_name} | {self.subject} | {self.day_of_week}"

