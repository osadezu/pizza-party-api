from django.urls import path
from . import views

urlpatterns = [
    path('teams/', views.TeamList.as_view(), name='team_list'),
    path('teams/<int:pk>', views.TeamDetail.as_view(), name='team_detail'),
    path('members/', views.MemberList.as_view(), name='member_list'),
    path('members/<int:pk>', views.MemberDetail.as_view(), name='member_detail'),
]
