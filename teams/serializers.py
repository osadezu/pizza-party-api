from rest_framework import serializers
from .models import Team, Member


class TeamSerializer(serializers.Serializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'blurb', 'hero_image', 'admin',
                  'custom_prompt', 'collab_prompt', 'required_fields', 'link', 'members', ]


class MemberSerializer(serializers.Serializer):
    class Meta:
        model = Member
        fields = ['id', 'user', 'team', 'first_name', 'last_name', 'goes_by', 'pronouns', 'avatar', 'link', 'location',
                  'loc_lat', 'loc_long', 'interests', 'pets', 'custom_answer', 'collab_answer', 'reactions_count', ]
