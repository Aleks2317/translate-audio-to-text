import speech_recognition as sr


r = sr.Recognizer()
mic = sr.Microphone()

sr.LANGUAGE = 'ru-RU'

# Запись речи
with mic as source:
    r.adjust_for_ambient_noise(source)  # регулировка окружающего шума
    print("Запись пошла, говорите...")
    audio = r.listen(source)  # сохраняем записанную речь

# преобразуем в текст
text = r.recognize_google(audio, language='ru-RU')

print(f'Вы сказали: {text}')

