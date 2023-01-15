
import webbrowser

user_search = input('Enter a search term: ').replace(' ', '+')

webbrowser.open('https://www.google.ie/search?q=' + user_search)

