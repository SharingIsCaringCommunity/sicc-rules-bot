# --------------------------
# rules-bot.py
# Sharing is Caring Community AKA SICC Discord server's rules bot
# --------------------------

# --------------------------
# START OF rules-bot.py CODE
# --------------------------

# --------------------
# Import Python module(s), package(s), function(s) and classe(s)
# --------------------
import os
import logging
import discord
from discord.ext import commands

# --------------------
# Logging module
# --------------------
logging.basicConfig(level=logging.INFO)

# --------------------
# Discord.py Intent(s)
# --------------------

# Set of Discord.py defauly intents that includes only basic events (guilds, channels and emojis)
intents = discord.Intents.default()

# Enable Message Content Intent to allow the bot to read actual text of messages sent by user
intents.message_content = True

# Enable Discord members related gateway events and caching
intents.members = True  

# Rules bot's commands for support e.g. !help
rulesBot = commands.Bot(command_prefix="!", intents=intents)

# --------------------
# Detailed Rules in English and Chinese (for !rules command or DM)
# --------------------

rulesSICC = """
===========================================================
📜 Sharing is Caring Community's AKA SICC's Server Rule(s)
📜 Sharing is Caring Community AKA SICC 的规矩
===========================================================

**SICC stands for Sharing is Caring Community**
**SICC 是代表 Sharing is Caring Community**

============
Introduction
介绍
============

In order to ensure a safe space for everyone in the Sharing is Caring Community AKA SICC, we hope that you are well aware of the general rule(s) that are given in this server as below. Kindly take note on the rule(s) and please behave according to the rules given as below.
為了確保給大家在 Sharing is Caring Community AKA SICC 有一個安全的空间，我們希望你們会意识到一些 server 的规矩，麻煩请大家注意一下并请注意您的行为举止。

=================================================================
TAKE NOTE OF THIS ONE TIME PERMANENT SICC DISCORD INVITATION LINK
请注意这一次性永久 SICC Discord 邀请 link
=================================================================

Please keep in mind you received the one-off Discord server invitation from PANG himself. Thus, there will be NO second chance to rejoin once you quit from the SICC Discord server. In the meantime, any kind of reasons for rejoining the server are NOT accepted. Hence, please THINK TWICE before quitting the SICC discord server and treat this server like you visit other people's house. This is to in line with our goals to create a safe community for everyone who joined the SICC Discord server.
请记住，PANG 本人只发出一次性 Discord的invite link。因此，一旦您退出 SICC Discord server将不再有第二次重新加入的机会。同时，任何重新加入Discord server的理由均不予受理。因此在您退出 SICC Discord server之前，请三思而后行并请表现像你访问别人的家一样，家有家规。这也符合了我们为所有加入 SICC Discord server的member 创建一个安全社区的目标。

===============================================
Consequence(s) IF NOT comply one of the rule(s)
什么后果如果不遵守其中一条规则
===============================================

ANY RESULT OF WRONGDOING(S) BELOW WILL BE GIVEN IN "PERMANENT BAN" FROM SHARING IS CARING COMMUNITY AKA SICC WITHOUT ANY WARNING(S).
任何以下的不当行为都将在没有任何警告的情况下被 "永久封禁" 此 Sharing is Caring Community AKA SICC。

=====================
SICC's server rule(s)
SICC的规矩
=====================

[#R1]
FOLLOW any necessary guideline(s) set by Discord such as Discord’s Terms of Service [https://discord.com/terms], Discord’s Community Guidelines [https://discord.com/guidelines], Discord’s Partnership Code of Conduct [https://support.discord.com/hc/en-us/articles/360024871991-Discord-Partnership-Code-of-Conduct].
遵守 Discord 制定的任何必要准则，例如 Discord 的服务条款 [https://discord.com/terms]、Discord 的社区准则 [https://discord.com/guidelines]、Discord 的合作伙伴行为准则 [https://support.discord.com/hc/en-us/articles/360024871991-Discord-Partnership-Code-of-Conduct]。
[#R1]

[#R2]
PROHIBITED to share any Self-Promotion(s) with advertisement(s), referral link(s) for your own personal gain(s) and benefit(s).
禁止分享任何自我推销。例如，通过广告、推荐链接来以获取个人的利益和好处。
[#R2]

[#R3]
PROHIBITED to impersonate other member(s) including members and admin(s) from SICC. This include(s) using misleading username(s) or profile picture(s).
禁止冒充其他成员。包括SICC的Admin和会员。这也包括使用误导性的用户名或头像。
[#R3]

[#R4]
PROHIBITED to share any attachment(s) with malware or virus to promote phishing and scamming activities.
禁止共享任何带有恶意软件或病毒的附件以促进网络钓鱼和诈骗活动。
[#R4]

[#R5]
PROHIBITED any form of harassment such as religion, race, age, sex, sexual oriented, marital status, gender identity, nation origin and disability through verbal, cyberbullying or hate speech.
禁止通过口头上、网络欺凌或仇恨言论进行任何形式的骚扰，例如宗教、种族、年龄、性别、性取向、婚姻状况、性别认同、国籍和残疾。
[#R5]

[#R6]
PROHIBITED to promote any sensitive topic(s) such as religion, politic ideology, low-quality content as this offend, hurt or create a non-inclusive environment.
禁止宣传任何敏感话题，如宗教、政治意识形态、低质量内容，因为这会冒犯、伤害或创造不包容的环境
[#R6]

[#R7]
PROHIBITED to share or discuss any explicit, NSFW topic(s) and content(s) which includes image(s), video(s) and link(s).
禁止分享或讨论任何色情、NSFW 主题和内容，包括图像、视频和链接。
[#R7]

[#R8]
PROHIBITED to share any sensitive information such as personal information or private conservation AKA DM or group conversation with and without any consent from any parties.
禁止在经任何人同意和未经任何人同意的情况下分享任何敏感信息，如个人信息或私人对话 AKA DM 或群主对话。
[#R8]

[#R9]
PROHIBITED to spam or mass spam message(s), emoji(s), GIF(s) and link(s). Ensure that every conversation is meaningful and on-topic for everyone.
禁止发送垃圾信息或群发垃圾信息、表情符号、动图和链接。请确保每次对话都有意义且与主题相关。
[#R9]

========================
SICC's server guidelines
SICC的指导方针
========================

[#G1]
Our current mode of language for engagement are ENGLISH and CHINESE. To avoid language barrier during the engagement, any other languages are NOT welcome unless received the consent from server admins.
我们目前是用英语和中文来交流。为避免出现一些语言障碍，我们不接受任何其他语言除非获得了admin的同意。
[#G1]

[#G2]
NO blank, unpingable, offensive or absurdly long username(s), nickname(s) or even profile picture(s).
禁止空白、无法 ping 通、冒犯性或过长的用户名、昵称甚至个人资料图片。
[#G2]

[#G3]
AVOID spamming the same message across multiple channels.
避免在多个渠道上发送相同的信息。
[#G3]

[#G4]
DO NOT mass @mention server members or direct message (DM) SICC admin as every member(s) with “Admin” roles are here on their own accord. Please respect their freedom and time. Do not ping or direct message them out of the blue. They are human too.
请勿群发 @mention server的会员或私信 (DM) SICC admin，因为所有拥有“Admin”角色的成员都是自愿加入的。请尊重他们的时间和自由，不要突发 ping 或私信给他们。他们和你一样也是人。
[#G4]

[#G5]
KINDLY post your topic(s) or message(s) in any appropriate channel(s) which are relevant to the channel’s purpose and follow each channel-specific rule(s) and purpose(s) at the same time.
请在任何与频道目的相关的适当频道中发布您的主题或消息，并同时遵循每个频道特定的规则和目的。
[#G5]

=============
Disclaimer(s)
免责声明
=============

[#D1]
EVERY RULE(S) are subjected to be CHANGE any time so please take note and do your part(s) to comply.
每条规则都可能随时发生更改，因此请注意并尽力遵守。
[#D1]

[#D2]
PLEASE take note that any violation of the rules that mentioned above will be resulted in permanent BANNED from participating SICC.
请注意，任何违反以上的规则都将导致永久封禁参与SICC。
[#D2]

[#D3]
ONCE you have react ✅ in the ⁠⁠✅-verify-yourself channel, you are AGREE to adhere every rule(s) as mentioned above.
一旦您在⁠⁠✅-verify-yourself 频道中react ✅，即表示您同意遵守上述所有规则。
[#D3]

[#D4]
PLEASE be MINDFUL before doing any necessary acts in the SICC.
请在 SICC 进行任何必要行为之前，注意您的行为举止。
[#D4]

"""

