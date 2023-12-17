import requests
from settings import url,msg_start
from sends import send_message,send_contact,send_photo
from time import sleep
def get_updets(url:str):
    endpoint = "/getUpdates"
    url+=endpoint
    respons = requests.get(url)
    if respons.status_code ==200:
        result = respons.json()['result']
        if len(result)!=0:
            return result[-1]
        else:
            return 404
    else:
        return respons.status_code
# Bosh sahifaning asosiy qismi
bosh_menu = {"text":"🏠Bosh menyu"}
btn_bosh1 = {"text":"🔥Mahsulotlar"}
btn_bosh11 = {"text":"📥Savat_bosh"}
btn_bosh2 = {"text":"💼Hamkorlik"}
btn_bosh22 = {"text":"ℹ️Ma'lumot"}
btn_boshtil = {"text":"🌐Tilni tanlash"}
replay_markub = {
    "keyboard":[
        [btn_bosh1,btn_bosh11],
        [btn_bosh2,btn_bosh22],
        [btn_boshtil],
    ],
    "resize_keyboard":True,
}
#end
#Bosh sahifa->Ma'lumot
mal1 = {"text":"✍️Izoh qoldirish"}
mal2 = {"text":"🚀Yetkazib berish shartlari"}
mal22 = {"text":"☎️Kontaktlar"}
replay_malumot = {
    "keyboard":[
        [mal1],
        [mal2,mal22],
        [bosh_menu],
    ],
    "resize_keyboard":True,
}

#Bosh sahifa ->Malumot->Izoh qoldirish
izoh1 = {"text":"☺️Menga hamma narsa yoqdi, 5❤️"}
izoh2 = {"text":"☺️Yaxshi, 4⭐️⭐️⭐️⭐️"}
izoh3 = {"text":"🙂Qoniqarli, 3⭐️⭐️⭐️"}
izoh4 = {"text":"☹️Yoqmadi, 2⭐️⭐️"}
izoh5 = {"text":"😤Men shikoyat qilmoqchiman👎🏻"}
replay_izoh = {
    "keyboard":[
        [izoh1],
        [izoh2],
        [izoh3],
        [izoh4],
        [izoh5],
        [bosh_menu]
    ]
}
#end
# Tilni tanlash qismi boshlandi 
til_inline1 = {"text":"🇷🇺Русский","url":"https://t.me/allamurod_2806"}
til_inline2 = {"text":"🇸🇱O'zbekcha","url":"https://t.me/allamurod_2806"}
inline_markub = {
    "inline_keyboard":[
        [til_inline1],
        [til_inline2],
    ]
}
#end
btn_savat = {"text":"📥Savat"}

#Mahsulotlar
btn1 = {"text":"🚖Buturtma berish"}
btn11 = {"text":"📥Savat_mahsulot"}
btn2 = {"text":"Troll.uz"}
btn22 = {"text":"Temur Alixonov"}
btn3 = {"text":"#ЧЗХ"}
btn33 = {"text":"Konsta"}
btn4 = {"text":"Go Uz"}
btn44 = {"text":"Subyektiv"}

replay_markup_asos = {
    "keyboard":[
        [btn1,btn11],
        [btn2,btn22],
        [btn3,btn33],
        [btn4,btn44],
        [bosh_menu]

    ],
    "resize_keyboard":True,
    "one_time_keyboard":False,
}
#end
#Mahsulot -> Troll.uz
btn_tr_savat = {"text":"📥Savat_mahsulot_tr"}
btn_tr_buyurtma  = {"text":"🚖Buturtma berish_byurtma"}
btn_tr1 = {"text":"Futbolkalar"}
btn_tr11 = {"text":"Xudi"}
btn_tr2 = {"text":"Svitshotlar"}
btn_tr22 = {"text":"Kepkalar"}
btn_tr3 = {"text":"Stikerlar"}
btn_tr33 = {"text":"To'plamlar"}

