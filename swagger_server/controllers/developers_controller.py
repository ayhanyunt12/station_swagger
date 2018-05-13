import connexion
import six

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.body1 import Body1  # noqa: E501
from swagger_server import util


def create_station(body):  # noqa: E501
    """create a new station

    Create new station with the given parameters, insert it to database and returns the created station information. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body1.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_stations():  # noqa: E501
    """get all station information

    Return a json with all station&#39;s information # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def station_id_delete(id):  # noqa: E501
    """Delete a user by public_id

     # noqa: E501

    :param id: Alphanumeric ID of the station to delete
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def station_id_get(id):  # noqa: E501
    """Get a user by ID

     # noqa: E501

    :param id: Numeric ID of the station to get
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def update_station(body):  # noqa: E501
    """update existing station

    Update the station with given id and return the new station informations. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
