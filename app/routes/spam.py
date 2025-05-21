from fastapi import APIRouter, HTTPException
from app.model.request import SpamRequest
from app.services.spam_detector import predict_spam
from app.utils.payload_cleaner import clean_message, extract_email_parts
from app.logger.logger import log

router = APIRouter()

@router.post("/predict")
def check_spam(request: SpamRequest):
    try:
        if not isinstance(request.message, str):
            raise HTTPException(status_code=422, detail="Message must be a string")
        
        cleaned_message = clean_message(request.message)
        
        parts = extract_email_parts(cleaned_message)
        if parts["subject"]:
            log(f"Subject: {parts['subject']}")
            log(f"Subject length: {len(parts['subject'])}")
        
        truncated_body = parts["body"][:300] + "..." if len(parts["body"]) > 300 else parts["body"]
        log(f"Cleaned body: {truncated_body}")
        
        is_spam = predict_spam(cleaned_message)
        
        
        return {
            "message": cleaned_message,
            "spam": is_spam,
            "parts": parts,
            "status": "success"
        }
    except HTTPException:
        raise
    except Exception as e:
        log(f"Error processing spam detection: {str(e)}", level="error", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
