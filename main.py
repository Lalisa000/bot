import telebot
import http.client
import json

# объявляем бота
bot = telebot.TeleBot('959530273:AAEEK9Mx2MwH_yG6y8poIhXvk78Cm9LjN9s')

# создаём кнопки на клавиатуре
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Собаки')
keyboard1.row('Коты')
keyboard1.row('Лисы и их друзья')
keyboard2 = telebot.types.ReplyKeyboardMarkup()
keyboard2.row('Хочу фото котиков', 'Хочу факты о котиках')
keyboard3 = telebot.types.ReplyKeyboardMarkup()
keyboard3.row('Фото лис', 'Фото сиба-ину')
keyboard4 = telebot.types.ReplyKeyboardMarkup()
keyboard4.row('Для чего ты создан?')
keyboard4.row('Что мне нужно делать?')
keyboard4.row('Что ты можешь делать?')
keyboard5 = telebot.types.ReplyKeyboardMarkup()
keyboard5.row('Да', 'Нет')


# обработчик команды start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Я AnimalBot. Я могу показать тебе фотографии милых животных.',
                     reply_markup=keyboard1)
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAINal7Qt5VkwnHIkyTurHCr_SNjYM_JAAJDAQAC9HsZAAEd5_BFZLHT8hkE')


# обработчик команды help
@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Чем я могу помочь, приятель?', reply_markup=keyboard4)
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAOvXtNu0a9ZS4rmBncaCgtpCGhspykAAg8BAAL0exkAAWb0ORQDVMz0GQQ')


# обработчик кнопок
@bot.message_handler(content_types=['text'])
def send_message(message):
    # обработки основных кнопок
    if message.text == 'Хочу фото котиков':
        bot.send_message(message.chat.id, 'Держи фотку 🐈!', reply_markup=keyboard1)
        conn = http.client.HTTPSConnection("api.thecatapi.com")  # устанавливаем связь с апи
        headers = {'x-api-key': "e44128e7-bf75-465b-90ef-1f2efb130354"}  # для catapi нужен ключ
        conn.request("GET", "/v1/images/search?", headers=headers)  # делаем GET запрос
        res = conn.getresponse()  # получаем ответ
        data = res.read()  # читаем его
        site = json.dumps(eval(data))  # переводим json файл data в формат str
        site2 = json.loads(site)  # переводит из формата str в list, чтобы можно было обратиться к переменной url
        x = site2[0]
        y = x.get('url')
        bot.send_photo(message.from_user.id, y)

    elif message.text == 'Собаки':
        conn = http.client.HTTPSConnection("random.dog")
        conn.request("GET", "/woof.json")
        res = conn.getresponse()
        data = res.read()
        site = json.dumps(eval(data))
        site2 = json.loads(site)
        y = site2['url']
        bot.send_message(message.from_user.id, 'Вот тебе фото собак!')
        bot.send_photo(message.from_user.id, y)

    elif message.text == 'Фото лис':
        conn = http.client.HTTPSConnection("randomfox.ca")
        conn.request("GET", "/floof/")
        res = conn.getresponse()
        data = res.read()
        site = json.dumps(eval(data))
        site2 = json.loads(site)
        y = site2.get('image')
        text = y
        arr = ["\\"]
        for x in arr:
            text = text.replace(x, "")
        bot.send_message(message.from_user.id, 'А вот и лисы!', reply_markup=keyboard1)
        bot.send_photo(message.from_user.id, text)

    elif message.text == 'Фото сиба-ину':
        conn = http.client.HTTPSConnection("shibe.online")
        conn.request("GET", "/api/shibes?count=[1-100]&httpsUrls=[true]")
        res = conn.getresponse()
        data = res.read()
        site = json.dumps(eval(data))
        site2 = json.loads(site)
        y = site2[0]
        bot.send_message(message.from_user.id, 'Держи сиба-ину, друг.', reply_markup=keyboard1)
        bot.send_photo(message.from_user.id, y)

    elif message.text == 'Коты':
        bot.send_message(message.from_user.id, 'Что ты хочешь узнать о котиках?', reply_markup=keyboard2)

    elif message.text == 'Лисы и их друзья':
        bot.send_message(message.from_user.id, 'Каких животных ты хочешь увидеть?', reply_markup=keyboard3)

    elif message.text == 'Хочу факты о котиках':
        conn = http.client.HTTPSConnection("cat-fact.herokuapp.com")
        conn.request("GET", "/facts/random")
        res = conn.getresponse()
        data = res.read()
        site = json.loads(data)
        bot.send_message(message.from_user.id, site['text'])
        bot.send_message(message.from_user.id, 'Держи факт о котиках!', reply_markup=keyboard1)

    # обработки кнопок help
    if message.text == 'Для чего ты создан?':
        bot.send_message(message.chat.id, 'Я AnimalBot.\n\nЯ отправляю милые картиночки животных. Могу даже '
                                          'рассказать интересные факты о котиках!', reply_markup=keyboard4)
        bot.send_message(message.chat.id, 'Ещё нужна помощь?', reply_markup=keyboard5)

    elif message.text == 'Что мне нужно делать?':
        bot.send_message(message.chat.id, 'Всё очень просто!\n\nТебе нужно нажмать кнопки на клавиатуре внизу экрана, '
                                          'и я покажу тебе то, что ты хочешь увидеть или узнать.\n\n')
        bot.send_message(message.chat.id, 'Ещё нужна помощь?', reply_markup=keyboard5)

    elif message.text == 'Что ты можешь делать?':
        bot.send_message(message.chat.id, 'Я могу отправлять фотографии собак, лис и котиков.\n\nТакже ты можешь '
                                          'узнать интересные факты о котиках, нажав специальную кнопку!')
        bot.send_message(message.chat.id, 'Ещё нужна помощь?', reply_markup=keyboard5)

    if message.text == 'Да':
        bot.send_message(message.chat.id, 'Я весь во внимании, приятель.', reply_markup=keyboard4)

    elif message.text == 'Нет':
        bot.send_message(message.chat.id, 'Что ты хочешь узнать, друг?', reply_markup=keyboard1)
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAP5XtN6armR8lBjvA5qQcR06-zPcBUAAhEBAAL0exkAAfWfP_aYyFnQGQQ')


# обработка стикеров
@bot.message_handler(content_types=['sticker'])
def send_text_sticker(message):
    bot.send_message(message.chat.id, 'Я люблю стикеры, но следуй правилам и нажимай предложенные мной кнопки!', reply_markup=keyboard1)
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIBF17TfVJOEKUPTFx1VeRpWLN9A2STAAI_AQAC9HsZAAFWKKg0qczYmhkE')


bot.polling()
