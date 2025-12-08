import os
from dotenv import load_dotenv
import discord
from discord import app_commands
from discord.ext import commands
import discord, asyncio
from datetime import datetime
import psutil
import random as r
import time

#------------------------------------------------ Basic Neccesities ------------------------------------------------------#

# Load Token
load_dotenv(".env")
TOKEN = os.getenv("TOKEN")

# Client and Bot 
# Intents are permissions for the bot that are enabled based on the features necessary to run the bot
client = discord.Client(intents=discord.Intents.default())
bot = commands.Bot(intents=discord.Intents.all(), command_prefix= "!")

# Removes the native help command
bot.remove_command('help')

# Warning Embed Basics
warning_embed_icon = "https://cdn.discordapp.com/attachments/935672317512650812/1154896305320112139/warning_2.png"
warning_embed_color = discord.Color.from_rgb(255,50,50)

#------------------------------------------------ Presets 🌟 ------------------------------------------------------#

# Important  
application_id = 1241854135079407646
application_pfp_url = "https://cdn.discordapp.com/attachments/1241578352293318759/1242223711956762745/DW_Logo_Square3.png?ex=664d0e7c&is=664bbcfc&hm=d7a3969820fab18a6ee66c8f053c21bce32a41281f2596649322df4ee6a13de6&"
club_server_id = 1241575849845592144
server_pfp_url = application_pfp_url
equinox_id = 882061427265921055
equinox_pfp_url = "https://cdn.discordapp.com/avatars/882061427265921055/d2dcf9ac35ef5a87677ce76d87811d4c.png?size=4096"

# Utility Channels
administrator_channel_id = 1241578352293318759
member_logs_channel_id = 1241865382868946945
club_tracker_channel_id = 1253389514945200229
audit_log_channel_id = 1241865420554899578

# Generic Channels
dw_announcements_channel_id = 1241578680711385131
dw_changelog_channel_id = 1241580350455681165
dw_devfeed_channel_id = 1241580364216926361
dw_socialmedia_channel_id = 1241581221335535686

# Utility Roles
active_role_id = 1241856965219717312
inactive_role_id = 1241857046756724766

# Generic Roles
club_member_role_id = 1241577709985992764
club_supporter_role_id = 1241944353916583947
confirmed_role_id = 1253519802920603668

# Badge Roles
badges_role_id = 1248785672370782300
trident_badge_role_id = 1248786236919775305
list_of_badge_role_id = [trident_badge_role_id]

# Statistic Roles
dwstats_role_id = 1241887741336092683
miles_role_id = 1241887061384888410
empty_miles_role_id = 1242165883384627221
wins_role_id = 1241887086479413338
empty_wins_role_id = 1242165857417695273
level_role_id = 1241887088563982386
empty_level_role_id = 1242165545130786836

# Ping Roles
proles_pings_role_id = 1242173050259247326
giveaway_pings_role_id = 1242173473573306449
announcements_pings_role_id = 1242173477524471891
dw_announcements_pings_role_id = 1242173592695865545
dw_devfeed_pings_role_id = 1242173753685708900
dw_changelog_pings_role_id = 1242173857629208677
dw_socialmedia_pings_role_id = 1242173921113935872

# Mile Statistic Roles
m500less = 1242563310155468933
m500 = 1241887737272074380
m1000 = 1241887743043436575
m2500 = 1241887745291325484
m5000 = 1241888317553901619
m7500 = 1242282207226101911
m10000 = 1241888315091976252
m15000 = 1241889398807855155
m20000 = 1241889403614269490
m25000 = 1241888500010324020
m30000 = 1241889401580028014
m35000 = 1241890082877735022
m40000 = 1241890079018979360
m45000 = 1241890017337540721
m50000 = 1241890223722598500
m55000 = 1241902290114445422
m60000 = 1241902291884183592
m65000 = 1241902697502736477
m70000 = 1241902286251364352
m75000 = 1241902221935906907
m80000 = 1241902224498491402
m85000 = 1241902699684040725
m90000 = 1241902699948015758
m95000 = 1241902697586626560
m100000 = 1241902701135265822

listOfMiles = [empty_miles_role_id, m500less, m500, m1000, m2500, m5000, m7500, m10000, m15000, m20000, m25000, m30000, m35000, m40000,
               m45000, m50000, m55000, m60000, m65000, m70000, m75000, m80000, m85000, m90000, m95000, m100000]

# Win Statistic Roles
w50less = 1242563312265330739
w50 = 1242529870408454254
w100 = 1241891412681818152
w200 = 1241891414581842021
w300 = 1241891417119391856
w400 = 1241891418767884371
w500 = 1241891421246459945
w600 = 1241891423402332170
w700 = 1241891602226479166
w800 = 1241891604260978779
w900 = 1241891605884043445
w1000 = 1241891607951970325
w1100 = 1241902218081341452
w1200 = 1241902220442734672
w1300 = 1241891666982473819
w1400 = 1241902288008773682
w1500 = 1241891668685488129
w1600 = 1241902701680263240
w1700 = 1241902701885919253
w1800 = 1241902703173701793
w1900 = 1241902779870478337
w2000 = 1241891410727145523

listOfWins = [empty_wins_role_id, w50less, w50, w100, w200, w300, w400, w500, w600, w700, w800, w900, w1000, w1100, w1200, w1300, w1400,
              w1500, w1600, w1700, w1800, w1900, w2000]

# Level Statistic Roles
l5less = 1242563284419481660
l5 = 1241892210279190658
l10 = 1241892213169066054
l15 = 1241892214825680906
l20 = 1241892216402608248
l25 = 1241892218403553321
l30 = 1241892220378939443
l35 = 1241892222517903422
l40 = 1241892223977521194
l45 = 1241892225953173626
l50 = 1241892397776900187

listOfLevels = [empty_level_role_id, l5less, l5, l10, l15, l20, l25, l30, l35, l40, l45, l50]

#------------------------------------------------ Start Up ------------------------------------------------------#

@bot.event
async def on_ready():
    print("Bot is online")

    # Sync the slash commands to Discord (necessary)
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} commands')
    except:
        print(f'Failed to sync slash commands')

    # Activity Status
    await bot.change_presence(status=discord.Status.online, activity = discord.Game(name = "Drive World⠀|⠀/stats"))
    await asyncio.sleep(120)
 
# Playing -> activity = discord.Game(name="!help")
# Streaming -> activity = discord.Streaming(name="!help", url="twitch_url_here")
# Listening -> activity = discord.Activity(type=discord.ActivityType.listening, name="!help")
# Watching -> activity = discord.Activity(type=discord.ActivityType.watching, name="!help")

#------------------------------------------------ Events ------------------------------------------------------#

