import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Recipe(client.Cog):#Class thing no touchy!!!111

    def __init__(self, bot):
         self.b = bot #Please no touchy thx

    @client.command()
    async def recipe(self,ctx): 
        recipes = ["https://www.foodnetwork.com/recipes/giada-de-laurentiis/smore-brownie-bites-recipe-2125911", "https://www.foodnetwork.com/recipes/rich-nut-cookies-recipe-1913332", "https://www.foodnetwork.com/recipes/sandra-lee/chocolate-caramel-brownies-recipe-1924027", "https://www.foodnetwork.com/recipes/apple-muffins-recipe-1927541", "https://www.foodnetwork.com/recipes/claire-robinson/brown-butter-banana-muffins-recipe-1920734", "https://www.foodnetwork.com/recipes/aaron-mccargo-jr/easy-sticky-buns-recipe-1924654", "https://www.foodnetwork.com/recipes/anne-thornton/nutella-banana-brioche-bread-pudding-recipe-1923849", "https://www.foodnetwork.com/recipes/ina-garten/fresh-peach-cake-recipe-1923148", "https://www.foodnetwork.com/recipes/patrick-and-gina-neely/cookie-pizza-recipe-1924170", "https://www.foodnetwork.com/recipes/melissa-darabian/petite-orange-and-raspberry-pochettes-recipe-1973221", "https://www.foodnetwork.com/recipes/ina-garten/cinnamon-elephant-ears-recipe-1923543", "https://www.foodnetwork.com/recipes/claire-robinson/lemon-pie-cookies-recipe-1923177", "https://www.foodnetwork.com/recipes/patrick-and-gina-neely/honey-cornbread-muffins-recipe-2013336", "https://www.foodnetwork.com/recipes/double-fudge-bread-pudding-with-chocolate-whipped-topping-recipe-1923356", "https://www.foodnetwork.com/recipes/giada-de-laurentiis/double-chocolate-and-mint-cookies-recipe-2010334", "https://www.foodnetwork.com/recipes/sandra-lee/milk-chocolate-cupcakes-with-dark-chocolate-icing-recipe-1923562", "https://www.foodnetwork.com/recipes/aaron-mccargo-jr/zucchini-and-apple-bread-recipe-1924223", "https://www.foodnetwork.com/recipes/food-network-kitchen/vanilla-cupcakes-recipe2-2042539", "https://www.foodnetwork.com/recipes/sunny-anderson/open-faced-plum-tart-recipe2-1973744", "https://www.foodnetwork.com/recipes/marcela-valladolid/polvorones-ground-walnut-cookies-recipe-1960437", "https://www.foodnetwork.com/recipes/anne-thornton/mama-thorntons-peach-pie-recipe-2047258", "https://www.foodnetwork.com/recipes/pumpkin-spice-cupcakes-with-brown-butter-buttercream-recipe-1923349", "https://www.foodnetwork.com/recipes/chocolate-cupcakes-with-ganache-and-marshmallow-frosting-recipe-1923296", "https://www.foodnetwork.com/recipes/melissa-darabian/chocolate-sponge-puddings-recipe-2014543", "https://www.foodnetwork.com/recipes/bubbys-sour-cherry-pie-recipe-2200888"]
        recipe_list = ["Oh, here's a really good one!", "This one's fun to make!", "Just wash your gross hands, first!", "This one's delicious!"]
        async with ctx.message.channel.typing():
            await asyncio.sleep(conf.type_speed)  
        await ctx.send(random.choice(recipe_list))
        await ctx.send(random.choice(recipes))


def setup(bot):#No no child keep your hands off or this will break and not load
    bot.add_cog(Recipe(bot))
