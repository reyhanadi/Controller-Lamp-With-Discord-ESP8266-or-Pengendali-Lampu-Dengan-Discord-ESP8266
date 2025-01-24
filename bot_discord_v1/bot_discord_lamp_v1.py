import discord
from discord.ext import commands
from discord.ui import Button, View
from discord import app_commands
import os
import requests

intents = discord.Intents.all()

# Menggunakan commands.when_mentioned_or untuk memungkinkan bot diaktifkan dengan mention atau tanpa prefix
bot = commands.Bot(command_prefix=commands.when_mentioned_or(''), intents=intents)

# Definisikan IP address sebagai variabel
lamp_ip = 'your ip'

def get_help_message():
    return (
        "\nBerikut adalah daftar perintah yang dapat digunakan:\n"
        "`l1n` - Menyalakan Lampu 1\n"
        "`l1m` - Mematikan Lampu 1\n"
        "`l2n` - Menyalakan Lampu 2\n"
        "`l2m` - Mematikan Lampu 2"
    )

@bot.event
async def on_ready():
    print(f'Terhubung sebagai {bot.user.name} ({bot.user.id})')
    try:
        synced = await bot.tree.sync()
        print(f"Sinkronisasi Slash Command: {len(synced)} commands")
    except Exception as e:
        print(f"Gagal sinkronisasi Slash Command: {e}")

    # Kirim pesan otomatis dengan daftar perintah
    guild = bot.get_guild(your_server_id)
    if guild:
        channel = guild.text_channels[0]
        help_message = get_help_message()
        await channel.send(help_message)

# Chat Command
@bot.command(name='l1n')
async def lamp1_on(ctx):
    await toggle_lamp(ctx, lamp=1, state='on')

@bot.command(name='l1m')
async def lamp1_off(ctx):
    await toggle_lamp(ctx, lamp=1, state='off')

@bot.command(name='l2n')
async def lamp2_on(ctx):
    await toggle_lamp(ctx, lamp=2, state='on')

@bot.command(name='l2m')
async def lamp2_off(ctx):
    await toggle_lamp(ctx, lamp=2, state='off')

@bot.command(name='bantuan')
async def help_command(ctx):
    await ctx.send(get_help_message())

# Slash Command
async def toggle_lamp(interaction, lamp, state):
    endpoint = f"lamp{lamp}_{state}"
    try:
        requests.get(f'{lamp_ip}/{endpoint}', timeout=5)
        message = f"Lampu {lamp} telah {'dinyalakan' if state == 'on' else 'dimatikan'}!"
    except requests.RequestException as e:
        message = f"Gagal {'menyalakan' if state == 'on' else 'mematikan'} Lampu {lamp}. Error: {e}"

    if isinstance(interaction, discord.Interaction):
        await interaction.response.send_message(message)
    else:
        await interaction.send(message)

@bot.tree.command(name="lampu1_nyala", description="Menyalakan Lampu 1")
async def slash_lamp1_on(interaction: discord.Interaction):
    await toggle_lamp(interaction, lamp=1, state='on')

@bot.tree.command(name="lampu1_mati", description="Mematikan Lampu 1")
async def slash_lamp1_off(interaction: discord.Interaction):
    await toggle_lamp(interaction, lamp=1, state='off')

@bot.tree.command(name="lampu2_nyala", description="Menyalakan Lampu 2")
async def slash_lamp2_on(interaction: discord.Interaction):
    await toggle_lamp(interaction, lamp=2, state='on')

@bot.tree.command(name="lampu2_mati", description="Mematikan Lampu 2")
async def slash_lamp2_off(interaction: discord.Interaction):
    await toggle_lamp(interaction, lamp=2, state='off')

bot.run('your token bot discord')