replay_markub_trr = {
    "keyboard":[
        [btn_tr_buyurtma,btn_tr_savat],
        [btn_tr1,btn_tr11],
        [btn_tr2,btn_tr22],
        [btn_tr3,btn_tr33],
        [bosh_menu]
    ],
    "resize_keyboard":True,
}
#end
#Mahsulot -> Troll.uz -> Futbolkalar
btn_trfut1 = {"text":"Don't br Sheep"}
btn_trfut11 = {"text":"Make Plove Not War"}
btn_trfut2 = {"text":"Turn on insoff"}
btn_trfut22 = {"text":"Mussafo sky"}
btn_trfut3 = {"text":"Surish kerak"}
btn_trfut33 = {"text":"Tanish Bilish"}
btn_trfut4 = {"text":"Tirikchilik"}
btn_trfut44 = {"text":"Use Farosat"}
btn_trfut5 = {"text":"Adolat😉"}
btn_trfut55 = {"text":"100% paxta"}
btn_trfut6 = {"text":"Plover"}
btn_trfut66 = {"text":"Haqiqat🚫"}
btn_trfut7 = {"text":"Somsa"}
btn_trfut77 = {"text":"QIS🤌"}
btn_trfut8 = {"text":"Not Like Non"}
btn_trfut88 = {"text":"Hes been selected"}
btn_trfut9 = {"text":"Shashlik"}
btn_trfut99 = {"text":"Say Xo'p"}
btn_nazad = {"text":"⬅️Ortga"}
replay_markub_fut = {
    "keyboard":[
        [btn_trfut1,btn_trfut11],
        [btn_trfut2,btn_trfut22],
        [btn_trfut3,btn_trfut33],
        [btn_trfut4,btn_trfut44],
        [btn_trfut5,btn_trfut55],
        [btn_trfut6,btn_trfut66],
        [btn_trfut7,btn_trfut77],
        [btn_trfut8,btn_trfut88],
        [btn_trfut9,btn_trfut99],
        [btn_nazad,btn_savat],

    ],
    "resize_keyboard":True,
}
#Mahsulot -> Troll.uz -> Futbolkalar -> photo
btn_oq = {"text":"Oq"}
btn_qora = {"text":"Qora"}
replay_btntrfut_markub = {
    "keyboard":[
        [btn_oq,btn_qora],
        [bosh_menu]
    ],
    "resize_keyboard":True
}

#end
# Mahsulotlar -> Trollar.uz -> Xuddi
btn_xuddi1 = {"text":"Plover"}
btn_xuddi11 = {"text":"Somsa"}
btn_xuddi2 = {"text":"Lagman"}
btn_xuddi22 = {"text":"Bas!"}
btn_xuddi3 = {"text":"Insofli o'g'ri"}
btn_xuddi33 = {"text":"Tirikchilik"}
btn_xuddi4 = {"text":"Make plove"}
btn_xuddi44 = {"text":"Surish kerak"}
btn_xuddi5 = {"text":"Don't be Sheep"}
btn_xuddi55 = {"text":"Musaffo Sky"}
btn_xuddi6 = {"text":"Turn on insoff"}
btn_xuddi66 = {"text":"User farosat"}
btn_xuddi7 = {"text":"Adolat☺️"}
btn_xuddi77 = {"text":"Tanish Bilish"}
btn_xuddi8 = {"text":"Haqiqat😰"}
btn_xuddi88 = {"text":"Hot Like Non"}
btn_xuddi9 = {"text":"Say xo'p😉"}
btn_xuddi99 = {"text":"Shashlik"}
btn_xuddi10 = {"text":"⬅️Ortga"}
btn_xuddi1010 = {"text":"📥Savat"}
replay_xuddi_markub = {
    "keyboard":[
        [btn_xuddi1,btn_xuddi11],
        [btn_xuddi44,btn_xuddi6],
        [btn_xuddi4,btn_xuddi33],
        [btn_xuddi66,btn_xuddi77],
        [btn_xuddi5,btn_xuddi7],
        [btn_xuddi55,btn_xuddi8],
        [btn_xuddi9,btn_xuddi99],
        [btn_xuddi88],
        [btn_xuddi10,btn_xuddi1010],

    ],
    "resize_keyboard":True,
}
# Trollar.uz -> Svitshotlar
replay_svitshot_markub = {
    "keyboard":[
        [btn_xuddi1,btn_xuddi11],
        [btn_xuddi2,btn_xuddi22],
        [btn_xuddi3,btn_xuddi33],
        [btn_xuddi4,btn_xuddi44],
        [btn_xuddi5,btn_xuddi55],
        [btn_xuddi6,btn_xuddi66],
        [btn_xuddi7,btn_xuddi77],
        [btn_xuddi8,btn_xuddi88],
        [btn_xuddi9,btn_xuddi99],
        [btn_xuddi10,btn_xuddi1010],

    ],
    "resize_keyboard":True,
}
#Trollar.uz -> Kepkalar
btn_kepka1 = {"text":"✈️⬛️"}
btn_kepka11 = {"text":"Adolat⬜️"}
btn_kepka2 = {"text":"Adolat⬛️"}
btn_kepka3 = {"text":"⬅️Ortga"}
btn_kepka33 = {"text":"📥Savat"}
replay_kepka_markub = {
    "keyboard":[
        [btn_kepka1,btn_kepka11],
        [btn_kepka2],
        [btn_kepka3,btn_kepka33]
    ],
    "resize_keyboard":True,
}

