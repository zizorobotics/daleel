from transformers import pipeline, AutoModelForQuestionAnswering, AutoTokenizer
from database import retrieve_document

# Load AraBERT (Arabic NLP model)
model_name = "aubmindlab/bert-base-arabertv02"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)

# Setup a Question Answering pipeline
qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)

def answer_legal_query(user_id, question):
    """
    Retrieves stored document and answers the question based on it.
    """
    context = retrieve_document(user_id)
    
    if context == "❌ No document found!":
        return "⚠️ No document found for this user."
    
    # Format context into a string
    context_text = " ".join(f"{k}: {v}" for k, v in context.items())

    # Get chatbot answer
    result = qa_pipeline(question=question, context=context_text)
    return result["answer"]
