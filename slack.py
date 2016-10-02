from slackbot.bot import listen_to, respond_to

@listen_to('help')
def help(message):
    message.reply("Hi, I can help you")
