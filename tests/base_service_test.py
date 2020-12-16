#
# voice-skill-sdk
#
# (C) 2020, Deutsche Telekom AG
#
# This file is distributed under the terms of the MIT license.
# For details see the file LICENSE in the top directory.
#
#
import unittest
from skill_sdk import tracing
from skill_sdk.services.base import BaseService, MalformedResponseException

tracing.initialize_tracer()


class TestBaseService(unittest.TestCase):

    def test_no_base_url(self):
        b = BaseService()
        with self.assertRaises(ValueError):
            self.assertEqual(b.url, None)

    def test_malformed_response_exception(self):
        e = MalformedResponseException('message', BaseService())
        self.assertEqual('message', e.message)
        self.assertEqual('MalformedResponseException in service [base]: message', repr(e))
