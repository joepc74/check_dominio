import whois,os
from telebot import TeleBot
from dotenv import load_dotenv

bot=None

# Function to check if a domain is available
def check_domain(domain_name:str):
    try:
        domain_info = whois.whois(domain_name)
        # If the domain is not registered, the 'domain_name' key usually returns empty or raises an exception
        if domain_info.domain_name==None:
            return None
        elif domain_info.domain_name:
            return domain_info
    except Exception:
        return None

def check_domains():
    # Check each domain in the list
    for domain_name in os.getenv("DOMAIN_LIST").split(","):
        info=check_domain(domain_name)
        if info==None:
            # if the domain is available, print a message and send a notification to the super user
            print(f"Domain {domain_name} is available.")
            if bot==None:
                # If the bot is not initialized, initialize it
                bot=TeleBot(os.getenv("TELEGRAM_TOKEN"))

            bot.send_message(os.getenv("SUPER_USER"), f'Domain {domain_name} is available for registration!')
        # else:
        #     print("Domain is taken.")
        #     print(f"   Created on: {info.creation_date}")

if __name__=="__main__":
    # Load environment variables from .env file
    load_dotenv()

    check_domains()