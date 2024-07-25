from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.db import models
from branch.models import Branch
from .userSession import *
from django import template
from django.contrib.auth.models import Group
from django.contrib.auth.hashers import make_password

class CustomUser(AbstractUser):
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE,verbose_name="Service",null=True,blank=True,db_constraint=False)
    is_staff = models.BooleanField(default=True,editable=False)
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name='customuser_groups',
        related_query_name='customuser',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='customuser_user_permissions',
        related_query_name='customuser',
    )

    def __str__(self):
        if self.branch!=None:
            return self.username+"-"+str(self.branch)
        else:
            
            return str(self.first_name)+" "+str(self.last_name)
    
 


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
         
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
class UserBatch(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class AppUsers(models.Model):
    id=models.BigAutoField(primary_key=True)
    fname=models.CharField(max_length=100,verbose_name="First Name",null=True,blank=True)
    lname=models.CharField(max_length=100,verbose_name="Last Name",null=True,blank=True)
    email=models.EmailField(max_length=100,verbose_name="Email Address",unique=True,null=True,blank=True)
    username=models.CharField(max_length=100,verbose_name="Username",unique=True,null=True,blank=True)
    password=models.CharField(max_length=100,verbose_name="Password",default="mainpass")
    branch_of=models.ForeignKey(Branch,on_delete=models.PROTECT,verbose_name="Branch",default=get_current_user_branch,editable=False)
    group_assigned=models.ForeignKey(Group, on_delete=models.CASCADE,verbose_name="User Group")

    def __str__(self):
        return str(self.fname) +" "+str(self.lname)

    class Meta:
        verbose_name="Application Users"
        verbose_name_plural="Application Users"
    def save(self, *args, **kwargs):
         
        if not self.id:
                num_users = AppUsers.objects.filter(branch_of=self.branch_of).count()
                if num_users < 5:
                    appusers=CustomUser.objects.create(
                            first_name=self.fname,
                            last_name=self.lname,
                            email=self.email,
                            username=self.username,
                            password=make_password(self.password),
                            branch=self.branch_of,
                            is_active=True,
                            is_staff=True,                            
                            ) 
                    
                    appusers.save( )
                    appusers.groups.set(Group.objects.filter(name=self.group_assigned))  
                    super().save(*args, **kwargs)
        else:
                super().save(*args, **kwargs)
    