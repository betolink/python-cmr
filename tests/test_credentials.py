import unittest
import requests

from cmr.queries import CollectionQuery, GranuleQuery

class TestCollectionClass(unittest.TestCase):

    def test_session_object_no_auth(self):
        c_query = CollectionQuery()
        g_query = GranuleQuery()

        self.assertTrue(hasattr(c_query, 'session'))
        self.assertEqual(type(c_query.session), requests.Session)

        self.assertTrue(hasattr(g_query, 'session'))
        self.assertEqual(type(g_query.session), requests.Session)


    def test_session_object_auth(self):
        credentials = {
            'username': 'rocinante',
            'password': 'Cervantes1'
        }
        c_auth_query = CollectionQuery(credentials=credentials)
        g_auth_query = GranuleQuery(credentials=credentials)

        self.assertTrue(hasattr(c_auth_query, 'session'))
        self.assertEqual(type(c_auth_query.session), requests.Session)
        self.assertTrue(hasattr(c_auth_query.session, 'cookies'))

        self.assertTrue(hasattr(g_auth_query, 'session'))
        self.assertEqual(type(g_auth_query.session), requests.Session)
        self.assertTrue(hasattr(g_auth_query.session, 'cookies'))


        collection = c_auth_query.concept_id(['C1938032626-POCLOUD'])
        self.assertEqual(1, collection.hits())


