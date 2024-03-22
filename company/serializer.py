from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Company, SocialMedia, HappyClientAchievement, AwardWonAchievement, ProjectAchievement, WorkCompletedImage
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class SocialMediaSerializer(ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'


class WorksCompletedSerializer(ModelSerializer):
    class Meta:
        model = WorkCompletedImage
        fields = "__all__"


class CompanySerializer(ModelSerializer):
    social_media = SocialMediaSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = "__all__"


class HappyClientAchievementSerializer(ModelSerializer):
    class Meta:
        model = HappyClientAchievement
        fields = "__all__"


class AwardWonAchievementSerializer(ModelSerializer):
    class Meta:
        model = AwardWonAchievement
        fields = "__all__"


class ProjectAchievementSerializer(ModelSerializer):
    class Meta:
        model = ProjectAchievement
        fields = "__all__"


class myTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['id'] = user.id
        token['username'] = user.username
        token['email'] = user.email
        token['is_admin'] = user.is_superuser
        token['is_active'] = user.is_active
        return token
