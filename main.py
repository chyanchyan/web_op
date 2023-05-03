from selenium import webdriver


def add_option():
    chrome_options = webdriver.ChromeOptions()
    # 不加载图片
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    # 使用无界面浏览器模式！！
    chrome_options.add_argument('--headless')
    # 使用隐身模式（无痕模式）
    chrome_options.add_argument('--incognito')
    # 禁用GPU加速
    chrome_options.add_argument('--disable-gpu')
    # 禁用通知警告
    chrome_options.add_argument('–disable - notifications')

    return chrome_options


