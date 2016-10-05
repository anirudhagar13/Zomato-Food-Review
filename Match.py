def partialMatch(mention_text, menu_item_text):
	'''
		a partial match occurs when more than
		half of the words in the mention can be 
		found in the menu item's name and description
	'''
	words_matched = 0
	words_mention = mention_text.split(" ")
	words_menu = menu_item_text.split(" ")
	if len(words_mention) <= len(words_menu):
		for i in words_mention:
			if i in words_menu:
				words_matched += 1
	else:
		for i in words_menu:
			if i in words_mention:
				words_matched += 1

	if words_matched >= (len(words_mention)/2 + 1) :
		return True
	else:
		return False
