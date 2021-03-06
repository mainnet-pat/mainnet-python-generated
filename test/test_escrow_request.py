# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in active development, breaking changes may be made prior to official release of version 1.  **Important:** This library is in active development   # noqa: E501

    The version of the OpenAPI document: 0.0.2
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mainnet
from mainnet.models.escrow_request import EscrowRequest  # noqa: E501
from mainnet.rest import ApiException

class TestEscrowRequest(unittest.TestCase):
    """EscrowRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EscrowRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mainnet.models.escrow_request.EscrowRequest()  # noqa: E501
        if include_optional :
            return EscrowRequest(
                buyer_addr = bchtest:qpttdv3qg2usm4nm7talhxhl05mlhms3ys43u76rn0, 
                arbiter_addr = bchtest:qpsm4nm7talhxhl05mlhms3ys43u76rn0ttdv3qg2u, 
                seller_addr = bchtest:qpttdv3qg2usm4nm7talhxhl05mlhms3ys43u76rn0
            )
        else :
            return EscrowRequest(
                buyer_addr = bchtest:qpttdv3qg2usm4nm7talhxhl05mlhms3ys43u76rn0,
                arbiter_addr = bchtest:qpsm4nm7talhxhl05mlhms3ys43u76rn0ttdv3qg2u,
                seller_addr = bchtest:qpttdv3qg2usm4nm7talhxhl05mlhms3ys43u76rn0,
        )

    def testEscrowRequest(self):
        """Test EscrowRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
