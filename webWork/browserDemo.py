import webbrowser
item = input("What are you shopping for?")

webbrowser.open(f"https://cabelas.com/SearchDisplay#q={item}")
webbrowser.open(f"https://amazon.com/s?k={item}")
webbrowser.open(f"https://www.bestbuy.com/site/searchpage.jsp?st={item}")