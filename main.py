import time

import discord
from discord.ext import commands

# from help_cog import help_cog

TOKEN = open("TOKENT.txt", "r").read()

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
Bot = commands.Bot(command_prefix=commands.when_mentioned_or("/"), intents=intents)


@Bot.event
async def on_ready():
    print("Altay hazir!")


@Bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="genel")
    await channel.send(f"Altaydan kaçar mı {member} ? Hoş geldin :smile:")
    print(f"Altaydan kaçar mı {member} ? Hoş geldin :smile:")


@Bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name="genel")
    await channel.send(f"Bunu tutamadik :( Ah be {member}!")
    print(f"Bunu tutamadik :( Ah be {member}!")


@commands.has_permissions(kick_members=True)
@Bot.command()
async def kick(ctx, member: discord.Member, *args, reason="Yok"):
    await member.kick(reason=reason)
    time.sleep(2)
    await ctx.channel.send(f"Altaydan {member}'e muhteşem şut!(Kicked)")


@commands.has_permissions(ban_members=True)
@Bot.command()
async def ban(ctx, member: discord.Member, *args, reason="Yok"):
    await member.ban(reason=reason)
    time.sleep(2)
    await ctx.channel.send(f"Altaydan {member}'e muhteşem şut!(Banned)")


@commands.has_role("abi")
@Bot.command()
async def unban(ctx, member: discord.Member, *args, reason="Yok"):
    await member.unban()
    time.sleep(2)
    await ctx.channel.send(f"Altaydan'dan {member}'e çok özürrrr :( (unBanned)")


@commands.has_permissions(manage_messages=True)
@Bot.command()
async def sil(ctx, mesajSayisi):
    await ctx.channel.purge(limit=int(mesajSayisi))
    await ctx.send(f"{mesajSayisi} mesaj kırmızı kart gördü!")


@Bot.command()
async def soyle(ctx, *args):
    await ctx.channel.purge(limit=1)

    await ctx.channel.send(f"{args}".replace("(", "").replace("'", "").replace(")", "").replace(",", ""))


komutlar1 = "sil {miktar} : Belirtilen miktarda mesajı siler."
komutlar2 = "kick {kisi} : Belirtilen kisinin geçici olarak atılmasını sağlar."
komutlar3 = "ban {kisi} : Kişiyi sunucudan yasaklamanızı sağlar. "
komutlar4 = "komutlar : Tüm komutları görüntülersiniz."
komutlar5 = "unban {kisi} : Yasaklanan kişinin yasağını kaldırır."
komutlar6 = "soyle {mesaj} : Altay istediğin mesajı yazar."


@Bot.command()
async def komutlar(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send(f"{komutlar1}\n{komutlar2}\n{komutlar3}\n{komutlar4}\n{komutlar5}\n{komutlar6}")


@Bot.command()
async def play(self, ctx, *args):
    query = " ".join(args)
    voice_channel = ctx.voice.channel
    if voice_channel is None:
        await ctx.send("Bir kanala katil")
    elif self.is_paused:
        self.vc.resume()
    else:
        song = self.search_yt(query)
        if type(song) == type(True):
            await ctx.send("Indırılemedi")
        else:
            await ctx.send("Şarkı sıraya eklendi")
            self.music_queue.append([song, voice_channel])

            if self.is_playing == False:
                await self.play_music(ctx)


Bot.run(TOKEN)
