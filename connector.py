import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


class DBConnector:
    def __init__(self):
        # Use a service account
        cred = credentials.Certificate('config/firebase-credential.json')
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def get_instance(self):
        return self.db
