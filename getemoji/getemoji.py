from redbot.core import commands, Config, checks
import aiohttp 
import discord

class GetEmoji(commands.Cog):
    def __init__(self):
        self.config = Config.get_conf(self, identifier=6574839238457654839284756548392384756)
        default_global = {"url": "http://localhost:6969" }
        self.config.register_global(**default_global)

    @commands.command
    @commands.admin
    async def emojiapiurl(self, ctx, url: str):
        await ctx.send("soon")



    @commands.group()
    async def getemoji(self, ctx):
        """get custom emojis from different providers!"""

    @getemoji.command()
    async def apple(self, ctx, emoji: str):
        """get an image of a apple emoji"""
        url = await self.config.url()
        async with aiohttp.ClientSession() as session:
            async with session.get(url + '/emoji/image/apple/' + emoji) as request:
                if request.status == 404:
                    return await ctx.send("Sorry, I couldn't find that emoji from my API.")
                if request is None:
                    return await ctx.send("Sorry, I seem to be having issues. Maybe try again")
                response = await request.json()
                embed = discord.Embed(color = ctx.me.color)
                embed.set_image(url = response['url'])
                await ctx.send(embed = embed)

    @getemoji.command()
    async def google(self, ctx, emoji: str):
        """get an image of a google emoji"""
        url = await self.config.url()
        async with aiohttp.ClientSession() as session:
            async with session.get(url + '/emoji/image/google/' + emoji) as request:
                if request.status == 404:
                    return await ctx.send("Sorry, I couldn't find that emoji from my API.")
                if request is None:
                    return await ctx.send("Sorry, I seem to be having issues. Maybe try again")
                response = await request.json()
                embed = discord.Embed(color = ctx.me.color)
                embed.set_image(url = response['url'])
                await ctx.send(embed = embed)
    @getemoji.command()
    async def samsung(self, ctx, emoji: str):
        """get an image of a samsung emoji"""
        url = await self.config.url()
        async with aiohttp.ClientSession() as session:
            async with session.get(url + '/emoji/image/samsung/' + emoji) as request:
                if request.status == 404:
                    return await ctx.send("Sorry, I couldn't find that emoji from my API.")
                if request is None:
                    return await ctx.send("Sorry, I seem to be having issues. Maybe try again")
                response = await request.json()
                embed = discord.Embed(color = ctx.me.color)
                embed.set_image(url = response['url'])
                await ctx.send(embed = embed)
    @getemoji.command()
    async def microsoft(self, ctx, emoji: str):
        """get an image of a microsoft emoji"""
        url = await self.config.url()
        async with aiohttp.ClientSession() as session:
            async with session.get(url + '/emoji/image/microsoft/' + emoji) as request:
                if request.status == 404:
                    return await ctx.send("Sorry, I couldn't find that emoji from my API.")
                if request is None:
                    return await ctx.send("Sorry, I seem to be having issues. Maybe try again")
                response = await request.json()
                embed = discord.Embed(color = ctx.me.color)
                embed.set_image(url = response['url'])
                await ctx.send(embed = embed)
    @getemoji.command()
    async def whatsapp(self, ctx, emoji: str):
        """get an image of a whatsapp emoji"""
        url = await self.config.url()
        async with aiohttp.ClientSession() as session:
            async with session.get(url + '/emoji/image/whatsapp/' + emoji) as request:
                if request.status == 404:
                    return await ctx.send("Sorry, I couldn't find that emoji from my API.")
                if request is None:
                    return await ctx.send("Sorry, I seem to be having issues. Maybe try again")
                response = await request.json()
                embed = discord.Embed(color = ctx.me.color)
                embed.set_image(url = response['url'])
                await ctx.send(embed = embed)
    @getemoji.command()
    async def twitter(self, ctx, emoji: str):
        """get an image of a twitter emoji"""
        url = await self.config.url()
        async with aiohttp.ClientSession() as session:
            async with session.get(url + '/emoji/image/twitter/' + emoji) as request:
                if request.status == 404:
                    return await ctx.send("Sorry, I couldn't find that emoji from my API.")
                if request is None:
                    return await ctx.send("Sorry, I seem to be having issues. Maybe try again")
                response = await request.json()
                embed = discord.Embed(color = ctx.me.color)
                embed.set_image(url = response['url'])
                await ctx.send(embed = embed)
    @getemoji.command()
    async def facebook(self, ctx, emoji: str):
        """get an image of a facebook emoji"""
        url = await self.config.url()
        async with aiohttp.ClientSession() as session:
            async with session.get(url + '/emoji/image/facebook/' + emoji) as request:
                if request.status == 404:
                    return await ctx.send("Sorry, I couldn't find that emoji from my API.")
                if request is None:
                    return await ctx.send("Sorry, I seem to be having issues. Maybe try again")
                response = await request.json()
                embed = discord.Embed(color = ctx.me.color)
                embed.set_image(url = response['url'])
                await ctx.send(embed = embed)
    @getemoji.command()
    async def joypixels(self, ctx, emoji: str):
        """get an image of a joypixels emoji"""
        url = await self.config.url()
        async with aiohttp.ClientSession() as session:
            async with session.get(url + '/emoji/image/joypixels/' + emoji) as request:
                if request.status == 404:
                    return await ctx.send("Sorry, I couldn't find that emoji from my API.")
                if request is None:
                    return await ctx.send("Sorry, I seem to be having issues. Maybe try again")
                response = await request.json()
                embed = discord.Embed(color = ctx.me.color)
                embed.set_image(url = response['url'])
                await ctx.send(embed = embed)
    @getemoji.command()
    async def openmoji(self, ctx, emoji: str):
        """get an image of a openmoji emoji"""
        url = await self.config.url()
        async with aiohttp.ClientSession() as session:
            async with session.get(url + '/emoji/image/openmoji/' + emoji) as request:
                if request.status == 404:
                    return await ctx.send("Sorry, I couldn't find that emoji from my API.")
                if request is None:
                    return await ctx.send("Sorry, I seem to be having issues. Maybe try again")
                response = await request.json()
                embed = discord.Embed(color = ctx.me.color)
                embed.set_image(url = response['url'])
                await ctx.send(embed = embed)
    @getemoji.command()
    async def emojidex(self, ctx, emoji: str):
        """get an image of a emojidex emoji"""
        url = await self.config.url()
        async with aiohttp.ClientSession() as session:
            async with session.get(url + '/emoji/image/emojidex/' + emoji) as request:
                if request.status == 404:
                    return await ctx.send("Sorry, I couldn't find that emoji from my API.")
                if request is None:
                    return await ctx.send("Sorry, I seem to be having issues. Maybe try again")
                response = await request.json()
                embed = discord.Embed(color = ctx.me.color)
                embed.set_image(url = response['url'])
                await ctx.send(embed = embed)
    @getemoji.command()
    async def lg(self, ctx, emoji: str):
        """get an image of a lg emoji"""
        url = await self.config.url()
        async with aiohttp.ClientSession() as session:
            async with session.get(url + '/emoji/image/lg/' + emoji) as request:
                if request.status == 404:
                    return await ctx.send("Sorry, I couldn't find that emoji from my API.")
                if request is None:
                    return await ctx.send("Sorry, I seem to be having issues. Maybe try again")
                response = await request.json()
                embed = discord.Embed(color = ctx.me.color)
                embed.set_image(url = response['url'])
                await ctx.send(embed = embed)
    @getemoji.command()
    async def htc(self, ctx, emoji: str):
        """get an image of a htc emoji"""
        url = await self.config.url()
        async with aiohttp.ClientSession() as session:
            async with session.get(url + '/emoji/image/htc/' + emoji) as request:
                if request.status == 404:
                    return await ctx.send("Sorry, I couldn't find that emoji from my API.")
                if request is None:
                    return await ctx.send("Sorry, I seem to be having issues. Maybe try again")
                response = await request.json()
                embed = discord.Embed(color = ctx.me.color)
                embed.set_image(url = response['url'])
                await ctx.send(embed = embed)
    @getemoji.command()
    async def softbank(self, ctx, emoji: str):
        """get an image of a softbank emoji"""
        url = await self.config.url()
        async with aiohttp.ClientSession() as session:
            async with session.get(url + '/emoji/image/softbank/' + emoji) as request:
                if request.status == 404:
                    return await ctx.send("Sorry, I couldn't find that emoji from my API.")
                if request is None:
                    return await ctx.send("Sorry, I seem to be having issues. Maybe try again")
                response = await request.json()
                embed = discord.Embed(color = ctx.me.color)
                embed.set_image(url = response['url'])
                await ctx.send(embed = embed)
    @getemoji.command()
    async def docomo(self, ctx, emoji: str):
        """get an image of a docomo emoji"""
        url = await self.config.url()
        async with aiohttp.ClientSession() as session:
            async with session.get(url + '/emoji/image/docomo/' + emoji) as request:
                if request.status == 404:
                    return await ctx.send("Sorry, I couldn't find that emoji from my API.")
                if request is None:
                    return await ctx.send("Sorry, I seem to be having issues. Maybe try again")
                response = await request.json()
                embed = discord.Embed(color = ctx.me.color)
                embed.set_image(url = response['url'])
                await ctx.send(embed = embed)
    @getemoji.command()
    async def mozilla(self, ctx, emoji: str):
        """get an image of a mozilla emoji"""
        url = await self.config.url()
        async with aiohttp.ClientSession() as session:
            async with session.get(url + '/emoji/image/mozilla/' + emoji) as request:
                if request.status == 404:
                    return await ctx.send("Sorry, I couldn't find that emoji from my API.")
                if request is None:
                    return await ctx.send("Sorry, I seem to be having issues. Maybe try again")
                response = await request.json()  
                embed = discord.Embed(color = ctx.me.color)
                embed.set_image(url = response['url'])
                await ctx.send(embed = embed)
    @getemoji.command()
    async def messenger(self, ctx, emoji: str):
        """get an image of a messenger emoji"""
        url = await self.config.url()
        async with aiohttp.ClientSession() as session:
            async with session.get(url + '/emoji/image/messenger/' + emoji) as request:
                if request.status == 404:
                    return await ctx.send("Sorry, I couldn't find that emoji from my API.")
                if request is None:
                    return await ctx.send("Sorry, I seem to be having issues. Maybe try again")
                response = await request.json()  
                embed = discord.Embed(color = ctx.me.color)
                embed.set_image(url = response['url'])
                await ctx.send(embed = embed)