# Generated by Django 4.2.9 on 2024-04-01 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0006_alter_solution_solution_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='solution_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/solutions_images/'),
        ),
    ]
