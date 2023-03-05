from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length=255)
    
    
class TaggedItem(models.Model):
    #what tag is applied to what object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    #type(product, video, article, etc)
    #ID of that object
    #generic field instead of product ->
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE) #for identifying the type of object
    object_id = models.PositiveIntegerField() #for identifying/refferencing the ID of the object
    content_object = GenericForeignKey() #for reading/referencing the actual object