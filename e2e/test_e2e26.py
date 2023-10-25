import os
import unittest
from unittest.mock import patch
import main


class E2E26(unittest.TestCase):


    DIR = os.path.dirname(os.path.abspath(__file__))
    csv = os.path.join(DIR, 'DailyWeekly.csv')
    @patch('builtins.input',
           side_effect=['2', '6', csv, '2fba2529-c166-8574-2da2-eac544d82634'])
    def test_get_historical_data(self, mock_input):
        result = main.main()
        self.assertEqual(result, {'weeklyAverage': 16200.0, 'dailyAverage': 6480.0})