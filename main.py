print("welcome to spam detector")
spamwords = ["make a lot of money", "buy now", "click this",
             "subscribe this", "free", "win", "winner", "prize"]
user = input("paste the messege to  check: ").lower()
if any(spam in user for spam in spamwords):
    print("this looks like a spam")
else:
    print("this looks safe")