# Ping reaction roles on new Drive World Posts (Section 1)
@bot.event
async def on_message(message):
    await bot.process_commands(message) # Commands fix

    if message.channel.id == dw_announcements_channel_id:
        print("New Drive World Post, Section 1.1")
        if message.author.id != application_id:
            channel = bot.get_channel(dw_announcements_channel_id)
            await channel.send(f'<@&{dw_announcements_pings_role_id}>')

    elif message.channel.id == dw_changelog_channel_id:
        print("New Drive World Post, Section 1.2")
        if message.author.id != application_id:
            channel = bot.get_channel(dw_changelog_channel_id)
            await channel.send(f'<@&{dw_changelog_pings_role_id}>')

    elif message.channel.id == dw_devfeed_channel_id:
        print("New Drive World Post, Section 1.3")
        if message.author.id != application_id:
            channel = bot.get_channel(dw_devfeed_channel_id)
            await channel.send(f'<@&{dw_devfeed_pings_role_id}>')

    elif message.channel.id == dw_socialmedia_channel_id:
        print("New Drive World Post, Section 1.4")
        if message.author.id != application_id:
            channel = bot.get_channel(dw_socialmedia_channel_id)
            await channel.send(f'<@&{dw_socialmedia_pings_role_id}>')
        
    # DIRECT MESSAGES TO BOT (DMS)
    # Redirect all dms sent to bot to discord channel
    elif isinstance(message.channel, discord.DMChannel):
        await bot.process_commands(message) # Commands fix
        channel = bot.get_channel(administrator_channel_id)
        log_author_pfp = message.author.display_avatar

        # Ignore if Application is the one sending the DM
        if message.author.id == application_id:
            pass

        else:
            print(f"New DM Incoming, Section 1.5 | {message.author.name} ({message.author.id})")
            # Send the user ID as a normal message (easier to copy and paste on mobile)
            await channel.send(f"{message.author.id}")

            # Embed for messages received by Solstice
            mail_embed = discord.Embed(title = "📮 Dm Received", colour = discord.Color.from_rgb(226,226,226)) # Title, Color
            mail_embed.add_field(name = f"DM received from {message.author.name}", value = (f"{message.content}")) # Show the content of the DM with author's name
            mail_embed.set_thumbnail(url=f"{log_author_pfp}") # Big Image in top right of embed
            mail_embed.set_footer(text=f"ID: {message.author.id}") # User's ID in footer
            mail_embed.timestamp = datetime.now() # Timestamp of when event occured

            # Set gif to empty until it confirms there was a gif in the message
            gif_content = "empty"
            # Message contains a gif
            if "https://tenor.com/view/" in (f"{message.content}"):
                gif_content = (f"{message.content}")

            # Attachments fix for received embed
            if message.attachments:
                if len(message.attachments) == 1:
                    # Check to see if it can be added to embed (image section)
                    if message.attachments[0].url.endswith(('.jpg', '.png', '.jpeg', '.gif')):
                        mail_embed.set_image(url=message.attachments[0].url)
                    # Wrong file format for embed
                    else:
                        mail_embed.add_field(name="", value = f"Attachment: \n{message.attachments[0].url}", inline = False) # Show any attachments

                # Up to 5 attachments logged
                # More than 1 image attched to message
                elif len(message.attachments) == 2:
                    mail_embed.add_field(name = "", value = f"Attachments: \n1. {message.attachments[0].url}\n2. {message.attachments[1].url}", inline = False) # Show any attachments
                # More than 2 images attched to message
                elif len(message.attachments) == 3:
                    mail_embed.add_field(name = "", value = f"Attachments: \n1. {message.attachments[0].url}\n2. {message.attachments[1].url}\n3. {message.attachments[2].url}", inline = False) # Show any attachments
                # More than 3 images attched to message
                elif len(message.attachments) == 4:
                    mail_embed.add_field(name = "", value = f"Attachments: \n1. {message.attachments[0].url}\n2. {message.attachments[1].url}\n3. {message.attachments[2].url}\n4. {message.attachments[3].url}", inline = False) # Show any attachments
                # More than 4 images attched to message
                elif len(message.attachments) == 5:
                    mail_embed.add_field(name = "", value = f"Attachments: \n1. {message.attachments[0].url}\n2. {message.attachments[1].url}\n3. {message.attachments[2].url}\n4. {message.attachments[3].url}\n5. {message.attachments[4].url}", inline = False) # Show any attachments
                # More than 5 images attched to message
                elif len(message.attachments) > 5:
                    mail_embed.add_field(name = "", value = f"Attachments Overload: \n1. {message.attachments[0].url}\n2. {message.attachments[1].url}\n3. {message.attachments[2].url}\n4. {message.attachments[3].url}\n5. {message.attachments[4].url}", inline = False) # Show any attachments

            # Send the embed DM along with the gif (if there is one)
            await channel.send(embed = mail_embed)
            if gif_content != "empty":
                await channel.send(gif_content)

    # END OF SECTION      
    else:
        await bot.process_commands(message) # Commands fix

# Add all basic Member roles when someone joins (Section 2)
@bot.event
async def on_member_join(member):
    print(f"Member Join, Section 2.1  | {member.name} ({member.id})")

    # Club Supporter Role
    supporter_role = discord.utils.get(member.guild.roles, id=club_supporter_role_id)
    # Statistic Roles
    stats_role = discord.utils.get(member.guild.roles, id=dwstats_role_id)
    miles_role = discord.utils.get(member.guild.roles, id=miles_role_id)
    emptyMiles_role = discord.utils.get(member.guild.roles, id=empty_miles_role_id)
    wins_role = discord.utils.get(member.guild.roles, id=wins_role_id)
    emptyWins_role = discord.utils.get(member.guild.roles, id=empty_wins_role_id)
    level_role = discord.utils.get(member.guild.roles, id=level_role_id)
    emptyLevel_role = discord.utils.get(member.guild.roles, id=empty_level_role_id)
    # Ping Roles Divider
    proles_role = discord.utils.get(member.guild.roles, id=proles_pings_role_id)
    # Badge Roles Divider
    broles_role = discord.utils.get(member.guild.roles, id=badges_role_id)
    # Audit Log Channel
    audit_channel = bot.get_channel(audit_log_channel_id)

    await asyncio.sleep(5)
    await member.add_roles(supporter_role)
    await member.add_roles(stats_role)
    await member.add_roles(miles_role)
    await asyncio.sleep(2.5)
    await member.add_roles(emptyMiles_role)
    await member.add_roles(wins_role)
    await member.add_roles(emptyWins_role)
    await asyncio.sleep(2.5)
    await member.add_roles(level_role)
    await member.add_roles(emptyLevel_role)
    await member.add_roles(proles_role)
    #await member.add_roles(broles_role)
    
    print("Member Join Logged, Section 2.2")
    # Log the new Member got the roles
    role_embed = discord.Embed(title = "New Member Roles Given", colour = 0x2ecc71)
    role_embed.add_field(name = "Information:", value = (f"I gave {member.mention} all the basic roles"))
    role_embed.set_footer(text=f"ID: {member.id}") # User's ID in footer
    role_embed.timestamp = datetime.now() # Timestamp of when event occured
    await audit_channel.send(embed = role_embed)

    # Redundancy
    await asyncio.sleep(15)
    await member.add_roles(supporter_role)
    await member.add_roles(stats_role)
    await member.add_roles(miles_role)
    await asyncio.sleep(5)
    await member.add_roles(emptyMiles_role)
    await member.add_roles(wins_role)
    await member.add_roles(emptyWins_role)
    await asyncio.sleep(5)
    await member.add_roles(level_role)
    await member.add_roles(emptyLevel_role)
    await member.add_roles(proles_role)
    #await member.add_roles(broles_role)

