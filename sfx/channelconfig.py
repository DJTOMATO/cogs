import discord
from redbot.core import commands
from redbot.core.utils.chat_formatting import pagify
from redbot.core.utils.menus import DEFAULT_CONTROLS, menu
from redbot.core.utils.predicates import MessagePredicate

from sfx.api import generate_urls

from .abc import MixinMeta
from .voices import voices


class ChannelConfigMixin(MixinMeta):
    @commands.group()
    @commands.guild_only()
    @commands.admin_or_permissions(manage_guild=True)
    async def ttschannel(self, ctx):
        """
        Configures automatic TTS channels.
        """
        pass

    @ttschannel.command()
    async def add(self, ctx, channel: discord.TextChannel):
        """
        Adds a channel for automatic TTS.
        """
        channel_list = await self.config.guild(ctx.guild).channels()
        if channel.id not in channel_list:
            channel_list.append(channel.id)
            await self.config.guild(ctx.guild).channels.set(channel_list)
            self.channel_cache[ctx.guild.id] = channel_list

            await ctx.send(
                f"Okay, {channel.mention} will now be used as a TTS channel."
            )
        else:
            await ctx.send(
                f"{channel.mention} is already a TTS channel, did you mean use the `{ctx.clean_prefix}ttschannel remove` command?"
            )

    @ttschannel.command(aliases=["delete", "del"])
    async def remove(self, ctx, channel: discord.TextChannel):
        """
        Removes a channel for automatic TTS.
        """
        channel_list = await self.config.guild(ctx.guild).channels()
        if channel.id in channel_list:
            channel_list.remove(channel.id)
            await self.config.guild(ctx.guild).channels.set(channel_list)
            self.channel_cache[ctx.guild.id] = channel_list
            await ctx.send(f"Okay, {channel.mention} is no longer a TTS channel.")
        else:
            await ctx.send(
                f"{channel.mention} isn't a TTS channel, did you mean use the `{ctx.clean_prefix}ttschannel add` command?"
            )

    @ttschannel.command()
    async def clear(self, ctx):
        """
        Removes all the channels for automatic TTS.
        """
        channel_list = await self.config.guild(ctx.guild).channels()
        if not channel_list:
            await ctx.send("There's no channels in the config.")
        else:
            try:
                await ctx.send(
                    "Are you sure you want to clear all this server's TTS channels? Respond with yes or no."
                )
                predictate = MessagePredicate.yes_or_no(ctx, user=ctx.author)
                await ctx.bot.wait_for("message", check=predictate, timeout=30)
            except asyncio.TimeoutError:
                await ctx.send(
                    "You never responded, please use the command again to clear all of this server's TTS channels."
                )
                return
            if predictate.result:
                await self.config.guild(ctx.guild).channels.clear()
                del self.channel_cache[ctx.guild.id]
                await ctx.send("Okay, I've cleared all TTS channels for this server.")
            else:
                await ctx.send("Okay, I won't clear any TTS channels.")

    @ttschannel.command()
    async def list(self, ctx):
        """
        Shows all the channels for automatic TTS.
        """
        try:
            channel_list = self.channel_cache[ctx.guild.id]
        except KeyError:
            channel_list = None
        if not channel_list:
            await ctx.send("This server doesn't have any TTS channels set up.")
        else:
            text = "".join(
                "<#" + str(channel) + "> - " + str(channel) + "\n"
                for channel in channel_list
            )
            pages = [p for p in pagify(text=text, delims="\n")]
            embeds = []
            for index, page in enumerate(pages):
                embed = discord.Embed(
                    title="Automatic TTS Channels",
                    color=await ctx.embed_colour(),
                    description=page,
                )
                if len(embeds) > 1:
                    embed.set_footer(text=f"Page {index+1}/{len(pages)}")
                embeds.append(embed)

            if len(pages) == 1:
                await ctx.send(embed=embeds[0])
            else:
                await menu(ctx, embeds, DEFAULT_CONTROLS, timeout=60)

    @commands.Cog.listener()
    async def on_message_without_command(self, message: discord.Message):
        if not message.guild:
            return
        if message.author.bot:
            return
        if not message.channel.permissions_for(message.guild.me).send_messages:
            return
        if await self.bot.allowed_by_whitelist_blacklist(who=message.author) is False:
            return
        if await self.bot.cog_disabled_in_guild(self, message.guild):
            return
        try:
            channel_list = self.channel_cache[message.guild.id]
        except KeyError:
            return

        if not channel_list:
            return
        if message.channel.id not in channel_list:
            return

        if not message.author.voice or not message.author.voice.channel:
            await message.channel.send("You are not connected to a voice channel.")
            return

        author_data = await self.config.user(message.author).all()
        author_voice = author_data["voice"]
        author_speed = author_data["speed"]
        author_volume = author_data["volume"]
        author_translate = author_data["translate"]

        if author_voice not in voices.keys():
            await self.config.user(message.author).voice.clear()
            author_voice = "Anna"

        text = self.decancer_text(message.clean_content)

        if text is None:
            await message.channel.send("That's not a valid message, sorry.")
            return

        char_number = len(text)

        if char_number > 1000:
            await message.channel.send(
                f"Sorry, I limit TTS to 1000 characters to avoid abuse. ({char_number}/1000)"
            )
            return

        urls = await generate_urls(
            self, author_voice, text, author_speed, author_volume, author_translate
        )

        await self.play_sfx(
            message.author.voice.channel,
            message.channel,
            True,
            author_data,
            text,
            urls,
        )
