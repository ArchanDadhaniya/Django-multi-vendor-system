
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver    
from .models import User, UserProfile






@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        print("User profile is created")
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except UserProfile.DoesNotExist:
            profile = UserProfile.objects.create(user=instance)
            print("User profile does not exist, creating a new one")
        print("User profile is updated")

# post_save.connect(post_save_create_profile_receiver, sender=User) This is the one way but i use the python decorator. 


@receiver(pre_save, sender=User)
def pre_save_create_profile_receiver(sender, instance, **kwargs):
    if not instance.pk:
        print("Creating a new user profile")