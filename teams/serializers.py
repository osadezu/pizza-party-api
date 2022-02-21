from rest_framework import serializers
from .models import Team, Member


class TeamSerializer(serializers.ModelSerializer):
    # admin = serializers.ReadOnlyField(source='admin.email')

    class Meta:
        model = Team
        fields = ['id', 'name', 'blurb', 'hero_image', 'admin',
                  'custom_prompt', 'collab_prompt', 'required_fields', 'link', 'members', ]
        read_only_fields = ['members']


class TeamDetailSerializer(serializers.ModelSerializer):
    admin = serializers.ReadOnlyField(source='admin.id')

    class Meta:
        model = Team
        fields = ['id', 'name', 'blurb', 'hero_image', 'admin',
                  'custom_prompt', 'collab_prompt', 'required_fields', 'link', 'members', ]
        read_only_fields = ['members']
        depth = 1


class MemberSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Member
        fields = ['id', 'user', 'team', 'first_name', 'last_name', 'goes_by', 'pronouns', 'avatar', 'link', 'location',
                  'loc_lat', 'loc_long', 'interests', 'pets', 'custom_answer', 'collab_answer', 'reactions_count', ]
