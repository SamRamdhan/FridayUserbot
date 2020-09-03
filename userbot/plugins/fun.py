from telethon import events
import random, re
from uniborg.util import admin_cmd

METOOSTR = [
    "`Cobalah berkaca, maka kamu akan tau arti segalanya bagiku.`",
    "`Izinkan aku menyebut doamu didalam doaku kepada Tuhan untuk kuminta sebagai jodohku.`",
    "`Aku benci ketika harus berbohong bahwa aku tidak mencintaimu.`",
    "`Walaupun ditawari seluruh bidadari surga untuk menemaniku, aku menolak. Aku hanya ingin kamu.`",
    "`Taukah pelangi yang sering kupandangi ketika hujan reda? Ia malu menampakkan diri lagi ketika kuceritakan bahwa cantikmu melebihi keindahannya.`",
    "`Ikan hiu sedang laper, i lop yu poreper. Wkwkwk`",
    "`Soekarno berkata : Berikan aku 10 pemuda maka akan kugoncangkan dunia. Kalau aku cuma butuh kamu menemaniku, maka akan kubuat 10 pemuda.`",
]
RUNSREACTS = [
    "`Apa? Kamu ingin aku berpuisi? Bukankah kamulah seindah-indahnya puisi itu?`",
    "`Sebenarnya aku tak pandai merangkai aksara, hanya saja ketika itu soal dirimu, apapun terasa begitu indah dan bermakna`",
    "`Demikianlah realitanya. Temu tak pernah terjadi, namun perasaanku nyata mengagumi wujudmu`",
    "`Jika kamu ibarat bunga, Aku akan menjadi pot sebagai wadah tempatmu tumbuh menjadi indah`",
    "`Apa kamu sering merasa kesemutan? Mungkin itu karena kamu terlalu manis`",
    "`Bolehkah aku memandangi wujud sempurna dirimu? Aku hanya ingin melihat betapa indahnya masa depanku`",
    "`Ya, memang benar kalau didekatmu adalah candu. Sehari saja tak bersamamu, rasanya aku seperti ingin mati karena overdosis rindu.`",
    "`Terseyumlah, rekah rona bibirmu begitu membuat hati semakin bergairah. Terseyumlah, hanya kamu, satu selain Tuhan yang mampu membuatku kagum. `",
    "`Semoga aku bisa menulis seindah wujudmu. Aku memang pengagum puisi. Penyuka hal-hal indah. Berbait-bait kata indah sering ku baca. Namun, tahukah kamu kata yang paling indah menurutku? Namamu!`",
    "`Jika mencintaimu adalah sesuatu yang melanggar hukum, Aku mungkin sudah jadi terpidana dengan hukuman paling lama`",
]
RAPE_STRINGS = [
     "`Hei, sibuk gak? Bantu aku cari sesuatu dong. Aku lagi nyari kekurangan kamu`",
     "`Kamu atlit lari yah? Kok sering banget lari-lari dipikiranku.`",
     "`Kamu punya keahlian lain gak sih selain membuat aku jatuh cinta? `",
     "`Aku tadi mau beli bunga buat kamu, kata penjualnya gausah, takut bunganya layu gara-gara malu kalah cantik`",
     "`AKU SAYANG KAMU! Pasti bacanya sambil ngegas yah? haha 😆`",
     "`Ukuran kakimu berapa? Aku mau tau aja berapa ukuran surga anak-anakku`",
] 
ABUSE_STRINGS = [
       "`Diam`",
	   "`Yaudah`",
	   "`Chutiya he rah jaye ga`",
	   "`Ja be Gaandu`",
	   "`Ma ka Bhodsa madharchod`",
	   "`mml`",
	   "`You MotherFukcer`",
	   "`Muh Me Lega Bhosdike ?`"
]
GEY_STRINGS = [
     "`dihh gajelas`",
     "`dih apaan sih`",
     "`dih bacot`",
     "`dih alay`",
     "`dih dih dih dih dih`",
     "`dih yaudah`",
]
PRO_STRINGS = [
     "`Iya bang jago.`",
     "`Jagoan datang-_- Waktunya pergi`",
]
INSULT_STRINGS = [ 
    "`Jangan khawatir soal virus yang menyerang otak... kamu kan gapunya otak.`",
    "`Jika ada perlombaan manusia paling bodoh, kamu pasti selalu terpilih jadi juara 1.`",
    "`Cobalah untuk tahan nafas selama 2 jam. Setelah itu kamu bisa menahannya selamanya.`",
    "`Kamu tau apa yang lebih kecil dari atom? Yaitu kemungkinanmu masuk surga.`",
    "`Ego mu terlalu tinggi, tak seperti IQ mu.`",
    "`Jangan percaya ketika orang mengatakan kamu hebat. Itu hoax.`",
    "`Bisa minta tolong? Bantu saya menemukan otakmu.`",
    "`Kelakuanmu memang pantas untuk menjadi penghuni kekal neraka jahannam.`",
    "`Omonganmu sama seperti otakmu, kosong!`",
    "`Kamu ini bicara apa? Terdengar seperti omong kosong.`",
    "`Ada pistol didekatmu, ambillah dan tembak kepalamu sendiri.`",
    "`Tetap putus asa dan jangan semangat.`",
    "`Sebagai makhluk asing, bagaimana tanggapan kamu tentang peradaban manusia?`",
    "`Kamu memang sangat luar biasa, dalam melakukan hal-hal bodoh.`",
    "`Ya teruslah berusaha, suatu hari kamu pasti bisa kaya raya!.......(tapi boong)`",
    "`Bersyukurlah, tidak semua orang bisa sebodoh dirimu.`",
    "`Kamu ini seperti pisang, punya jantung tapi tak punya hati .`",
    "`Kamu butuh tidur, selamanya.`",
    "`Wowww katanya ada nama kamu dalam daftar penghuni abadi neraka.`",
    "`Berbahagialah, sebentar lagi gebetanmu akan datang ke rumahmu, untuk mengundangmu datang ke pesta pernikahan dia bersama kekasihnya`",
    "`Tarik nafas kemudian tahan sampai besok.`",
    "`Go Green! Jangan hisap oksigen lagi.`",
    "`Cobalah ketik cara menemukan otakmu di google, pasti sia-sia saja karena tidak ada hasil.`",
    "`Kekuranganmu cuma satu, yaitu tidak punya kelebihan.`",
    "`Cobalah menyebrang jalan tol sambil bernyanyi lagu favoritmu.`",
    "`Coba berdiri di samping monyet itu, mirip kan kamu?`",
    "`Artis idolamu mengajak bertemu, kamu akan dijadikan tumbal pesugihan.`",
    "`Tidak ada manusia yang bisa bernafas melalu mulut ketika lidahnya dijulurkan keluar, kecuali kamu. Cobalah!`",
    "`Aku benci melihat kamu menangis, wajahmu sangat buruk ketika menangis!.`",
]
# ===========================================
                          

