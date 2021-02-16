# -*- coding: utf-8 -*-

from django.db import models

from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField
from ndarray import NDArrayField
import numpy as np

class NamedAndDescripted(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name')
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        abstract = True

class Territory(NamedAndDescripted, TimeStampedModel):
    remote_id = models.IntegerField()


class Candidate(NamedAndDescripted, TimeStampedModel):
    profile_path = models.CharField(max_length=255)
    party = models.ForeignKey('Party', related_name='candidates', null=True, blank=True, on_delete=models.CASCADE)
    coalition = models.ForeignKey('Coalition', related_name='candidates', null=True, blank=True, on_delete=models.CASCADE)
    img_url = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)
    territory = models.ForeignKey(Territory, related_name='candidates', null=True, blank=True, on_delete=models.CASCADE)
    email = models.EmailField()
    
class Proposal(TimeStampedModel):
    remote_id = models.IntegerField()
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title')
    territory = models.ForeignKey(Territory, related_name='proposals', on_delete=models.CASCADE)
    description = models.TextField()
    representation = models.BinaryField(default=None, null=True, blank=True)
    votes = models.IntegerField()
    remote_url = models.URLField(blank=True)
    
    def __str__(self):
        return self.title
    

class Commitment(TimeStampedModel):
    candidate = models.ForeignKey(Candidate, related_name='commitments', on_delete=models.CASCADE)
    proposal = models.ForeignKey(Proposal, related_name='commitments', on_delete=models.CASCADE)

    def __str__(self):
        return '{candidate} con {proposal} en {territory}'.format(candidate=self.candidate.name,
                                                                  proposal=self.proposal.title,
                                                                  territory=self.candidate.territory.name)
    

class Party(NamedAndDescripted, TimeStampedModel):
    pass
    

class Coalition(NamedAndDescripted, TimeStampedModel):
    pass
    


