from django.db.models.signals import pre_save, post_delete
from .models import BlockPic, BlockVid
from django.dispatch import receiver
from home.settings import delete_media

@receiver(pre_save, sender=BlockPic)
def pre_save_block_pic(sender, **kwargs):
    try:
        instance = kwargs['instance']
        pic = str(BlockPic.objects.get(pk=instance.pk).pic)
        if str(instance.pic) != pic:
            delete_media(pic)
    except BlockPic.DoesNotExist:
        pass

@receiver(post_delete, sender=BlockPic)
def post_delete_block_pic(sender, **kwargs):
    delete_media(str(kwargs['instance'].pic))

@receiver(pre_save, sender=BlockVid)
def pre_save_block_vid(sender, **kwargs):
    try:
        instance = kwargs['instance']
        vid = str(BlockVid.objects.get(pk=instance.pk).vid)
        if str(instance.vid) != vid:
            delete_media(vid)
    except BlockVid.DoesNotExist:
        pass

@receiver(post_delete, sender=BlockVid)
def post_delete_block_vid(sender, **kwargs):
    delete_media(str(kwargs['instance'].vid))
