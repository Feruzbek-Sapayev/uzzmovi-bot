from aiogram import Bot, Dispatcher, types
from aiogram.types import *
from aiogram.utils import executor
import requests
from bs4 import BeautifulSoup as BS


TOKEN = "5872267661:AAEWakCi9KKhTgeXcrJEFlUqXnMvMA0ayIc"

bot = Bot(token=TOKEN)

dp = Dispatcher(bot=bot)
page = 1
tr_kino=[]
tr_kino_link =[]
urlll = ''
users = []




def connect(page):
    global tr_kino, tr_kino_link
    tr_kino=[]
    tr_kino_link=[]
    r = requests.get(page)
    soup = BS(r.text, 'html.parser')

    imgs = soup.find_all('h4', {'class': 'short-link'})
    i=1
    for j in imgs:
        img=j.find('a')
        if i<=10:
            if img.attrs.get('href')!=None and img.attrs.get('title')!=None:
                i+=1
                link = img.attrs.get('href')
                name = img.attrs.get('title')
                tr_kino.append(name.upper())
                tr_kino_link.append(link)

def download(link):
    info = []
    info1 = []
    r = requests.get(link)
    soup = BS(r.text, 'html.parser')

    s = soup.find_all('div', {'class': 'finfo'})

    for src in s:

        if 'Nomi' in str(src):
            tittle = str(src.find('b'))
            info.append(tittle[3:len(tittle)-4])
            info1.append('Nomi - ')

        if 'Davlati' in str(src):
            country = str(src.find('b'))
            k=0
            for i in range(len(country)):
                if country[i]=='>':
                    k+=1
                    if k==2:
                        p = i
            info.append(country[p+1:len(country)-8])
            info1.append('Davlati - ')

        if 'Sanasi' in str(src):
            date = str(src.find('b'))
            info.append(date[3:len(date)-4])
            info1.append('Sanasi - ')

        if 'Janr' in str(src):
            janr = str(src.find('b'))
            janr+='@'
            k=0
            l = ''
            for i in range(len(janr)-1):
                if janr[i]=='<':
                    k=1
                elif janr[i]=='>':
                    k=0
                if k==0 and janr[i]!='>':
                    l+=janr[i]
            info.append(l)
            info1.append('Janr - ')

        if 'Tili' in str(src):
            lan = str(src.find('b'))
            info.append(lan[3:len(lan)-4])
            info1.append('Tili - ')

        if 'Davomiyligi' in str(src):
            time = str(src.find('b'))
            info.append(time[3:len(time)-4])
            info1.append('Davomiyligi - ')
    s = soup.find('div', {'class': 'fstory-poster'})
    photo = s.find('img').attrs.get('data-src')
    return info, info1, photo


menu = ReplyKeyboardMarkup(resize_keyboard=True).row('🎥 Tarjima Kinolar 🎥', '📣 Premyeralar 📣').row('🇮🇳 Hind kinolar 🇮🇳', '🧸 Multfilm 🧸').row('👨🏻‍💻 Dasturchi 👨🏻‍💻', '📊 Statistika 📊')
b1 = InlineKeyboardButton(text='1', callback_data='bt1')
b2 = InlineKeyboardButton(text='2', callback_data='bt2')
b3 = InlineKeyboardButton(text='3', callback_data='bt3')
b4 = InlineKeyboardButton(text='4', callback_data='bt4')
b5 = InlineKeyboardButton(text='5', callback_data='bt5')
b6 = InlineKeyboardButton(text='6', callback_data='bt6')
b7 = InlineKeyboardButton(text='7', callback_data='bt7')
b8 = InlineKeyboardButton(text='8', callback_data='bt8')
b9 = InlineKeyboardButton(text='⬅️', callback_data='back')
b11 = InlineKeyboardButton(text='➡️', callback_data='next')
btns = InlineKeyboardMarkup(row_width=4).add(b1, b2, b3, b4).add(b5, b6, b7, b8,).add(b9, b11)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    if not(message.from_user.id in users):
        users.append(message.from_user.id)
    await message.reply(f"👋Assalomu aleykum, {message.from_user.first_name}. Uzmovi saytining norasmiy botiga *XUSH KELIBSIZ!*.\nQuyidagi bo'limlandan birini tanlang👇", reply_markup=menu, parse_mode='Markdown')
    


