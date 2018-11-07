# Generated by Django 2.1.1 on 2018-11-06 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=24, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='RoleToPrivilege',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('privilege', models.CharField(max_length=512, verbose_name='权限')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Role', verbose_name='角色')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=24, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=36, verbose_name='密码')),
                ('sex', models.CharField(max_length=1, null=True, verbose_name='性别')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Role', verbose_name='角色')),
            ],
        ),
    ]
