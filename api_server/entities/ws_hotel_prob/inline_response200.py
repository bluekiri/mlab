# coding: utf-8

from __future__ import absolute_import

from typing import List

from api_server.entities.base_model_ import Model
from api_server.entities.ws_hotel_prob.inline_response200_probabilities import InlineResponse200Probabilities
from api_server.util import deserialize_model


class InlineResponse200(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    def __init__(self, model: str = None, probabilities: List[InlineResponse200Probabilities] = None,
                 unknown_hotels: List[int] = None):
        """
        InlineResponse200 - a model defined in Swagger

        :param model: The model of this InlineResponse200.
        :type model: str
        :param probabilities: The probabilities of this InlineResponse200.
        :type probabilities: List[InlineResponse200Probabilities]
        :param unknown_hotels: The unknown_hotels of this InlineResponse200.
        :type unknown_hotels: List[int]
        """
        self.swagger_types = {
            'model': str,
            'probabilities': List[InlineResponse200Probabilities],
            'unknown_hotels': List[int]
        }

        self.attribute_map = {
            'model': 'model',
            'probabilities': 'probabilities',
            'unknown_hotels': 'unknown_hotels'
        }

        self._model = model
        self._probabilities = probabilities
        self._unknown_hotels = unknown_hotels

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse200':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200 of this InlineResponse200.
        :rtype: InlineResponse200
        """
        return deserialize_model(dikt, cls)

    @property
    def model(self) -> str:
        """
        Gets the model of this InlineResponse200.

        :return: The model of this InlineResponse200.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model: str):
        """
        Sets the model of this InlineResponse200.

        :param model: The model of this InlineResponse200.
        :type model: str
        """

        self._model = model

    @property
    def probabilities(self) -> List[InlineResponse200Probabilities]:
        """
        Gets the probabilities of this InlineResponse200.

        :return: The probabilities of this InlineResponse200.
        :rtype: List[InlineResponse200Probabilities]
        """
        return self._probabilities

    @probabilities.setter
    def probabilities(self, probabilities: List[InlineResponse200Probabilities]):
        """
        Sets the probabilities of this InlineResponse200.

        :param probabilities: The probabilities of this InlineResponse200.
        :type probabilities: List[InlineResponse200Probabilities]
        """

        self._probabilities = probabilities

    @property
    def unknown_hotels(self) -> List[int]:
        """
        Gets the unknown_hotels of this InlineResponse200.

        :return: The unknown_hotels of this InlineResponse200.
        :rtype: List[int]
        """
        return self._unknown_hotels

    @unknown_hotels.setter
    def unknown_hotels(self, unknown_hotels: List[int]):
        """
        Sets the unknown_hotels of this InlineResponse200.

        :param unknown_hotels: The unknown_hotels of this InlineResponse200.
        :type unknown_hotels: List[int]
        """

        self._unknown_hotels = unknown_hotels
