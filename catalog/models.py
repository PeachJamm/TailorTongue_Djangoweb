from django.db import models
from django.urls import reverse
# Create your models here.


class WordInfo(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    wordid=models.CharField(max_length=20, help_text='ID of the word ')
    word = models.CharField(max_length=40, help_text='word itself')
    definition=models.CharField(max_length=100, help_text='Meanings of the word')
    # …

    # Metadata
    class Meta:
        ordering = ['wordid']

    # Methods
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.id = None

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('my_field_name', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.word
