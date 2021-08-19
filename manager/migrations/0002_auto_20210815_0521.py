# Generated by Django 3.2.6 on 2021-08-15 05:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='telephone',
            field=models.CharField(default='t', max_length=10),
        ),
        migrations.AddField(
            model_name='patient',
            name='test_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Tested Date'),
        ),
        migrations.AddField(
            model_name='patient',
            name='treatment',
            field=models.CharField(choices=[('Home', 'Home'), ('Workplace', 'Workplace'), ('Hospital', 'Hospital')], default='a', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='treatment_place',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]