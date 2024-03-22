from django.http import HttpResponse
import json
from rest_framework_simplejwt.views import TokenObtainPairView
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from django.shortcuts import get_object_or_404
from .serializer import *
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class CompanyRetrieval(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_id = self.kwargs.get('pk')
        try:
            user = User.objects.get(id=user_id)

            companies = Company.objects.filter(user=user)
            if not companies:
                return Response({"error": "No companies found for this user."}, status=status.HTTP_404_NOT_FOUND)

            serializer = CompanySerializer(companies, many=True)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({"message": "User not Found"}, status=status.HTTP_404_NOT_FOUND)


class RetrieveAchievements(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        company_id = kwargs.get("pk")
        company = get_object_or_404(Company, id=company_id)

        happy_clients = HappyClientAchievement.objects.filter(company=company)
        awards_won = AwardWonAchievement.objects.filter(company=company)
        projects_completed = ProjectAchievement.objects.filter(company=company)

        happy_clients_data = HappyClientAchievementSerializer(
            happy_clients, many=True).data
        awards_won_data = AwardWonAchievementSerializer(
            awards_won, many=True).data
        projects_completed_data = ProjectAchievementSerializer(
            projects_completed, many=True).data

        data = {
            'happy_clients': happy_clients_data,
            'awards_won': awards_won_data,
            'projects_completed': projects_completed_data
        }

        return Response(data=data, status=status.HTTP_200_OK)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = myTokenObtainPairSerializer
