import os
# from dotenv import load_dotenv

# load_dotenv()


class Config(object):
    API_ID = int(os.getenv("API_ID", "15316095"))
    API_HASH = os.getenv("API_HASH", "6a293d116082b81260ac83d21f595ffa")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "5928413945:AAEoToTPUf0KQhjkdmRT3WUMhAN6saPbr2w")
    BOT_SESSION_NAME = os.getenv("BOT_SESSION_NAME", "MdiskSearch")
    USER_SESSION_STRING = os.getenv("USER_SESSION_STRING", "1BVtsOLoBu2Fv41wKRFGAqMGVJXBFA_S2GeKDTc0H5dexX6hLZvlcvkk04-SJC7N_vKzHGwtySQkbQC2FOakqF9xxYMocARJu31HVjIHJ5dG3e1Q6MjakqFlAIYXljkUG0kgEAIRdnzABY84ZEVUN-VX0SG_uX7xbyUOS_GtBxiPpoqO0p7G-BWs4vxjbInkr3j3tyj8JREk5xEKCLFykcQLJDQ2wCSGNiEqNNYl4WHbI4lFGBco4HKbzNRrPswHFAVZPPT-mnYdXsTMCNttU2UF1eALp__oPq9ffZA02VwNBkUR7G8NAGMnxsDsRHCWrwVmhiv31JrDYvxShRismgKC12MRMVVM=")
    CHANNEL_ID = int(os.getenv("CHANNEL_ID", "-1001831347923")) 
    BOT_USERNAME = os.getenv("BOT_USERNAME", "Mdisc_search_bot")
    BOT_OWNER = int(os.getenv("BOT_OWNER", "5047601096"))
#    OWNER_USERNAME = os.getenv("OWNER_USERNAME", "Beastonejnanesh")
    BACKUP_CHANNEL = os.getenv("BACKUP_CHANNEL", "ROCKERSBACKUP")
