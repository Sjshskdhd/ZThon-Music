#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯ ʑᴇʟᴢᴀʟ_ᴍᴜsɪᴄ ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯  T.me/ZThon   ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯ T.me/Zelzal_Music ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import InlineKeyboardButton, CallbackQuery, InlineKeyboardMarkup, Message
from typing import Union
from pyrogram.types import InlineKeyboardButton
from ZelzalMusic import app
from ZelzalMusic.misc import HAPP, SUDOERS, XCB
from config import OWNER_ID
                                       
                                       
@app.on_callback_query(filters.regex("zzzback"))
async def mpdtsf(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""<b>» مرحبـاً عـزيـزي</b>\n<b>- استخـدم الازرار بالاسفـل لـ تصفـح اوامـر الميـوزك 🥁</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• اوامــر التشغيــل •", callback_data="zzzll"),
                ],[
                    InlineKeyboardButton(
                        "• اوامـر القنـاة •", callback_data="zzzch"),
                    InlineKeyboardButton(
                        "• اوامـر الادمـن •", callback_data="zzzad"),
                ],[
                    InlineKeyboardButton(
                        "• اوامــر المطــور •", callback_data="zzzdv"),
                ],[
                    InlineKeyboardButton(
                        "• قنــاة الســورس •", url="https://t.me/Zelzal_Music"),
                ],
            ]
        ),
    )





@app.on_callback_query(filters.regex("zzzll"))
async def elkatob(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""ٴ<b>•────‌‌‏✯ ʑ_ᴍᴜsɪᴄ ✯──‌‌‏─‌‌‏─•</b>
<b>- قائمــة اوامــر التشغيــل ✅ :</b>
ٴ<b>•────‌‌‏✯ ʑ_ᴍᴜsɪᴄ ✯──‌‌‏─‌‌‏─•</b>
تشغيل + اسم الاغنية
<b>- لــ تـشـغـيل اغـنـيـة فـي الـمكـالـمـة الـصـوتـيـة</b>
فيديو + اسم المقـطـع
<b>- لــ تـشـغـيل فيـديـو فـي الـمكـالـمـة المـرئيـة</b>
ايقاف / انهاء / اسكت
<b>- لـ إيقـاف تـشغـيـل الـمـوسـيـقـى فـي المكـالمـة</b>
وقف / توقف
<b>- لـ إيقـاف تشغيـل الموسيـقـى فـي المكالمـة مـؤقتـاً</b>
كمل / كملي
<b>- لـ إسـتـئـنـاف تـشغـيـل الـمـوسـيـقـى فـي المكـالمـة</b>
تخطي
<b>- لـ تخطـي الاغنيـة وتشغيـل الاغنيـة التاليـه</b>
ريستارت
<b>- لـ إعـادة تشغيـل البـوت</b>
بحث + الاسـم
<b>- لـ تحميـل الاغانـي والمقـاطـع الصوتيـه مـن اليوتيـوب</b>
الاغاني
<b>- لـ معـرفـة الاغـانـي المـوجـودة فـي قائمـة الانتظـار</b>
بنج
<b>- لـ عـرض سـرعـة تشغيـل البـوت</b>
ٴ<b>•────‌‌‏✯ ʑ_ᴍᴜsɪᴄ ✯──‌‌‏─‌‌‏─•</b>""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="zzzback"),
               ],
          ]
        ),
    )




