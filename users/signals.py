from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from awards.models import Profile

#send signal to create_profile receiver when a user is registered

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    '''
    function to automatically create a profile for each newly registered user
    '''

    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    '''
    function to save a user profile for each new user
    '''
    instance.profile.save()