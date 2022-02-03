import discord
from discord.ext import commands

from datetime import datetime
import datetime

from peewee import *

import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from urllib import parse, request
from random import randrange

import wikipedia
import requests
import logging
import sqlite3
import json


def log_com(ctx):

    ctx.author.name


#Define KarlFranz
KarlFranz = commands.Bot(command_prefix="+", description="I AM KARL FRANZ, PRINCE-ELECTOR AND EMPEROR!")

#Commands
@KarlFranz.command()
async def hail(ctx):
    log_com(ctx)
    await ctx.send("GREETINGS")

@KarlFranz.command()
async def tester(ctx):
    print(ctx)
    print(ctx.message)
    print(ctx.command)

@KarlFranz.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="The server dedicated to containing Karl Franz.", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://static.wikia.nocookie.net/warhammerfb/images/f/f5/Empire_Shield.png/revision/latest/scale-to-width-down/250?cb=20150517025022")

    await ctx.send(embed=embed)

@KarlFranz.command()
async def picsearch(ctx, term):
    url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/ImageSearchAPI"
    querystring = {"q": term, "pageNumber": "1", "pageSize": "1", "autoCorrect": "true"}
    headers = {
        'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com",
        'x-rapidapi-key': "40a1081129msh86e084bb5711ab5p1f7a9djsnf42b275c6324"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    diction = json.loads(response.text)
    await ctx.send(diction["value"][0]["url"])


@KarlFranz.command()
async def insult(ctx):
    insult = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=text").content
    await ctx.send(insult.decode("utf-8"))


@KarlFranz.command()
async def wiki(ctx, query):
    try:
        await ctx.send(wikipedia.page(query, auto_suggest=False).url)
    except Exception as err:
        insult = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=text").content
        await ctx.send(insult.decode("utf-8") + "\n\n" + str(err))


@KarlFranz.command()
async def ealert(ctx, target):
    user = ctx.author.name
    r_code = email_ping(target, user)
    if r_code == 1:
        await ctx.send(f"{target} has been summoned!", delete_after=1)
        await ctx.message.delete(delay=1)
    if r_code == 0:
        await ctx.send(f"{target} has been obfuscated by Chaos")



@KarlFranz.command()
async def stats(ctx, name):
    print(name)

#@KarlFranz.command()
#async def newuser(ctx, *string):
    #username = string[0]
   # nickname = string[1]
  #  bio = string[1:-1]
 #   email = string[-1]

#    try:



#    def user_stats(name):
#        return(name)

#    def new_user(username, nickname, bio, email):
#        cur.execute(f''' SELECT * FROM USERS WHERE username='{username}' ''')
#        if cur.fetchone() == None:
#            cur.execute(f''' INSERT INTO USERS(username, nickname, bio, email, experience)
#            VALUES ("{username}", "{nickname}", "{bio}", "{email}", 0) ''')
#            con.commit()
#            print("Commit")
#        else:
#            return(1)
#            await message.channel.send("User found, to update use the +nickname, +bio or +email commands.")







def quote_gen():
    quote_pull = open("C:\Python Project Holder\Key Dump\Discord\Quotes.txt", "r").read()
    quotes = quote_pull.splitlines()
    q_grab =randrange(len(quotes))
    return(quotes[q_grab-1])


def email_ping(target, user):
    try:
        Email_Config = open("C:\Python Project Holder\Key Dump\Discord\EmailInfo.txt", "r").read()
        Email_Infomation_Breakdown = Email_Config.split()

        smtp_server = Email_Infomation_Breakdown[0]
        sender_email = Email_Infomation_Breakdown[1]
        password = Email_Infomation_Breakdown[2]

        quote = quote_gen()

        port = 587
        time = datetime.datetime.utcnow().strftime("%H:%M:%S - %D")
        subject = "KarlFranz Calling!"
        body = f'''"{quote}" - {user} at {time}'''

        target_email = (User_table.get_or_none(Username=target)).Email

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = target_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        text = message.as_string()

        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls(context=context)
            server.login(sender_email, password)
            server.sendmail(sender_email, target_email, text)
            return(1)
    except:
        return(0)

#Test database connection:
with open("C:\Python Project Holder\Key Dump\Discord\Database.txt") as json_file:
    database_directions = json.load(json_file)
database = MySQLDatabase("discordDB", user=database_directions["username"],
    password=database_directions["password"], host=database_directions["host"],
    port=database_directions["port"])

class BaseModel(Model):
    class Meta:
        database = database

class User_table(Model):
    Username = CharField()
    Nickname = CharField()
    Bio = TextField()
    Email = CharField()
    Experience = IntegerField()
    class Meta:
        database = database

class Logs(Model):
    Command = CharField()
    User = CharField()
    Time = TimeField()
    class Meta:
        database = database

try:
    table_exist = database.get_tables()
    if 'user_table' in table_exist:
        db_status = 1

except (ConnectionRefusedError, OperationalError) as e:
    print("Connection refused -", e)
    db_status = 0

except Exception as e:
    print("General error -", e)
    db_status = 0

#Pull token and run
token_file = open("C:\Python Project Holder\Key Dump\Discord\Token.txt", "r")
TOKEN_READ = token_file.read()
KarlFranz.run(TOKEN_READ)












#def startup():
#    try:
#        logging.basicConfig(filename="C:\Python Project Holder\Key Dump\Discord\KarlFranzLogs.txt", encoding="utf-8", level=logging.DEBUG)
#        logging.debug("Intialising logs " + datetime.utcnow().strftime("%H:%M:%S - %D"))
#        logging.getLogger("peewee").setLevel(logging.WARNING)
#    except:
#        print("Logging failure, exiting...")
#        exit()

#    token_file = open("C:\Python Project Holder\Key Dump\Discord\Token.txt", "r")
#    TOKEN_READ = token_file.read()
#    client = discord.Client()
#    logging.debug("Token read - " + datetime.utcnow().strftime("%H:%M:%S - %D"))

#    table_exist = len(database.get_tables())
#    if table_exist < 1:
#        database.create_tables([User_table])
#        logging.debug("Table not found - creating new - " + datetime.utcnow().strftime("%H:%M:%S - %D"))
#    else:
#        logging.debug("Table found - "+ datetime.utcnow().strftime("%H:%M:%S - %D"))

#    return(TOKEN_READ, client, database)


#TOKEN_READ, client, database = startup()

#@client.event
#async def on_ready():
#    print("Logged in as {0.user}".format(client))

#@client.event
#async def on_message(message):

#    if message.author == client.user:
#        return

#    if message.content.startswith("+stats"):
#        name = (message.content).split()
#        name = name[1]
#        query = User_table.get(Username=name)
#        stat_check = f"The user {query.Username} has {query.Experience} exp!"
#        await message.channel.send(stat_check)


#    if message.content.startswith("+newuser"):
#        string = (message.content).split()
#        query = User_table.get_or_none(Username=string[1])
#        bio = " ".join(string[3:-1])

#        if query == None:
#            row = {
#                "Username" : string[1],
#                "Nickname" : string[2],
#                "Bio" : bio,
#                "Email" : string[-1],
#                "Experience" : 0
#            }
#            User_table.insert(row).execute()
#        else:
#            await message.channel.send("Already in database")


#client.run(TOKEN_READ)









#con = sqlite3.connect("UserDB.db")
#cur = con.cursor()

#def KarlFranz():

#    try:
#        cur.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='USERS' ''')
#        if cur.fetchone()[0] == 1:
#            print("Table Found")
#        else:
#            cur.execute('''CREATE TABLE USERS (
#            username TEXT PRIMARY KEY,
#            nickname TEXT,
#            bio TEXT NOT NULL,
#            email TEXT NOT NULL,
#            experience INTEGER NOT NULL
#        );''')
#            con.commit()
#    except:
#        print("error")

#    def user_stats(name):
#        return(name)

#    def new_user(username, nickname, bio, email):
#        cur.execute(f''' SELECT * FROM USERS WHERE username='{username}' ''')
#        if cur.fetchone() == None:
#            cur.execute(f''' INSERT INTO USERS(username, nickname, bio, email, experience)
#            VALUES ("{username}", "{nickname}", "{bio}", "{email}", 0) ''')
#            con.commit()
#            print("Commit")
#        else:
#            return(1)
#            await message.channel.send("User found, to update use the +nickname, +bio or +email commands.")


#    @client.event
#    async def on_ready():
#        print("Logged in as {0.user}".format(client))


#    @client.event
#    async def on_message(message):

#        if message.author == client.user:
#            return

#        if message.content.startswith("+stats"):
#            name = (message.content).split()
#            name = name[1]
#            print(user_stats(name))

#            try:
#                await message.channel.send(name)

#            except:
#                print("bad attempt")

#        if message.content.startswith("+newuser"):
#            infomation = message.content.split()
#            bio_one = infomation[3:-1]
#            bio = ""

#            for x in bio_one:
#                bio = bio + " "+ x
#            bio = bio[1:]

#            if len(bio) > 200:
#                await message.channel.send("Error: Bio too long")
#            print(infomation[1])
#            print(infomation[2])
#            print(bio)
#            print(infomation[4])
#            new_user(infomation[1], infomation[2], bio, infomation[4])

        #if message.content.startswith("+"):
        #    print(message.content)

        #    try:
        #        await message.channel.send(quote_pool[message.content])
        #    except:
        #        print("bad attempt")

#    client.run(TOKEN_READ)


#if __name__ == "__main__":
#    KarlFranz()
