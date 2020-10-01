from django.db import models


# Create your models here.

class Event(models.Model):
    # title
    title = models.CharField(max_length=300, default="Title has not been set")
    # date
    date = models.DateField(default="Date has not been set")
    # countdown description
    countdownDescription = models.CharField(
        max_length=200, default="Countdown Description has not been set")
    # summary
    summary = models.CharField(max_length=(
        60*20), default='Summary has not been set')
    # imageLink
    imageLink = models.CharField(
        max_length=200, default="Image link has not been set")
    # linkType (ie. coming soon, view more, etc.)
    linkType = models.CharField(max_length=50, default='Coming soon!')
    # link
    link = models.CharField(max_length=500, default="Link has not been set")


def __str__(self):
    return self.title
