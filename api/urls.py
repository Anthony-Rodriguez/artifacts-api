from django.urls import path
from .views.artifact_views import AllArtifacts, Artifacts, ArtifactDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
  	# Restful routing
    path('home/', AllArtifacts.as_view(), name='artifacts'),
    path('artifacts/', Artifacts.as_view(), name='artifacts'),
    path('artifacts/<int:pk>/', ArtifactDetail.as_view(), name='artifacts'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-password/', ChangePassword.as_view(), name='change-pw')
]
