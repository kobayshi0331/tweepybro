# herokuのchromedriverのPATHを指定
driver_path = '/app/.chromedriver/bin/chromedriver'
options = webdriver.ChromeOptions()
options.add_argument('--headless')
#※headlessにしている
driver = webdriver.Chrome(options=options, executable_path=driver_path)
