from framework.api import *
from unittest import *

class TestPostMethod(TestCase):

  def test_post_method_happy_flow(self):
      # testing a simple calcuation

    testdata = [1, 2, 3]
    expected_respons = "6"

    Postmethod.addintegers(testdata, expected_respons);

  def test_post_method_one_value(self):
      # testing with a single integer

    testdata = [1]
    expected_respons = "1"

    Postmethod.addintegers(testdata, expected_respons);

  def test_post_method_negative_value(self):
      # testing with a negative value

    testdata = [1, -1, 12]
    expected_respons = "12"

    Postmethod.addintegers(testdata, expected_respons);

  def test_post_method_long(self):
      # testing with largest long integer

    testdata = [9223372036854775808, 1]
    expected_respons = "1"

    Postmethod.addintegers(testdata, expected_respons);

    #Apparently the longest type of integer the API can process is a long
    #This test validates that this is indeed the case

  def test_post_method_uint(self):
      # testing with largest uint integer

    testdata = [4924967295, 1]
    expected_respons = "4924967296"

    Postmethod.addintegers(testdata, expected_respons);

      # This test fails. It should be discussed if this is a bug or a feature.
      # If necessary, the testcase needs to be adjusted accordingly.

  def test_post_method_over_32_bit_int(self):
      # testing with integer larger than 32 bits

    testdata = [2147483647, 1]
    expected_respons = "2147483648"

    Postmethod.addintegers(testdata, expected_respons);

      #Like the previous testcase, a discussion is needed wether the API should be able to process integers
      #bigger than 32 bits. For now the test fails.

  def test_post_method_largest_allowed_32bit_int(self):
      # testing with largest int integer

    testdata = [2147483646, 1]
    expected_respons = "2147483647"

    Postmethod.addintegers(testdata, expected_respons);

  def test_post_method_negative_int_outcome(self):
      # testing if a negative outcome is possible

    testdata = [-5, -3]
    expected_respons = "-8"

    Postmethod.addintegers(testdata, expected_respons);

  def test_post_method_many_values(self):
      # testing with many values

    testdata = [12, 13, 5, 8, 1, 2, 3, 4, 5, 6, 7, 19, 234, 12, -2, 0, 12, 13, 3, 2]
    expected_respons = "359"

    Postmethod.addintegers(testdata, expected_respons);
