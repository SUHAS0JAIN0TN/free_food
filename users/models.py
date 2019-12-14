from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManager
# Create your models here.

class User(AbstractBaseUser):
	email = models.EmailField(
		verbose_name='Email Field',
		max_length=255,
		unique=True
		)
	name=models.CharField(max_length=30)
	active = models.BooleanField(default=True)
	staff = models.BooleanField(default=False)
	admin = models.BooleanField(default=False)
	USERNAME_FIELD='email'
	REQUIRED_FIELDS=['name']

	def __str__(self):
		return self.email

	@property
	def is_admin(self):
		return self.admin
	
	@property
	def is_active(self):
		return self.active

	@property
	def is_staff(self):
		return self.staff
	

	objects=UserManager()


class Food(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	food_item_decription = models.CharField(max_length=50)
	latitude = models.DecimalField(max_digits=18,decimal_places=15)
	longitude = models.DecimalField(max_digits=18,decimal_places=15)
	phone_number = models.IntegerField()