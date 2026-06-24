import asyncio
import re
from telethon import TelegramClient, events
from telethon.network import ConnectionTcpFull

# 1. API መረጃዎች (የቀድሞዎቹን ይጠቀሙ)
API_ID = 37042950
API_HASH = 'a5ad2cd871b0e716687f390cbd61ca44'
TARGET_CHANNEL = '@Ethiofreelancejobs'
MY_LINK = "https://t.me/Ethiofreelancejobs"

# 2. ምንጭ ቻናሎች (እዚህ ጋር ሌሎች ቻናሎችን መጨመር ይችላሉ)
SOURCE_CHANNELS = ['@freelance_ethio']

# 3. የቴሌግራም ክሊየንት (ለRender ሰርቨር የተስተካከለ)
client = TelegramClient('my_user_session', API_ID, API_HASH, timeout=300, connection=ConnectionTcpFull)

@client.on(events.NewMessage(chats=SOURCE_CHANNELS))
async def my_event_handler(event):
    if event.message.text:
        text = event.message.text
        
        # 4. አላስፈላጊ ሊንኮችን ለማስወገድ (አዲሶቹን እዚህ ያክሉ)
        unwanted_links = [
            r'afrimarket\.com', 
            r'@freelanceethbot', 
            r'@freelance_ethio', 
            r'@afriworkamharic',
            r'@afriworkapplicantbot'
        ]
        for pattern in unwanted_links:
            text = re.sub(pattern, "", text, flags=re.IGNORECASE)
        
        # 5. የራስዎን ሊንክ መላክ
        new_text = f"{text}\n\nምንጭ፦ {MY_LINK}"
        await client.send_message(TARGET_CHANNEL, new_text)

async def main():
    print("🤖 ቦቱ እየተጀመረ ነው...")
    await client.start()
    print("✅ ቦቱ አሁን እየሰራ ነው!")
    await client.run_until_disconnected()

asyncio.run(main())

