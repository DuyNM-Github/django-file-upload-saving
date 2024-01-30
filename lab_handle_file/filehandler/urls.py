from django.urls import path
from filehandler.views import handle_files

urlpatterns = [
    path('file/', handle_files)
]