@dp.message_handler()
async def events(message: types.Message):
    global tr_kino, urlll
    global page
    page=1
    
    if message.text=='🎥 Tarjima Kinolar 🎥':
        urlll = 'http://uzmovi.com/tarjima-kino/page/'
        connect(urlll + str(page))
        await message.answer(f'Marhamat, kinolardan birni tanlang👇 \n\n<b>1. {tr_kino[0]}\n2. {tr_kino[1]}\n3. {tr_kino[2]}\n4. {tr_kino[3]}\n5. {tr_kino[4]}\n6. {tr_kino[5]}\n7. {tr_kino[6]}\n8. {tr_kino[7]}</b>', reply_markup=btns, parse_mode='html')
    elif message.text=='📣 Premyeralar 📣':
        urlll = 'http://uzmovi.com/xfsearch/year/2022/page/'
        connect(urlll + str(page))
        await message.answer(f'Marhamat, kinolardan birni tanlang👇 \n\n<b>1. {tr_kino[0]}\n2. {tr_kino[1]}\n3. {tr_kino[2]}\n4. {tr_kino[3]}\n5. {tr_kino[4]}\n6. {tr_kino[5]}\n7. {tr_kino[6]}\n8. {tr_kino[7]}</b>', reply_markup=btns, parse_mode='html')  
    elif message.text=='🇮🇳 Hind kinolar 🇮🇳':
        urlll = 'http://uzmovi.com/hind-kinolar/page/'
        connect(urlll + str(page))
        await message.answer(f'Marhamat, kinolardan birni tanlang👇 \n\n<b>1. {tr_kino[0]}\n2. {tr_kino[1]}\n3. {tr_kino[2]}\n4. {tr_kino[3]}\n5. {tr_kino[4]}\n6. {tr_kino[5]}\n7. {tr_kino[6]}\n8. {tr_kino[7]}</b>', reply_markup=btns, parse_mode='html')
    elif message.text=='🧸 Multfilm 🧸':
        urlll = 'http://uzmovi.com/multfilmla/page/'
        connect(urlll + str(page))
        await message.answer(f'Marhamat, kinolardan birni tanlang👇 \n\n<b>1. {tr_kino[0]}\n2. {tr_kino[1]}\n3. {tr_kino[2]}\n4. {tr_kino[3]}\n5. {tr_kino[4]}\n6. {tr_kino[5]}\n7. {tr_kino[6]}\n8. {tr_kino[7]}</b>', reply_markup=btns, parse_mode='html')
    elif message.text=='👨🏻‍💻 Dasturchi 👨🏻‍💻':
        txt = "👨🏻‍💻 <b>Dasturchi</b> - <i>Feruzbek Sapayev</i>\n\n📨 <b>Taklif va murojaat uchun</b> - <i>@Feruzbek_Sapayev</i>"
        await message.answer(txt, parse_mode='html')
    elif message.text == '📊 Statistika 📊':
        t = len(users)
        await message.answer(f"👨🏻‍💻 *Obunachilar soni* — {t}\n\n📊  https://t.me/UzMoviKinolarBot  statistikasi", parse_mode='Markdown')



