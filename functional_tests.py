from selenium import webdriver
# import org.openqa.selenium.WebDriver;
# import org.openqa.selenium.chrome.ChromeDriver;

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title 