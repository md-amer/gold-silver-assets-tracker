#Gold Silver Tracker
#By Amer

from bs4 import BeautifulSoup as BS
import requests
from time import sleep

#Assets present (in grams)
gold_amount = 0
silver_amount = 0

#Cost at which assets were bought (in Rupees/gram)
gold_cost_original = 0
silver_cost_original = 0

#Get current cost from internet
gold_cost_current = 0
silver_cost_current = 0

def get_gold_price():
	global gold_cost_current
	data = requests.get('https://www.policybazaar.com/gold-rate-bangalore/') 
	soup = BS(data.text, 'html.parser') 
	ans = soup.find("div", class_ = "dailyGoldrate").text 
	ans = ans.replace(',','') 
	gold_cost_current = (float(ans[:-3])/10)
	
def get_silver_price():
	global silver_cost_current
	data = requests.get('https://www.policybazaar.com/silver-rate-bangalore/') 
	soup = BS(data.text, 'html.parser') 
	print(soup)
	ans = soup.find("div", class_ = "dailyGoldrate").text 
	ans = ans.replace(',','') 
	silver_cost_current = (float(ans[:-3])/1000)
    
#Stats
def update_stats():
	global gold_profit_check, gold_profit, gold_profit_percent, silver_profit_check, silver_profit, silver_profit_percent, currency_spent, current_value_of_assets, total_profit
	
	gold_profit_check = gold_cost_current > gold_cost_original

	gold_profit = (gold_cost_current - gold_cost_original) * gold_amount

	gold_profit_percent = (gold_cost_current - gold_cost_original) / gold_cost_original *100
	gold_profit_percent = round(gold_profit_percent, 2)


	silver_profit_check = silver_cost_current > silver_cost_original

	silver_profit = (silver_cost_current - silver_cost_original) * silver_amount

	silver_profit_percent = (silver_cost_current - silver_cost_original) / silver_cost_original *100
	silver_profit_percent = round(silver_profit_percent, 2)
	
	currency_spent = (gold_amount * gold_cost_original) + (silver_amount * silver_cost_original)
	current_value_of_assets = (gold_amount * gold_cost_current) + (silver_amount * silver_cost_current)
	
	total_profit = current_value_of_assets - currency_spent
	
def output():
	print('Hello, Amer!')
	print('')
	print('You have '+str(gold_amount)+' g Gold and '+str(silver_amount)+' g Silver.')
	print('')
	print('Your total profit is Rs. '+str(total_profit)+'.')
	print('')
	print('The total value of your assets is Rs. '+str(current_value_of_assets)+'.')
	
def run():
	print('Welcome to Assets Tracker')
	print('')
	print('Loading assets',end='')
	dots()
	print('Accessing live prices',end='')
	dots()
	get_gold_price()
	get_silver_price()
	print('Updating stats',end='')
	dots()
	update_stats()
	print('')
	output()
	
def dots():
	for i in range(2):
		sleep(0.2)
		print('.',end=' ',flush=True)
	sleep(0.2)
	print('.',flush=True)
	
run()
