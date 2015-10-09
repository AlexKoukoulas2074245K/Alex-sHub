from django.db import models
from django.template.defaultfilters import slugify

'''class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)'''

class Project(models.Model):
    name = models.CharField(max_length=32, unique=True)
    img_small_name = models.CharField(max_length=32, default="")
    img_large_name = models.CharField(max_length=32, default="")
    subheading = models.CharField(max_length=32)
    description = models.CharField(max_length=1024)
    details = models.CharField(max_length=1024)
    download_link = models.URLField(null=True)
    github_link = models.URLField(null=True)
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)
        
    def __unicode__(self):
        return self.name
