# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	Candidate,
	Proposal,
	Commitment,
	Party,
	Coalition,
)


class CandidateCreateView(CreateView):

    model = Candidate


class CandidateDeleteView(DeleteView):

    model = Candidate


class CandidateDetailView(DetailView):

    model = Candidate


class CandidateUpdateView(UpdateView):

    model = Candidate


class CandidateListView(ListView):

    model = Candidate


class ProposalCreateView(CreateView):

    model = Proposal


class ProposalDeleteView(DeleteView):

    model = Proposal


class ProposalDetailView(DetailView):

    model = Proposal


class ProposalUpdateView(UpdateView):

    model = Proposal


class ProposalListView(ListView):

    model = Proposal


class CommitmentCreateView(CreateView):

    model = Commitment


class CommitmentDeleteView(DeleteView):

    model = Commitment


class CommitmentDetailView(DetailView):

    model = Commitment


class CommitmentUpdateView(UpdateView):

    model = Commitment


class CommitmentListView(ListView):

    model = Commitment


class PartyCreateView(CreateView):

    model = Party


class PartyDeleteView(DeleteView):

    model = Party


class PartyDetailView(DetailView):

    model = Party


class PartyUpdateView(UpdateView):

    model = Party


class PartyListView(ListView):

    model = Party


class CoalitionCreateView(CreateView):

    model = Coalition


class CoalitionDeleteView(DeleteView):

    model = Coalition


class CoalitionDetailView(DetailView):

    model = Coalition


class CoalitionUpdateView(UpdateView):

    model = Coalition


class CoalitionListView(ListView):

    model = Coalition

