import os

import discord
from discord.ext import commands
import asyncio
from discord.utils import get
from discord.ext import tasks
for_help = True 
I = ["Я"]
trista = ["300", "150 + 150", "трста", "3*100"]
bye = ["bye", "goodbye", "poca", "poka", "пока", "гудбай", "бувай", "допобачення", "досвидания", "астала", "виста", "иди в мут", "я спать", "я пошел", " гуд бай", "астала виста", "я ухожу"]     # создаем список "привет" слов

hello = ["hi", "hello", "privet", "привет", "хай", "халоу", "воц", "ап", "whats", "up", "привіт", "салам", "вос", "ап", "доброго времени суток", "малам алекум", "всем хай",
         "всем привет", "я новенький", "я пришел", "я вернулся", "приветули"] # создаес список "пока" слов

forbidden_words = ["нигер", "нига", "пидор", "ебал", "говноед", "мразь", "пидор", "пидар", "еблан", "уебок", "пиздабол", "ебло", "ебало", "долбоящер", "мать в канаве",
                   "мать ебал", "мамку ебал", "ебал мамку", "твой отчим", "мамка в канаве", "отчим твой", "пошол нахуй", "пошел нахуй", "пошол нах", "пошел нах" ]  # you can add as many words as you like, but make sure they are all lower case
lox = ["лох", "лошара", "бля", "даун", "дебил", "дибил" ]
help = ["?help", "?what", "?pomogi", "?помощь", "?помоги", ]

bot = commands.Bot(command_prefix='!')















# # tasks.loop(seconds=8)
# # async def message():
#     await bot.get_channel(844615914242310167).send("hello")

@bot.event
async def on_ready():
    global mainchannel # если переменную не сделать глобальной, её нельзя будет использовать из других функций
    global bot_message_count
    mainchannel = bot.get_channel(853564879869050880) # определяем канал на нашем сервере
    gr = '😎Бот успешно запущен!😎'
    await mainchannel.send(gr, delete_after=30) # отправ
async  def  on_message(msg):
    if message.content.lower().startswith("?help"):
         await message.channel.send(f'Список слов за которые дается мут (5 часов) "нигер", "нига", "пидор", "ебал", "говноед", "мразь", "пидор", "пидар", "еблан", "уебок", "пиздабол", "ебло", "ебало", "долбоящер", "мать в канаве", "мать ебал", "мамку ебал", "ебал мамку", "твой отчим", "мамка в канаве", "отчим твой" {message.author.mention}\nПо всем вопросам писать админу(Max0n)')


         


    activity = discord.Activity(name=f"Я в разработке")
    await bot.change_presence(status=discord.Status.online, activity=activity) # меняем боту статус
@bot.event
async def on_message(message):
    if message.author == bot.user:  # ignores itself
        return
    if message.author.bot == True:  # ignores other bots
        return
    if message.guild == None:  # ignores dms
        return

    for word in forbidden_words:
        if word in message.content.lower():
            await message.delete()
            await message.author.add_roles(get(message.guild.roles, id=846083325672161332),reason=f"He said a forbidden word")
            await bot.get_channel(853564879869050880).send(f"Message was deleted in {message.channel.mention} by {message.author.mention}:\n`{message.content}`")
            await asyncio.sleep(18000)
            await message.author.remove_roles(get(message.guild.roles, id=846083325672161332), reason=f"Mute has expired")
    if for_help == True:
      
                  
         
         

    # print(msg_list)
    # print(hello)
    # print(list(set(msg_list + hello)))
    # print(len(set(msg_list + hello)))
         msg = message.content.lower()
         msg_list = msg.split()

         find_hello = False
         for item in hello:
                  if msg.find(item) >= 0:
                           find_hello = True
                           if (find_hello):
                                    await message.channel.send(f'  Привет {message.author.mention} !') # рекация на "привет" слово
    find_bye = False
    for item in bye:
        if msg.find(item) >= 0:
            find_bye = True
    if (find_bye):
        await message.channel.send(f'  Пока {message.author.mention} !') # реакция на "пока" слово

    find_lox = False
    for item in lox:
        if msg.find(item) >= 0:
            find_lox = True
    if (find_lox):
        await message.channel.send(f'  не матюкайся{message.author.mention} !') # рекация на "матюк" слово
    find_help = False
    for item in help:
        if msg.find(item) >= 0:
            find_help = True
    if (find_help):
        
        await message.channel.send("Правила чата")
        await message.channel.send("Мат запрещен(мут 30мин)")
        await message.channel.send("Реклама запрещена(Мут на 14 дней)")
        await message.channel.send("Порнографические материалы запрещены(бан навседа)")# рекация на "help" слово
    find_trista = False
    for item in trista:
        if msg.find(item) >= 0:
            find_trista = True
    if (find_trista):
        await message.channel.send(f'[ШУТКА ПРО ТРАКТОРИСТА УДАЛЕНА]') # реакция на "300" слово

    find_I = False
    for item in I:
        if msg.find(item) >= 0:
            find_I = True
    if (find_I):
        await message.channel.send('Головка от хуя', mention_author=False) # реакция на "пока" слово


#     messages.start()

token = os.environ.get('BOT_TOKEN')
bot.run(str(token))
