from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class Profile(models.Model):
    '''
    Profile model acts as blueprint for all profile instances
    '''
    bio = models.CharField(max_length =150, default='User has no bio yet')
    profile_photo = CloudinaryField('image', default='default')
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    linkedIn_url = models.CharField(max_length = 150, null=True, blank=True)
    twitter_url = models.CharField(max_length = 150, null=True, blank=True)
    website_url = models.CharField(max_length = 150, null=True, blank=True)
    
    def __str__(self):
        return str(self.user)


# Create your models here.
class Project(models.Model):
    '''
    Project model acts as blueprint for all project instances
    '''
    title = models.CharField(max_length =60)
    description = models.TextField()
    image = CloudinaryField('image', default='default')
    link = models.CharField(max_length =120)
    date_posted = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    @classmethod
    def search_project(cls,search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects
    
    class Meta:
        ordering = ['-date_posted']



RATE_CHOICES = [
  (1, '1'),
  (2, '2'),
  (3, '3'),
  (4, '4'),
  (5, '5'),
  (6, '6'),
  (7, '7'),
  (8, '8'),
  (9, '9'),
  (10, '10'),
]

class Rate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    design = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
    content = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
    usability = models.PositiveSmallIntegerField(choices=RATE_CHOICES)

    def __str__(self):
        return str(self.user)

    @classmethod
    def find_sum(cls,title):
        rates = cls.objects.filter(project__title=title)
        design_list = []
        content_list = []
        usability_list = []
    
        for rate in rates:
            design_list.append(rate.design)
            content_list.append(rate.content)
            usability_list.append(rate.usability)
            

        design_sum = sum(design_list)
        content_sum = sum(content_list)
        usability_sum = sum(usability_list)
        users = len(design_list)

        design = design_sum/users
        content = content_sum/users
        usability = usability_sum/users

        design = int(round(design))
        content = int(round(content))
        usability = int(round(usability))

        average_score = (design + content + usability)/3

        average_score = int(round(average_score))

        print(design, content, usability, average_score)
        return design, content, usability, average_score
