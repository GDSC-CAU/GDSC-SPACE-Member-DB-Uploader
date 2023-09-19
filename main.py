from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('serviceAccount.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()

load_dotenv()

data = {
    "Behance": "",
    "Comment": "",
    "Email": "",
    "Gender": "",
    "Github": "",
    "Image": "",
    "Instagram": "",
    "Name": "",
    "Nickname": "",
    "Position": "",
    "Role": ""
}

member_ref = db.collection("Members").document("2")
member_ref.update({"list": firestore.ArrayUnion([data])})
