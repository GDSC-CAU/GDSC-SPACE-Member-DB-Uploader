from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('serviceAccount.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()

load_dotenv()

# names = ['음호준', '김명승', '유용민', '장준성']
# names = ['김동휘', '고은서', '조하연', '이혜원', '안현엽', '박일상', '신정윤', '이주형', '이강민', '이승연', '좌민주', '반상하', '윤상호', '신상우', '한신', '손유진', '정다연', '권혁민', '이승훈', '송섬균', '나정원', '이현섭']
# names = ['정우현', '김은솔', '김희민', '여일구', '오송경', '조용주', '김경훈', '김문선', '김영빈', '김휘경', '송지우', '양희웅', '이서연', '이재형', '이주영', '임준호', '정하경', '조석주', '최건우', '최민준']

dataFile = open("data.csv", "r")
dataList = dataFile.readlines()

dataList.sort()

for line in dataList:
    user = line.split(',')
    if user[1] != 'Core':
        data = {
            "Behance": "",
            "Comment": user[3],
            "Email": user[8],
            "Gender": "Male",
            "Github": user[6],
            "Image": "",
            "Instagram": user[7],
            "Name": user[0],
            "Nickname": user[5],
            "Position": user[2],
            "Role": user[1]
        }

        member_ref = db.collection("Members").document("3")
        member_ref.update({"list": firestore.ArrayUnion([data])})
