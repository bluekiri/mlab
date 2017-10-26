# coding: utf-8

from __future__ import absolute_import
from api_server.entities.base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from api_server.util import deserialize_model


class BookRequest(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, advance: int=None, nights: int=None, num_adults: int=None, num_children: int=None, hotels: List[int]=None):
        """
        BookRequest - a model defined in Swagger

        :param advance: The advance of this BookRequest.
        :type advance: int
        :param nights: The nights of this BookRequest.
        :type nights: int
        :param num_adults: The num_adults of this BookRequest.
        :type num_adults: int
        :param num_children: The num_children of this BookRequest.
        :type num_children: int
        :param hotels: The hotels of this BookRequest.
        :type hotels: List[int]
        """
        self.swagger_types = {
            'advance': int,
            'nights': int,
            'num_adults': int,
            'num_children': int,
            'hotels': List[int]
        }

        self.attribute_map = {
            'advance': 'advance',
            'nights': 'nights',
            'num_adults': 'numAdults',
            'num_children': 'numChildren',
            'hotels': 'hotels'
        }

        self._advance = advance
        self._nights = nights
        self._num_adults = num_adults
        self._num_children = num_children
        self._hotels = hotels

    @classmethod
    def from_dict(cls, dikt) -> 'BookRequest':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The bookRequest of this BookRequest.
        :rtype: BookRequest
        """
        return deserialize_model(dikt, cls)

    @property
    def advance(self) -> int:
        """
        Gets the advance of this BookRequest.

        :return: The advance of this BookRequest.
        :rtype: int
        """
        return self._advance

    @advance.setter
    def advance(self, advance: int):
        """
        Sets the advance of this BookRequest.

        :param advance: The advance of this BookRequest.
        :type advance: int
        """
        if advance is None:
            raise ValueError("Invalid value for `advance`, must not be `None`")

        self._advance = advance

    @property
    def nights(self) -> int:
        """
        Gets the nights of this BookRequest.

        :return: The nights of this BookRequest.
        :rtype: int
        """
        return self._nights

    @nights.setter
    def nights(self, nights: int):
        """
        Sets the nights of this BookRequest.

        :param nights: The nights of this BookRequest.
        :type nights: int
        """
        if nights is None:
            raise ValueError("Invalid value for `nights`, must not be `None`")

        self._nights = nights

    @property
    def num_adults(self) -> int:
        """
        Gets the num_adults of this BookRequest.

        :return: The num_adults of this BookRequest.
        :rtype: int
        """
        return self._num_adults

    @num_adults.setter
    def num_adults(self, num_adults: int):
        """
        Sets the num_adults of this BookRequest.

        :param num_adults: The num_adults of this BookRequest.
        :type num_adults: int
        """
        if num_adults is None:
            raise ValueError("Invalid value for `num_adults`, must not be `None`")

        self._num_adults = num_adults

    @property
    def num_children(self) -> int:
        """
        Gets the num_children of this BookRequest.

        :return: The num_children of this BookRequest.
        :rtype: int
        """
        return self._num_children

    @num_children.setter
    def num_children(self, num_children: int):
        """
        Sets the num_children of this BookRequest.

        :param num_children: The num_children of this BookRequest.
        :type num_children: int
        """
        if num_children is None:
            raise ValueError("Invalid value for `num_children`, must not be `None`")

        self._num_children = num_children

    @property
    def hotels(self) -> List[int]:
        """
        Gets the hotels of this BookRequest.
        Array of hotels

        :return: The hotels of this BookRequest.
        :rtype: List[int]
        """
        return self._hotels

    @hotels.setter
    def hotels(self, hotels: List[int]):
        """
        Sets the hotels of this BookRequest.
        Array of hotels

        :param hotels: The hotels of this BookRequest.
        :type hotels: List[int]
        """
        if hotels is None:
            raise ValueError("Invalid value for `hotels`, must not be `None`")

        self._hotels = hotels

