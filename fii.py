from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from advanced_search import AdvancedSearchFundamentus

filters = {
  'divy_min': 0.1,
  'divy_max': 0.16,
  'pvp_min': 0.6,
  'pvp_max': 0.95,
  'mk_cap_min': 1000000000,
}

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

with webdriver.Chrome(options=chrome_options) as driver:
  advanced_search_fundamentus = AdvancedSearchFundamentus(driver)

  df = advanced_search_fundamentus.search("https://www.fundamentus.com.br/fii_buscaavancada.php", filters)

for column in ['Dividend Yield', 'P/VP', 'Valor de Mercado', 'Liquidez']:
  if column in df.columns:
    df = df.sort_values(by=column, ascending=column not in ['Dividend Yield', 'Valor de Mercado', 'Liquidez'])
    df.iloc[:5, df.columns.get_loc('Nota')] += 1

df = df.sort_values(by='Nota', ascending=False)

if not os.path.exists('data'):
  os.makedirs('data')

df.to_excel('/app/data/fii.xlsx', index=False)

print("Dados extraídos com sucesso!")