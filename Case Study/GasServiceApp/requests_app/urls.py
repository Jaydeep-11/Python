from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_request, name='submit_request'),
    path('view/', views.view_requests, name='view_requests'),
    path('manage/', views.manage_requests, name='manage_requests'),
    path('resolve/<int:request_id>/', views.resolve_request, name='resolve_request'),

]
