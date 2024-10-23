import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AdvancedSearchFundamentus:
  def __init__(self, driver):
    self.driver = driver

  def search(self, url, filters):
    self.driver.get(url)

    for filter_name, value_input in filters.items():
      input_field = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//input[@name='{filter_name}']"))
      )
      input_field.clear()
      input_field.send_keys(str(value_input))

    search_button = WebDriverWait(self.driver, 10).until(
      EC.element_to_be_clickable((By.CLASS_NAME, "buscar"))
    )
    search_button.click()

    table = WebDriverWait(self.driver, 10).until(
      EC.presence_of_element_located((By.TAG_NAME, 'table'))
    )

    return self._extract_table(table)

  def _extract_table(self, table):
    headers = []
    for th in table.find_element(By.TAG_NAME, 'thead').find_elements(By.TAG_NAME, 'th'):
      if th.value_of_css_property("display") != "none":
        headers.append(th.text)

    rows = []
    for row in table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr'):
      row_data = []
      for cell in row.find_elements(By.TAG_NAME, 'td'):
        if cell.value_of_css_property("display") != "none":
          row_data.append(cell.text)
      if row_data:
        link = row.find_element(By.TAG_NAME, 'a')
        row_data[0] = link.text
        row_data.append(0)
        rows.append(row_data)

    headers.append('Nota')
    return pd.DataFrame(rows, columns=headers)