#Trollar.uz -> Stikerlar
btn_stiker1 = {"text":"Sticker Pack №1"}
btn_stiker2 = {"text":"⬅️Ortga"}
btn_stiker22 = {"text":"📥Savat"}

replay_stiker_markup = {
    "keyboard":[
        [btn_stiker1],
        [btn_stiker2,btn_stiker22]
    ],
    "resize_keyboard":True
}
#Trollar.uz -> To'plamlar 
btn_toplam1 = {"text":"Pro"}
btn_toplam11 = {"text":"Pro Max"}
btn_toplam2 = {"text":"Ultra"}
btn_toplam3 = {"text":"⬅️Ortga"}
btn_toplam33 = {"text":"📥Savat"}
replay_toplam_markub = {
    "keyboard":[
        [btn_toplam1,btn_toplam11],
        [btn_toplam2],
        [btn_toplam3,btn_toplam33]
    ],
    "resize_keyboard":True,
}
#Temur Alixonov start
btn_temur1 = {"text":"⬅️Ortga"}
btn_temur2 = {"text":"🚖 Buyurtma berish_Temur"}
btn_temur22 = {"text":"📥Savat_Temur"}
btn_temur3 = {"text":"Futbolkalar_Temur"}
btn_temur33 = {"text":"Xuddi_Temur"}
btn_temur4 = {"text":"Svitshotlar_Temur"}
replay_temur_markub = {
    "keyboard":[
        [btn_temur1],
        [btn_temur2,btn_temur22],
        [btn_temur3,btn_temur33],
        [btn_temur4],
        [bosh_menu],
    ],
    "resize_keyboard":True

}
#Temur Alixonov -> Futbolkalar
btn_temur_fut1 = {"text":"Такой лёгкий!"}
btn_temur_fut11 = {"text":"Boylarga mazza!"}
btn_temur_fut2 = {"text":"Bonuni yigiti"}
btn_temur_fut22 = {"text":"Futbolkaa nechi?"}
btn_temur_fut3 = {"text":"Shunchaki biznes!"}
btn_temur_fut33 = {"text":"Odamlar nima deydi?"}
btn_temur_fut4 = {"text":"⬅️Ortga"}
btn_temur_fut44 = {"text":"📥Savat"}
replay_temurfut = {
    "keyboard":[
        [btn_temur_fut1,btn_temur_fut11],
        [btn_temur_fut2,btn_temur_fut22],
        [btn_temur_fut3,btn_temur_fut33],
        [btn_temur_fut4,btn_temur_fut44],
    ],
    "resize_keyboard":True
}
# Temur -> Xudi
replay_temurxudi = {
    "keyboard":[
        [btn_temur_fut1,btn_temur_fut3],
        [btn_temur_fut11,btn_temur_fut2],
        [btn_temur_fut33],
        [btn_temur_fut4,btn_temur_fut44]
    ],
    "resize_keyboard":True
}
# #ЧЗХ -> start
btn_ЧЗХ1= {"text":"Cheklangan Futbolkalar!"}
btn_ЧЗХ2 = {"text":"⬅️Ortga"}
btn_ЧЗХ22 = {"text":"📥Savat"}
replay_ЧЗХ_markub = {
    "keyboard":[
        [btn_ЧЗХ1],
        [btn_ЧЗХ2,btn_ЧЗХ22],
    ],
    "resize_keyboard":True,
}
#Konsta ->start
btn_konsta1 = {"text":"🚖 Buyurtma berish_Konsta"}
btn_konsta11 = {"text":"📥Savat_Konsta"}
btn_konsta2 = {"text":"Futbolkalar_Konsta"}
btn_konsta22 = {"text":"Svitshotlar_Konsta"}
btn_konsta3 = {"text":"Xudi_Konsta"}
btn_konsta33 = {"text":"Stikerlar_Konsta"}
btn_konsta4 = bosh_menu
replay_konsta_markub = {
    "keyboard":[
        [btn_konsta1,btn_konsta11],
        [btn_konsta2,btn_konsta22],
        [btn_konsta3,btn_konsta33],
        [btn_konsta4],
    ],
    "resize_keyboard":True
}
#Konsta -> Futbolka 
btn_konstfut1 = {"text":"Birgina pul bilan..."}
btn_konstfut11 = {"text":"Bugundanmi?"}
btn_konstfut2 = {"text":"Odamlar ucha olar!"}
btn_konstfut22 = {"text":"Orzularing o'zingnikimi?"}
btn_konstfut3 = {"text":"O'zgarmasa - noyobsan"}
btn_konstfut33 = {"text":"Haqiqat"}
btn_konstfut4 = {"text":"O'zingni qutqar!"}
btn_konstfut44 = {"text":"O'tkinchi dunyo"}
btn_konstfut5 = {"text":"Qabul qil o'zingni"}
btn_konstfut6 = {"text":"⬅️Ortga"}
btn_konstfut66 = {"text":"📥Savat"}

