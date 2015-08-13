from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.utils import timezone
import datetime

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30, blank=True, null=True)
    with_us = models.DateField()

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


def dir_name(self, filename):
    url = "%s/%s" % (self.author.last_name, filename)
    return url

class Image(models.Model):
    title = models.CharField(max_length=30)
    creation_date = models.DateField()
    country = models.CharField(max_length=30)
    style = models.CharField(max_length=30)
    main_colour = models.CharField(max_length=30)
    author = models.ForeignKey(Author)

    pub_date = models.DateTimeField('date published')

    original_img = models.ImageField(upload_to=dir_name)
    admin_block_img = ImageSpecField(source='original_img',
                               processors=[ResizeToFill(150, 100)],
                               format='JPEG',
                               options={'quality': 60})

    block_img = ImageSpecField(source='original_img',
                               processors=[ResizeToFill(width=300)],
                               format='JPEG',
                               options={'quality': 90})

    preview_img = ImageSpecField(source='original_img',
                                 processors=[ResizeToFill(width=500)],
                                 format='JPEG',
                                 options={'quality':95})

    def image_tag(self):
        return u'<img src="%s" />' % self.original_img
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def __unicode__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published?'