# Member's roles are updated post-join (Section 3)
@bot.event
async def on_member_update(before, after):
    print(f"Member Roles Updated, Section 3.1  | {after.name} ({after.id})")

    # Roles
    supporter_role = discord.utils.get(after.guild.roles, id=club_supporter_role_id)
    club_member_role = discord.utils.get(after.guild.roles, id=club_member_role_id)
    # Badges
    badges_role = discord.utils.get(after.guild.roles, id=badges_role_id)
    # Channels
    audit_channel = bot.get_channel(audit_log_channel_id)
    club_tracker_channel = bot.get_channel(club_tracker_channel_id)

    if len(before.roles) < len(after.roles):
        print("Member Roles Updated, Section 3.2")
        new_role = next(role for role in after.roles if role not in before.roles)
        
        if new_role.id == club_member_role_id:
            await after.remove_roles(supporter_role)
            print("Member Roles Updated, Section 3.3")
            log_embed = discord.Embed(title = "🔰 New Club Member", colour = 0xf1c40f)
            log_embed.add_field(name = "Information:", value = (f"{after.mention} has received the Club Member role"))
            log_embed.set_footer(text=f"ID: {after.id}") # User's ID in footer
            log_embed.timestamp = datetime.now() # Timestamp of when event occured
            await audit_channel.send(embed = log_embed)

            # Club Tracker
            ct_embed = discord.Embed(title = "🔰 New Club Member", colour = 0xf1c40f)
            ct_embed.add_field(name = "Information:", value = (f"{after.mention} has received the Club Member role"))
            ct_embed.set_footer(text=f"ID: {after.id}") # User's ID in footer
            ct_embed.timestamp = datetime.now() # Timestamp of when event occured
            empty_ct_embed = discord.Embed(colour = 0xf1c40f)
            empty_ct_embed.add_field(name = f"<t:{int(time.time())}:R>, {after.name.capitalize()} received the Club Member role", value = " ")

            await club_tracker_channel.send(embed = ct_embed)
            await club_tracker_channel.send(f"ID: {after.id} \nEpoch: {int(time.time())}")
            await club_tracker_channel.send(embed = empty_ct_embed)

        elif new_role.id == club_supporter_role_id:
            await after.remove_roles(club_member_role)
            print("Member Roles Updated, Section 3.4")
            log_embed = discord.Embed(title = "🔰 Club Supporter", colour = 0x2ecc71)
            log_embed.add_field(name = "Information:", value = (f"{after.mention} has received the Club Supporter role"))
            log_embed.set_footer(text=f"ID: {after.id}") # User's ID in footer
            log_embed.timestamp = datetime.now() # Timestamp of when event occured
            await audit_channel.send(embed = log_embed)

            # Club Tracker
            ct_embed = discord.Embed(title = "🚫 Removed Club Member", colour = 0x2ecc71)
            ct_embed.add_field(name = "Information:", value = (f"{after.mention} has received the Club Supporter role"))
            ct_embed.set_footer(text=f"ID: {after.id}") # User's ID in footer
            ct_embed.timestamp = datetime.now() # Timestamp of when event occured
            empty_ct_embed = discord.Embed(colour = 0x2ecc71)
            empty_ct_embed.add_field(name = f"<t:{int(time.time())}:R>, {after.name.capitalize()} received the Club Supporter role", value = " ")

            # Get the id of the role that was removed
            for role in before.roles:
                if role not in after.roles:
                    removed_role = role.id
                    # They were a previous Club Member
                    if removed_role == club_member_role_id:
                        await club_tracker_channel.send(embed = ct_embed)
                        await club_tracker_channel.send(f"ID: {after.id} \nEpoch: {int(time.time())}")
                        await club_tracker_channel.send(embed = empty_ct_embed)

        elif new_role.id == trident_badge_role_id:
            await after.add_roles(badges_role)
            print("Member Roles Updated, Section 3.5")
            log_embed = discord.Embed(title = "🔱 New Badge Collected", colour = 0xf1c40f)
            log_embed.add_field(name = "Information:", value = (f"{after.mention} has received the Trident Badge"))
            log_embed.set_footer(text=f"ID: {after.id}") # User's ID in footer
            log_embed.timestamp = datetime.now() # Timestamp of when event occured
            await audit_channel.send(embed = log_embed)

        # Remove the previous statistic role | Miles
        elif new_role.id in listOfMiles:
            for role in before.roles:
                if role.id in listOfMiles:
                    await after.remove_roles(role)
        
        # Remove the previous statistic role | Wins
        elif new_role.id in listOfWins:
            for role in before.roles:
                if role.id in listOfWins:
                    await after.remove_roles(role)

        # Remove the previous statistic role | Level
        elif new_role.id in listOfLevels:
            for role in before.roles:
                if role.id in listOfLevels:
                    await after.remove_roles(role)

#------------------------------------------------ Admin Commands ------------------------------------------------------#

# Talk through bot command !say <message>
@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)
@commands.cooldown(3, 5, commands.BucketType.user)
async def say(ctx, *args):
    await ctx.message.delete()
    await ctx.send("{}".format(" ".join(args)))
    print("Running Commands, !say")

# Send message through bot to another channel !send <channel> <message>
@bot.command(pass_context = True)
@commands.has_permissions(administrator = True)
@commands.cooldown(3, 5, commands.BucketType.user)
async def send(ctx, channel, *args):
    await ctx.message.delete()
    # Remove the <#> from channel input
    channel_id = ''.join(filter(str.isdigit, channel))
    send_channel = bot.get_channel(int(channel_id))
    await send_channel.send("{}".format(" ".join(args)))
    s_sent = await ctx.send(f"**Message sent to <#{channel_id}>**")
    # Delete confirmation
    await asyncio.sleep(5)
    await s_sent.delete()

# Send a user a dm through bot !dm <user> <message>
@bot.command(pass_context = True)
@commands.has_permissions(administrator = True)
@commands.cooldown(3, 5, commands.BucketType.guild)
async def dm(ctx, user: discord.User, *, message):
    await ctx.message.delete()
    await user.send(message)
    s_sent = await ctx.send(f"**Dm succesfully sent to {user.name}**")

    # Send embed to log channel
    audit_channel = bot.get_channel(audit_log_channel_id)
    log_embed = discord.Embed(title = "📧 Dm Sent", colour = 0x3498db)
    log_embed.add_field(name = f"DM sent by Solstice to {user.name}", value = (f"{message}"))
    log_embed.set_thumbnail(url= f"{application_pfp_url}")
    log_embed.set_footer(text=f"ID: {user.id}") # User's ID in footer
    log_embed.timestamp = datetime.now() # Timestamp of when event occured
    await audit_channel.send(f"{user.id}") # Send the user ID as a normal message (easier to copy and paste on mobile)
    await audit_channel.send(embed = log_embed)

    # Delete confirmation message
    await asyncio.sleep(5)
    await s_sent.delete()

