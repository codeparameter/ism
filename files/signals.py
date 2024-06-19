from django.db.models.signals import pre_save, post_delete
from .models import Pic, Vid
from django.dispatch import receiver
from home.settings import delete_media

@receiver(pre_save, sender=Pic)
def pre_save_pic(sender, **kwargs):
    try:
        instance = kwargs['instance']
        pic = str(Pic.objects.get(pk=instance.pk).pic)
        if str(instance.pic) != pic:
            delete_media(pic)
    except Pic.DoesNotExist:
        pass

@receiver(post_delete, sender=Pic)
def post_delete_pic(sender, **kwargs):
    instance = kwargs['instance']
    print(instance.dependencies)
    delete_media(str(instance.pic))

@receiver(pre_save, sender=Vid)
def pre_save_vid(sender, **kwargs):
    try:
        instance = kwargs['instance']
        vid = str(Vid.objects.get(pk=instance.pk).vid)
        if str(instance.vid) != vid:
            delete_media(vid)
    except Vid.DoesNotExist:
        pass

@receiver(post_delete, sender=Vid)
def post_delete_vid(sender, **kwargs):
    instance = kwargs['instance']
    print(instance.dependencies)
    delete_media(str(instance.pic))
