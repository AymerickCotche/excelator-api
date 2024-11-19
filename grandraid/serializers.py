from django.contrib.auth.models import Group, User
from rest_framework import serializers

from grandraid.models import Club, Course, Size, RunnerCategory, Meal, Runner


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = "__all__"

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = "__all__"

class RunnerCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RunnerCategory
        fields = "__all__"
        
class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = "__all__"
        
class RunnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Runner
        fields = "__all__"
        