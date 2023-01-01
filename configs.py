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

ᴅᴍ ꜰᴏʀ ᴀɴʏ 𝐐ᴜᴇʀʏ @Beastonejnanesh"" )
    ABOUT_WATCH_TEXT = """
ʜᴇʏ ʙᴜᴅᴅʏ, 

ᴍᴅɪsᴋ - ᴀɢᴀʀ ᴀᴘᴋᴏ ɴᴀʜɪ ᴘᴀᴛᴀ ᴋɪ ᴍᴅɪsᴋ ʟɪɴᴋ sᴇ ᴍᴏᴠɪᴇ ᴋᴀɪsᴇ ᴅᴇᴋʜᴇ ᴛᴏ ɴɪᴄᴇ ᴅɪʏᴇ ɢᴀʏᴇ ᴍᴅɪsᴋ ᴡᴀʟᴇ ʙᴜᴛᴛᴏɴ ᴘᴀʀ ᴄʟɪᴄᴋ ᴋᴀʀᴇ 


ᴛᴇʀᴀ ʙᴏx - ᴀɢᴀʀ ᴀᴘᴘᴋᴏ ɴᴀʜɪ ᴘᴀᴛᴀ ᴋɪ ᴛᴇʀᴀʙᴏx sᴇ ᴍᴏᴠɪᴇs ᴋᴀɪsᴇ ᴅᴇᴋʜᴇ ᴛᴏ ɴɪᴄʜᴇ ᴅɪʏᴇ ɢᴀʏᴇ ᴛᴇʀᴀ ʙᴏx ʙᴜᴛᴛᴏɴ ᴘᴀʀ ᴄʟɪᴄᴋ ᴋᴀʀᴇ

ʀᴇɢᴀʀᴅs - @Beastonejnanesh"""
    ABOUT_MDISK_TEXT = """
 how to open mdisk link https://t.me/+Rf7HPykmLC5hOWQ9"""

    ABOUT_HELP_TEXT = """

💎 RᴇQᴜɪʀᴇᴍᴇɴᴛ ᴛᴏ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ!

💎 Sᴛᴇᴘ 1 - Aᴘᴋᴏ ᴇᴋ ɢʀᴏᴜᴘ ᴋɪ ᴊᴀʀᴜʀᴀᴛ ʜᴏɢɪ, ᴊɪꜱᴍᴇ ᴍᴇᴍʙᴇʀꜱ ʙʜɪ ʜᴏ, ᴀᴜʀ ᴇᴋ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ᴋɪ ᴊᴀʀᴜʀᴀᴛ ʜᴏɢɪ, ᴊɪꜱᴍᴇ ᴀᴘᴋᴇ ꜱᴀʀᴇ ᴘᴏꜱᴛ ʜᴏɴɢᴇ!

💎 Sᴛᴇᴘ 2 - ʙᴏᴛ ᴋᴏ ᴀᴘɴᴇ ɢʀᴏᴜᴘ ᴀᴜʀ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ᴋᴀ ᴀᴅᴍɪɴ ʙᴀɴᴀɴᴀ ʜᴏɢᴀ.

💎 Sᴛᴇᴘ 3 - ɢʀᴏᴜᴘ ᴍᴇ "/License" ᴛʏᴘᴇ ᴋᴀʀ ᴋᴇ ꜱᴇɴᴅ ᴋᴀʀɴᴀ ʜᴏɢᴀ!

ꜰɪʀ ʙᴏᴛ ᴋᴇ ᴏᴡɴᴇʀ ᴀᴘᴋᴀ ʏᴇ ʀᴇQᴜᴇꜱᴛ ᴀᴄᴄᴇᴘᴛ ᴋᴀʀ ʟᴇɴɢᴇ. 

💎 Sᴛᴇᴘ 4 - ɢʀᴏᴜᴘ ᴍᴇ "/database - ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ɪᴅ" ᴛʏᴘᴇ ᴋᴀʀ ᴋᴇ ꜱᴇɴᴅ ᴋᴀʀɴᴀ ʜᴏɢᴀ.

ꜰɪʀ ʙᴏᴛ ᴋᴇ ᴏᴡɴᴇʀ ᴀᴘᴋᴀ ʏᴇ ʀᴇQᴜᴇꜱᴛ ʙʜɪ ᴀᴄᴄᴇᴘᴛ ᴋᴀʀ ʟᴇɴɢᴇ 

💎 Sᴛᴇᴘ 5 - ᴀʙ ᴀᴘᴋᴏ ᴀᴘɴᴇ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ᴍᴇ ᴘᴏꜱᴛ ᴅᴀʟɴɪ ʜᴏɢɪ,

ᴊɪꜱꜱᴇ ᴋɪ ᴀɢᴀʀ ɢʀᴏᴜᴘ ᴍᴇ ᴋᴏɪ ᴜꜱᴇʀ ꜱᴇᴀʀᴄʜ ᴋᴀʀᴇ ᴛᴏ ʏᴇ ʙᴏᴛ ᴜɴ ᴜꜱᴇʀ ᴋᴇ Qᴜᴀʀʏ ᴋᴏ ꜱᴀᴍᴀᴊʜ ᴋᴇ ᴀᴘᴋᴇ ᴄʜᴀɴɴᴇʟ ꜱᴇ ᴘᴏꜱᴛ ᴜᴛʜᴀ ᴋᴇ ᴜɴʜᴇ ᴅᴇ ᴘᴀʏᴇ.

💎 Nᴏᴛᴇ : Bᴏᴛ ᴀᴅᴍɪɴ ᴀᴘᴋᴇ ᴄʜᴀɴɴᴇʟ ᴍᴇ ᴊᴏɪɴ ʜᴏɴᴇ ᴄʜᴀʜɪʏᴇ,

ᴀɢᴀʀ ʙᴏᴛ ᴀᴅᴍɪɴ ᴀᴘᴋᴀ ʀᴇQᴜᴇꜱᴛ ᴀᴄᴄᴇᴘᴛ ɴʜɪ ᴋᴀʀ ʀᴀʜᴇ ʜᴀɪɴ ᴛᴏ ᴜɴʜᴇ ᴘᴇʀꜱᴏɴᴀʟ ᴍꜱɢ ᴋᴀʀᴇɴ.

👉 @Beastonejnanesh 

""")