# Dm all Club Members a message !dmall <message>
@bot.command()
@commands.has_permissions(administrator = True)
@commands.cooldown(2, 120, commands.BucketType.guild)
async def dmall(ctx, *args):
    await ctx.message.delete()
    s_sent = await ctx.send("**📧 Sending DMs to all Club Members**")
    for guild in bot.guilds:
        for member in guild.members:
            if guild.id == club_server_id:
                try:
                    thumbnail = ctx.guild.icon.url # Command author's pfp
                    log_embed = discord.Embed(title = f"<:DW_1:1248798986748559392><:DW_2:1248798987599876187><:DW_3:1248798985892921454> Hello {member.name.capitalize()},", colour = discord.Color.from_rgb(250, 250, 250))
                    log_embed.set_thumbnail(url=f"{thumbnail}") # Big Image in top right of embed
                    log_embed.add_field(name = "", value = ("{}".format(" ".join(args))), inline = False)
                    log_embed.set_footer(text = f"{ctx.message.guild.name}")
                    log_embed.timestamp = datetime.now() # Timestamp of when event occured
                    await member.send(embed = log_embed)
                    
                    print(f"DM sent to {member}")
                    await asyncio.sleep(3)

                # Member was unable to recieve the dm
                except:
                    print(f"Unable to send DM to {member}")
                    pass 
            # Pass Members that are not in the correct server
            else:
                pass
        # Not a guild Member
        else:
            pass
    # Loop ends
    await ctx.send("**📧 Finished sending DMs to all Club Members**")
    await s_sent.delete()

# Logs all member's roles and join dates !logmembers
@bot.command()
@commands.has_permissions(administrator = True)
@commands.cooldown(2, 120, commands.BucketType.guild)
async def logmembers(ctx):
    await ctx.message.delete()
    intents = discord.Intents.default()
    intents.members = True
    channel = bot.get_channel(member_logs_channel_id)
    # Counter System for Progress
    total_members = str(ctx.guild.member_count)
    counter = 0
    five_counter = 5
    counter_message = await ctx.send(f"**🔄 {str(counter)} out of {str(total_members)} Members currently logged.**")

    # Loop through all Members
    for guild in bot.guilds:
        for member in guild.members:
            if guild.id != club_server_id:
                pass
            else:
                # Embed Message
                logging = discord.Embed(title = '', description = f'{member.mention}', colour = discord.Color.from_rgb(0, 0, 0)) # Member's name and embed color
                logging.set_author(name = f"{member}", icon_url = str(member.display_avatar)) # Member's ID at top
                roles = [role.mention for role in member.roles[1:]]
                num_of_roles = (str(len(roles)))
                roles = (" ".join(roles))
                logging.add_field(name = 'Account Created:', value = f'{member.created_at.strftime("%m/%d/%y")}', inline = True) # Discord join date
                logging.add_field(name = 'Joined Server:', value = f'{member.joined_at.strftime("%m/%d/%y")}', inline = True) # Server join date
                logging.add_field(name = f'✅ Roles [{num_of_roles}]', value = f"{roles}", inline = False) # List out the member's roles
                logging.set_footer(text=f"{member.id}") # Text + ID in footer
                logging.timestamp = datetime.now() # Timestamp of when event occured
                await channel.send(embed = logging)
                
                # Counter system
                counter +=1
                if counter >= five_counter:
                    await counter_message.edit(content = f"**🔄 {counter} out of {total_members} Members currently logged.**")
                    # Add 5 more to the five counter
                    five_counter += 5
                    await asyncio.sleep(2)
                # Skip every 5
                else:
                    await asyncio.sleep(2)
                    pass
    # Loop ends
    await counter_message.edit(content = f"**🔄 {counter} out of {total_members} Members currently logged.**")

# Reset everyone's nickname (everyone under bot role) !resetnick
@bot.command()
@commands.has_permissions(administrator = True)
@commands.cooldown(2, 120, commands.BucketType.guild)
async def resetnick(ctx):
    await ctx.message.delete()
    # Counter System for Progress
    total_members = str(ctx.guild.member_count)
    counter = 0
    five_counter = 5
    counter_message = await ctx.send(f"**🔄 {str(counter)} out of {str(total_members)} nicknames are currently reset.**")

    # Loop to reset all nicknames
    for member in ctx.guild.members: # loop through every member in the guild
        try:
            await member.edit(nick=None) # reset their nickname
            counter +=1
        except:
            print(f"I was unable to change {member}'s nickname.")
            counter +=1
            pass
        # Counter system
        if counter >= five_counter:
            await counter_message.edit(content = f"**🔄 {str(counter)} out of {str(total_members)} nicknames are currently reset.**")
            # Add 5 more to the five counter
            five_counter += 5
            await asyncio.sleep(2)
        # Skip every 5
        else:
            await asyncio.sleep(2) # Keeps bot from rate limiting
            pass

    # Loop ends
    await counter_message.edit(content = f"**🔄 {str(counter)} out of {str(total_members)} nicknames are currently reset.**")

# Change everyone's nickname (everyone under bot role) !trollnick <name>
@bot.command()
@commands.has_permissions(administrator = True)
@commands.cooldown(2, 120, commands.BucketType.guild)
async def trollnick(ctx, *args):
    await ctx.message.delete()
    # Counter System for Progress
    total_members = str(ctx.guild.member_count)
    counter = 0
    five_counter = 5
    nickname = str("{}".format(" ".join(args)))
    counter_message = await ctx.send(f"**🔄 {str(counter)} out of {str(total_members)} nicknames are currently changed to __{nickname}__.**")

    # Loop to change all member's nicknames
    for member in ctx.guild.members: # loop through every member in the guild
        try:
            await member.edit(nick=f'{nickname}') # Reset their nickname
            counter +=1
        except:
            print(f"I was unable to change {member}'s nickname.")
            counter +=1
            pass
        # Counter system
        if counter >= five_counter:
            await counter_message.edit(content = f"**🔄 {str(counter)} out of {str(total_members)} nicknames are currently changed to __{nickname}__.**")
            # Add 5 more to the five counter
            five_counter += 5
            await asyncio.sleep(2)
        # Skip every 5
        else:
            await asyncio.sleep(2) # Keeps bot from rate limiting
            pass

    # Loop ends
    await counter_message.edit(content = f"**🔄 {str(counter)} out of {str(total_members)} nicknames are currently changed to __{nickname}__..**")

# Check bot ping command !ping
@bot.command()
@commands.has_permissions(administrator = True)
@commands.cooldown(3, 5, commands.BucketType.user)
async def ping(ctx):
    await ctx.message.delete()
    # Send embed
    warning_embed = discord.Embed()
    warning_embed.set_author(name = f"Ping: {round(bot.latency * 1000)}ms", icon_url = "https://cdn.discordapp.com/attachments/935672317512650812/1155259162553503864/Ping_Icon.png") 
    await ctx.send(embed = warning_embed)

# Get current Epoch command !epoch
@bot.command()
@commands.has_permissions(administrator = True)
@commands.cooldown(3, 5, commands.BucketType.user)
async def epoch(ctx):
    await ctx.message.delete()
    await ctx.send(f"{int(round(time.time(), 0))}")
    await ctx.send(f"<t:{int(round(time.time(), 0))}:R>")
            
#------------------------------------------------ Slash Commands ------------------------------------------------------#

tree = app_commands.CommandTree

# Makes the is_owner requirement to be used in slash commands
def is_owner():
    def predicate(interaction : discord.Interaction):
        if interaction.user.id == interaction.guild.owner_id:
            return True
    return app_commands.check(predicate)

