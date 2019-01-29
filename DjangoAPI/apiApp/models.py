from django.db import models

# Create your models here.


class Test(models.Model):
    name = models.CharField(u'姓名', max_length=100, default='no_name')
    sex = models.CharField(u'性别', max_length=10, default='male')
    age = models.CharField(u'年龄', max_length=3, default='0')

    def __unicode__(self):
        return '%d: %s' % (self.pk, self.name)