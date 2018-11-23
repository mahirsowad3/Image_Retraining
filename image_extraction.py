from giextractor import GoogleImageExtractor
from selenium import webdriver

imageExtractor = GoogleImageExtractor()
imageExtractor.extract_images(imageQuery='bed', imageCount=300)
