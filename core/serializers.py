from rest_framework import serializers
from .models import Employee, Attendance
from datetime import date


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = "__all__"

    def validate(self, data):
        if data["date"].weekday() >= 5:
            raise serializers.ValidationError("Cannot mark attendance on weekends.")
        return data