# --------------------
# VARIABLES (read from environment) ===
# WARNING: Set these in Railway → Project → Variables
# --------------------

# Discord Bot Token *REQUIRED*
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")       

# Rules Channel ID optional; numeric string
RULES_CHANNEL_ID = os.getenv("RULES_CHANNEL_ID")  

# Prompt error msgs if Discord Bot Token not exist
if not DISCORD_TOKEN:
    raise RuntimeError("Missing DISCORD_TOKEN environment variable.")

# Convert Rules text channel ID to Integer
rules_channel_id_int = int(RULES_CHANNEL_ID) if RULES_CHANNEL_ID else None

# --------------------
# Functions
# Splits string into chunks of lines in order to respect the limits set by Discord
# --------------------
def chunk_text(s: str, limit: int):
    # Split into line(s)
    lines = s.splitlines(keepends=True)
    # Setup buffer and output
    buf, out = "", []
    # Process each lines
    for ln in lines:
        if len(buf) + len(ln) > limit:
            out.append(buf)
            buf = ln
        else:
            buf += ln
    # Add the last buffer (if not empty)
    if buf:
        out.append(buf)
    # Return result(s)
    return out

# --------------------
# Async Functions
# Splits SICC rules text into less than 4000 characters chunks
# Send the SICC rules to SICC new members through DM
# --------------------
async def send_rules_embed(target: discord.abc.Messageable):
    # Split rules text to at most 4000 characters as Discord embeds have a limit of 4096 characters for its descriptions
    for part in chunk_text(rulesSICC, 4000):  
        # Create new embed for SICC's discord rules
        embed = discord.Embed(
            title="📜 SICC's Server Rules",
            description=part,
            color=0x2ecc71
        )
        # Send the created embed to the target channel which is SICC's new members through DM
        await target.send(embed=embed)

