from fastapi import APIRouter
from app.model.request import SpamRequest
from app.services.spam_detector import predict_spam

router = APIRouter()

@router.post("/predict")
def check_spam(request: SpamRequest):
    is_spam = predict_spam(request.message)
    return {"message": request.message, "spam": is_spam}
