# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in active development, breaking changes may be made prior to official release of version 1.  **Important:** This library is in active development   # noqa: E501

    The version of the OpenAPI document: 0.0.1-rc
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mainnet
from mainnet.models.contract_response import ContractResponse  # noqa: E501
from mainnet.rest import ApiException

class TestContractResponse(unittest.TestCase):
    """ContractResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ContractResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mainnet.models.contract_response.ContractResponse()  # noqa: E501
        if include_optional :
            return ContractResponse(
                contract_id = '0', 
                address = bchtest:qpttdv3qg2usm4nm7talhxhl05mlhms3ys43u76rn0
            )
        else :
            return ContractResponse(
        )

    def testContractResponse(self):
        """Test ContractResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