@borg.on(admin_cmd(pattern="sajak ?(.*)"))
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(RUNSREACTS) - 1)    
    input_str = event.pattern_match.group(1)
    reply_text = RUNSREACTS[bro]
    await event.edit(reply_text)


@borg.on(admin_cmd(pattern="gombal ?(.*)"))
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(METOOSTR) - 1)    
    input_str = event.pattern_match.group(1)
    reply_text = METOOSTR[bro]
    await event.edit(reply_text)


@borg.on(admin_cmd(pattern="rayu ?(.*)"))
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(RAPE_STRINGS) - 1)    
    input_str = event.pattern_match.group(1)
    reply_text = RAPE_STRINGS[bro]
    await event.edit(reply_text)
			  
                          
@borg.on(admin_cmd(pattern="insultt ?(.*)"))
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(INSULT_STRINGS) - 1)    
    input_str = event.pattern_match.group(1)
    reply_text = INSULT_STRINGS[bro]
    await event.edit(reply_text)
			  
			  
@borg.on(admin_cmd(pattern="proo ?(.*)"))
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(PRO_STRINGS) - 1)    
    input_str = event.pattern_match.group(1)
    reply_text = PRO_STRINGS[bro]
    await event.edit(reply_text)
			  
			  
@borg.on(admin_cmd(pattern="abusee ?(.*)"))
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(ABUSE_STRINGS) - 1)    
    input_str = event.pattern_match.group(1)
    reply_text = ABUSE_STRINGS[bro]
    await event.edit(reply_text)
			  
			  
@borg.on(admin_cmd(pattern="dih ?(.*)"))
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(GEY_STRINGS) - 1)    
    input_str = event.pattern_match.group(1)
    reply_text = GEY_STRINGS[bro]
    await event.edit(reply_text) 
