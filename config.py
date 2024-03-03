import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "")
    API_HASH  = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

    # database config
    DB_NAME = os.environ.get("DB_NAME","madflixbotz")     
    DB_URL  = os.environ.get("DB_URL","")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://graph.org/file/4b306f4b15c23a8f22e58.jpg")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]
    FORCE_SUB   = os.environ.get("FORCE_SUB", "") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
    
    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))


class Txt(object):
    # part of text configuration
        
    START_TXT = """Hello {} 
    
➻ I'm a simple Powerful Rename Bot.
    
➻ By Using me You Can Auto Rename your Your Files.
    
➻ I can Support Custom Thumbnail And Custom Caption.
    
➻ Use /tutorial Command To Know How To Use Me.
    
<b>Bot Is Made By @MR_V_BOTS</b>"""
    
    FILE_NAME_TXT = """<b><u>SETUP AUTO RENAME FORMAT</u></b>

Use These Keywords To Setup Custom File Name

✓ episode :- To Replace Episode Number
✓ quality :- To Replace Video Resolution

<b>➻ Example :</b> <code> /autorename WEDNESDAY S01 - EPepisode - quality  [Dual Audio] - @A1PHER </code>

<b>➻ Your Current Auto Rename Template :</b> <code>{format_template}</code> """
    
    ABOUT_TXT = f"""<b>🤖 My Name :</b> <a href='https://t.me/renamer_v_bot'>Auto Rename Bot ⚡</a>
<b>📝 Language :</b> <a href='https://python.org'>Python 3</a>
<b>📚 Library :</b> <a href='https://pyrogram.org'>Pyrogram 2.0</a>
<b>🗄 Server :</b> <a href='https://heroku.com'>Heroku</a>
<b>🔔 Channel :</b> <a href='https://t.me/Mr_V_bots'>Mr_V_bots</a>
<b>⚙️ Developer :</b> <a href='https://t.me/C0nt4ct_bot>MR_V</a>
    
<b>💡Bot Made By :</b> @Mr_V_bots"""

    
    THUMBNAIL_TXT = """<b><u>🖼️  HOW TO SET THUMBNAIL</u></b>
    
⦿ You Can Add Custom Thumbnail By Sending A Photo To Me....
    
⦿ /viewthumb - Use This Command To See Your Thumbnail
⦿ /delthumb - Use This Command To Delete Your Thumbnail"""

    CAPTION_TXT = """<b><u>📝  HOW TO SET CAPTION</u></b>
    
⦿ /set_caption - Use This Command To Set Your Caption
⦿ /see_caption - Use This Command To See Your Caption
⦿ /del_caption - Use This Command To Delete Your Caption"""

    PROGRESS_BAR = """\n
<b>📁 Size</b> : {1} | {2}
<b>⏳️ Done</b> : {0}%
<b>🚀 Speed</b> : {3}/s
<b>⏰️ ETA</b> : {4} """
    
    
    DONATE_TXT = """<b>🥲 Thanks For Showing Interest In Donation! ❤️</b>
    
If You Like My Bots & Projects, You Can Donate Me Any Amount From 10 Rs Upto Your Choice.
    
<b>To Donate,Contact admin by @C0nt4ct_bot</b>"""
    
    HELP_TXT = """<b>Hey</b> {}
    
Here Is The Help Commands for You"""