replay_konstafut = {
    "keyboard":[
        [btn_konstfut1,btn_konstfut11],
        [btn_konstfut2,btn_konstfut22],
        [btn_konstfut3,btn_konstfut33],
        [btn_konstfut4,btn_konstfut44],
        [btn_konstfut5],
        [btn_konstfut6,btn_konstfut66],
    ],
    "resize_keyboard":True,
}
#Konsta -> Svitshotlar
replay_konstasvitshot = {
    "keyboard":[
        [btn_konstfut4,btn_konstfut5],
        [btn_konstfut3,btn_konstfut44],
        [btn_konstfut33,btn_konstfut1],
        [btn_konstfut11,btn_konstfut2],
        [btn_konstfut22],
        [btn_konstfut6,btn_konstfut66],
        
    ],
    "resize_keyboard":True,
}
#Konsta -> Stikirlar
btn_konstastikir = {"text":"Sticker Pack №3"}
replay_konstastikir = {
    "keyboard":[
        [btn_konstastikir],
        [btn_konstfut6,btn_konstfut66],
    ],
    "resize_keyboard":True,
}
#Go Uz start 
btn_gouz1 = {"text":"⬅️Ortga"}
btn_gouz2 = {"text":"🚖 Buyurtma berish_Gouz"}
btn_gouz22 = {"text":"📥Savat_Gouz"}
btn_gouz3 = {"text":"Futbolkalar_Gouz"}
btn_gouz33 = {"text":"Svitshotlar_Gouz"}
btn_gouz4 = {"text":"Xudi_Gouz"}
btn_gouz5 = bosh_menu
replay_gouz_markub = {
    "keyboard":[
        [btn_gouz1],
        [btn_gouz2,btn_gouz22],
        [btn_gouz3,btn_gouz33],
        [btn_gouz4],
        [btn_gouz5],
    ],
    "resize_keyboard":True
}
# Svitshot start
btn_svit1 = {"text":"⬅️Ortga"}
btn_svit2 = {"text":"🚖 Buyurtma berish_svit"}
btn_svit22 = {"text":"📥Savat_svit"}
btn_svit3 = {"text":"Futbolkalar_svit"}
btn_svit33 = {"text":"Svitshotlar_svit"}
btn_svit4 = {"text":"Xudi_svit"}
btn_svit5 = bosh_menu
replay_svit_markub = {
    "keyboard":[
        [btn_svit1],
        [btn_svit2,btn_svit22],
        [btn_svit3,btn_svit33],
        [btn_svit4],
        [btn_svit5],
    ],
    "resize_keyboard":True
}

