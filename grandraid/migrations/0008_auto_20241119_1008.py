# Generated by Django 5.1.3 on 2024-11-19 10:08

from django.db import migrations

courses = [
    {"name": "Cap Caroux", "price": 27, "has_discount": True},
    {"name": "Grand Raid 6666", "price": 120, "has_discount": True},
    {"name": "Saute Mouflon", "price": 50, "has_discount": True},
    {"name": "Trail de la Factrice", "price": 20, "has_discount": True},
    {"name": "Roquebrune", "price": 12, "has_discount": True},
    {"name": "Randonnée", "price": 5, "has_discount": False},
]

def populate_courses(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Course = apps.get_model("grandraid", "Course")

    for course in courses:
        new_course = Course(**course)
        new_course.save()
    
def depopulate_courses(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Course = apps.get_model("grandraid", "Course")

    for course in Course.objects.all():
        course.delete()

class Migration(migrations.Migration):

    dependencies = [
        ('grandraid', '0007_auto_20241119_1001'),
    ]

    operations = [
        migrations.RunPython(populate_courses, depopulate_courses)
    ]
