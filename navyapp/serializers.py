from rest_framework import serializers

from .models import Aircraft, Origin


class OriginSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Origin
        fields = (
            'id', 'name',
        )
        # Specifying fields in datatables_always_serialize
        # will also force them to always be serialized.
        datatables_always_serialize = ('id',)


class AircraftSerializer(serializers.ModelSerializer):
    origin_name = serializers.ReadOnlyField(source='origin.name')
    # DRF-Datatables can deal with nested serializers as well.
    origin = OriginSerializer()
    purposes = serializers.SerializerMethodField()

    def get_purposes(self, aircraft):
        return ', '.join([str(purpose) for purpose in aircraft.purposes.all()])

    # If you want, you can add special fields understood by Datatables,
    # the fields starting with DT_Row will always be serialized.
    # See: https://datatables.net/manual/server-side#Returned-data
    DT_RowId = serializers.SerializerMethodField()
    DT_RowAttr = serializers.SerializerMethodField()

    def get_DT_RowId(self, aircraft):
        return 'row_%d' % aircraft.pk

    def get_DT_RowAttr(self, aircraft):
        return {'data-pk': aircraft.pk}

    class Meta:
        model = Aircraft
        fields = (
            'DT_RowId', 'DT_RowAttr', 'rank', 'name',
            'year', 'origin_name', 'purposes', 'origin',
        )