@app.on_callback_query(filters.regex("zzzad"))
async def zzzad(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""ٴ<b>•────‌‌‏✯ ʑ_ᴍᴜsɪᴄ ✯──‌‌‏─‌‌‏─•</b>
<b>- قائمــة اوامــر الادمــن ✅ :</b>
ٴ<b>•────‌‌‏✯ ʑ_ᴍᴜsɪᴄ ✯──‌‌‏─‌‌‏─•</b>
بنج
<b>- لـ عـرض سـرعـة تشغيـل البـوت</b>
الاعدادات
<b>- لـ عـرض اعـدادات البــوت</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<b>- قائمــة اوامــر الـرتب ✅ :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
رفع ادمن
<b>- لـ رفـع شخـص ادمـن فـي البـوت</b>
تنزيل ادمن
<b>- لــ تـنزيل شخـص مـن قائمـة ادمنيـة البـوت</b>
الادمنيه
<b>- لـ عـرض قائمـة ادمنيـة البـوت</b>
ٴ<b>•────‌‌‏✯ ʑ_ᴍᴜsɪᴄ ✯──‌‌‏─‌‌‏─•</b>""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="zzzback"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzch"))
async def zzzch(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""ٴ<b>•────‌‌‏✯ ʑ_ᴍᴜsɪᴄ ✯──‌‌‏─‌‌‏─•</b>
<b>- قائمــة اوامــر التشغيــل فـي القنــاة ✅ :</b>
ٴ<b>•────‌‌‏✯ ʑ_ᴍᴜsɪᴄ ✯──‌‌‏─‌‌‏─•</b>
<b>- ارفـع البـوت إشـراف في القنـاة و شغـل مباشـر</b>
<b>- ارسـل (/channelplay او ربط) + يـوزر القنـاة لـ الربـط</b>
<b>- ثم استخـدم الاوامــر بالاسفـل لـ التشغيـل</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
تشغيل + اسم الاغنية
<b>- لــ تـشـغـيل اغـنـيـة فـي الـمكـالـمـة الـصـوتـيـة</b>
فيديو + اسم المقـطـع
<b>- لــ تـشـغـيل فيـديـو فـي الـمكـالـمـة المـرئيـة</b>
ايقاف / انهاء / اسكت
<b>- لـ إيقـاف تـشغـيـل الـمـوسـيـقـى فـي المكـالمـة</b>
وقف / توقف
<b>- لـ إيقـاف تشغيـل الموسيـقـى فـي المكالمـة مـؤقتـاً</b>
كمل / استئناف
<b>- لـ إسـتـئـنـاف تـشغـيـل الـمـوسـيـقـى فـي المكـالمـة</b>
تخطي
<b>- لـ تخطـي الاغنيـة وتشغيـل الاغنيـة التاليـه</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
/seek + عـدد الثـوانـي
<b>- لـ تقديـم الاغنيـه لـ الامـام</b>
/seekback + عـدد الثـوانـي
<b>- لـ إرجـاع الاغنيـه لـ الخـلف</b>
ٴ<b>•────‌‌‏✯ ʑ_ᴍᴜsɪᴄ ✯──‌‌‏─‌‌‏─•</b>""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="zzzback"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzdv") & SUDOERS)
async def zzzad(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""ٴ<b>•────‌‌‏✯ ʑ_ᴍᴜsɪᴄ ✯──‌‌‏─‌‌‏─•</b>
<b>- قائمــة اوامــر المطــور ✅ :</b>
ٴ<b>•────‌‌‏✯ ʑ_ᴍᴜsɪᴄ ✯──‌‌‏─‌‌‏─•</b>
السجل تفعيل/تعطيل
<b>- لـ تفعيـل/تعطيـل اشعـارات مجموعـة سجـل البــوت</b>
حدث/ريستارت
<b>- لـ تحديـث/اعـادة تشغيـل البــوت</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<b>- قائمــة اوامــر الـرفــع & الحظــر ✅ :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
اضف مطور/تنزيل مطور
<b>- لـ رفـع/تنزيـل شخـص مطـور فـي ميـوزك البـوت</b>
المطورين
<b>- لـ عـرض قائمـة مطـورين البـوت</b>
بلوك/الغاء بلوك/المبلكين
<b>- لـ حظـر/الغـاء حظـر شخـص من استخـدام ميـوزك البـوت</b>
احظره عام/الغاء حظره عام
<b>- لـ حظـر/الغـاء حظـر شخـص من استخـدام ميـوزك البـوت عـام</b>
المحظورين عام
<b>- لـ جلب قائمـة المحظـورين عـام فـي البـوت</b>
حظر مجموعة/سماح
<b>- لـ حظـر/الغـاء حظـر مجموعـة من استخـدام ميـوزك البـوت</b>
المجموعات المحظورة
<b>- لـ جلب قائمـة بالمجمـوعـات المحظـورة مـن استـخـدام البـوت</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<b>- قائمــة اوامــر المســاعــد ✅ :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
المغادره التلقائيه تفعيل/تعطيل
<b>- لـ تفعيـل/تعطيـل المغـادره التلقائيـه لـ الحسـاب المسـاعـد مـن المجمـوعـات عنـد عـدم استـخـدام الميـوزك</b>
ٴ<b>•────‌‌‏✯ ʑ_ᴍᴜsɪᴄ ✯──‌‌‏─‌‌‏─•</b>""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="zzzback"),
               ],
          ]
        ),
    )