# --------------------
# Async Functions
# Ensure the SICC rules bot automatically post the rules in the rules text channel on startup
# Scan the last 50 messages to prevent duplicates if the rules are already existed in the rules text channel
# --------------------
# Run once rules bot has successfully connected to Discord
@rulesBot.event
async def on_ready():
    # Print confirmation in the console with the bot's username
    print(f"✅ Logged in as {rulesBot.user}")

    # Check if the rules channel ID is configured
    # Only try to post in rules channel if env var provided
    if rules_channel_id_int:
        # Get the channel object
        channel = rulesBot.get_channel(rules_channel_id_int)
        # 
        if channel:
            # Scan the recent messages
            # Read the last 50 messages in the rules channel
            async for message in channel.history(limit=50):
                # If the message is sent by the SICC rules bot
                if message.author == rulesBot.user and message.embeds:
                    # The first embed has the title as shown below
                    if message.embeds[0].title == "📜 SICC's Server Rules":
                        # Bots will print the message as shown below if the rules already exist in the rules text channel
                        print("ℹ️ Rules already posted, skipping...")
                        # Stop the loop
                        break
            # Else, the rules bot will post the SICC rules in the rules text channel
            else:
                await send_rules_embed(channel)
                # Prompt the success msgs once posted the rules in the console
                print("✅ Rules posted in #rules channel")

# --------------------
# Async Functions
# Run the SICC rules bot when typing !rules command
# --------------------
# Register the below function as a bot command which is !rules
@rulesBot.command(name="rules")
# Ensure that ONLY SICC Discord server member with admin permission can run this command 
@commands.has_permissions(administrator=True)
# Define the command function for !rules
# ctx refers to context
async def rules(ctx):
    # Build an embed containing SICC Discord server rules and send to the specific channel
    await send_rules_embed(ctx)

