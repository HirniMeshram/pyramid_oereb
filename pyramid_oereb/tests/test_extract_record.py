# -*- coding: utf-8 -*-
import datetime
import pytest
from pyramid_oereb.lib.records.real_estate import RealEstateRecord
from pyramid_oereb.lib.records.extract import ExtractRecord
from shapely.geometry.multipolygon import MultiPolygon


def test_get_fields():
    expected_fields = [
        'extract_identifier',
        'real_estate',
        'notconcerned_theme',
        'concerned_theme',
        'theme_without_data',
        'logo_plr_cadastre',
        'creation_date',
        'federal_logo',
        'cantonal_logo',
        'municipality_logo',
        'exclusions_of_liability',
        'glossaries'
    ]
    fields = ExtractRecord.get_fields()
    assert fields == expected_fields


def test_class_variables():
    assert ExtractRecord.creation_date is None
    assert ExtractRecord.electronic_signature is None
    assert ExtractRecord.concerned_theme is None
    assert ExtractRecord.notconcerned_theme is None
    assert ExtractRecord.theme_without_data is None
    assert ExtractRecord.is_reduced is False
    assert ExtractRecord.extract_identifier is None
    assert ExtractRecord.qr_code is None
    assert ExtractRecord.general_information is None
    assert ExtractRecord.base_data is None


def test_mandatory_fields():
    with pytest.raises(TypeError):
        ExtractRecord()


def test_init():
    real_estate = RealEstateRecord('test', 'BL', 'Laufen', 2770, 1000, MultiPolygon())
    record = ExtractRecord(real_estate, bin(100), bin(100), bin(100), bin(100))
    assert isinstance(record.extract_identifier, str)
    assert isinstance(record.real_estate, RealEstateRecord)
    assert isinstance(record.notconcerned_theme, list)
    assert isinstance(record.concerned_theme, list)
    assert isinstance(record.theme_without_data, list)
    assert isinstance(record.creation_date, datetime.date)
    assert isinstance(record.logo_plr_cadastre, bytes)
    assert isinstance(record.federal_logo, bytes)
    assert isinstance(record.cantonal_logo, bytes)
    assert isinstance(record.municipality_logo, bytes)
    assert isinstance(record.exclusions_of_liability, list)
    assert isinstance(record.glossaries, list)