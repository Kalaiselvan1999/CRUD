# Generated by Django 4.2 on 2023-04-19 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='employee',
            name='department_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operations.department'),
        ),
        migrations.DeleteModel(
            name='Deparment',
        ),
    ]
