from django.urls import path
from . import views

# ----------------------------------------------------------------
# Define users routes
# ----------------------------------------------------------------

urlpatterns = [
    
    # ------------------------------------------------
    # Auth
    # ------------------------------------------------
    path('signup', views.signup ),
    path('profile', views.profile ),

]
