from rest_framework import serializers
from .models import Class, Subject, Teacher, Timeslot, Timetable

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class TimeslotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeslot
        fields = '__all__'


class TimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timetable
        fields = '__all__'
