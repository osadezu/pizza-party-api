from rest_framework import generics
from .serializers import TeamSerializer, MemberSerializer
from .models import Team, Member


class TeamList(generics.ListCreateAPIView):
    def perform_create(self, serializer):
        serializer.save(admin=self.request.user)
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class MemberList(generics.ListCreateAPIView):
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
