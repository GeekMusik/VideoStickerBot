from pyrogram import emoji
from database import database
from pystark import Stark, Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@Stark.cmd('settings', description='Configure personal bot settings.', private_only=True)
async def settings(_, msg: Message):
    text, markup = await user_settings(msg.from_user.id)
    await msg.react(text, reply_markup=markup)


async def user_settings(user_id):
    data = await database.get('users', user_id)
    if not data:
        return False, False
    tick = ' ✔'
    cross = ' ✖️ '
    ask_emojis = "Minta Emoji"
    ask_emojis_msg = f"Setel ke True jika Anda ingin bot meminta emoji yang akan disetel ke stiker video sambil menambahkan ke paket. Jika disetel ke Salah, semua stiker akan menggunakan emoji default, yaitu - {emoji.RED_HEART}"
    get_webm = "Mendapatkan WEBM"
    get_webm_msg = f"Setel ke True jika Anda ingin mendapatkan file webm saat Anda mengirim stiker video yang ada. Dengan cara ini, Anda dapat menambahkan stiker dari paket orang lain menggunakan @mr_theherd. Jika False, bot akan mengabaikan stiker."
    kang_mode = "Kang Mode"
    kang_mode_msg = "Setel ke True jika Anda ingin menambahkan stiker ke paket Anda hanya dengan mengirim stiker video dari beberapa paket yang ada. Dengan cara ini, Anda dapat menambahkan stiker dari paket orang lain ke paket Anda. Jika False, bot akan "
    default_emojis = "Emoji bawaan"
    default_emojis_msg = f"Setel emoji default untuk digunakan di stiker Anda. Jika tidak ada yang diatur, {emoji.RED_HEART} akan digunakan."
    text = f'**Settings** \n\n'
    ask_emojis_db = data['ask_emojis']
    get_webm_db = data['get_webm']
    kang_mode_db = data['kang_mode']
    default_emojis_db = data['default_emojis']
    general_text = "**{}** : {} \n{} \n\n"
    if ask_emojis_db:
        text += general_text.format(ask_emojis, 'True', ask_emojis_msg)
        ask_emojis += tick
    else:
        text += general_text.format(ask_emojis, 'False', ask_emojis_msg)
        ask_emojis += cross
    if get_webm_db:
        text += general_text.format(get_webm, 'True', get_webm_msg)
        get_webm += tick
    else:
        text += general_text.format(get_webm, 'False', get_webm_msg)
        get_webm += cross
    if kang_mode_db:
        text += general_text.format(kang_mode, 'True', kang_mode_msg)
        kang_mode += tick
    else:
        text += general_text.format(kang_mode, 'False', kang_mode_msg)
        kang_mode += cross
    if default_emojis_db:
        text += general_text.format(default_emojis, default_emojis_db, default_emojis_msg)
        default_emojis += ' - SET'
    else:
        text += general_text.format(default_emojis, 'Not Set', default_emojis_msg)
        default_emojis += ' - NOT SET'
    text += 'Use below buttons to change values. A tick means True and cross means False'
    markup = InlineKeyboardMarkup([
        [InlineKeyboardButton(ask_emojis, callback_data="emojis")],
        [InlineKeyboardButton(default_emojis, callback_data="default_emojis")],
        [InlineKeyboardButton(kang_mode, callback_data="kang_mode")],
        [InlineKeyboardButton(get_webm, callback_data="webm")],
    ])
    return text, markup


async def default_emojis_settings(user_id):
    data = await database.get('users', user_id)
    if not data:
        return False, False
    data = data['default_emojis']
    if data:
        markup = InlineKeyboardMarkup([
            [InlineKeyboardButton('Ubah Emoji', callback_data="change_default_emojis")],
            [InlineKeyboardButton('Hapus Emoji Default', callback_data="remove_default_emojis")],
            [InlineKeyboardButton('<-- Kembali', callback_data="back")],
        ])
        text = f'Emoji Default saat ini adalah `{data}` \n\nGunakan tombol di bawah ini untuk mengubah atau menghapusnya'
    else:
        markup = InlineKeyboardMarkup([
            [InlineKeyboardButton('Tambahkan Emoji', callback_data="change_default_emojis")],
            [InlineKeyboardButton('<-- Kembali', callback_data="back")],
        ])
        text = 'Saat ini tidak ada Emoji yang disetel. Gunakan tombol di bawah ini untuk menambahkannya.'
    return text, markup
