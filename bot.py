import discord
from discord.ext import commands
import asyncio
from dbmanager import syncmembers as syncmdb
from dbmanager import createQ, nonpayes
from dbmanager import contribute as ctb
from dbmanager import showquests as shq
from dbmanager import delquest
from dbmanager import memberlist as tt

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

@bot.command(pass_context=True, name='syncmembers')
@commands.has_any_role('Brasseur étoile', 'Maître brasseur étoile')
async def syncmembers(context, *args):    
    x = context.message.server.members
    syncmdb(conn,x)                
    await bot.send_message(context.message.channel, "Done")


@commands.has_any_role('Brasseur étoile', 'Maître brasseur étoile')
@bot.command(pass_context=True, name='quest')
async def quest(context, *args):
    if len(args) != 3:
        await bot.send_message(context.message.channel, "Commande : .quest nom prix nbpersonnes")
    else:
        createQ(conn, args[0], args[1], args[2])
        await bot.send_message(context.message.channel, "Done")

@bot.command(pass_context=True, name='contribute')
async def contribute(context, *args):
    if len(args) != 2:
        await bot.send_message(context.message.channel, "Commande : .contribute quest amount")
    else:
        ctb(conn,args[0], context.message.author.id, args[1])
        await bot.send_message(context.message.channel, "Done")

@bot.command(pass_context=True, name='showquests')
async def showquests(context, *args):
    if len(args) != 0:
        await bot.send_message(context.message.channel, "Commande : .showquests")
    else:
        await bot.send_message(context.message.channel, '\n'.join(shq(conn)))

@bot.command(pass_context=True, name='showpay')
async def showpay(context, *args):
    if len(args) != 1:
        await bot.send_message(context.message.channel, "Commande : .showpay quete")
    else:
        st = []
        for m in nonpayes(conn,args[0]):      
            if(context.message.server.get_member(m).nick):
                st.append(context.message.server.get_member(m).nick)
            else:
                st.append(context.message.server.get_member(m).name)
        
        await bot.send_message(context.message.channel, "Non payé sur la quête " + args[0] + " :\n" + '\n'.join(st))

@commands.has_any_role('Brasseur étoile', 'Maître brasseur étoile')
@bot.command(pass_context=True, name='delete')
async def delete(context, *args):
    if len(args) != 1:
        await bot.send_message(context.message.channel, "Commande : .del quete")
    else:
        delquest(conn, args[0])
        await bot.send_message(context.message.channel, "Done")





        

    
    
          
    

bot.run(TOKEN)



