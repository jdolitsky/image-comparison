"""Unit testing

Usage:

python test.py
"""

import os
import unittest

import pandas as pd

from filter_data import filter_df

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

class TestFilterDataFunctions(unittest.TestCase):
    """Test trivy-related functions."""

    def test_filter_df(self):
        """Test filter_df()."""
        TEST_INPUT_DATA = os.path.join(
            DIR_PATH, "test_data", "test_input_data.csv"
        )
        TEST_EXPECTED_DATA = os.path.join(
            DIR_PATH, "test_data", "test_expected_data.csv"
        )
        input_df = pd.read_csv(TEST_INPUT_DATA)
        df_got = filter_df(input_df)
        df_expected = pd.read_csv(TEST_EXPECTED_DATA)

        pd.testing.assert_frame_equal(df_got, df_expected)

if __name__ == "__main__":
    unittest.main()