from .. import Riz, SUDO_USERS
from telethon import events
from time import time
from datetime import datetime

    
HELP_PIC = "https://telegra.ph/file/a8a793a8716bdcc923fd3.jpg"

RiZoeLX = "π₯ π΄π¨π΄π©π¨ πΏ πΊπ·π¨π΄ π₯\n\n"
 
RiZoeLX += f"__α΄α΄α΄s α΄α΄ α΄ΙͺΚα΄ΚΚα΄ ΙͺΙ΄ π΄π¨π΄π©π¨ πΏ πΊπ·π¨π΄__\n\n"

RiZoeLX += f" β§ πππ΄ππ±πΎπ π²πΌπ³π β§\n\n"

RiZoeLX += f" `.ping` - to check ping\n `.alive` - to check bot alive/version (only main userbot will reply)\n `.setname` - to change Name\n .`inviteall` - to add members using spam bots\n .`restart` - to restart all spam bots\n\n"
 
RiZoeLX += f" β§ πΉπΎπΈπ½/π»π΄π°ππ΄ π²πΌπ³π β§\n\n"

RiZoeLX += f" `.join` - to join public channel/groups\n `.pjoin` - to join public channel/groups\n `.leave` - to leave public/private channel/groups\n\n"
 
RiZoeLX += f" β§ ππΏπ°πΌ π²πΌπ³π β§\n\n"

RiZoeLX += f" `.raid` - to raid\n `.replyraid` - to active reply raid\n `.dreplyraid` - to de-active reply raid\n `.spam` - this cmd use for Normal spam\n `.bigspam` - this cmd use for big spam\n `.delayspam` - this cmd use for delay spam\n\n"
 
RiZoeLX += f"ALL CMDS WITH DETAILS [HERE.](https://telegra.ph/a8a793a8716bdcc923fd3.jpg)\n\n"
 
RiZoeLX += f"Β© @MAMBA_NETWORK | @MAMBA_X_SUPPORT\n"


@Riz.on(events.NewMessage(pattern=r"\.help"))
async def help(event):
    if event.sender_id in SUDO_USERS:
     await Riz.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=RiZoeLX)                                                         
