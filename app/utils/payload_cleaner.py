# File: app/utils/payload_cleaner.py
import re
from app.logger.logger import log

def clean_message(message: str) -> str:
    
    original_length = len(message)
    
    message = message.replace('\r\n', '\n').replace('\r', '\n')
    
    message = re.sub(r'\n{3,}', '\n\n', message)
    
    message = re.sub(r' {2,}', ' ', message)

    lines = [line.strip() for line in message.split('\n')]
    message = '\n'.join(lines)
    
    message = message.strip()
    
    if message.startswith("Subject:") or "From:" in message[:100]:
        # Find and normalize email headers
        message = re.sub(r'([A-Za-z-]+):\s+', r'\1: ', message)
    
    # Log the changes made
    new_length = len(message)
    char_difference = original_length - new_length
    
    if char_difference > 0:
        log(f"Whitespace cleaning removed {char_difference} characters", level="debug")
    
    return message

def extract_email_parts(message: str) -> dict:
    parts = {"subject": "", "body": "", "headers": {}}

    if "Subject:" in message[:100]:
        # Extract subject
        subject_match = re.search(r'Subject: (.*?)(?:\n|$)', message)
        if subject_match:
            parts["subject"] = subject_match.group(1).strip()
        
        # Separate headers from body
        split_message = re.split(r'\n\s*\n', message, 1)
        
        if len(split_message) > 1:
            headers, body = split_message
            parts["body"] = body.strip()
            
            header_pattern = re.compile(r'^([A-Za-z-]+): (.*?)$', re.MULTILINE)
            for match in header_pattern.finditer(headers):
                key, value = match.groups()
                parts["headers"][key.lower()] = value.strip()
        else:
            parts["body"] = message
    else:
        parts["body"] = message
    
    return parts