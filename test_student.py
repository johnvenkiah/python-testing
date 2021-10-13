import unittest
from student import Student
from datetime import timedelta


class TestStudent(unittest.TestCase):
    """
    * Create a new test method called test_apply_extension
    * Inside test_apply_extension, store the current end_date for our student
        instance in a variable called old_end_date
    * Call method named apply_extension that will take a number of days as an
        argument on the student instance to update the end_date
    * Assert whether the instance's end_date equals the old end date plys the
        days argument that was passed in using timedelta
    * Run the test to confirm that the new method is working
    * In the Student class create a new method called apply_extension that
        has a parameter called days
    * Use the timedelta method from from datetime to update the
        end_date property
    * Run the tests to comfirm they are working.

    """

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setUp')
        self.student = Student('John', 'Doe', timedelta(days=50))

    def tearDown(self):
        print('tearDown')

    def test_full_name(self):
        print('test_full_name')
        self.assertEqual(self.student.full_name, 'John Doe')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.student.email, 'john.doe@email.com')

    def test_apply_extension(self, days):
        print('test_apply_extension')
        old_end_date = self.student.end_date
        self.student.apply_extension(5)
        self.assertEqual(self.student.end_date, old_end_date + timedelta(days=5))

    def test_alert_santa(self):
        print('test_alert_santa')
        self.student.alert_santa()
        self.assertTrue(self.student.naughty_list)


if __name__ == '__main__':
    unittest.main()