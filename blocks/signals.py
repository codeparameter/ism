from django.db.models.signals import pre_delete, post_delete
from .models import BlockPic, BlockVid
from django.dispatch import receiver
from home.settings import delete_media

@receiver(post_delete, sender=BlockPic)
def post_delete_block_pic(sender, **kwargs):
    delete_media(str(kwargs['instance'].pic))

@receiver(post_delete, sender=BlockVid)
def post_delete_block_vid(sender, **kwargs):
    delete_media(str(kwargs['instance'].vid))
