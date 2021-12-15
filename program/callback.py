# Copyright (C) 2021 By VeezMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Salam [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) Bot Telegram Qruplarda Səsli Söhbətdə Musiqi və Video Oynatmağa imkan verir\n\n🎧 Səslidə Musiqi Üçün /oynat'yazın 🎥 Video Üçün /vplay'yazın **

💡 **Əmrlər düyməsini klikləməklə Botun bütün əmrlərini və onların necə işlədiyini öyrənin!**

🔖 **Bu botdan necə istifadə edəcəyinizi bilmək üçün, lütfən, » ❓ Qurulum düyməsinə basın!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Qurupa əlavə et ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("❓ Qurulum", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("📚 Əmirlər", callback_data="cbcmds"),
                    InlineKeyboardButton("👨🏻‍💻 Sahibim", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "💭 Söhbət Group", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "🌐 Support", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "🎵 Musiqi Kanalı", url="https://t.me/BS_Kanall"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **Qurulum haqqında məlumat:**

1.) **Birinci, məni qrupunuza əlavə edin.**
2.) Sonra məni administrator kimi yüksəldin və Anonim Admindən başqa bütün icazələri verin.**
3.) **Məni təbliğ etdikdən sonra admin məlumatlarını yeniləmək üçün qrupa /yenile yazın.**
4.) **Əlavə et @{ASSISTANT_NAME} qrupunuza /userbotjoin onu dəvət etmək.**
5.) **Video/musiqi oynatmağa başlamazdan əvvəl video söhbəti yandırın.**
6.) **Bəzən /yenile əmrindən istifadə edərək botu yenidən yükləmək bəzi problemləri həll etməyə kömək edə bilər.**

📌 **İstifadəçi robotu video çata qoşulmayıbsa, video çatın artıq aktiv olub olmadığına əmin olun və ya /userbotleave yazın, sonra yenidən /userbotjoin yazın..**

💡 **Bu bot haqqında əlavə suallarınız varsa, onu buradakı dəstək söhbətimdə deyə bilərsiniz: @{GROUP_SUPPORT}**

⚡ __𝐍 𝐄 𝐗 𝐔 𝐒 {BOT_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Geri", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Salam [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» **izahatı oxumaq və mövcud əmrlərin siyahısına baxmaq üçün aşağıdakı düyməni basın! !**

⚡ __𝐍 𝐄 𝐗 𝐔 𝐒 {BOT_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷🏻 Admin əmirləri", callback_data="cbadmin"),
                    InlineKeyboardButton("🧙🏻 Sudo əmirləri", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("📚 İstifadəçi əmirləri", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("🔙 Geri", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the basic commands:

» oynat - <mahnı adı> - istədiyiniz mahnını çalın
» /vplay - <video adı> - istədiyiniz video çalın
» /vstream - youtube live/m3u8-dən canlı video oynayın
» /playlist - show you the playlist
» /video (sorğu) - youtube-dan videonu endir
» /bul - <mahnı adı> - istədiyiniz mahnıları tez tapın
» /lyric (sorğu) - mahnının sözlərini sil
» /search (sorğu) - youtube video linkini axtarın

» /ping - bot ping statusunu göstərin
» /uptime - botun işləmə müddətini göstərin
» /alive - botun canlı məlumatını göstərin (qrupda)

⚡️ __𝐍 𝐄 𝐗 𝐔 𝐒 {BOT_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Geri", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the admin commands:

» /dur  - mahnının səsləndirilməsini dayandırın
» /devam - mahnı oxumağa davam edin
» /atla  - növbəti mahnıya keçid edin
» /bitir  - musiqi çalmağı dayandırın
» /vmute - səsli söhbətdə istifadəçi robotunun səsini söndürün
» /vunmute - səsli söhbətdə istifadəçi robotunun səsini açın
» /volume `1-200` - musiqinin səsini tənzimləyin (userbot admin olmalıdır)
» /yenile - botu yenidən yükləyin və admin məlumatlarını təzələyin
» /userbotjoin - istifadəçi robotunu qrupa qoşulmağa dəvət edin
» /userbotleave - userbot-a qrupdan çıxmağı əmr edin

⚡️ __𝐍 𝐄 𝐗 𝐔 𝐒 {BOT_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Geri", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the sudo commands:

» /rmw - bütün xam faylları təmizləyin
» /rmd - bütün yüklənmiş faylları təmizləyin
» /sysinfo - sistem məlumatlarını göstərin
» /update - botunuzu ən son versiyaya yeniləyin
» /yenile - botunuzu yenidən başladın
» /leaveall - userbotun bütün qrupdan çıxmasını əmr edin

⚡ __𝐍 𝐄 𝐗 𝐔 𝐒 {BOT_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Geri", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **Ayarlar** {query.message.chat.title}\n\n⏸ : Durdu\n▶️ : Başladı\n🔇 : mute userbot\n🔊 : unmute userbot\n⏹ : Sonlandı",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("⏹", callback_data="cbstop"),
                      InlineKeyboardButton("⏸", callback_data="cbpause"),
                      InlineKeyboardButton("▶️", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("🗑 Bağla", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("❌ hazırda heç nə yayımlanmır", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    await query.message.delete()
