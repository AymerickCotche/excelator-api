# Generated by Django 5.1.3 on 2024-11-19 10:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grandraid', '0005_repas_runnercategory_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField()),
                ('prix', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Runner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.TextField(max_length=20)),
                ('lastname', models.TextField(max_length=20)),
                ('sexe', models.CharField(choices=[('H', 'Homme'), ('F', 'Femme')], default='F', max_length=1)),
                ('birth_date', models.DateField()),
                ('category', models.TextField()),
                ('meal_before', models.BooleanField(default=False)),
                ('meal_after', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Repas',
        ),
        migrations.AlterField(
            model_name='club',
            name='city',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='club',
            name='name',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='runnercategory',
            name='category',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='size',
            name='name',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='size',
            name='symbol',
            field=models.CharField(),
        ),
        migrations.AddField(
            model_name='runner',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grandraid.course'),
        ),
        migrations.AddField(
            model_name='runner',
            name='shirt_size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grandraid.size'),
        ),
    ]
