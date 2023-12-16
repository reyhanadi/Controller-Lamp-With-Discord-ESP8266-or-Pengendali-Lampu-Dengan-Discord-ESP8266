import discord
from discord.ext import commands
from discord.ui import Button, View
import os
import requests

intents = discord.Intents.all()

# Menggunakan commands.when_mentioned_or untuk memungkinkan bot diaktifkan dengan mention atau tanpa prefix
bot = commands.Bot(command_prefix=commands.when_mentioned_or(''), intents=intents)

# Definisikan IP address sebagai variabel
lamp_ip = 'your ip'

@bot.event
async def on_ready():
    print(f'Terhubung sebagai {bot.user.name} ({bot.user.id})')

    # Gantilah ID server dengan ID server Discord yang diinginkan
    channel = bot.get_guild(id server anda).text_channels[0]

    # Kirim pesan otomatis dengan daftar perintah
    help_message = (
        "Berikut adalah daftar perintah yang dapat digunakan:\n"
        "`l1n` - Menyalakan Lampu 1\n"
        "`l1m` - Mematikan Lampu 1\n"
        "`l2n` - Menyalakan Lampu 2\n"
        "`l2m` - Mematikan Lampu 2"
    )

    # Kirim pesan ke channel tersebut dengan jarak
    await channel.send(help_message)

@bot.command(name='l1n')
async def lamp1_on(ctx):
    try:
        requests.get(f'{lamp_ip}/lamp1_on', timeout=5)
        await ctx.send('Lampu 1 telah dinyalakan!\n' + get_help_message())
    except requests.RequestException as e:
        await ctx.send(f'Gagal menyalakan Lampu 1. Error: {e}')

@bot.command(name='l1m')
async def lamp1_off(ctx):
    try:
        requests.get(f'{lamp_ip}/lamp1_off', timeout=5)
        await ctx.send('Lampu 1 telah dimatikan!\n' + get_help_message())
    except requests.RequestException as e:
        await ctx.send(f'Gagal mematikan Lampu 1. Error: {e}')

@bot.command(name='l2n')
async def lamp2_on(ctx):
    try:
        requests.get(f'{lamp_ip}/lamp2_on', timeout=5)
        await ctx.send('Lampu 2 telah dinyalakan!\n' + get_help_message())
    except requests.RequestException as e:
        await ctx.send(f'Gagal menyalakan Lampu 2. Error: {e}')

@bot.command(name='l2m')
async def lamp2_off(ctx):
    try:
        requests.get(f'{lamp_ip}/lamp2_off', timeout=5)
        await ctx.send('Lampu 2 telah dimatikan!\n' + get_help_message())
    except requests.RequestException as e:
        await ctx.send(f'Gagal mematikan Lampu 2. Error: {e}')

# Tidak perlu command prefix di sini
@bot.command(name='bantuan')
async def help_command(ctx):
    # Kirim pesan dengan satu baris enter setelah status
    await ctx.send("\n" + get_help_message())

def get_help_message():
    return (
        "\nBerikut adalah daftar perintah yang dapat digunakan:\n"
        "`l1n` - Menyalakan Lampu 1\n"
        "`l1m` - Mematikan Lampu 1\n"
        "`l2n` - Menyalakan Lampu 2\n"
        "`l2m` - Mematikan Lampu 2"
    )

# Jalankan bot
bot.run('your token bot discord')
