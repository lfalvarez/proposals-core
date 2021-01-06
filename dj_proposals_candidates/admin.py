# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import (
   Candidate,
   Proposal,
   Commitment,
   Party,
   Coalition,
)


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    pass


@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    pass


@admin.register(Commitment)
class CommitmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Party)
class PartyAdmin(admin.ModelAdmin):
    pass


@admin.register(Coalition)
class CoalitionAdmin(admin.ModelAdmin):
    pass



