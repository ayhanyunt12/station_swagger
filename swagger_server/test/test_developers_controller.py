# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.body1 import Body1  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDevelopersController(BaseTestCase):
    """DevelopersController integration test stubs"""

    def test_create_station(self):
        """Test case for create_station

        create a new station
        """
        body = Body1()
        response = self.client.open(
            '/ayhanyunt12/MeteorolojiAPI/1.0.0/station',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_stations(self):
        """Test case for get_stations

        get all station information
        """
        response = self.client.open(
            '/ayhanyunt12/MeteorolojiAPI/1.0.0/stations',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_station_id_delete(self):
        """Test case for station_id_delete

        Delete a user by public_id
        """
        response = self.client.open(
            '/ayhanyunt12/MeteorolojiAPI/1.0.0/station/{id}'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_station_id_get(self):
        """Test case for station_id_get

        Get a user by ID
        """
        response = self.client.open(
            '/ayhanyunt12/MeteorolojiAPI/1.0.0/station/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_station(self):
        """Test case for update_station

        update existing station
        """
        body = Body()
        response = self.client.open(
            '/ayhanyunt12/MeteorolojiAPI/1.0.0/station',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
