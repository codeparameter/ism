from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime


def pic_path(instance, filename):
    return f'{Pic.media_path()}{str(datetime.now())}{filename}'


class Pic(models.Model):
    dependencies = models.JSONField(default=list, blank=True)
    pic = models.ImageField(_('Image'), upload_to=pic_path)

    @staticmethod
    def media_path():
        return 'img/'


def vid_path(instance, filename):
    return f'{Vid.media_path()}{str(datetime.now())}{filename}'

class Vid(models.Model):
    dependencies = models.JSONField(default=list, blank=True)
    vid = models.FileField(upload_to=vid_path)

    @staticmethod
    def media_path():
        return 'vid/'

