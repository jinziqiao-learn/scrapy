from django.db import models

# Create your models here.


class HotSpot(models.Model):

    content = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publishTime = models.CharField(max_length=255)
    repost = models.IntegerField()
    comment = models.IntegerField()
    approve = models.IntegerField()
    address = models.URLField()

    # 排序
    class Meta:
        ordering = ['-id']


