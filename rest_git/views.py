from django.shortcuts import render, get_object_or_404

from rest_framework import generics

from rest_git.serializers import RepositorySerializer, CommitSerializer
from rest_git.models import *

class RepositoryList(generics.ListCreateAPIView):
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer
    paginate_by = 10


class RepositoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer

class CommitList(generics.ListAPIView):

    serializer_class = CommitSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        repository = get_object_or_404(Repository, pk=pk)
        repo = repository.repo
        print("Returning commits for %s" % repository)
        return repo.iter_commits()
