# Made By @TIMEX_OF_CLOCK
# Keep Credits else gay....

"""Create Private Groups
Available Commands:
.create (b|g|c) GroupName"""

from telethon.tl import functions
from BLACK_MAMBA import CMD_HELP
from BLACK_MAMBA.utils import admin_cmd, edit_or_reply, sudo_cmd


@bot.on(admin_cmd(pattern="create (b|g|c) (.*)"))  # pylint:disable=E0602
@bot.on(sudo_cmd(pattern="create (b|g|c) (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    type_of_group = event.pattern_match.group(1)
    group_name = event.pattern_match.group(2)
    event = await edit_or_reply(event, "Creating weit sur.....")
    if type_of_group == "b":
        try:
            result = await event.client(
                functions.messages.CreateChatRequest(  # pylint:disable=E0602
                    users=["@sarah_robot"],
                    # Not enough users (to create a chat, for example)
                    # Telegram, no longer allows creating a chat with ourselves
                    title=group_name,
                )
            )
            created_chat_id = result.chats[0].id
            await event.client(
                functions.messages.DeleteChatUserRequest(
                    chat_id=created_chat_id, user_id="@sarah_robot"
                )
            )
            result = await event.client(
                functions.messages.ExportChatInviteRequest(
                    peer=created_chat_id,
                )
            )
            await event.edit(
                "Group `{}` created successfully.\nJoin {}".format(
                    group_name, result.link
                )
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            await event.edit(str(e))
    elif type_of_group in ["g", "c"]:
        try:
            r = await event.client(
                functions.channels.CreateChannelRequest(
                    title=group_name,
                    about="𝑪𝒓𝒆𝒂𝒕𝒆𝒅 𝑩𝒚 υℓтяα χ",
                    megagroup=type_of_group != "c",
                )
            )

            created_chat_id = r.chats[0].id
            result = await event.client(
                functions.messages.ExportChatInviteRequest(
                    peer=created_chat_id,
                )
            )
            await event.edit(
                "Channel `{}` created successfully.\nJoin {}".format(
                    group_name, result.link
                )
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            await event.edit(str(e))
    else:
        await event.edit("Read `.plinfo create` to know how to use me")


CMD_HELP.update(
    {
        "create": "**SYNTAX :** `.create b`\
    \n**USAGE : **Creates a super group and send you link\
    \n\n**SYNTAX : **`.create g`\
    \n**USAGE : **Creates a private group and sends you link\
    \n\n**SYNTAX : **`.create c`\
    \n**USAGE : **Creates a Channel and sends you link\
    \n\nhere the bot accout is owner\
    "
    }
)
