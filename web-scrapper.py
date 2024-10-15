import re
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

####GET LIST OF MOVIES
driver = webdriver.Chrome()
driver.maximize_window()
# movie_urls = [
#     'https://www.imdb.com/search/title/?title_type=feature&genres=action',
#     'https://www.imdb.com/search/title/?title_type=feature&genres=adventure',
#     # 'https://www.imdb.com/search/title/?title_type=feature&genres=animation',
#     # 'https://www.imdb.com/search/title/?title_type=feature&genres=biography',
#     # 'https://www.imdb.com/search/title/?title_type=feature&genres=comedy',
#     # 'https://www.imdb.com/search/title/?title_type=feature&genres=crime',
#     # 'https://www.imdb.com/search/title/?title_type=feature&genres=documentary',
#     # 'https://www.imdb.com/search/title/?title_type=feature&genres=drama',
#     # 'https://www.imdb.com/search/title/?title_type=feature&genres=family',
#     # 'https://www.imdb.com/search/title/?title_type=feature&genres=fantasy',
#     # 'https://www.imdb.com/search/title/?title_type=feature&genres=film-noir',
#     # 'https://www.imdb.com/search/title/?title_type=feature&genres=history',
#     # 'https://www.imdb.com/search/title/?title_type=feature&genres=horror',
#     # 'https://www.imdb.com/search/title/?title_type=feature&genres=musical',
#     # 'https://www.imdb.com/search/title/?title_type=feature&genres=mystery',
#     # 'https://www.imdb.com/search/title/?title_type=feature&genres=romance',
#     # 'https://www.imdb.com/search/title/?title_type=feature&genres=sci-fi',
#     # 'https://www.imdb.com/search/title/?title_type=feature&genres=sport',
#     # 'https://www.imdb.com/search/title/?title_type=feature&genres=thriller',
#     # 'https://www.imdb.com/search/title/?title_type=feature&genres=war',
#     # 'https://www.imdb.com/search/title/?title_type=feature&genres=western'
# ]

# def click_load_more():
#     try:
#         load_more_button = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, '//button[@class="ipc-btn ipc-btn--single-padding ipc-btn--center-align-content ipc-btn--default-height ipc-btn--core-base ipc-btn--theme-base ipc-btn--on-accent2 ipc-text-button ipc-see-more__button"]'))
#         )
#         driver.execute_script("arguments[0].scrollIntoView();", load_more_button)
#         time.sleep(5)
#         ActionChains(driver).move_to_element(load_more_button).click().perform()
#     except Exception as e:
#         print(f"Failed to click 'Load More' button: {str(e)}")

# def extract_imdb_id(url):
#     match = re.search(r'/title/tt(\d+)/', url)
#     if match:
#         return f'tt{match.group(1)}'
#     else:
#         return None

# href_list = []

# for movie_url in movie_urls:
#     driver.get(movie_url)
#     duration = 10
#     end_time = time.time() + duration

#     while time.time() < end_time:
#         click_load_more()
#         time.sleep(5)
        
#         elements = driver.find_elements(By.CLASS_NAME, 'ipc-title-link-wrapper')
#         new_href_values = [extract_imdb_id(element.get_attribute('href')) for element in elements]
#         new_href_values = [value for value in new_href_values if value is not None]
        
#         if not new_href_values:
#             break
        
#         href_list.extend(new_href_values)

# unqiue_list_urls = list(set(href_list))


# ###GET MOVIE DATA

driver.get('https://www.imdb.com/title/tt1856101/')

title = ''
img_src = ''
desc = ''
formatted_date = ''
movie_runtime = ''
genres = ''
director_name = ''
cast_members = ''
original_language = ''

try:
    title = driver.find_element(By.CSS_SELECTOR, '[data-testid="hero__pageTitle"] .hero__primary-text').text.strip()
except:
    print("No Title")

img_container = driver.find_element(By.CLASS_NAME, 'ipc-lockup-overlay')
img_src = img_container.get_attribute('href')

desc = driver.find_element(By.CLASS_NAME, 'ipc-html-content-inner-div').text.strip()

formatted_date = driver.find_element(By.CLASS_NAME, 'ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link').text.strip()

movie_dict = {
        'Poster':img_src,
        'Title': title,
        'Plot': desc,
        'Released': formatted_date,
        'Runtime': movie_runtime,
        'Genre': genres,
        'Director': director_name,
        'Actors': cast_members,
        'Language': original_language
    }

print(json.dumps(movie_dict, indent=2))

driver.quit()
