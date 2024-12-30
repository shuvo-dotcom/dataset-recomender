from transformers import MarianMTModel, MarianTokenizer
import torch
def load_model_and_tokenizer(src_lang, trg_lang):
    model_name = f'Helsinki-NLP/opus-mt-{src_lang}-{trg_lang}'
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    return model, tokenizer

def translate(model, tokenizer, sentence):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.eval()
    inputs = tokenizer(sentence, return_tensors='pt', padding=True, truncation=True).to(device)
    with torch.no_grad():
        translated = model.generate(inputs['input_ids'])
    translated_sentence = tokenizer.decode(translated[0], skip_special_tokens=True)
    return translated_sentence
