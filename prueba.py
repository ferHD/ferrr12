import discord

client = discord.Client()

@client.event

async def on_ready():
    print("El bot esta ready")
    print("El bot ha entrado como: " + client.user.name)

@client.event

async def on_message(message):
    await client.change_presence(game=discord.Game(name='Configurando'))

    if message.content.startswith('buenas'):
        await client.send_message(message.channel, "Que pasa lokoo!!.")







client.run("NDMyNTUzMzg1MjA4NzA5MTIx.DqNsHA.k-_fm8rYRJuvYm6HQOBJbULVInk")