# Catch Errors/Cooldowns with the slash commands
@bot.tree.error
async def on_app_command_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    print(f"Slash Commands Error has been triggered (Possible Cooldown)")
    if isinstance(error, app_commands.CommandOnCooldown):
        await interaction.response.send_message(f'Command on cooldown, wait {round(error.retry_after, 0)} seconds.', ephemeral= True)
    #else:
        #raise error
    
# Update Drive World Statistics slash Command
@bot.tree.command(name= "stats", description= "Update your Drive World Statistics")
@app_commands.describe(miles = "Enter how many miles you have driven in Drive World", wins = "Enter the number of Wins you have in Drive World", level = "Enter your level in Drive World")
@app_commands.checks.cooldown(1, 25, key = lambda i: (i.guild_id, i.user.id)) # Regulate per Discord User
async def stats(interaction: discord.Interaction, miles: int, wins: int, level: int):
    member = interaction.user
    print(f"Member has updated their Drive World Statistics, Section 4.1  | {member.name} ({member.id})")
    #---------------------------------------- Library (START)----------------------------------------#
    # Mile Statistic Role IDs
    empty_miles_role_id = 1242165883384627221
    m500less = 1242563310155468933
    m500 = 1241887737272074380
    m1000 = 1241887743043436575
    m2500 = 1241887745291325484
    m5000 = 1241888317553901619
    m7500 = 1242282207226101911
    m10000 = 1241888315091976252
    m15000 = 1241889398807855155
    m20000 = 1241889403614269490
    m25000 = 1241888500010324020
    m30000 = 1241889401580028014
    m35000 = 1241890082877735022
    m40000 = 1241890079018979360
    m45000 = 1241890017337540721
    m50000 = 1241890223722598500
    m55000 = 1241902290114445422
    m60000 = 1241902291884183592
    m65000 = 1241902697502736477
    m70000 = 1241902286251364352
    m75000 = 1241902221935906907
    m80000 = 1241902224498491402
    m85000 = 1241902699684040725
    m90000 = 1241902699948015758
    m95000 = 1241902697586626560
    m100000 = 1241902701135265822
    
    # Mile Statistic Roles
    mNone = interaction.guild.get_role(empty_miles_role_id)
    m500less = interaction.guild.get_role(m500less)
    m500 = interaction.guild.get_role(m500)
    m1000 = interaction.guild.get_role(m1000)
    m2500 = interaction.guild.get_role(m2500)
    m5000 = interaction.guild.get_role(m5000)
    m7500 = interaction.guild.get_role(m7500)
    m10000 = interaction.guild.get_role(m10000)
    m15000 = interaction.guild.get_role(m15000)
    m20000 = interaction.guild.get_role(m20000)
    m25000 = interaction.guild.get_role(m25000)
    m30000 = interaction.guild.get_role(m30000)
    m35000 = interaction.guild.get_role(m35000)
    m40000 = interaction.guild.get_role(m40000)
    m45000 = interaction.guild.get_role(m45000)
    m50000 = interaction.guild.get_role(m50000)
    m55000 = interaction.guild.get_role(m55000)
    m60000 = interaction.guild.get_role(m60000)
    m65000 = interaction.guild.get_role(m65000)
    m70000 = interaction.guild.get_role(m70000)
    m75000 = interaction.guild.get_role(m75000)
    m80000 = interaction.guild.get_role(m80000)
    m85000 = interaction.guild.get_role(m85000)
    m90000 = interaction.guild.get_role(m90000)
    m95000 = interaction.guild.get_role(m95000)
    m100000 = interaction.guild.get_role(m100000)

    # Win Statistic Role IDs
    empty_wins_role_id = 1242165857417695273
    w50less = 1242563312265330739
    w50 = 1242529870408454254
    w100 = 1241891412681818152
    w200 = 1241891414581842021
    w300 = 1241891417119391856
    w400 = 1241891418767884371
    w500 = 1241891421246459945
    w600 = 1241891423402332170
    w700 = 1241891602226479166
    w800 = 1241891604260978779
    w900 = 1241891605884043445
    w1000 = 1241891607951970325
    w1100 = 1241902218081341452
    w1200 = 1241902220442734672
    w1300 = 1241891666982473819
    w1400 = 1241902288008773682
    w1500 = 1241891668685488129
    w1600 = 1241902701680263240
    w1700 = 1241902701885919253
    w1800 = 1241902703173701793
    w1900 = 1241902779870478337
    w2000 = 1241891410727145523
     
    # Win Statistic Roles
    wNone = interaction.guild.get_role(empty_wins_role_id)
    w50less = interaction.guild.get_role(w50less)
    w50 = interaction.guild.get_role(w50)
    w100 = interaction.guild.get_role(w100)
    w200 = interaction.guild.get_role(w200)
    w300 = interaction.guild.get_role(w300)
    w400 = interaction.guild.get_role(w400)
    w500 = interaction.guild.get_role(w500)
    w600 = interaction.guild.get_role(w600)
    w700 = interaction.guild.get_role(w700)
    w800 = interaction.guild.get_role(w800)
    w900 = interaction.guild.get_role(w900)
    w1000 = interaction.guild.get_role(w1000)
    w1100 = interaction.guild.get_role(w1100)
    w1200 = interaction.guild.get_role(w1200)
    w1300 = interaction.guild.get_role(w1300)
    w1400 = interaction.guild.get_role(w1400)
    w1500 = interaction.guild.get_role(w1500)
    w1600 = interaction.guild.get_role(w1600)
    w1700 = interaction.guild.get_role(w1700)
    w1800 = interaction.guild.get_role(w1800)
    w1900 = interaction.guild.get_role(w1900)
    w2000 = interaction.guild.get_role(w2000)

    # Level Statistic Role IDs
    empty_level_role_id = 1242165545130786836
    l5less = 1242563284419481660
    l5 = 1241892210279190658
    l10 = 1241892213169066054
    l15 = 1241892214825680906
    l20 = 1241892216402608248
    l25 = 1241892218403553321
    l30 = 1241892220378939443
    l35 = 1241892222517903422
    l40 = 1241892223977521194
    l45 = 1241892225953173626
    l50 = 1241892397776900187

    # Level Statistic Roles
    lNone = interaction.guild.get_role(empty_level_role_id)
    l5less = interaction.guild.get_role(l5less)
    l5 = interaction.guild.get_role(l5)
    l10 = interaction.guild.get_role(l10)
    l15 = interaction.guild.get_role(l15)
    l20 = interaction.guild.get_role(l20)
    l25 = interaction.guild.get_role(l25)
    l30 = interaction.guild.get_role(l30)
    l35 = interaction.guild.get_role(l35)
    l40 = interaction.guild.get_role(l40)
    l45 = interaction.guild.get_role(l45)
    l50 = interaction.guild.get_role(l50)
    #---------------------------------------- Library (END) ----------------------------------------#

    await interaction.response.send_message(f'Drive World Statistics Updated!', ephemeral= True)

    # MILES
    if miles < 100000:
        if miles < 95000:
            if miles < 90000:
                if miles < 85000:
                    if miles < 80000:
                        if miles < 75000:
                            if miles < 70000:
                                if miles < 65000:
                                    if miles < 60000:
                                        if miles < 55000:
                                            if miles < 50000:
                                                if miles < 45000:
                                                    if miles < 40000:
                                                        if miles < 35000:
                                                            if miles < 30000:
                                                                if miles < 25000:
                                                                    if miles < 20000:
                                                                        if miles < 15000:
                                                                            if miles < 10000:
                                                                                if miles < 7500:
                                                                                    if miles < 5000:
                                                                                        if miles < 2500:
                                                                                            if miles < 1000:
                                                                                                if miles < 500:
                                                                                                    await member.add_roles(m500less)
                                                                                                else:
                                                                                                    await member.add_roles(m500)
                                                                                            else:
                                                                                                await member.add_roles(m1000)
                                                                                        else:
                                                                                            await member.add_roles(m2500)
                                                                                    else:
                                                                                        await member.add_roles(m5000)
                                                                                else:
                                                                                    await member.add_roles(m7500)
                                                                            else:
                                                                                await member.add_roles(m10000)
                                                                        else:
                                                                            await member.add_roles(m15000)
                                                                    else:
                                                                        await member.add_roles(m20000)
                                                                else:
                                                                    await member.add_roles(m25000)
                                                            else:
                                                                await member.add_roles(m30000)
                                                        else:
                                                            await member.add_roles(m35000)
                                                    else:
                                                        await member.add_roles(m40000)
                                                else:
                                                    await member.add_roles(m45000)
                                            else:
                                                await member.add_roles(m50000)
                                        else:
                                            await member.add_roles(m55000)
                                    else:
                                        await member.add_roles(m60000)
                                else:
                                    await member.add_roles(m65000)
                            else:
                                await member.add_roles(m70000)
                        else:
                            await member.add_roles(m75000)
                    else:
                        await member.add_roles(m80000)
                else:
                    await member.add_roles(m85000)
            else:
                await member.add_roles(m90000)
        else:
            await member.add_roles(m95000)
    else:
        await member.add_roles(m100000)   
    await asyncio.sleep(2.5)

    # WINS
    if wins < 2000:
        if wins < 1900:
            if wins < 1800:
                if wins < 1700:
                    if wins < 1600:
                        if wins < 1500:
                            if wins < 1400:
                                if wins < 1300:
                                    if wins < 1200:
                                        if wins < 1100:
                                            if wins < 1000:
                                                if wins < 900:
                                                    if wins < 800:
                                                        if wins < 700:
                                                            if wins < 600:
                                                                if wins < 500:
                                                                    if wins < 400:
                                                                        if wins < 300:
                                                                            if wins < 200:
                                                                                if wins < 100:
                                                                                    if wins < 50:
                                                                                        await member.add_roles(w50less)
                                                                                    else:
                                                                                        await member.add_roles(w50)
                                                                                else:
                                                                                    await member.add_roles(w100)
                                                                            else:
                                                                                await member.add_roles(w200)
                                                                        else:
                                                                            await member.add_roles(w300)
                                                                    else:
                                                                        await member.add_roles(w400)
                                                                else:
                                                                    await member.add_roles(w500)
                                                            else:
                                                                await member.add_roles(w600)
                                                        else:
                                                            await member.add_roles(w700)
                                                    else:
                                                        await member.add_roles(w800)
                                                else:
                                                    await member.add_roles(w900)
                                            else:
                                                await member.add_roles(w1000)
                                        else:
                                            await member.add_roles(w1100)
                                    else:
                                        await member.add_roles(w1200)
                                else:
                                    await member.add_roles(w1300)
                            else:
                                await member.add_roles(w1400)
                        else:
                            await member.add_roles(w1500)
                    else:
                        await member.add_roles(w1600)
                else:
                    await member.add_roles(w1700)
            else:
                await member.add_roles(w1800)
        else:
            await member.add_roles(w1900)
    else:
        await member.add_roles(w2000)
    await asyncio.sleep(2.5)

    # LEVEL
    if level < 50:
        if level < 45:
            if level < 40:
                if level < 35:
                    if level < 30:
                        if level < 25:
                            if level < 20:
                                if level < 15:
                                    if level < 10:
                                        if level < 5:
                                            await member.add_roles(l5less)
                                        else:
                                            await member.add_roles(l5)
                                    else:
                                        await member.add_roles(l10)
                                else:
                                    await member.add_roles(l15)
                            else:
                                await member.add_roles(l20)
                        else:
                            await member.add_roles(l25)
                    else:
                        await member.add_roles(l30)
                else:
                    await member.add_roles(l35)
            else:
                await member.add_roles(l40)
        else:
            await member.add_roles(l45)
    else:
        await member.add_roles(l50)
    await asyncio.sleep(2.5)

    await interaction.response.send_message(f'Drive World Statistics Updated!', ephemeral= True)