def main():
    get_updet_id = -1
    while True:
        get_updet_msg = get_updets(url)
        user = get_updet_msg['message']['from']
        if get_updet_msg['update_id']!=get_updet_id:
            if get_updet_msg['message']['text'] == "/start":
                send_message(url,user['id'],reply_markup=replay_markub,text=msg_start)
            #Bosh menu 
            if get_updet_msg['message']['text'] == bosh_menu['text']:
                send_message(url,user['id'],reply_markup=replay_markub,text=msg_start)
            elif get_updet_msg['message']['text'] == btn_bosh11['text']:
                send_message(url,user['id'],reply_markup=replay_markub,text="Sizning savatingiz bo'sh")
            elif get_updet_msg['message']['text'] == btn_bosh2['text']:
                hamkor_ms = """
                Biz sizning kompaniyangiz bilan hamkorlik qilishdan mamnunmiz va sizning buyurtmangizga asosan futbolkalar, xudi, svitshot va boshqa ko'p narsalarni tayyorlashimiz mumkin.

Menejer bilan bog'lanish uchun: @tirik_chilik    
                """
                send_message(url,user['id'],reply_markup=replay_markub,text=hamkor_ms)
            elif get_updet_msg['message']['text'] == btn_bosh22['text']:
                send_message(url,user['id'],reply_markup=replay_malumot,text="Kerakli bo'limni tanlang ⬇️")
            elif get_updet_msg['message']['text'] == mal1['text']:
                izoh_msg = """
                ✅ Tirikchilik loyihasini tanlaganingiz uchun rahmat.
Bizning xizmatlarimiz sifatini yaxshilashga yordam bersangiz juda xursand bo’lar edik :)
Buning uchun 5 ballik tizim asosida bizni baholang yoki o'z tilaklaringizni yozib jo'nating.
"""
                send_message(url,user['id'],reply_markup=replay_izoh,text=izoh_msg)
            #izoh qisim 
            elif get_updet_msg['message']['text'] == izoh1['text']:
                izohmsg1 = """Mamnun qolganingizdan xursandmiz 😊. Siz va yaqinlaringizni har doim xursand qilishga harakat qilamiz 🤗"""
                send_message(url,user['id'],reply_markup=replay_markub,text=izohmsg1)
            elif get_updet_msg['message']['text'] == izoh2['text']:
                izohmsg2 = """Sizga yoqqanidan xursandmiz 😊. Bot ishlashini yaxshilash uchun qanday maslahatlaringiz bor?👇🏻"""
                send_message(url,user['id'],reply_markup=replay_markub,text=izohmsg2)
            elif get_updet_msg['message']['text'] == izoh3['text']:
                izohmsg3 = """Botimiz sizni qoniqtirmaganidan afsusdamiz 😔. 
Bizni yaxshilashga yordam bering, 
sharh va takliflaringizni qoldiring👇🏻. 
Yaxshilashga harakat qilamiz🙏🏻."""
                send_message(url,user['id'],reply_markup=replay_markub,text=izohmsg3)
            elif get_updet_msg['message']['text'] == izoh4['text']:
                izohmsg4 = """Botimiz sizni qoniqtirmaganidan afsusdamiz 😔. Bizni yaxshilashga yordam bering, sharh va takliflaringizni qoldiring👇🏻. Yaxshilashga harakat qilamiz🙏🏻"""
                send_message(url,user['id'],reply_markup=replay_markub,text=izohmsg4)
            elif get_updet_msg['message']['text'] == izoh5['text']:
                izohmsg5 = """Botimiz sizni qoniqtirmaganidan afsusdamiz 😔. Bizni yaxshilashga yordam bering, sharh va takliflaringizni qoldiring👇🏻. Yaxshilashga harakat qilamiz🙏🏻"""
                send_message(url,user['id'],reply_markup=replay_markub,text=izohmsg5)
            #izoh qisim tugadi 
            #Yetkazib berish hizmati boshlandi
            elif get_updet_msg['message']['text'] == mal2['text']:
                yetkazish_msg = """Yetkazib berish shartlari:
O'zbekiston bo'ylab yetkazib berish 2-5 ish kuni ichida amalga oshiriladi. 
Toshkent bo'ylab yetkazib berish - 20 000 so'm.
O‘zbekiston bo'ylab yetkazib berish - 30 000 so‘m.

450 000 so'mdan ortiq buyurtmalarni yetkazib berish - tekin!"""
                send_message(url,user['id'],reply_markup=replay_malumot,text=yetkazish_msg)
            elif get_updet_msg['message']['text'] == mal22['text']:
                contact = send_contact(url,chat_id=user['id'],phone_number="+998938554640",first_name="Xakimov",last_name="Allamurod")
                send_message(url,user['id'],reply_markup=replay_malumot,text=contact)
            elif get_updet_msg['message']['text'] == btn_boshtil['text']:
                til_msg = """Iltimos, tilni tanlang
Пожалуйста, выберите язык ⬇️"""
                send_message(url,user['id'],reply_markup=inline_markub,text=til_msg)
            #end
            #Mahsulotni tanlash
            elif get_updet_msg['message']['text'] == btn_bosh1['text']:
                send_message(url,user['id'],reply_markup=replay_markup_asos,text="Bo'limni tanlang👇🏻")
            elif get_updet_msg['message']['text'] == btn1['text']:
                send_message(url,user['id'],reply_markup=replay_markup_asos,text="Sizning savatingiz bo'sh")
            
            elif get_updet_msg['message']['text'] == btn11['text']:
                send_message(url,user['id'],reply_markup=replay_markup_asos,text="Sizning savatingiz bo'sh")
            # Mahsulot -> Troll.uz start
            elif get_updet_msg['message']['text'] == btn2['text']:
                send_message(url,user['id'],reply_markup=replay_markub_trr,text="Bo'limni tanlang👇🏻")
            elif get_updet_msg['message']['text'] == btn_tr_buyurtma['text']:
                send_message(url,user['id'],reply_markup=replay_markub_trr,text="Sizning savatingiz bo'sh")
            elif get_updet_msg['message']['text'] == btn_tr_savat['text']:
                send_message(url,user['id'],reply_markup=replay_markub_trr,text="Sizning savatingiz bo'sh")
            # Mahsulot -> Troll.uz -> Futbolkalar start
            elif get_updet_msg['message']['text'] == btn_tr1['text']:
                send_message(url,user['id'],reply_markup=replay_markub_fut,text="Mahsulotni tanlang 👇🏻")
            #Mahsulot -> Troll.uz -> Futbolkalar -> btn_trfut1
            elif get_updet_msg['message']['text'] == btn_trfut1['text'] or get_updet_msg['message']['text'] == btn_trfut11['text'] or get_updet_msg['message']['text'] == btn_trfut2['text'] or get_updet_msg['message']['text'] == btn_trfut22['text'] or get_updet_msg['message']['text'] == btn_trfut3['text'] or get_updet_msg['message']['text'] == btn_trfut33['text'] or get_updet_msg['message']['text'] == btn_trfut4['text'] or get_updet_msg['message']['text'] == btn_trfut44['text'] or get_updet_msg['message']['text'] == btn_trfut5['text'] or get_updet_msg['message']['text'] == btn_trfut55['text'] or get_updet_msg['message']['text'] == btn_trfut6['text'] or get_updet_msg['message']['text'] == btn_trfut66['text'] or get_updet_msg['message']['text'] == btn_trfut7['text'] or get_updet_msg['message']['text'] == btn_trfut77['text'] or get_updet_msg['message']['text'] == btn_trfut8['text'] or get_updet_msg['message']['text'] == btn_trfut88['text'] or get_updet_msg['message']['text'] == btn_trfut9['text'] or get_updet_msg['message']['text'] == btn_trfut99['text']:
                rasm = "photo.jpg"
                msg_photo = """
                Don't be Sheep

So’kinishni xush ko’rmaydiganlar, ammo ichidagi gapni yumshoqroq aytmoqchi bo’lganlar uchun futbolka😌

Matosi: 100% o’zbek paxtasi

Qo'shimcha sovg'a sifatida  Stiсker Pack №1 beriladi :)

Narxi: 140 000 UZS
"""
                photo = send_photo(url,user['id'],photo=rasm,text=msg_photo)
                send_message(url,user['id'],reply_markup=replay_btntrfut_markub,text=photo)
            # oq rasm
            elif get_updet_msg['message']['text'] == btn_oq['text']:
                msg_photo = """
                Ajoyib tanlov! 

Endi o'lcham tanlang. Bizda standart o'lchamlar. "Malomerka" emas. Ya'ni M bu M, L bu L.
"""
                rasm = "photo_oq.jpg"
                photo = send_photo(url,user['id'],photo=rasm,text=msg_photo)
                send_message(url,user['id'],reply_markup=replay_markub_fut,text=photo)
            # qora rasm 
            elif get_updet_msg['message']['text'] == btn_qora['text']:
                rasm = "photo_qora.jpg"
                msg_photo = """
Ajoyib tanlov! 

Endi o'lcham tanlang. Bizda standart o'lchamlar. "Malomerka" emas. Ya'ni M bu M, L bu L.
"""
                photo = send_photo(url,user['id'],photo=rasm,text=msg_photo)
                send_message(url,user['id'],reply_markup=replay_markub_fut,text=photo)
            # Mahsulotlar -> Troll.uz -> Xuddi start
            elif get_updet_msg['message']['text'] == btn_tr11['text']:
                send_message(url,user['id'],reply_markup=replay_xuddi_markub,text="Mahsulotni tanlang 👇🏻")
            # Mahsulotlar -> Troll.uz -> Xuddi -> photo
            elif get_updet_msg['message']['text'] == btn_xuddi1['text'] or get_updet_msg['message']['text'] == btn_xuddi11['text'] or get_updet_msg['message']['text'] == btn_xuddi2['text'] or get_updet_msg['message']['text'] == btn_xuddi22['text'] or get_updet_msg['message']['text'] == btn_xuddi3['text'] or get_updet_msg['message']['text'] == btn_xuddi33['text'] or get_updet_msg['message']['text'] == btn_xuddi4['text'] or get_updet_msg['message']['text'] == btn_xuddi44['text'] or get_updet_msg['message']['text'] == btn_xuddi5['text']:
                xudi_msg = f"{btn_xuddi1}"
                xudi_msgs = """
Somsa

Somsani sevadiganlar uchun!

Matosi:
70% paxta
30% poliester
3 ipli (Трехнитка)

Stickerpack №1 sovg'a!

Narxi: 250 000 UZS
"""
                xudi_msg+=xudi_msgs
                rasm = "photo_xudi.jpg"
                photo = send_photo(url,user['id'],photo=rasm,text=xudi_msg)
                send_message(url,user['id'],reply_markup=replay_xuddi_markub,text=photo)
            #Mahsulotlar -> Trollar.uz -> Svitshotlar
            elif get_updet_msg['message']['text'] == btn_tr2['text']:
                send_message(url,user['id'],reply_markup=replay_svitshot_markub,text="Mahsulotni tanlang 👇🏻")
            #Trollar.uz -> Kepkalar
            elif get_updet_msg['message']['text'] == btn_tr22['text']:
                send_message(url,user['id'],reply_markup=replay_kepka_markub,text="Mahsulotni tanlang 👇🏻")
            #Trollar.uz -> Stikerlar
            elif get_updet_msg['message']['text'] == btn_tr3['text']:
                send_message(url,user['id'],reply_markup=replay_stiker_markup,text="Mahsulotni tanlang 👇🏻")
            #Trollar.uz -> Toplamlar
            elif get_updet_msg['message']['text'] == btn_tr33['text']:
                send_message(url,user['id'],reply_markup=replay_toplam_markub,text="Mahsulotni tanlang 👇🏻")
            #Temur Alixonov start
            elif get_updet_msg['message']['text'] == btn22['text']:
                send_message(url,user['id'],reply_markup=replay_temur_markub,text="Bo'limni tanlang👇🏻")
            #Temur Alixonov -> Buyurtma berish 
            elif get_updet_msg['message']['text'] == btn_temur2['text']:
                send_message(url,user['id'],reply_markup=replay_temur_markub,text="Sizning savatingiz bo'sh")
            #Temur Alixonov -> Savat 
            elif get_updet_msg['message']['text'] == btn_temur22['text']:
                send_message(url,user['id'],reply_markup=replay_temur_markub,text="Sizning savatingiz bo'sh")
            #Temur Alixonov -> Futbolkalar 
            elif get_updet_msg['message']['text'] == btn_temur3['text']:
                send_message(url,user['id'],reply_markup=replay_temurfut,text="Mahsulotni tanlang 👇🏻")
            #Temur Alixonov -> Xuddi
            elif get_updet_msg['message']['text'] == btn_temur33['text']:
                send_message(url,user['id'],reply_markup=replay_temurxudi,text="Mahsulotni tanlang 👇🏻")
            #Temur Alixonov -> Svitshotlar
            elif get_updet_msg['message']['text'] == btn_temur4['text']:
                send_message(url,user['id'],reply_markup=replay_temurxudi,text="Mahsulotni tanlang 👇🏻")
            #ЧЗХ -> start
            elif get_updet_msg['message']['text'] == btn3['text']:
                send_message(url,user['id'],reply_markup=replay_ЧЗХ_markub,text="Mahsulotni tanlang 👇🏻")
            #Konsta -> start
            elif get_updet_msg['message']['text'] == btn33['text']:
                send_message(url,user['id'],reply_markup=replay_konsta_markub,text="Bo'limni tanlang👇🏻")
            #Konsta -> Buyurtma 
            elif get_updet_msg['message']['text'] == btn_konsta1['text']:
                send_message(url,user['id'],reply_markup=replay_konsta_markub,text="Sizning savatingiz bo'sh")
            #Konsta -> Savat 
            elif get_updet_msg['message']['text'] == btn_konsta11['text']:
                send_message(url,user['id'],reply_markup=replay_konsta_markub,text="Sizning savatingiz bo'sh")
            #Konsta -> Futbolka 
            elif get_updet_msg['message']['text'] == btn_konsta2['text']:
                send_message(url,user['id'],reply_markup=replay_konstafut,text="Mahsulotni tanlang 👇🏻")
            #Konsta -> Svitshotlar 
            elif get_updet_msg['message']['text'] == btn_konsta22['text']:
                send_message(url,user['id'],reply_markup=replay_konstasvitshot,text="Mahsulotni tanlang 👇🏻")
            #Konsta -> Xudi 
            elif get_updet_msg['message']['text'] == btn_konsta3['text']:
                send_message(url,user['id'],reply_markup=replay_konstafut,text="Mahsulotni tanlang 👇🏻")
            #Konsta -> Stikirlar 
            elif get_updet_msg['message']['text'] == btn_konsta33['text']:
                send_message(url,user['id'],reply_markup=replay_konstastikir,text="Mahsulotni tanlang 👇🏻")
            # Go UZ start
            elif get_updet_msg['message']['text'] == btn4['text']:
                send_message(url,user['id'],reply_markup=replay_gouz_markub,text="Bo'limni tanlang👇🏻")
            #Svitshot start
            elif get_updet_msg['message']['text'] == btn44['text']:
                send_message(url,user['id'],reply_markup=replay_svit_markub,text="Bo'limni tanlang👇🏻")
            
            get_updet_id = get_updet_msg['update_id']
        sleep(0.3)
main()