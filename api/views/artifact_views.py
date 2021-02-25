from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.artifacts import Artifact
from ..serializers import ArtifactSerializer, ArtifactReadSerializer, UserSerializer

class AllArtifacts(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request):
        """Index request"""
        artifacts = Artifact.objects
        data = ArtifactReadSerializer(artifacts, many=True).data
        return Response({ 'artifacts': data })

class Artifacts(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = ArtifactSerializer
    def get(self, request):
        """Index request"""
        artifacts = Artifact.objects.filter(owner=request.user.id)
        data = ArtifactReadSerializer(artifacts, many=True).data
        return Response({ 'artifacts': data })

    def post(self, request):
        """Create request"""
        request.data['artifact']['owner'] = request.user.id
        artifact = ArtifactSerializer(data=request.data['artifact'])
        if artifact.is_valid():
            artifact.save()
            return Response({ 'artifact': artifact.data }, status=status.HTTP_201_CREATED)
        return Response(artifact.errors, status=status.HTTP_400_BAD_REQUEST)

class ArtifactDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        artifact = get_object_or_404(Artifact, pk=pk)
        data = ArtifactReadSerializer(artifact).data
        return Response({ 'artifact': data })

    def delete(self, request, pk):
        """Delete request"""
        artifact = get_object_or_404(Artifact, pk=pk)
        if not request.user.id == artifact.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this artifact')
        artifact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        if request.data['artifact'].get('owner', False):
            del request.data['artifact']['owner']

        artifact = get_object_or_404(Artifact, pk=pk)
        if not request.user.id == artifact.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this artifact')

        request.data['artifact']['owner'] = request.user.id
        data = ArtifactSerializer(artifact, data=request.data['artifact'])
        if data.is_valid():
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