# Clear Drive World Statistics slash Command
@bot.tree.command(name= "clear-stats", description= "Clear your Drive World Statistics")
@app_commands.checks.cooldown(1, 25, key = lambda i: (i.guild_id, i.user.id)) # Regulate per Discord User
async def clearstats(interaction: discord.Interaction):
    member = interaction.user
    print(f"Member has cleared their Drive World Statistics, Section 4.2  | {member.name} ({member.id})")

    # Mile Statistic Role
    empty_miles_role_id = 1242165883384627221
    mNone = interaction.guild.get_role(empty_miles_role_id)
    # Win Statistic Role
    empty_wins_role_id = 1242165857417695273
    wNone = interaction.guild.get_role(empty_wins_role_id)
    # Level Statistic Role
    empty_level_role_id = 1242165545130786836
    lNone = interaction.guild.get_role(empty_level_role_id)

    await interaction.response.send_message(f'Drive World Statistics Cleared!', ephemeral= True)

    await member.add_roles(mNone)
    await asyncio.sleep(2.5)
    await member.add_roles(wNone)
    await asyncio.sleep(2.5)
    await member.add_roles(lNone)

# View how many points you currently averaging per day
@bot.tree.command(name= "average", description= "View how many points you currently averaging per day in Drive World")
@app_commands.describe(points = "Enter how many points you currently have in Drive World")
@app_commands.checks.cooldown(3, 25, key = lambda i: (i.guild_id, i.user.id)) # Regulate per Discord User
async def average(interaction: discord.Interaction, points: int):
    member = interaction.user
    print(f"Member viewed how many points they are currently averaging per day, Section 4.3  | {member.name} ({member.id})")

    channel = bot.get_channel(club_tracker_channel_id)
    messages = [message.content async for message in channel.history(limit=500)]
    member_id = str(member.id)

    for msg in messages:
        if member_id in msg:
            message = str(msg.replace(f'{member_id}', ''))
            message1 = str(message.replace(' ', ''))
            past_epoch = int(''.join(e for e in message1 if e.isdigit()))
            current_epoch = int(time.time())
            seconds = current_epoch - past_epoch
            minutes = seconds / 60
            hours = minutes / 60
            days = hours / 24
            if days < 1:
                days = 1
            average = points / days    
            await interaction.response.send_message(f"You average **{round(average, 1)}** points per day.", ephemeral= False)
    await interaction.response.send_message(f"Your points cannot currently be averaged.", ephemeral= True)

