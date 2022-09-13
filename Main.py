import disnake, os
from disnake.ext import commands



intents = disnake.Intents.all()
intents.message_content = True
bot = commands.InteractionBot(intents=intents)

DEALER = 558040366889304105




class slashCommands():

    def __init__(self) -> None:
        None

    @bot.slash_command(description="Place a bet", dm_permission=True)
    async def placebet(self, ctx, bet : int):
        Dealer = await bot.fetch_user(DEALER)
        DealerDm = await Dealer.create_dm()

        await DealerDm.send(f"{ctx.author} has submitted a bet of :{bet}")
        await ctx.response.send_message(content=f"Bet of {bet} has been submitted", ephemeral=True)


    @bot.slash_command(description="HIT", dm_permission=True)
    async def hit(ctx):
        Dealer = await bot.fetch_user(DEALER)
        DealerDm = await Dealer.create_dm()

        await DealerDm.send(f"{ctx.author} hits!")
        await ctx.response.send_message(content="You hit", ephemeral=True)

        
    @bot.slash_command(description="STAND", dm_permission=True)
    async def stand(ctx):
        Dealer = await bot.fetch_user(DEALER)
        DealerDm = await Dealer.create_dm()

        await DealerDm.send(f"{ctx.author} stands!")
        await ctx.response.send_message(content="You stand", ephemeral=True)


    @bot.slash_command(description="SPLIT", dm_permission=True)
    async def split(ctx):
        Dealer = await bot.fetch_user(DEALER)
        DealerDm = await Dealer.create_dm()

        await DealerDm.send(f"{ctx.author} splits!")
        await ctx.response.send_message(content="You split", ephemeral=True)

bot.run(os.getenv("ToePicBotKey"))