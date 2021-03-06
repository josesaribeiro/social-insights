import nltk
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime

# Use a service account with DB
cred = credentials.Certificate('firebase-admin-key.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

def updateLogs(query):
    doc_ref = db.collection('trending-searches').document('searches-log')
    try:
        doc_ref.set({
            query: datetime.datetime.now()
        }, merge=True)
        print("Logs Updated")
    except:
        print("Error updating logs")


import random

nouns = ("puppy", "car", "rabbit", "girl", "monkey", "guy", "truck", "laptop")
verbs = ("runs", "hits", "jumps", "drives", "barfs", "dances", "coughs", "sneezes") 
adv = ("crazily", "dutifully", "foolishly", "merrily", "occasionally", "joyfully", "lavishly", "harmlessly")
adj = ("adorable", "clueless", "dirty", "odd", "stupid", "smart", "happy", "even")

for i in range(10):
    num = random.randrange(0,8)
    randomQuery = nouns[num] + ' ' + verbs[num] + ' ' + adv[num] + ' ' + adj[num]
    print (randomQuery)
    updateLogs(randomQuery)
