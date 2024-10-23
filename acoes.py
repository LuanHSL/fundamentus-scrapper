from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from advanced_search import AdvancedSearchFundamentus

filters = {
  'pl_min': 3.5,
  'pl_max': 12,
  'pvp_min': 0.5,
  'pvp_max': 2.3,
  'roe_min': 0.15,
  'roe_max': 0.3,
  'divy_min': 0.07,
  'divy_max': 0.2,
  'liq_min': 1000000,
  'divbruta_max': 2,
  'tx_cresc_rec_min': 0.1,
}

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

with webdriver.Chrome(options=chrome_options) as driver:
  advanced_search_fundamentus = AdvancedSearchFundamentus(driver)

  df = advanced_search_fundamentus.search("https://www.fundamentus.com.br/buscaavancada.php", filters)

for column in ['P/L', 'P/VP', 'Div.Yield', 'ROE', 'Liq.2meses', 'Dív.Brut/ Patrim.', 'Cresc. Rec.5a']:
  if column in df.columns:
    df = df.sort_values(by=column, ascending=column not in ['Div.Yield', 'ROE', 'Liq.2meses', 'Cresc. Rec.5a'])
    df.iloc[:5, df.columns.get_loc('Nota')] += 1

df = df.sort_values(by='Nota', ascending=False)

if not os.path.exists('data'):
  os.makedirs('data')

df.to_excel('/app/data/acoes.xlsx', index=False)

print("Dados extraídos com sucesso!")