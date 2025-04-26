from ninja import Router, Schema
from classify.utils import classify_text 

router = Router()

class MessageSchema(Schema):
    text: str

@router.post("/predict")
def predict(request, data: MessageSchema):
 label, confidence = classify_text(data.text)
    
 statement = "Spam" if label == "spam" else "Not Spam"
 return {
        "result": label,
        "confidence": f"{confidence * 100:.2f}%",
        "statement": statement
 }