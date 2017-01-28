import contextlib
import sys
import inspect
import os
import shutil
import subprocess

# Common imports that can be used by the debugger.
import datetime
import time
import traceback
import re
import io
import gc
import math
import random
import json
import asyncio
from bs4 import BeautifulSoup
from discord.ext import commands
import discord
import urllib
import requests

with open('config.json', 'r') as f:
    config = json.load(f)

isBot = config['bot_identifier'] + ' '
if isBot == ' ':
    isBot = ''

class Subpro:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def runstuff(self, ctx):
        try:
            for i in range(4):
                await self.bot.send_message(ctx.message.channel, 'stuff')
                await asyncio.sleep(2)


        except Exception as e:
            var = traceback.format_exc()
            await self.bot.send_message(ctx.message.channel, '```' + var.rstrip() + '```')

        await self.bot.send_message(ctx.message.channel, isBot + 'Finished')


def setup(bot):
    bot.add_cog(Subpro(bot))