# --------------------
# Async Functions
# Run the SICC rules bot when typing !postrules command
# ONLY SICC Discord server member with admin permission can run this command
# --------------------
# Register the below function as a bot command which is !postrules
@rulesBot.command(name="postrules")
# Ensure that ONLY SICC Discord server member with admin permission can run this command 
@commands.has_permissions(administrator=True)
# Define the command function for !postrules
# ctx refers to context
async def postrules(ctx):
    # If detected the rules text channel ID is not set
    if not rules_channel_id_int:
        # SICC rules bot will prompt the important msgs
        await ctx.send("⚠️ RULES_CHANNEL_ID is not set in environment.")
        # Stop the loop
        return
    # Converts to usable Discord channel object which is rules text channel ID
    channel = rulesBot.get_channel(rules_channel_id_int)
    # If SICC rules bot found and match the right rules text channel ID
    if channel:
        # Call the send_rules_embed function and send the rules embed to the rules text channel
        await send_rules_embed(channel)
        # Prompt the msgs to the rules text channel where SICC Discord server member used !postrules command
        await ctx.send("✅ SICC rules have been posted in the #rules text channel.")
    # Else if SICC rules bot not able to find and match the right rules text channel ID
    else:
        # Prompt the msgs that the rules channel is not found and check the rules text channel ID
        await ctx.send("⚠️ SICC rules channel not found. Please check the #rules text channel ID.")

# --------------------
# Async Functions
# List ALL usable bot commands for SICC rules bot by typing !rulesbot
# --------------------
# Command: List all usable bot commands with !rulesbot
@rulesBot.command(name="rulesbot")
# Ensure that ONLY SICC Discord server member with admin permission can run this command 
@commands.has_permissions(administrator=True)
# Define the command list function for 
# ctx refers to context
async def list_commands(ctx):
    # Create embed message for list of usable commands for SICC rules bot
    embed = discord.Embed(
        title="🤖 Usable ADMIN ONLY commands for SICC rules bot",
        description="Here’s a list of usable ADMIN ONLY command(s) you can use for SICC rules bot:",
        color=0x7289da
    )
    # Check permission If the Discord member is Administrator permission
    if ctx.author.guild_permissions.administrator:
        # Add fields for each of usable commands for SICC rules bot
        embed.add_field(name="!rulesbot", value="List all available SICC rules bot command(s).", inline=False)
        embed.add_field(name="!rules", value="Show the detailed Discord server rule(s).", inline=False)
        embed.add_field(name="!postrules", value="Post or Repost Discord server rule(s) in the #rules text channel.", inline=False)
    # Send the embed message into the text channel where the command was used
    await ctx.send(embed=embed)

# --------------------
# Async Functions
# Custom error handler
# Prompt an error message when Discord member with no Administrator permission using !rulesbot
# --------------------
# Error handler Decorator
@list_commands.error
# Define the function when to raise error when Discord member with no Administrator permission using the !rulesbot command
async def list_commands_error(ctx, error):
    # If the Discord member with no Admin permission tried to run !rulesbot command 
    if isinstance(error, commands.MissingPermissions):
        # Prompt the error message to the Discord member with no Admin permission
        await ctx.send("❌ You don’t have permission to use this ADMIN ONLY command.")
    # Handle unknown commands
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("❓ That command doesn’t exist.")
        
    # Handle other errors (optional, for debugging)
    else:
        raise error  # re-raise so you can still see errors in console

# --------------------
# Async Functions
# SICC rules bot will send SICC Discord server rules to the new members through DM
# --------------------
# Discord event listener to trigger when new member joins SICC Discord server
@rulesBot.event
# Define the function when a new member joins SICC Discord server
async def on_member_join(member):
    try:
        # Using chunk_text that splits a long string into smaller pieces in order to split SICC server rules text into chunks of 1900 characters without hitting the limit that is set by Discord which is 2000 character(s) of msgs length limit for DM(s)
        for part in chunk_text(rulesSICC, 1900):
            # Send each part of rules text as DM to the new member
            await member.send(part)
    # Ignore any error if Discord member closed DMs
    except Exception:
        pass

# --------------------
# Login to Discord with the provided Discord bot token and run SICC rules bot with defined commands and events as above
# --------------------
rulesBot.run(DISCORD_TOKEN)

# ------------------------
# END OF rules-bot.py CODE
# ------------------------