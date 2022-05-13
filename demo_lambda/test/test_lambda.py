import unittest
from unittest import mock
from unittest.mock import patch
from demo_lambda.src.demo_lambda import lambda_handler, add


class TestLambda(unittest.TestCase):
    def setUp(self):
        pass

    @patch('demo_lambda.src.demo_lambda.add')
    def test_dynamodbSuccessful(self, mock_db):
        event = {'Name': 'jyo', 'Age': 8}
        mock_db.return_value = "added"
        actual_output = lambda_handler(event)
        print(actual_output)
        self.assertEqual(actual_output, "added")

    @patch('demo_lambda.src.demo_lambda.add')
    def test_dynamodbFailure(self, mock_db):
        event = {'Name': 'jyo', 'Age': 8}
        mock_db.return_value = "added"
        actual_output = lambda_handler(event)
        print(actual_output)
        assert actual_output != "Failure"