@dp.callback_query_handler(text=['next','back','bt1', 'bt2','bt3','bt4','bt5','bt6', 'bt7', 'bt8'])
async def kino(call: types.CallbackQuery):
    global page
    if call.data=='next':
        page+=1
        connect(urlll + str(page))
        await call.message.edit_text(f'Marhamat, kinolardan birni tanlang👇 \n\n<b>1. {tr_kino[0]}\n2. {tr_kino[1]}\n3. {tr_kino[2]}\n4. {tr_kino[3]}\n5. {tr_kino[4]}\n6. {tr_kino[5]}\n7. {tr_kino[6]}\n8. {tr_kino[7]}</b>', reply_markup=btns, parse_mode='html')
    elif call.data=='back':
        if page>1:
            page-=1
            connect(urlll + str(page))
            await call.message.edit_text(f'Marhamat, kinolardan birni tanlang👇 \n\n<b>1. {tr_kino[0]}\n2. {tr_kino[1]}\n3. {tr_kino[2]}\n4. {tr_kino[3]}\n5. {tr_kino[4]}\n6. {tr_kino[5]}\n7. {tr_kino[6]}\n8. {tr_kino[7]}</b>', reply_markup=btns, parse_mode='html')
        else:
            await call.answer()
    elif call.data=='bt1':
        img, img1, photo  = download(tr_kino_link[0])
        b1 = InlineKeyboardButton(text="📽 ONLINE KO'RISH 📽", url=tr_kino_link[0])
        btn = InlineKeyboardMarkup().add(b1)
        text = f'🎥 *{img[0]}*\n\n'
        for i in range(len(img)):
            text += f"  🔹 *{img1[i]}*  _{img[i]}_\n\n"
        text +="*Eng so'ngi tarjima kinolar faqat bizda!*\nhttps://t.me/UzMoviKinolarBot "
        await bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption=text, parse_mode='Markdown', reply_markup=btn)
    
    elif call.data=='bt2':
        img, img1, photo  = download(tr_kino_link[1])
        b1 = InlineKeyboardButton(text="📽 ONLINE KO'RISH 📽", url=tr_kino_link[1])
        btn = InlineKeyboardMarkup().add(b1)
        text = f'🎥 *{img[0]}*\n\n'
        for i in range(len(img)):
            text += f"  🔹 *{img1[i]}*  _{img[i]}_\n\n"
        text +="*Eng so'ngi tarjima kinolar faqat bizda!*\nhttps://t.me/UzMoviKinolarBot "
        await bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption=text, parse_mode='Markdown', reply_markup=btn)
    
    elif call.data=='bt3':
        img, img1, photo  = download(tr_kino_link[2])
        b1 = InlineKeyboardButton(text="📽 ONLINE KO'RISH 📽", url=tr_kino_link[2])
        btn = InlineKeyboardMarkup().add(b1)
        text = f'🎥 *{img[0]}*\n\n'
        for i in range(len(img)):
            text += f"  🔹 *{img1[i]}*  _{img[i]}_\n\n"
        text +="*Eng so'ngi tarjima kinolar faqat bizda!*\nhttps://t.me/UzMoviKinolarBot "
        await bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption=text, parse_mode='Markdown', reply_markup=btn)

    elif call.data=='bt4':
        img, img1, photo  = download(tr_kino_link[3])
        b1 = InlineKeyboardButton(text="📽 ONLINE KO'RISH 📽", url=tr_kino_link[3])
        btn = InlineKeyboardMarkup().add(b1)
        text = f'🎥 *{img[0]}*\n\n'
        for i in range(len(img)):
            text += f"  🔹 *{img1[i]}*  _{img[i]}_\n\n"
        text +="*Eng so'ngi tarjima kinolar faqat bizda!*\nhttps://t.me/UzMoviKinolarBot "
        await bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption=text, parse_mode='Markdown', reply_markup=btn)
    
    elif call.data=='bt5':
        img, img1, photo  = download(tr_kino_link[4])
        b1 = InlineKeyboardButton(text="📽 ONLINE KO'RISH 📽", url=tr_kino_link[4])
        btn = InlineKeyboardMarkup().add(b1)
        text = f'🎥 *{img[0]}*\n\n'
        for i in range(len(img)):
            text += f"  🔹 *{img1[i]}*  _{img[i]}_\n\n"
        text +="*Eng so'ngi tarjima kinolar faqat bizda!*\nhttps://t.me/UzMoviKinolarBot "
        await bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption=text, parse_mode='Markdown', reply_markup=btn)
    
    elif call.data=='bt6':
        img, img1, photo  = download(tr_kino_link[5])
        b1 = InlineKeyboardButton(text="📽 ONLINE KO'RISH 📽", url=tr_kino_link[5])
        btn = InlineKeyboardMarkup().add(b1)
        text = f'🎥 *{img[0]}*\n\n'
        for i in range(len(img)):
            text += f"  🔹 *{img1[i]}*  _{img[i]}_\n\n"
        text +="*Eng so'ngi tarjima kinolar faqat bizda!*\nhttps://t.me/UzMoviKinolarBot "
        await bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption=text, parse_mode='Markdown', reply_markup=btn)
    
    elif call.data=='bt7':
        img, img1, photo  = download(tr_kino_link[6])
        b1 = InlineKeyboardButton(text="📽 ONLINE KO'RISH 📽", url=tr_kino_link[6])
        btn = InlineKeyboardMarkup().add(b1)
        text = f'🎥 *{img[0]}*\n\n'
        for i in range(len(img)):
            text += f"  🔹 *{img1[i]}*  _{img[i]}_\n\n"
        text +="*Eng so'ngi tarjima kinolar faqat bizda!*\nhttps://t.me/UzMoviKinolarBot "
        await bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption=text, parse_mode='Markdown', reply_markup=btn)

    elif call.data=='bt8':
        img, img1, photo  = download(tr_kino_link[7])
        b1 = InlineKeyboardButton(text="📽 ONLINE KO'RISH 📽", url=tr_kino_link[7])
        btn = InlineKeyboardMarkup().add(b1)
        text = f'🎥 *{img[0]}*\n\n'
        for i in range(len(img)):
            text += f"  🔹 *{img1[i]}*  _{img[i]}_\n\n"
        text +="*Eng so'ngi tarjima kinolar faqat bizda!*\nhttps://t.me/UzMoviKinolarBot "
        await bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption=text, parse_mode='Markdown', reply_markup=btn)
    
    await call.answer()


if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)


