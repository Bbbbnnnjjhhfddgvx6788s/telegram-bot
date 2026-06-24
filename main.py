import asyncio
from telethon import TelegramClient, events
import re
import nest_asyncio

# የራስዎን API መረጃዎች እዚህ ያስገቡ
API_ID = 37042998
API_HASH = "a5ad2cd871b0e716687f390cbd61ca44"
TARGET_CHANNEL = "@Ethiofreelancjobs"
MY_LINK = "https://t.me/Ethiofreelancjobs"

# መረጃው የሚቀዳበት ቻናል
SOURCE_CHANNELS = ["@freelance_ethio"]

client = TelegramClient("my_user_session", API_ID, API_HASH)

@client.on(events.NewMessage(chats=SOURCE_CHANNELS))
async def my_event_handler(event):
    if event.message.text:
        text = event.message.text
        # የድሮዎቹን ምንጮች ማጽጃ
        unwanted_links = [r"afriworket\.com", r"@freelanceethbot", r"@freelance_ethio", r"@afriworkamharic"]
        for pattern in unwanted_links:
            text = re.sub(pattern, "", text, flags=re.IGNORECASE)
        # የራስን ሊንክ መጨመር
        new_text = f"{text}\n\nተጨማሪ ስራዎችን ለማግኘት፦ {MY_LINK}"
        await client.send_message(TARGET_CHANNEL, new_text)

async def main():
    await client.start()
    print("🤖 ቦቱ እየሰራ ነው!")
    await client.run_until_disconnected()

nest_asyncio.apply()
asyncio.run(main())

