# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.station import Station  # noqa: F401,E501
from swagger_server import util


class StationDataDay(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, station_id: Station=None, time: str=None, temperature_max: float=None, temperature_min: float=None, precipitation_probability: int=None, precipitation: float=None, windspeed_max: float=None, windspeed_min: float=None, windspeed_mean: float=None, relative_humidity_max: int=None, relative_humidity_min: int=None, relative_humidity_mean: int=None):  # noqa: E501
        """StationDataDay - a model defined in Swagger

        :param id: The id of this StationDataDay.  # noqa: E501
        :type id: int
        :param station_id: The station_id of this StationDataDay.  # noqa: E501
        :type station_id: Station
        :param time: The time of this StationDataDay.  # noqa: E501
        :type time: str
        :param temperature_max: The temperature_max of this StationDataDay.  # noqa: E501
        :type temperature_max: float
        :param temperature_min: The temperature_min of this StationDataDay.  # noqa: E501
        :type temperature_min: float
        :param precipitation_probability: The precipitation_probability of this StationDataDay.  # noqa: E501
        :type precipitation_probability: int
        :param precipitation: The precipitation of this StationDataDay.  # noqa: E501
        :type precipitation: float
        :param windspeed_max: The windspeed_max of this StationDataDay.  # noqa: E501
        :type windspeed_max: float
        :param windspeed_min: The windspeed_min of this StationDataDay.  # noqa: E501
        :type windspeed_min: float
        :param windspeed_mean: The windspeed_mean of this StationDataDay.  # noqa: E501
        :type windspeed_mean: float
        :param relative_humidity_max: The relative_humidity_max of this StationDataDay.  # noqa: E501
        :type relative_humidity_max: int
        :param relative_humidity_min: The relative_humidity_min of this StationDataDay.  # noqa: E501
        :type relative_humidity_min: int
        :param relative_humidity_mean: The relative_humidity_mean of this StationDataDay.  # noqa: E501
        :type relative_humidity_mean: int
        """
        self.swagger_types = {
            'id': int,
            'station_id': Station,
            'time': str,
            'temperature_max': float,
            'temperature_min': float,
            'precipitation_probability': int,
            'precipitation': float,
            'windspeed_max': float,
            'windspeed_min': float,
            'windspeed_mean': float,
            'relative_humidity_max': int,
            'relative_humidity_min': int,
            'relative_humidity_mean': int
        }

        self.attribute_map = {
            'id': 'id',
            'station_id': 'station_id',
            'time': 'time',
            'temperature_max': 'temperature_max',
            'temperature_min': 'temperature_min',
            'precipitation_probability': 'precipitation_probability',
            'precipitation': 'precipitation',
            'windspeed_max': 'windspeed_max',
            'windspeed_min': 'windspeed_min',
            'windspeed_mean': 'windspeed_mean',
            'relative_humidity_max': 'relative_humidity_max',
            'relative_humidity_min': 'relative_humidity_min',
            'relative_humidity_mean': 'relative_humidity_mean'
        }

        self._id = id
        self._station_id = station_id
        self._time = time
        self._temperature_max = temperature_max
        self._temperature_min = temperature_min
        self._precipitation_probability = precipitation_probability
        self._precipitation = precipitation
        self._windspeed_max = windspeed_max
        self._windspeed_min = windspeed_min
        self._windspeed_mean = windspeed_mean
        self._relative_humidity_max = relative_humidity_max
        self._relative_humidity_min = relative_humidity_min
        self._relative_humidity_mean = relative_humidity_mean

    @classmethod
    def from_dict(cls, dikt) -> 'StationDataDay':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Station_data_day of this StationDataDay.  # noqa: E501
        :rtype: StationDataDay
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this StationDataDay.


        :return: The id of this StationDataDay.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this StationDataDay.


        :param id: The id of this StationDataDay.
        :type id: int
        """

        self._id = id

    @property
    def station_id(self) -> Station:
        """Gets the station_id of this StationDataDay.


        :return: The station_id of this StationDataDay.
        :rtype: Station
        """
        return self._station_id

    @station_id.setter
    def station_id(self, station_id: Station):
        """Sets the station_id of this StationDataDay.


        :param station_id: The station_id of this StationDataDay.
        :type station_id: Station
        """
        if station_id is None:
            raise ValueError("Invalid value for `station_id`, must not be `None`")  # noqa: E501

        self._station_id = station_id

    @property
    def time(self) -> str:
        """Gets the time of this StationDataDay.


        :return: The time of this StationDataDay.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time: str):
        """Sets the time of this StationDataDay.


        :param time: The time of this StationDataDay.
        :type time: str
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

    @property
    def temperature_max(self) -> float:
        """Gets the temperature_max of this StationDataDay.


        :return: The temperature_max of this StationDataDay.
        :rtype: float
        """
        return self._temperature_max

    @temperature_max.setter
    def temperature_max(self, temperature_max: float):
        """Sets the temperature_max of this StationDataDay.


        :param temperature_max: The temperature_max of this StationDataDay.
        :type temperature_max: float
        """
        if temperature_max is None:
            raise ValueError("Invalid value for `temperature_max`, must not be `None`")  # noqa: E501

        self._temperature_max = temperature_max

    @property
    def temperature_min(self) -> float:
        """Gets the temperature_min of this StationDataDay.


        :return: The temperature_min of this StationDataDay.
        :rtype: float
        """
        return self._temperature_min

    @temperature_min.setter
    def temperature_min(self, temperature_min: float):
        """Sets the temperature_min of this StationDataDay.


        :param temperature_min: The temperature_min of this StationDataDay.
        :type temperature_min: float
        """
        if temperature_min is None:
            raise ValueError("Invalid value for `temperature_min`, must not be `None`")  # noqa: E501

        self._temperature_min = temperature_min

    @property
    def precipitation_probability(self) -> int:
        """Gets the precipitation_probability of this StationDataDay.


        :return: The precipitation_probability of this StationDataDay.
        :rtype: int
        """
        return self._precipitation_probability

    @precipitation_probability.setter
    def precipitation_probability(self, precipitation_probability: int):
        """Sets the precipitation_probability of this StationDataDay.


        :param precipitation_probability: The precipitation_probability of this StationDataDay.
        :type precipitation_probability: int
        """
        if precipitation_probability is None:
            raise ValueError("Invalid value for `precipitation_probability`, must not be `None`")  # noqa: E501

        self._precipitation_probability = precipitation_probability

    @property
    def precipitation(self) -> float:
        """Gets the precipitation of this StationDataDay.


        :return: The precipitation of this StationDataDay.
        :rtype: float
        """
        return self._precipitation

    @precipitation.setter
    def precipitation(self, precipitation: float):
        """Sets the precipitation of this StationDataDay.


        :param precipitation: The precipitation of this StationDataDay.
        :type precipitation: float
        """
        if precipitation is None:
            raise ValueError("Invalid value for `precipitation`, must not be `None`")  # noqa: E501

        self._precipitation = precipitation

    @property
    def windspeed_max(self) -> float:
        """Gets the windspeed_max of this StationDataDay.


        :return: The windspeed_max of this StationDataDay.
        :rtype: float
        """
        return self._windspeed_max

    @windspeed_max.setter
    def windspeed_max(self, windspeed_max: float):
        """Sets the windspeed_max of this StationDataDay.


        :param windspeed_max: The windspeed_max of this StationDataDay.
        :type windspeed_max: float
        """
        if windspeed_max is None:
            raise ValueError("Invalid value for `windspeed_max`, must not be `None`")  # noqa: E501

        self._windspeed_max = windspeed_max

    @property
    def windspeed_min(self) -> float:
        """Gets the windspeed_min of this StationDataDay.


        :return: The windspeed_min of this StationDataDay.
        :rtype: float
        """
        return self._windspeed_min

    @windspeed_min.setter
    def windspeed_min(self, windspeed_min: float):
        """Sets the windspeed_min of this StationDataDay.


        :param windspeed_min: The windspeed_min of this StationDataDay.
        :type windspeed_min: float
        """
        if windspeed_min is None:
            raise ValueError("Invalid value for `windspeed_min`, must not be `None`")  # noqa: E501

        self._windspeed_min = windspeed_min

    @property
    def windspeed_mean(self) -> float:
        """Gets the windspeed_mean of this StationDataDay.


        :return: The windspeed_mean of this StationDataDay.
        :rtype: float
        """
        return self._windspeed_mean

    @windspeed_mean.setter
    def windspeed_mean(self, windspeed_mean: float):
        """Sets the windspeed_mean of this StationDataDay.


        :param windspeed_mean: The windspeed_mean of this StationDataDay.
        :type windspeed_mean: float
        """
        if windspeed_mean is None:
            raise ValueError("Invalid value for `windspeed_mean`, must not be `None`")  # noqa: E501

        self._windspeed_mean = windspeed_mean

    @property
    def relative_humidity_max(self) -> int:
        """Gets the relative_humidity_max of this StationDataDay.


        :return: The relative_humidity_max of this StationDataDay.
        :rtype: int
        """
        return self._relative_humidity_max

    @relative_humidity_max.setter
    def relative_humidity_max(self, relative_humidity_max: int):
        """Sets the relative_humidity_max of this StationDataDay.


        :param relative_humidity_max: The relative_humidity_max of this StationDataDay.
        :type relative_humidity_max: int
        """
        if relative_humidity_max is None:
            raise ValueError("Invalid value for `relative_humidity_max`, must not be `None`")  # noqa: E501

        self._relative_humidity_max = relative_humidity_max

    @property
    def relative_humidity_min(self) -> int:
        """Gets the relative_humidity_min of this StationDataDay.


        :return: The relative_humidity_min of this StationDataDay.
        :rtype: int
        """
        return self._relative_humidity_min

    @relative_humidity_min.setter
    def relative_humidity_min(self, relative_humidity_min: int):
        """Sets the relative_humidity_min of this StationDataDay.


        :param relative_humidity_min: The relative_humidity_min of this StationDataDay.
        :type relative_humidity_min: int
        """
        if relative_humidity_min is None:
            raise ValueError("Invalid value for `relative_humidity_min`, must not be `None`")  # noqa: E501

        self._relative_humidity_min = relative_humidity_min

    @property
    def relative_humidity_mean(self) -> int:
        """Gets the relative_humidity_mean of this StationDataDay.


        :return: The relative_humidity_mean of this StationDataDay.
        :rtype: int
        """
        return self._relative_humidity_mean

    @relative_humidity_mean.setter
    def relative_humidity_mean(self, relative_humidity_mean: int):
        """Sets the relative_humidity_mean of this StationDataDay.


        :param relative_humidity_mean: The relative_humidity_mean of this StationDataDay.
        :type relative_humidity_mean: int
        """
        if relative_humidity_mean is None:
            raise ValueError("Invalid value for `relative_humidity_mean`, must not be `None`")  # noqa: E501

        self._relative_humidity_mean = relative_humidity_mean
