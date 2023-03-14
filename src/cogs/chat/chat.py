import discord
from discord.ext.commands import Bot, Cog, command, Context

from main import logger
import config
import random
import langdetect
import pathlib
import datetime

should_responses = [
    "Yes",
    "No",
    "Maybe",
    "I don't think so",
    "Go balls",
    "This bot doesn't provide a free therapy for a mentally ill person"
]

prefixes = [
    "riz,",
    "riz",
]

class RandomChat():
    chatlog = None

    @classmethod
    def update(cls):
        fp = open(f"{config.SRC_DIR}/cogs/chat/data/id/chatlog.csv", "r")
        chatlog = fp.readlines()
        fp.close()

        if len(chatlog) <= 1:
            return

        else:
            cls.chatlog = chatlog


    @classmethod
    async def is_exist(cls, message: str) -> bool:
        cls.update()
        
        message = message+'\n'
        if message in cls.chatlog:
            return True
        else:
            return False

    @classmethod
    async def insert(message: str) -> None:
        message = message.lstrip("> ")  


        fp = open(f"{config.SRC_DIR}/cogs/chat/data/id/chatlog.csv", "a")
        fp.write(f"{message}\n")
        fp.close()

        logger.info(f"Write: {message}")

    @classmethod
    async def get(cls) -> None:
        cls.update()
        return res.rstrip('\n')


class Chat(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    async def command_hander()


    async def process_command(self, message: discord.Message) -> None:
        if ((message.content.split())[0]).lower() not in prefixes:
            return


    @Cog.listener("on_message")
    async def message_listener(self, message: discord.Message) -> None:
        if len(message.content.split()) < 2 or len(message.content.split()) > 12:
            return
        
        if message.author.bot:
            return

        if 'riz' in message.content:
            return

        for res in langdetect.detect_langs(message.content):
            if res.lang == 'id':
                await RandomChat.insert(message.content)

    @Cog.listener("on_message")
    async def message_response(self, message: discord.Message) -> None:
        if 'riz' not in message.content.lower():
            return
        await message.channel.send(await RandomChat.get())
            



    @command(name="nuke")
    async def nuke_discord(self, ctx: Context):
        await ctx.send(f"Ip ban incoming!")
# after=datetime.datetime(2020, 2, 9)
        async for msg in ctx.channel.history(limit=10000, oldest_first=True, ):
            try: 
                if len(msg.content.split()) < 2:
                    continue

                if msg.author.bot:
                    continue

                if 'riz' in msg.content:
                    continue

                if await RandomChat.is_exist(msg.content):
                    continue

                for res in langdetect.detect_langs(msg.content):
                    if res.lang == 'id':
                        await RandomChat.insert(msg.content)
            except: 
                continue

    
    @command(name="are")
    async def are_command(self, ctx):
        await self.eightball(ctx)

    @command(name="may")
    async def may_command(self, ctx):
        await self.eightball(ctx)

    @command(name="can")
    async def can_command(self, ctx):
        await self.eightball(ctx)

    @command(name="could")
    async def could_command(self, ctx):
        await self.eightball(ctx)

    @command(name="should")
    async def should_command(self, ctx):
        await self.eightball(ctx)

    @command(name="really")
    async def should_command(self, ctx):
        await self.eightball(ctx)


    async def eightball(self, ctx: Context):
        await ctx.send(f"{random.choice(should_responses)}")


async def setup(bot: Bot):
    await bot.add_cog(Chat(bot))