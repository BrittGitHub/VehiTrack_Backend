from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.maintenance import Maintenance
from ..serializers import MaintenanceSerializer

# Create your views here.


class Maintenances(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = MaintenanceSerializer

    def get(self, request, pk):
        """Index request"""
        # Get all the maintenances:
        # maintenances = Maintenance.objects.all()
        # Filter the maintenances by owner, so you can only see your owned maintenances
        # request.data['maintenance']['vehicle'] = pk
        maintenances = Maintenance.objects.all()#.filter(owner=request.user.id)
        # Run the data through the serializer
        data = MaintenanceSerializer(maintenances, many=True).data
        return Response({'maintenances': data})

    def post(self, request, pk):
        """Post request"""
        print(request.data)
        request.data['maintenance']['vehicle'] = pk
        maintenance = MaintenanceSerializer(data=request.data['maintenance'])
        if maintenance.is_valid():
            b = maintenance.save()
            return Response(maintenance.data, status=status.HTTP_201_CREATED)
        else:
            return Response(maintenance.errors, status=status.HTTP_400_BAD_REQUEST)


class MaintenanceDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk, sk):
        """Show request"""
        # Locate the maintenance to show
        maintenance = get_object_or_404(Maintenance, vehicle_id=pk, id=sk)
        # Only want to show owned maintenances?
        # if request.user != maintenance.owner:
        #     raise PermissionDenied('Unauthorized, you do not own this maintenance')
        data = MaintenanceSerializer(maintenance).data
        return Response({'maintenance': data})

        # Run the data through the serializer so it's formatted
        # data = MaintenanceSerializer(maintenance).data
        # return Response({'maintenance': data})

    def delete(self, request, pk, sk):
        """Delete request"""
        # Locate maintenance to delete
        maintenance = get_object_or_404(Maintenance, vehicle_id=pk, id=sk)
        # Check the maintenance's owner against the user making this request
        # if request.user != maintenance.owner:
        #     raise PermissionDenied('Unauthorized, you do not own this maintenance')
        # Only delete if the user owns the  maintenance
        maintenance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk, sk):
        """Update Request"""
        # Locate Maintenance
        # get_object_or_404 returns a object representation of our Maintenance
        maintenance = get_object_or_404(Maintenance, vehicle_id=pk, id=sk)
        # Check the maintenance's owner against the user making this request
        # if request.user != maintenance.owner:
        #     raise PermissionDenied('Unauthorized, you do not own this maintenance')

        # Ensure the owner field is set to the current user's ID
        # request.data['maintenance']['vehicle'] = request.user.id
        # Validate updates with serializer
        data = MaintenanceSerializer(
            maintenance, data=request.data['maintenance'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
