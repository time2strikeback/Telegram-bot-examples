from pyrogram import Client, filters
from pyrogram.raw import types
from pyrogram.raw import functions
from pyrogram.utils import get_channel_id

app = Client(
    "hmmm",
    api_id= "987108",
    api_hash="5371695457:AAGcfz2e1WQ4iuM8pcWnoq1sfzGQPzt10Mw",
    bot_token="5371695457:AAGcfz2e1WQ4iuM8pcWnoq1sfzGQPzt10Mw"
)


@app.on_message(filters.command("start"))
async def hello(_, message):
    await message.reply_text("hey")


@app.on_raw_update()
async def join_req(client, update, _, __):
    if isinstance(update, types.UpdateBotChatInviteRequester):
        channel = await client.resolve_peer(
            get_channel_id(update.peer.channel_id)
        )
        user = await client.resolve_peer(update.user_id)
        await client.send(
            functions.messages.HideChatJoinRequest(
                peer=channel,
                user_id=user,
                approved=True
            )
        )


app.run()
