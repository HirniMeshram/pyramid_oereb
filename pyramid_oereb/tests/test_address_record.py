# -*- coding: utf-8 -*-

import pytest
import shapely.wkt
import shapely.geometry
from pyramid_oereb.lib.records.address import AddressRecord


def test_get_fields():
    expected_fields = [
            'street_name',
            'zip_code',
            'street_number',
            'geom'
        ]
    fields = AddressRecord.get_fields()
    assert fields == expected_fields


def test_mandatory_fields():
    with pytest.raises(TypeError):
        AddressRecord()


def test_init():
    record = AddressRecord(u"Mühlemattstrasse", 4410, '36', 'POINT(123 456)')
    assert isinstance(record.street_name, unicode)
    assert isinstance(record.zip_code, int)
    assert isinstance(record.street_number, str)
    assert isinstance(shapely.wkt.loads(record.geom), shapely.geometry.point.Point)