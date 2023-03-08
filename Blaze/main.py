from Automation import Bot

bot = Bot()

# bot.Start(False)
bot.Start()

login, reason = bot.Login(email="digaodigao1@gmail.com", password="pG9012**")

if login == True:
    
    real, bonus, currencie= bot.Get_Balance()
    print(f"Balance: Real:{real} Bonus:{bonus}")
     
    
    
    # Uncomment to perform a bet
    # doubleBet = bot.Bet(game="double", bets=[{ "color": "red", "amount": 1.7 }], return_results=True)
    # print(doubleBet)
    
    crashBet = bot.Bet(game="crash", bets=[{"autoCashout": 1.2, "amount": 0.1}], return_results=True)
    print(crashBet)
    
    real, bonus, currencie= bot.Get_Balance()
    print(f"Balance: Real:{real} Bonus:{bonus}")
else:
    print(reason)


bot.Stop()