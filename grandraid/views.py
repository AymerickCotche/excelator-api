from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from grandraid.serializers import GroupSerializer, UserSerializer, ClubSerializer, CourseSerializer, SizeSerializer, RunnerCategorySerializer, MealSerializer, RunnerSerializer

from grandraid.models import Club, Course, Size, RunnerCategory, Meal, Runner


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class ClubViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows clubs to be viewed or edited.
    """
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed or edited.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class SizeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows sizes to be viewed or edited.
    """
    queryset = Size.objects.all()
    serializer_class = SizeSerializer

class RunnerCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows runner categories to be viewed or edited.
    """
    queryset = RunnerCategory.objects.all()
    serializer_class = RunnerCategorySerializer

class MealViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows runner categories to be viewed or edited.
    """
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

class RunnerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows runners to be viewed or edited.
    """
    queryset = Runner.objects.all()
    serializer_class = RunnerSerializer