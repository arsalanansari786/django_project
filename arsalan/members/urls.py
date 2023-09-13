from django.urls import path ,include
from arsalan.members.views import ReactView
from members import views

urlpatterns = [
    # path('', views.user_form, name='user_form'),
      # path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
      path('wel/',ReactView.as_view(),name="something"),
]
