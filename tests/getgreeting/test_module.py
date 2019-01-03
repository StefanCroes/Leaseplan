from framework.api import *
from unittest import *

class TestPostMethod(TestCase):

  def test_post_method_id1(self):
      # testing the respons for id1

    test_input = 'id1'
    expected_respons = '[id1-content.]'

    Hellogreeting.getgreeting(test_input, expected_respons);

  def test_post_method_id2(self):
      # testing the respons for id2

    test_input = 'id2'
    expected_respons = '[id2-content.]'

    Hellogreeting.getgreeting(test_input, expected_respons);

  def test_post_method_id3(self):
      # testing the respons for id3. No content expected

    test_input = 'id3'
    expected_respons = '[no content]'

    Hellogreeting.getgreeting(test_input, expected_respons);

