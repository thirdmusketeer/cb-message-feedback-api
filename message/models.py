from django.db import models


class Message(models.Model):
    keywords = models.CharField(max_length=120, blank=False)
    message = models.CharField(max_length=255, blank=False)
    rating = models.BooleanField()

    def __str__(self):
        return "{0} - {1} - {2}".format(self.keywords, self.message, self.rating)
