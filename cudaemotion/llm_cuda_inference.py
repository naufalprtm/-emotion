import torch

def analyze_text_emotion_cuda(text):
    inputs = tokenizer(text, return_tensors="pt").to("cuda")
    model.to("cuda")
    with torch.no_grad():
        logits = model(**inputs).logits
    return torch.argmax(logits).item()
