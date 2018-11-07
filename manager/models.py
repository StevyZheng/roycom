from django.db import models


# Create your models here.
class Role(models.Model):
	role_name = models.CharField(max_length=24, unique=True)
	

class User(models.Model):
	user_name = models.CharField(max_length=24, unique=True, verbose_name="用户名")
	password = models.CharField(max_length=36, verbose_name="密码")
	sex = models.CharField(max_length=1, null=True, verbose_name="性别")
	role = models.ForeignKey(Role, on_delete=models.CASCADE, verbose_name="角色")


class RoleToPrivilege(models.Model):
	role = models.ForeignKey(Role, on_delete=models.CASCADE, verbose_name="角色")
	privilege = models.CharField(max_length=512, verbose_name="权限")

