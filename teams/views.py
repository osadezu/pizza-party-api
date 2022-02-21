from rest_framework import generics
from .serializers import TeamSerializer, TeamDetailSerializer, MemberSerializer
from .models import Team, Member

# Custom permissions
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly


class TeamList(generics.ListCreateAPIView):
    def perform_create(self, serializer):
        serializer.save(admin=self.request.user)
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated]


class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]


class MemberList(generics.ListCreateAPIView):
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [permissions.IsAuthenticated]


class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsOwnerOrReadOnly]
