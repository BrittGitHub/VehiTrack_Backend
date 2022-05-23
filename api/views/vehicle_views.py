from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.vehicle import Vehicle
from ..serializers import VehicleSerializer

# Create your views here.


class Vehicles(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = VehicleSerializer

    def get(self, request):
        """Index request"""
        # Get all the vehicles:
        # vehicles = Vehicle.objects.all()
        # Filter the vehicles by owner, so you can only see your owned vehicles
        vehicles = Vehicle.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = VehicleSerializer(vehicles, many=True).data
        return Response({'vehicles': data})

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['vehicle']['owner'] = request.user.id
        # Serialize/create vehicle
        vehicle = VehicleSerializer(data=request.data['vehicle'])
        # If the vehicle data is valid according to our serializer...
        if vehicle.is_valid():
            # Save the created vehicle & send a response
            vehicle.save()
            return Response({'vehicle': vehicle.data}, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(vehicle.errors, status=status.HTTP_400_BAD_REQUEST)


class VehicleDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        """Show request"""
        # Locate the vehicle to show
        vehicle = get_object_or_404(Vehicle, pk=pk)
        # Only want to show owned vehicles?
        if request.user != vehicle.owner:
            raise PermissionDenied('Unauthorized, you do not own this vehicle')

        # Run the data through the serializer so it's formatted
        data = VehicleSerializer(vehicle).data
        return Response({'vehicle': data})

    def delete(self, request, pk):
        """Delete request"""
        # Locate vehicle to delete
        vehicle = get_object_or_404(Vehicle, pk=pk)
        # Check the vehicle's owner against the user making this request
        if request.user != vehicle.owner:
            raise PermissionDenied('Unauthorized, you do not own this vehicle')
        # Only delete if the user owns the  vehicle
        vehicle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Locate Vehicle
        # get_object_or_404 returns a object representation of our Vehicle
        vehicle = get_object_or_404(Vehicle, pk=pk)
        # Check the vehicle's owner against the user making this request
        if request.user != vehicle.owner:
            raise PermissionDenied('Unauthorized, you do not own this vehicle')

        # Ensure the owner field is set to the current user's ID
        request.data['vehicle']['owner'] = request.user.id
        # Validate updates with serializer
        data = VehicleSerializer(vehicle, data=request.data['vehicle'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
