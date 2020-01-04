import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from flaskr import create_app
from models import setup_db, Question, Category

# Rememeber to leave trivia_test database empty
class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}/{}".format('gerrard:testpass@localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_question = {
            "answer": None,
            "category": None,
            "difficulty": None,
            "id": None,
            "question": None
        }

        self.data = {
            'previous_questions': '',
            'quiz_category': {
                'type': 'Book',
                'id': 1
            }
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    # Handle failed GET requests for all available categories.
    def test_get_all_categories_fail(self):
        res = self.client().get('/api/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')
        
    # Handle failed GET requests for all available questions.
    def test_get_all_questions_fail(self):
        res = self.client().get('/api/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

    # Handle failed DELETE requests for a question.
    def test_delete_a_question_fail(self):
        res = self.client().delete('/api/questions/{}'.format(''))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

   
    # Handle failed POST request for single question.
    def test_post_a_question_fail(self):
        res = self.client().post('/api/questions', json={})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

    # Handle failed POST request for searching questions.
    def test_search_a_question_fail(self):
        res = self.client().post('/api/questions/search', json={'searchTerm': 1})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Request failed')

    # Handle failed GET requests for all available categories by id.
    def test_get_all_categories_by_id_fail(self):
        res = self.client().get('/api/categories/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

    # Handle the quiz section test.
    def test_quizz_fail(self):
        res = self.client().post('/api/quizzes', json=self.data)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()