#    GROUP_USERNAME = os.getenv("GROUP_USERNAME")
    START_MSG = os.getenv("START_MSG", """**𝐇𝐞𝐲 {}, 

𝐈 𝐚𝐦 𝐚𝐮𝐭𝐨 𝐌𝐝𝐢𝐬𝐜 𝐥𝐢𝐧𝐤 𝐬𝐞𝐚𝐫𝐜𝐡 𝐛𝐨𝐭

𝐉𝐮𝐬𝐭 𝐚𝐝𝐝 𝐦𝐞 𝐭𝐨 𝐮 𝐫 𝐠𝐫𝐨𝐮𝐩

𝐔 𝐜𝐚𝐧 𝐚𝐥𝐬𝐨 𝐞𝐚𝐫𝐧 𝐦𝐨𝐧𝐞𝐲 💰 𝐭𝐡𝐫𝐨𝐮𝐠𝐡 𝐦𝐲 𝐛𝐨𝐭

message here @Beastonejnanesh**""" ) 
    START_PHOTO = os.getenv("START_PHOTO", "https://te.legra.ph/file/8dc3715008f6cf89930bc.jpg")
    HOME_TEXT = os.getenv("HOME_TEXT", """ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕

ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴛʜᴇʀᴇ ʏᴏᴜʀ ʟɪɴᴋꜱ.

ꜰᴏʀ ᴍᴏʀᴇ ɪɴꜰᴏ ᴄʟɪᴄᴋ ᴏɴ ʜᴇʟᴘ ✅""" )
    UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", "-1001219225979")
    DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://jnanesh:jnanesh@cluster0.8pzxa6s.mongodb.net/?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1001230076027"))
    RESULTS_COUNT = int(os.getenv("RESULTS_COUNT", 20))
    BROADCAST_AS_COPY = os.getenv("BROADCAST_AS_COPY", "True")
    UPDATES_CHANNEL_USERNAME = os.getenv("UPDATES_CHANNEL_USERNAME", "ROCKERSBACKUP1")
    FORCE_SUB = os.getenv("FORCE_SUB", "True")
    AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", 60))
    MDISK_API = os.getenv("MDISK_API", "nx7N3INpOrexpfSHYnp7")
    VERIFIED_TIME  = int(os.getenv("VERIFIED_TIME", "31"))
    ABOUT_BOT_TEXT = os.getenv("ABOUT_TEXT", """𝐈 ᴏɴʟʏ ꜱʜᴀʀᴇ ᴛʜᴇ ᴘᴏꜱᴛ ꜰʀᴏᴍ ᴘᴇᴏᴘʟᴇ'ꜱ ᴄʜᴀɴɴᴇʟ! 

ᴡʜᴏ ᴍᴀᴅᴇ ᴍᴇ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ, 

𝐢 ɴᴏᴛ ꜱᴛᴏʀᴇ ᴀɴʏ ꜰɪʟᴇꜱ ᴏʀ ᴛᴇ𝐱ᴛ ɪɴ  ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ.

ᴅᴍ ꜰᴏʀ ᴀɴʏ 𝐐ᴜᴇʀʏ @Beastonejnanesh """ )
    ABOUT_WATCH_TEXT = """
ʜᴇʏ ʙᴜᴅᴅʏ, 

ᴍᴅɪsᴋ - ᴀɢᴀʀ ᴀᴘᴋᴏ ɴᴀʜɪ ᴘᴀᴛᴀ ᴋɪ ᴍᴅɪsᴋ ʟɪɴᴋ sᴇ ᴍᴏᴠɪᴇ ᴋᴀɪsᴇ ᴅᴇᴋʜᴇ ᴛᴏ ɴɪᴄᴇ ᴅɪʏᴇ ɢᴀʏᴇ ᴍᴅɪsᴋ ᴡᴀʟᴇ ʙᴜᴛᴛᴏɴ ᴘᴀʀ ᴄʟɪᴄᴋ ᴋᴀʀᴇ 


ᴛᴇʀᴀ ʙᴏx - ᴀɢᴀʀ ᴀᴘᴘᴋᴏ ɴᴀʜɪ ᴘᴀᴛᴀ ᴋɪ ᴛᴇʀᴀʙᴏx sᴇ ᴍᴏᴠɪᴇs ᴋᴀɪsᴇ ᴅᴇᴋʜᴇ ᴛᴏ ɴɪᴄʜᴇ ᴅɪʏᴇ ɢᴀʏᴇ ᴛᴇʀᴀ ʙᴏx ʙᴜᴛᴛᴏɴ ᴘᴀʀ ᴄʟɪᴄᴋ ᴋᴀʀᴇ

ʀᴇɢᴀʀᴅs - @Beastonejnanesh"""
    ABOUT_MDISK_TEXT = """
 how to open mdisk link https://t.me/+Rf7HPykmLC5hOWQ9"""

    ABOUT_HELP_TEXT = """

💎 𝐇𝐨𝐰 𝐭𝐨 𝐞𝐚𝐫𝐧 𝐦𝐨𝐧𝐞𝐲 𝐮𝐬𝐢𝐧𝐠 𝐭𝐡𝐢𝐬 𝐛𝐨𝐭 🤔!

💎 Sᴛᴇᴘ 1 - 𝐔 𝐧𝐞𝐞𝐝 𝟏 𝐠𝐫𝐨𝐮𝐩 𝐚𝐧𝐝 𝟏 𝐜𝐡𝐚𝐧𝐧𝐞𝐥 [𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞 𝐜𝐡𝐚𝐧𝐧𝐞𝐥]!

💎 Sᴛᴇᴘ 2 - 𝐀𝐝𝐝 𝐦𝐲 𝐛𝐨𝐭 𝐚𝐬 𝐚𝐝𝐦𝐢𝐧 𝐢𝐧 𝐲𝐨𝐮𝐫 𝐠𝐫𝐨𝐮𝐩 𝐚𝐧𝐝 𝐜𝐡𝐚𝐧𝐧𝐞𝐥.

💎 Sᴛᴇᴘ 3 - 𝐀𝐟𝐭𝐞𝐫 𝐝𝐨𝐧𝐞 𝐠𝐨 𝐭𝐨 𝐮𝐫 𝐠𝐫𝐨𝐮𝐩 𝐚𝐧𝐝 𝐭𝐲𝐩𝐞 𝐚 𝐜𝐨𝐦𝐦𝐚𝐧𝐝 "/License" ! 

𝐍𝐨𝐭𝐞 : 𝐰𝐢𝐭𝐡𝐢𝐧 𝟐𝟒𝐡𝐨𝐮𝐫𝐬 𝐮 𝐚𝐫𝐞 𝐥𝐢𝐜𝐞𝐧𝐬𝐞 𝐰𝐢𝐥𝐥 𝐛𝐞 𝐚𝐥𝐥𝐨𝐰𝐞𝐝 𝐛𝐲 𝐚𝐝𝐦𝐢𝐧 .

💎 Sᴛᴇᴘ 4 - 𝐍𝐞𝐱𝐭 𝐬𝐞𝐧𝐝 "/database -𝟏𝟎𝟎xxxxxxxxx[𝐮𝐫 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞 𝐜𝐡𝐚𝐧𝐧𝐞𝐥 𝐢𝐝]

𝐍𝐨𝐭𝐞 : 𝐰𝐢𝐭𝐡𝐢𝐧 𝟐𝟒𝐡𝐨𝐮𝐫𝐬 𝐮 𝐚𝐫𝐞 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞 𝐰𝐢𝐥𝐥 𝐛𝐞 𝐚𝐥𝐥𝐨𝐰𝐞𝐝 𝐛𝐲 𝐚𝐝𝐦𝐢𝐧 .

💎 Sᴛᴇᴘ 5 - 𝐃𝐨𝐧𝐞 𝐤𝐧𝐨𝐰 𝐬𝐭𝐚𝐫𝐭 𝐮𝐩𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐦𝐨𝐯𝐢𝐞𝐬 𝐢𝐧 𝐮𝐫 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞 𝐜𝐡𝐚𝐧𝐧𝐞𝐥.

💎 Nᴏᴛᴇ :  𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞 𝐜𝐡𝐚𝐧𝐧𝐞𝐥 𝐦𝐮𝐬𝐭 𝐛𝐞 𝐩𝐫𝐢𝐯𝐚𝐭𝐞 𝐚𝐧𝐝 𝐚𝐝𝐦𝐢𝐧 𝐦𝐮𝐬𝐭 𝐛𝐞 𝐦𝐞𝐦𝐛𝐞𝐫,

𝐄𝐱𝐭𝐫𝐚 𝐟𝐞𝐚𝐭𝐮𝐫𝐞𝐬

📌 𝐀𝐮𝐭𝐨 𝐝𝐞𝐥𝐞𝐭𝐞 𝟔𝟎𝐬𝐞𝐜 𝐬𝐨 𝐧𝐨 𝐧𝐞𝐞𝐝 𝐭𝐨 𝐰𝐨𝐫𝐫𝐲 𝐚𝐛𝐨𝐮𝐭 𝐜𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 🥰

📌 𝐌𝐲 𝐛𝐨𝐭 𝐢𝐬 𝐜𝐨𝐩𝐲𝐫𝐞𝐢𝐠𝐡𝐭𝐟𝐫𝐞𝐞 𝐚𝐧𝐝 𝐭𝐫𝐮𝐬𝐭𝐞𝐝

👉 @Beastonejnanesh 

"""

