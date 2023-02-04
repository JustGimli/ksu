from speech import speechRecognition, text_to_speech
from API import get_price,get_time,google_search,get_news

# logic press on button

while True:
    # text_to_speech.voise_speech("Я вас внимательно слушаю")
    try:
        text = speechRecognition.get_text().lower()
    except:
        text_to_speech.voise_speech("повторите свой вопрос")
        continue

    if "хабр" in text:
        get_news.get_habr()
    elif "цена" in text or "цену" in text:
        text = text.replace("цена", "")
        
        if "доллара"  in text:
            result = get_price.get_currency(query="USD")
            answer = f"цена доллара: {result['price']} белорусских рубля"
        elif "евро" in text:
            result = get_price.get_currency(query="EUR")
            answer = f"цена евро: {result['price']} белорусских рубля"
        else:
            pass # API FOR CRYPTO
    elif "время" in text:
        time = get_time.get_time_now()
        answer = f"сейчас {time}"
    elif "число" in text:
        data = get_time.get_date_now()
        answer = f"сегодня {data}"
    elif "поиск" in text:
        google_search.get_links(text.replace("поиск", ""))
    else:
        answer = "извините неизвестный запрос"

    text_to_speech.voise_speech(answer)
