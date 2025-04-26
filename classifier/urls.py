from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from classify.api import router as robot_router

api = NinjaAPI()
api.add_router("/classifier/", robot_router)  # Attach your app’s router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),  # Mount the API
]