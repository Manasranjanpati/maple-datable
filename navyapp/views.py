from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework_datatables import pagination as dt_pagination

from .models import Aircraft, Origin, Purpose
from .serializers import AircraftSerializer, OriginSerializer


def index(request):
    return render(request, 'navyapp/albums.html')


def get_aircraft_options():
    return "options", {
        "origin": [{'label': obj.name, 'value': obj.pk} for obj in Origin.objects.all()],
        "purpose": [{'label': obj.name, 'value': obj.pk} for obj in Purpose.objects.all()]
    }


class AircraftViewSet(viewsets.ModelViewSet):
    queryset = Aircraft.objects.all().order_by('rank')
    serializer_class = AircraftSerializer

    def get_options(self):
        return get_aircraft_options()

    class Meta:
        datatables_extra_json = ('get_options', )


class OriginViewSet(viewsets.ViewSet):
    queryset = Origin.objects.all().order_by('name')
    serializer_class = OriginSerializer

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def get_options(self):
        return get_aircraft_options()

    class Meta:
        datatables_extra_json = ('get_options', )


class AircraftPostListView(generics.ListAPIView):
    queryset = Aircraft.objects.all().order_by('rank')
    serializer_class = AircraftSerializer
    pagination_class = dt_pagination.DatatablesLimitOffsetPagination

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
