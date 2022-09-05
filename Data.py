from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hai {}

Selamat Datang di {}

Saya dapat mengonversi GIF dan Video ke Stiker Video dan membuat Paket Stiker khusus untuk Anda! Gunakan tombol di bawah untuk mempelajari lebih lanjut.

Oleh @mr_theherd
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("✨ Status Bot✨", url="https://t.me/MH_Projects/10")],
        [InlineKeyboardButton(text="🏠 Kembali 🏠", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("✨ Status Bot✨", url="https://t.me/MH_Projects/10")
        ],
        [
            InlineKeyboardButton("Cara Penggunaan ❔", callback_data="help"),
            InlineKeyboardButton("🎪 Tentang 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ DONASI ♥", url="https://trakteer.id/mhpay/tip")],
        [InlineKeyboardButton("🎨 Customer Service 🎨", url="https://t.me/mr_theherd")],
    ]

    # Help Message
    HELP = """
Saya dapat mengonversi GIF dan Video ke Stiker Video. Kirimkan saja stikernya dan saya akan melakukan sisanya untuk Anda. Anda akan mendapatkan paket Anda segera setelah Anda menambahkan stiker. Kirim lebih banyak gif/video untuk menambahkan stiker dalam paket saat ini.

Fitur
1) Paket stiker video yang dipersonalisasi
2) Beberapa paket stiker video
3) Video ke WEBM
4) Konversi otomatis Stiker Video ke WEBM
5) Emoji Stiker yang Dapat Disesuaikan
6) Dapatkan daftar paket menggunakan /packs
7) Pengaturan 

**Catatan:**
1) Cobalah untuk mengirim video/gif sekecil mungkin hanya dalam 3 detik pertama!
2) Jangan mencoba untuk peduli dengan audio karena audio juga tidak masalah! GIF yang sama dan Video yang sama tanpa audio akan memberikan hasil yang sama
3) 'Minta emoji' di /settings menimpa 'Emoji Khusus'


✨**Available Commands**✨

/settings - Konfigurasikan pengaturan bot pribadi. 
/packs - Dapatkan Daftar Paket Anda 
/start - Mulai bot 
/help - Bagaimana cara menggunakan botnya? 
/about - Tentang bot 
/id - Dapatkan ID Telegram Anda
    """

    # About Message
    ABOUT = """
**Tentang Bot Ini** 

Bot dibuat oleh @mr_theherd

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @MH_Projects
    """