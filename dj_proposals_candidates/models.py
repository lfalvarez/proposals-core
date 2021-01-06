# -*- coding: utf-8 -*-

from django.db import models

from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField
from ndarray import NDArrayField

class NamedAndDescripted(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name')
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        abstract = True

class Territory(NamedAndDescripted, TimeStampedModel):
    pass


class Candidate(NamedAndDescripted, TimeStampedModel):
    party = models.ForeignKey('Party', related_name='candidates', null=True, blank=True, on_delete=models.CASCADE)
    coalition = models.ForeignKey('Coalition', related_name='candidates', null=True, blank=True, on_delete=models.CASCADE)
    
class Proposal(TimeStampedModel):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title')
    territory = models.ForeignKey(Territory, related_name='proposals', on_delete=models.CASCADE)
    description = models.TextField()
    representation = NDArrayField()
    
    def __str__(self):
        return self.title
    

class Commitment(TimeStampedModel):
    candidate = models.ForeignKey(Candidate, related_name='commitments', on_delete=models.CASCADE)
    proposal = models.ForeignKey(Proposal, related_name='commitments', on_delete=models.CASCADE)
    

class Party(NamedAndDescripted, TimeStampedModel):
    pass
    

class Coalition(NamedAndDescripted, TimeStampedModel):
    pass
    


