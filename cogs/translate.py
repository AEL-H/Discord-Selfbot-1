import urllib.request
import re
import requests
import string
import json
import discord
import prettytable
from PythonGists import PythonGists
from appuselfbot import bot_prefix
from discord.ext import commands
from cogs.utils.checks import *

'''Translator cog - Love Archit & Lyric'''


class Translate:

    def __init__(self, bot):
        self.bot = bot

    # Thanks to lyric for helping me in making this possible. You are not so bad afterall :] ~~jk~~
    @commands.command(pass_context=True)
    async def translate(self, ctx, to_language, *, msg):
        """Translates words from one language to another. Do >help translate for more information.
        Usage:
        >translate <new language> <words> - Translate words from one language to another. Full language names must be used.
        The original language will be assumed automatically.
        """
        codes = requests.get("http://lyricly.tk/langs.json").text
        lang_codes = json.loads(codes)
        real_language = False
        to_language = to_language.lower()
        for entry in lang_codes:
            if to_language in lang_codes[entry]["name"].replace(";", "").replace(",", "").lower().split():
                language = lang_codes[entry]["name"].replace(";", "").replace(",", "").split()[0]
                to_language = entry
                real_language = True
        if real_language:
            orMsg = msg
            msg = msg.replace("&","%26")
            translate = requests.get("https://translate.google.com/m?hl={}&sl=auto&q={}".format(to_language, msg)).text
            result = str(translate).split('class="t0">')[1].split("</div>")[0]
            l1 = re.findall('\&\#(.*?)\;',result)
            listb = []
            for a in l1:
                listb.append(chr(int(a)))
            i = 0 
            while i < len(listb): 
                result = re.sub('\&\#(.*?)\;',listb[i],result,1) 
                i = i+1
            if result:
                embed = discord.Embed(color=discord.Color.blue())
                embed.add_field(name="Original", value=orMsg, inline=False)
                embed.add_field(name=language, value=result.replace("&amp;","&"), inline=False)
                await self.bot.say("", embed=embed)
            else:
                await self.bot.say("That language either isn't supported by Google Translate, or there's a bug in the bot.")
        else:
            await self.bot.say("That's not a real language.")

def setup(bot):
    bot.add_cog(Translate(bot))