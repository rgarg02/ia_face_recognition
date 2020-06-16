from Tools.scripts import google
import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore

cred = credentials.Certificate("C:/Users/daduh/Downloads/face123-deb3b-firebase-adminsdk-v1wkh-1b66669c24.json")
app1 = firebase_admin.initialize_app(cred)
store = firestore.client()
peopleRef = store.collection(u'People')
salaryRef = store.collection('Salary')
recordRef = store.collection('Records')

docs = peopleRef.stream()
posts = []
for doc in docs:
    posts.append(doc.to_dict())
print(posts)
