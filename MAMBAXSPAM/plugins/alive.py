from .. import Riz, SUDO_USERS
from .. import ALIVE_PIC
from telethon import events
from time import time
from datetime import datetime

RIZ_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/a8a793a8716bdcc923fd3.jpg"
  

          
rizoel = "✧ 𝑀𝐴𝑀𝐵𝐴 𝑆𝑃𝐴𝑀 𝐼𝑍𝑍 𝐴𝐿𝐼𝑉𝐸𝐸 ✧\n\n"

rizoel += f"┏━━━━━━━━━━━━━━━━━━━\n"

rizoel += f"┣➣ **ᴘʏᴛʜᴏɴ ** : `3.9.6`\n"

rizoel += f"┣➣ **DEVELOPER** : `{🇲🇦🇲🇧🇦}`\n"

rizoel += f"┣➣ **🇴🇼🇳🇪🇷**  : `[BLACK MAMBA]{https://t.me/BLACKMAMBA_OFFICIAL}`\n"
    
rizoel += f"┣➣ **sᴜᴘᴘᴏʀᴛ** : [JOIN](https://t.me/MAMBA_X_SUPPORT)\n"

rizoel += f"┣➣ **ᴄʜᴀɴɴᴇʟ** : [JOIN](https://t.me/MAMBA_NETWORK)\n"

rizoel += f"┗━━━━━━━━━━━━━━━━━━━\n\n"

rizoel += f"🖤 [𝐑𝐄𝐏𝐎](https://github.com/SUKHPAL443/MAMBAXSPAM) 🖤"            
                                    
@Riz.on(events.NewMessage(pattern=r"\.alive"))
async def alive(event):
    if event.sender_id in SUDO_USERS:
     await Riz.send_file(event.chat_id,
                                  RIZ_PIC,
                                  caption=rizoel)
    
