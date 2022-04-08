from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Project(models.Model):
    '''
    Project model acts as blueprint for all project instances
    '''
    title = models.CharField(max_length =60)
    description = models.TextField()
    image = CloudinaryField('image', default='default')
    #owner = models.ForeignKey(User,on_delete=models.CASCADE)
    link = models.CharField(max_length =120)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @classmethod
    def search_project(cls,search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects


class Profile(models.Model):
    '''
    Profile model acts as blueprint for all profile instances
    '''
    bio = models.CharField(max_length =150)
    profile_photo = CloudinaryField('image', default='default')
    name = models.CharField(max_length=30)
    # email = models.EmailField()
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        #return f'{self.user.username} Profile'
        return self.name