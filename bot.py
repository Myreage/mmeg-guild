import discord
from discord.ext import commands
import asyncio
import dbmanager
from priv import TOKEN

import sqlite3

conn = sqlite3.connect('database.db')
conn.execute("PRAGMA foreign_keys = ON")

bot = commands.Bot(command_prefix='.')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(pass_context=True, name='sync')
@commands.has_any_role('Brasseur étoile', 'Maître brasseur étoile')
async def sync(context, *args):    
    x = context.message.server.members
    dbmanager.syncmembers(conn,x)                
    await bot.send_message(context.message.channel, "Done")


@commands.has_any_role('Brasseur étoile', 'Maître brasseur étoile')
@bot.command(pass_context=True, name='quest')
async def quest(context, *args):
    if len(args) != 3:
        await bot.send_message(context.message.channel, "Commande : .quest nom prix nbpersonnes")
    else:
        dbmanager.createQ(conn, args[0], args[1], args[2])
        await bot.send_message(context.message.channel, "Done")

@bot.command(pass_context=True, name='cb')
async def cb(context, *args):
    if len(args) != 2:
        await bot.send_message(context.message.channel, "Commande : .contribute quest amount")
    else:
        dbmanager.contribute(conn,args[0], context.message.author.id, args[1])
        await bot.send_message(context.message.channel, "Done")

@bot.command(pass_context=True, name='sq')
async def sq(context, *args):
    if len(args) != 0:
        await bot.send_message(context.message.channel, "Commande : .showquests")
    else:
        await bot.send_message(context.message.channel, '\n'.join(dbmanager.showquests(conn)))

@commands.has_any_role('Brasseur étoile', 'Maître brasseur étoile')
@bot.command(pass_context=True, name='end')
async def end(context, *args):
    if len(args) != 1:
        await bot.send_message(context.message.channel, "Commande : .del quete")
    else:
        dbmanager.endquest(conn, args[0])
        await bot.send_message(context.message.channel, "Done")

@bot.command(pass_context=True, name='accounts')
async def accounts(context, *args):
    if len(args) != 0:
        await bot.send_message(context.message.channel, "Commande : .accounts")
    else:
        result = ""
        accounts = dbmanager.showaccounts(conn)
        for a in accounts:
            (name,balance) = a
            if(context.message.server.get_member(name).nick):
                nick = context.message.server.get_member(name).nick
            else:
                nick = context.message.server.get_member(name).name
            result = result + ("\n" + nick + "\t\t" + str(balance))

        await bot.send_message(context.message.channel, result)





        

    
    
          
    

bot.run(TOKEN)



