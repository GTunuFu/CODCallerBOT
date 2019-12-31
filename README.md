# CODCallerBOT
Call of Duty Modern Warfare stats Discord bot. Once added to a server all members will be able to call and react with the bot's assigned functions.

**Version 1(month) .0(production level: ground) .1(upload #)**
  - So far just running test on the bot. It has three working client events:
    - Alert when bot is ready
      ```
      @client.event
      async def on_ready(): #when function is ready to run
          print('Bot is ready.')                     
      # common first event to run      
      ```
    - Alert when member joins
      ```
      @client.event
      async def on_member_join(member):
          print(f'{member} has joined a server.')
       ```
    - Alert when member leaves
      ```
      @client.event
      async def on_member_remove(member):
          print(f'{member} has left a server')
      # this work with any form of leaving ie. kicking, leaving, banning
      ```
  - I have uploaded a virtual environment to access the Discord API
  
  **Version 1.0.2**
  
  - started to mess around with simple command functions
      one of the commands will call for ping (keep in mind when typing a comman must include '.' before as this is defult           command caller in discord.
      ```
      @client.command() #legit just a command
      async def ping(ctx):
          await ctx.send(f'Pong! {round(client.latency * 1000)}ms')
      ```
      the ctx passed through in ping() is so we can look for a a command.
      
      for the second command we import ```random``` library so we can simulat an 8ball.
      ```
      @client.command(aliases=['8ball','test']) #works as these any of these functions can call for the command
      async def _8ball(ctx, *, question):
          responses = ['It is certain',
                'It is decidedly so',
                'Without a doubt',
                'Yes - definitely',
                  ***
                  ***
                  ***
                'Outlook not so good',
                'Very doubtful']
     await ctx.send(f'Question: {question} \n Answer: {random.choice(responses)}')
     ```
     With the same ctx parameter we do ```*, question``` to take in multiple arguements. Then we wait for command context and      then send to console, or so to say
     
      
      