# Administrator - Update a User's roles to have all the Basic ones needed
@bot.tree.command(name= "update-roles", description= "Reset a Member's roles to default ones")
@app_commands.checks.cooldown(5, 25, key = lambda i: (i.guild_id, i.user.id)) # Regulate per Discord User
@is_owner()
async def updateroles(interaction: discord.Interaction, member: discord.Member):
    print(f"A Member's roles have been updated by an Admin, Section 4.4'  | {member.name} ({member.id})")

    # Generic Roles
    club_member_role_id = 1241577709985992764
    club_supporter_role_id = 1241944353916583947
    club_member_role = interaction.guild.get_role(club_member_role_id)
    club_supporter_role = interaction.guild.get_role(club_supporter_role_id)
    # Statistic Roles
    dwstats_role_id = 1241887741336092683
    miles_role_id = 1241887061384888410
    empty_miles_role_id = 1242165883384627221
    wins_role_id = 1241887086479413338
    empty_wins_role_id = 1242165857417695273
    level_role_id = 1241887088563982386
    empty_level_role_id = 1242165545130786836

    dwstats_role = interaction.guild.get_role(dwstats_role_id)
    miles_role = interaction.guild.get_role(miles_role_id)
    empty_miles_role = interaction.guild.get_role(empty_miles_role_id)
    wins_role = interaction.guild.get_role(wins_role_id)
    empty_wins_role = interaction.guild.get_role(empty_wins_role_id)
    level_role = interaction.guild.get_role(level_role_id)
    empty_level_role = interaction.guild.get_role(empty_level_role_id)
    # Ping Roles
    proles_pings_role_id = 1242173050259247326
    proles_pings_role = interaction.guild.get_role(proles_pings_role_id)

    await interaction.response.send_message(f"{member.mention}'s roles have been updated!", ephemeral= True)

    if club_member_role not in member.roles and club_supporter_role not in member.roles:
        await member.add_roles(club_supporter_role)
    
    await member.add_roles(dwstats_role)
    await asyncio.sleep(1)
    await member.add_roles(miles_role)
    await asyncio.sleep(1)
    await member.add_roles(empty_miles_role)
    await asyncio.sleep(1)
    await member.add_roles(wins_role)
    await asyncio.sleep(1)
    await member.add_roles(empty_wins_role)
    await asyncio.sleep(1)
    await member.add_roles(level_role)
    await asyncio.sleep(1)
    await member.add_roles(empty_level_role)
    await asyncio.sleep(1)
    await member.add_roles(proles_pings_role)

# Administrator - View average daily points of a Member
@bot.tree.command(name= "member-average", description= "View how many points someone is currently averaging per day in Drive World")
@app_commands.describe(points = "Enter how many points the Member currently has in Drive World")
@app_commands.checks.cooldown(5, 10, key = lambda i: (i.guild_id, i.user.id)) # Regulate per Discord User
@is_owner()
async def average(interaction: discord.Interaction, member: discord.Member, points: int):
    print(f"Admin viewed how many points a Member is currently averaging per day, Section 4.5  | {member.name} ({member.id})")

    channel = bot.get_channel(club_tracker_channel_id)
    messages = [message.content async for message in channel.history(limit=500)]
    member_id = str(member.id)

    for msg in messages:
        if member_id in msg:
            message = str(msg.replace(f'{member_id}', ''))
            message1 = str(message.replace(' ', ''))
            past_epoch = int(''.join(e for e in message1 if e.isdigit()))
            current_epoch = int(time.time())
            seconds = current_epoch - past_epoch
            minutes = seconds / 60
            hours = minutes / 60
            days = hours / 24
            if days < 1:
                days = 1
            average = points / days    
            await interaction.response.send_message(f"{member.mention} is averaging **{round(average, 1)}** points per day.", ephemeral= False)
    await interaction.response.send_message(f"{member.mention} points cannot currently be averaged.", ephemeral= True)

# Administrator - Reset Club Member role, so it logs in Club Tracker for beginning of new season
@bot.tree.command(name= "club-reset", description= "Re-add Club Member to all current Club Members")
@app_commands.checks.cooldown(5, 25, key = lambda i: (i.guild_id, i.user.id)) # Regulate per Discord User
async def clubreset(interaction: discord.Interaction):

    print(f"Admin is reseting Club Member role, Section 4.6")
    confirmed_role = interaction.guild.get_role(confirmed_role_id)
    club_member_role = interaction.guild.get_role(club_member_role_id)
    await interaction.response.send_message(f"Club Member role is being reset.", ephemeral= True)

    # Loop through all Members
    for member in interaction.guild.members:
        if club_member_role in member.roles:
            print(member.name)
            await member.remove_roles(club_member_role)
            await member.add_roles(confirmed_role)
            await asyncio.sleep(2.5) # Keeps bot from rate limiting

        elif confirmed_role in member.roles:
            print(member.name)
            await member.remove_roles(confirmed_role)
            await member.add_roles(club_member_role)
            await asyncio.sleep(2.5) # Keeps bot from rate limiting

#------------------------------------------------ List out all Commands ------------------------------------------------------#

# Administrator Commands Embed
administrator_cmds_embed = discord.Embed(title = 'Administrator Commands', colour = discord.Color.from_rgb(0, 0, 0))
administrator_cmds_embed.set_thumbnail(url=f"{server_pfp_url}") # Big Image in top right of embed
administrator_cmds_embed.add_field(name = '💬⠀ !say', value = "Enter a message for the bot to repeat in the same channel", inline = True)
administrator_cmds_embed.add_field(name = '📤⠀ !send', value = "Enter a channel and a message for the bot to send in that specific channel", inline = True)
administrator_cmds_embed.add_field(name = '📧⠀ !dm', value = "Enter a User ID and message to be sent to that user through the bot's Dms", inline = True)
administrator_cmds_embed.add_field(name = '🏷️⠀ !dmall', value = "Enter a message to be sent to all Members of the server through the bot's Dms", inline = True)
administrator_cmds_embed.add_field(name = '📋⠀ !logmembers', value = "Log information about each Server Member including roles, dates, etc.", inline = True)
administrator_cmds_embed.add_field(name = '🧭⠀ !clubreset', value = "Run twice to remove and add club member and start the club tracker channel", inline = True)
administrator_cmds_embed.add_field(name = '♻️⠀ !resetnick', value = "Reset all Member's nicknames to their default value", inline = True)
administrator_cmds_embed.add_field(name = '☢️⠀ !trollnick', value = "Enter a name that everyone's nickname will be changed to", inline = True)
administrator_cmds_embed.add_field(name = '🏓⠀ !ping', value = "Get the bot's current latency", inline = True)
administrator_cmds_embed.add_field(name = '⏱️⠀ !epoch', value = "Get the current epoch time", inline = True)
administrator_cmds_embed.set_footer(text=f"Created by @Equinox21")
administrator_cmds_embed.timestamp = datetime.now() # Timestamp of when event occured

