from django.db import models
from django.core.exceptions import ValidationError

from django_extensions.db.models import TimeStampedModel

from git import Repo

class Repository(TimeStampedModel):

    class Meta:
        verbose_name_plural = "Repositories"

    name = models.CharField("Name", max_length=255)
    location = models.CharField("Repository Location", max_length=255)

    def __unicode__(self):
        return self.name

    @property
    def repo(self):
        return Repo(self.location)

    def clean_location(self):
        if not os.path.exists(self.location):
            raise ValidationError("The path %s does not exist" % self.location)
        git_dir = os.path.join(self.location, ".git")
        if not os.path.exists(git_dir):
            raise ValidationError("The path %s does not have a .git " \
                "directory" % self.location)

