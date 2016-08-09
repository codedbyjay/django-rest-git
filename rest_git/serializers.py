from rest_framework import serializers
from rest_framework.pagination import LimitOffsetPagination

from rest_git.models import Repository

class RepositorySerializer(serializers.ModelSerializer):

    paginator_class = LimitOffsetPagination

    class Meta:
        model = Repository
        fields = ['name']

class CommitSerializer(serializers.BaseSerializer):

    sha = serializers.CharField(max_length=255)

    def to_representation(self, obj):
        print("Asked to represent: %s" % obj)
        return {
            "sha" : unicode(obj),
            "authored_date" : obj.authored_date,
            "committed_date" : obj.committed_date,
            "committer" : {
                "name" : obj.committer.name,
                "email" : obj.committer.email,
            },
            "message" : obj.message,
        }

