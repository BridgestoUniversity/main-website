from django.db import models

# Create your models here.


class Articles(models.Model):
    # title
    title = models.CharField(max_length=300, default='Title has not been set')
    # date
    date = models.DateField(default="Date has not been set")
    # topic(s)  --> go for ListCharField or JSONField?
    topics = models.CharField(
        max_length=100, default='Topics have not been set')
    # tags
    tags = models.CharField(max_length=400, default='Tags have not been set')
    # type
    articleType = models.CharField(
        max_length=50, default='Article Type has not been set')
    # summary
    summary = models.CharField(max_length=(
        60*20), default='Summary has not been set')
    # author(s)
    authors = models.CharField(
        max_length=100, default='Authors have not been set')
    # link
    link = models.CharField(max_length=200, default='Link has not been set')
    # todo: set default to an article not found page, or redirect back to articles

    def __str__(self):
        return self.title
