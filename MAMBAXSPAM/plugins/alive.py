from .. import Riz, SUDO_USERS
from .. import ALIVE_PIC
from telethon import events
from time import time
from datetime import datetime

RIZ_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/a8a793a8716bdcc923fd3.jpg"
  

          
rizoel = "β§ ππ΄ππ΅π΄ πππ΄π πΌππ π΄πΏπΌππΈπΈ β§\n\n"

rizoel += f"ββββββββββββββββββββ\n"

rizoel += f"β£β£ **α΄Κα΄Κα΄Ι΄ ** : `3.9.6`\n"

rizoel += f"β£β£ **DEVELOPER** : `{π²π¦π²π§π¦}`\n"

rizoel += f"β£β£ **π΄πΌπ³πͺπ·**  : `[BLACK MAMBA]{https://t.me/BLACKMAMBA_OFFICIAL}`\n"
    
rizoel += f"β£β£ **sα΄α΄α΄α΄Κα΄** : [JOIN](https://t.me/MAMBA_X_SUPPORT)\n"

rizoel += f"β£β£ **α΄Κα΄Ι΄Ι΄α΄Κ** : [JOIN](https://t.me/MAMBA_NETWORK)\n"

rizoel += f"ββββββββββββββββββββ\n\n"

rizoel += f"π€ [ππππ](https://github.com/SUKHPAL443/MAMBAXSPAM) π€"            
                                    
@Riz.on(events.NewMessage(pattern=r"\.alive"))
async def alive(event):
    if event.sender_id in SUDO_USERS:
     await Riz.send_file(event.chat_id,
                                  RIZ_PIC,
                                  caption=rizoel)
    
