from pymongo import MongoClient

# MongoDB Connection URI
MONGO_URI = "mongodb+srv://AdamElkadri:TVQ8cXxy4Cs31Fau@daleel.y7wvs.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)

# Database & Collection
db = client["legal_documents"]
collection = db["user_docs"]

def store_document(user_id, document_data):
    """Stores extracted document data in MongoDB."""
    document = {
        "user_id": user_id,
        "data": document_data
    }
    collection.insert_one(document)
    return "✅ Document stored successfully!"

def retrieve_document(user_id):
    """Retrieves stored document details for a user."""
    document = collection.find_one({"user_id": user_id}, {"_id": 0, "data": 1})
    return document["data"] if document else "❌ No document found!"
