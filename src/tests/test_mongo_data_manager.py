import pytest

from src.mongo_connection import MongoDataManager


class TestMongoDataManager:

    def setup_method(self):
        self.db_name = 'test'
        self.collection_name = 'user'
        self.client = MongoDataManager(db_name='test', collection_name='user')

    @pytest.mark.parametrize(
            "input, expected_output", [
                pytest.param(
                             [{"_id": "201", "username": "tester1", "location": "Bengaluru"},
                              {"_id": "202", "username": "tester2", "location": "Kochi"}],
                              True
                ),
                pytest.param({"_id": "203", "username": "tester3", "location": "Mumbai"}, True),
                pytest.param(["tester4", "Delhi"], False)
            ]
    )
    def test_insert_document(self, input, expected_output):
        """
        expected_output:
            True -> Inserted documents successfully.
            False -> Couldn't insert the document.
        """
        response = self.client.insert_document(input)
        assert response == expected_output
    
    def teardown_method(self):
        self.client.collection.delete_many({})
