import sys
import unittest
from datetime import datetime, timedelta
sys.path.insert(0, 'src')
from taskValidator import taskValidator

class TestTaskValidator(unittest.TestCase):
    def test_validateDeadline_future_date(self):
        future_date = (datetime.now() + timedelta(days=1)).strftime("%d.%m.%Y")
        self.assertIsNotNone(taskValidator.validateDeadline(future_date))
        
    def test_validateDeadline_far_future_date(self):
        far_future_date = (datetime.now() + timedelta(days=365)).strftime("%d.%m.%Y")
        self.assertIsNotNone(taskValidator.validateDeadline(far_future_date))

    def test_validateDeadline_past_date(self):
        past_date = (datetime.now() - timedelta(days=1)).strftime("%d.%m.%Y")
        self.assertIsNone(taskValidator.validateDeadline(past_date))
    
    def test_validateDeadline_past_date_few_hours(self):
        past_date = (datetime.now() - timedelta(hours=2)).strftime("%d.%m.%Y")
        self.assertIsNone(taskValidator.validateDeadline(past_date))

    def test_validateDeadline_past_date_yesterday(self):
        past_date = (datetime.now() - timedelta(days=1)).strftime("%d.%m.%Y")
        self.assertIsNone(taskValidator.validateDeadline(past_date))

    def test_validateDeadline_past_date_last_week(self):
        past_date = (datetime.now() - timedelta(days=7)).strftime("%d.%m.%Y")
        self.assertIsNone(taskValidator.validateDeadline(past_date))

    def test_validateDeadline_invalid_format(self):
        invalid_format = "2024/05/08"
        self.assertIsNone(taskValidator.validateDeadline(invalid_format))
        
    def test_validateDeadline_invalid_format_no_dots(self):
        invalid_format = "20240508"
        self.assertIsNone(taskValidator.validateDeadline(invalid_format))

    def test_validateDeadline_invalid_format_extra_slash(self):
        invalid_format = "2024/05/08/"
        self.assertIsNone(taskValidator.validateDeadline(invalid_format))

    def test_validateDeadline_invalid_format_wrong_order(self):
        invalid_format = "08/05/2024"  # Month/Day/Year
        self.assertIsNone(taskValidator.validateDeadline(invalid_format))
    
    def test_validatePriority_invalide_string(self):
        invalide_string = 'Hi i am Invalid'
        self.assertEqual(taskValidator.validatePriority(invalide_string), 0)

    def test_validatePriority_valid_string(self):
        valid_string = '3'
        self.assertEqual(taskValidator.validatePriority(valid_string), 3)

    def test_validatePriority_valid_string_to_high(self):
        valid_string_tohigh = '100'
        self.assertEqual(taskValidator.validatePriority(valid_string_tohigh), 3)

    def test_validatePriority_valid_string_to_low(self):
        valid_string_tohigh = '-100'
        self.assertEqual(taskValidator.validatePriority(valid_string_tohigh), 0)

    def test_validatePriority_negative_priority(self):
        self.assertEqual(taskValidator.validatePriority(-1), 0)

    def test_validatePriority_valid_priority(self):
        self.assertEqual(taskValidator.validatePriority(2), 2)

    def test_validatePriority_high_priority(self):
        self.assertEqual(taskValidator.validatePriority(5), 3)

    def test_validatePriority_valid_priority_low(self):
        self.assertEqual(taskValidator.validatePriority(1), 1)

    def test_validatePriority_valid_priority_middle(self):
        self.assertEqual(taskValidator.validatePriority(3), 3)

    def test_validateStatus_valid_status(self):
        self.assertEqual(taskValidator.validateStatus("To Do"), "To Do")
        
    def test_validateStatus_valid_status_uppercase(self):
        self.assertEqual(taskValidator.validateStatus("TO DO"), "To Do")

    def test_validateStatus_valid_status_extra_space(self):
        self.assertEqual(taskValidator.validateStatus("In Progress "), "In Progress")

    def test_validateStatus_invalid_status(self):
        self.assertIsNone(taskValidator.validateStatus("Invalid Status"))
        
    def test_validateStatus_invalid_status_empty_string(self):
        self.assertIsNone(taskValidator.validateStatus(""))

    def test_validateStatus_invalid_status_special_characters(self):
        self.assertIsNone(taskValidator.validateStatus("St@tus#"))


if __name__ == '__main__':
    unittest.main()