# Member Commands Embed
member_cmds_embed = discord.Embed(title = 'Member Commands', colour = discord.Color.from_rgb(0, 0, 0))
member_cmds_embed.set_thumbnail(url=f"{server_pfp_url}") # Big Image in top right of embed
member_cmds_embed.add_field(name = '📊⠀ /stats', value = "Update your server roles to accurately represent what your current Drive World statistics are", inline = True)
member_cmds_embed.add_field(name = '📈⠀ /average', value = "See how many points you are averaging per day in Drive World", inline = False)
member_cmds_embed.add_field(name = '<:Bloxlink:1242325891313307679>⠀ /verify', value = "Verify your Roblox account with Bloxlink", inline = True)
member_cmds_embed.add_field(name = '<:Bloxlink:1242325891313307679>⠀ /getrole', value = "Update your roles for this specific Server", inline = True)
member_cmds_embed.add_field(name = '<:Bloxlink:1242325891313307679>⠀ /getinfo', value = "Retrieve the Roblox username of a Server Member", inline = True)
member_cmds_embed.add_field(name = '🎉⠀ /messages', value = "View how many messages someone has sent", inline = True)
member_cmds_embed.add_field(name = '🔎⠀ /wiki', value = "Find information about cars in Drive World", inline = True)
member_cmds_embed.add_field(name = '🔎⠀ /diff', value = "Show edits/changes in the Drive World wiki", inline = True)
member_cmds_embed.set_footer(text=f"Created by @Equinox21")
member_cmds_embed.timestamp = datetime.now() # Timestamp of when event occured

# ------------------------ FULL ADMINISTRATOR VIEW ------------------------ #

class AdminSelect(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label = "Administrator Commands", emoji = "⚙️"),
            discord.SelectOption(label = "Member Commands", emoji = "🔨"),
            ]
        super().__init__(placeholder = "Select an option", max_values = 1, min_values = 1, options = options)
    async def callback(self, interaction: discord.Interaction):

        if self.values[0] == "Administrator Commands":
            # Administrator Commands
            await interaction.response.edit_message(embed = administrator_cmds_embed)

        elif self.values[0] == "Member Commands":
            # Member Commands
            await interaction.response.edit_message(embed = member_cmds_embed)

class AdminSelectView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(AdminSelect())

# ------------------------ MEMBER VIEW ------------------------ #
        
class MemberSelect(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label = "Member Commands", emoji = "🔨"),
            ]
        super().__init__(placeholder = "Select an option", max_values = 1, min_values = 1, options = options)
    async def callback(self, interaction: discord.Interaction):

        if self.values[0] == "Member Commands":
            # Member Commands
            await interaction.response.edit_message(embed = member_cmds_embed)

class MemberSelectView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(MemberSelect())

# ------------------------ COMMAND TO RUN ALL ------------------------ #
        
@bot.command()
@commands.cooldown(2, 15, commands.BucketType.user)
async def help(ctx):
        await ctx.message.delete()
        print(f"Help command used, Section 5.1  | {ctx.author.name} ({ctx.author.id})")
        
        # Has Administrator
        if ctx.message.author.guild_permissions.administrator:
            # Will only send the full menu in Hidden channels
            if ctx.message.channel.id == administrator_channel_id: 
                # Administrator Embed
                await ctx.send(embed = administrator_cmds_embed, view = AdminSelectView())
            else:
                # Normal Member Embed
                await ctx.send(embed = member_cmds_embed, view = MemberSelectView())
        # Normal Member Embed
        else: 
            await ctx.send(embed = member_cmds_embed, view = MemberSelectView())

#------------------------------------------------ Error Messages ------------------------------------------------------#

@bot.event
async def on_command_error(ctx, error):
    print("Running Errors Section")
    # User errors
    # Cooldown error (deletes command)
    if isinstance(error, commands.CommandOnCooldown):
        error_msg_1 = "This command is on cooldown, please try again in {:.0f} seconds.".format(error.retry_after)
        await ctx.message.delete()
        print("Error 1, cooldown")
        # Send warning embed
        warning_embed = discord.Embed(colour = warning_embed_color)
        warning_embed.set_author(name = error_msg_1, icon_url = warning_embed_icon) 
        warning_msg = await ctx.send(embed = warning_embed)
        await asyncio.sleep(10)
        await warning_msg.delete()

    # Missing role error (deletes command)
    elif isinstance(error, commands.MissingRole):
        error_msg_2 = "You do not have the role needed to run this command."
        await ctx.message.delete()
        print("Error 2, missing role")
        # Send warning embed
        warning_embed = discord.Embed(colour = warning_embed_color)
        warning_embed.set_author(name = error_msg_2, icon_url = warning_embed_icon) 
        warning_msg = await ctx.send(embed = warning_embed)
        await asyncio.sleep(10)
        await warning_msg.delete()

    # Missing permissions error (deletes command)
    elif isinstance(error, commands.MissingPermissions):
        error_msg_3 = "You do not have the permissions needed to run this command."
        await ctx.message.delete()
        print("Error 3, missing permissions")
        # Send warning embed
        warning_embed = discord.Embed(colour = warning_embed_color)
        warning_embed.set_author(name = error_msg_3, icon_url = warning_embed_icon) 
        warning_msg = await ctx.send(embed = warning_embed)
        await asyncio.sleep(10)
        await warning_msg.delete()

    elif isinstance(error, commands.MissingRequiredArgument):
        error_msg_4 = "You did not provide a required argument needed to run this command."
        await ctx.message.delete()
        print("Error 4, missing agruement")
        # Send warning embed
        warning_embed = discord.Embed(colour = warning_embed_color)
        warning_embed.set_author(name = error_msg_4, icon_url = warning_embed_icon) 
        warning_msg = await ctx.send(embed = warning_embed)
        await asyncio.sleep(10)
        await warning_msg.delete()

    elif isinstance(error, commands.MissingRequiredAttachment):
        error_msg_5 = "You did not provide a required attachment needed to run this command."
        await ctx.message.delete()
        print("Error 5, missing attachment")
        # Send warning embed
        warning_embed = discord.Embed(colour = warning_embed_color)
        warning_embed.set_author(name = error_msg_5, icon_url = warning_embed_icon) 
        warning_msg = await ctx.send(embed = warning_embed)
        await asyncio.sleep(10)
        await warning_msg.delete()

    # Bot errors
    # Bot missing permissions error
    elif isinstance(error, commands.BotMissingPermissions):
        bot_error_msg_1 = "I do not have the permissions needed to run this command."
        await ctx.message.delete()
        print("Bot Error 1, missing permissions")
        # Send warning embed
        warning_embed = discord.Embed(colour = warning_embed_color)
        warning_embed.set_author(name = bot_error_msg_1, icon_url = warning_embed_icon) 
        warning_msg = await ctx.send(embed = warning_embed)
        await asyncio.sleep(10)
        await warning_msg.delete()

    # Bot missing role error
    elif isinstance(error, commands.BotMissingRole):
        bot_error_msg_2 = "I do not have the role needed to run this command."
        await ctx.message.delete()
        print("Bot Error 2, missing role")
        # Send warning embed
        warning_embed = discord.Embed(colour = warning_embed_color)
        warning_embed.set_author(name = bot_error_msg_2, icon_url = warning_embed_icon) 
        warning_msg = await ctx.send(embed = warning_embed)
        await asyncio.sleep(10)
        await warning_msg.delete()
    
    # There was an undefined Error
    #else:
        # Send warning embed
        #warning_embed = discord.Embed(colour = warning_embed_color)
        #warning_embed.set_author(name = "There was an error performing this action.", icon_url = warning_embed_icon) 
        #warning_msg = await ctx.send(embed = warning_embed)
        #await asyncio.sleep(10)
        #await warning_msg.delete()

# Run the Bot
bot.run(TOKEN)