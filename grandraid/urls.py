from django.urls import include, path
from rest_framework import routers

from grandraid import views

router = routers.DefaultRouter()
router.register(r'clubs', views.ClubViewSet)
router.register(r'courses', views.CourseViewSet)
router.register(r'sizes', views.SizeViewSet)
router.register(r'runnercategories', views.RunnerCategoryViewSet)
router.register(r'meals', views.MealViewSet)
router.register(r'runners', views.RunnerViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]