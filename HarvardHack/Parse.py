import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('/Users/williamlee/Desktop/HarvardHack/harvardshake-firebase-adminsdk-gy5wj-b6c07bc92f.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://harvardshake-default-rtdb.firebaseio.com/"
})

ref = db.reference('/professors')
professors_dict = ref.get()

ref = db.reference('/students')
students_dict = ref.get()

print(len(students_dict))
