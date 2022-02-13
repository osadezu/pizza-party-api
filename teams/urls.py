from django.urls import path
from . import views

urlpatterns = [
    path('teams/', views.TeamList.as_view(), name='team-list'),
    path('teams/<int:pk>', views.TeamDetail.as_view(), name='team-detail'),
    path('members/', views.MemberList.as_view(), name='member-list'),
    path('members/<int:pk>', views.MemberDetail.as_view(), name='member-detail'),
]
