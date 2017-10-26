# coding: utf-8

from __future__ import absolute_import

from flask import json

from . import BaseTestCase
from ..entities.ws_hotel_prob.body import Body


class TestBookController(BaseTestCase):
    """ BookController integration tests stubs """

    def test_prob_hotel_request(self):
        """
        Test case for prob_hotel_request

        Request hotel booking probability
        """
        body = Body()
        body.hotels = [122]
        body.num_adults = 2
        body.num_children = 2
        body.advance = 2

        response = self.client.open('/v1/book',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest

    unittest.main()
