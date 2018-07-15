import random
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot

prefix = ("!", "?")
TOKEN = NDY3ODUzODgzNTg3NDI4MzYz.Diwqlg.M5HkhygMJ9q-h0-Wgfuw2xUlLf4

client = Bot(command_prefix = prefix)

@client.command(name = "y2k",
                description = "Kim daha y2k moruk",
                aliases = ["yikik"],
                pass_context = True)
async def y2k(context):
    i

