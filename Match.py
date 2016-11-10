def ExactMatch(mention, menu_item):
    if mention == menu_item:
        return True
    else:
        return False
def horsepool(mention, menu_item):

def partialMatch(mention, menu_item):
	'''
		a partial match occurs when more than
		half of the words in the mention can be
		found in the menu item's name and description
	'''
	words_matched = 0
	words_mention = mention.split(" ")
	words_menu = menu_item.split(" ")
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

def Fuzzymatch(mention, menu_item, edit):
    '''
        Create a table to store results of subproblems
        Compares edit distance between strings, equal
        if less than edit parameter.
    '''
    m = len(mention)
    n = len(menu_item)
    dp = [[0 for x in range(m+1)] for x in range(n+1)]

    # Initialize matrix
    for i in list(range(n+1)):
        dp[i][0] = i
    for i in list(range(m+1)):
        dp[0][i] = i

    # Measuring Edit distance
    for i in range(1, n+1):
        for j in range(1, m+1):
            # If characters match
            if str1[j-1] == str2[i-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min( dp[i-1][j],
                                dp[i-1][j-1],
                                dp[i][j-1]) + 1

    # Edit distance @end position of matrix
    dist = dp[n][m]
    if dist > edit:
        return False
    else:
        return True

def Substring(mention, menu_item):
    '''
        Checks if either of strings part of the other
    '''
    if mention in menu_item or menu_item in mention:
        return True
    else:
        return False
