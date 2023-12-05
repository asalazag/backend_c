from django.test import TestCase

from ..utils import *

class PickingOrderTest(TestCase):

    def setUp(self):
        create_customer()

