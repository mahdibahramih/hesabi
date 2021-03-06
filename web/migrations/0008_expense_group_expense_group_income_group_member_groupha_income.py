# Generated by Django 3.0.2 on 2020-01-20 12:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0007_auto_20200120_1229'),
    ]

    operations = [
        migrations.CreateModel(
            name='income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('amount', models.BigIntegerField()),
                ('sour', models.CharField(max_length=20)),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='groupha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('discription', models.TextField()),
                ('status', models.CharField(max_length=10)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='group_member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('this_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.groupha')),
                ('this_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='group_income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('amount', models.BigIntegerField()),
                ('this_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.groupha')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='group_expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('amount', models.BigIntegerField()),
                ('this_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.groupha')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('amount', models.BigIntegerField()),
                ('sour', models.CharField(max_length=20)),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
