from __future__ import division

def ExactMatch(mention, menu_item):
    '''
        check for exact match of strings
    '''
    if mention == menu_item:
        return True
    else:
        return False

def CharMatch(mention, menu_item):
    '''
        counts similar characters
    '''
    length1 = len(menu_item)
    length2 = len(mention)
    matched = 0
    i,j,count,big = 0,0,0,0

    if length1 == length2:
        matched = [x == y for (x, y) in zip(mention, menu_item)].count(True)
        return matched
    elif length1 > length2:
        while i < length1:
            if j < length2 and menu_item[i] == mention[j]:
                j += 1
                count += 1
            else:
                if big < count:
                    big = count
                j = 0
                count = 0
            i += 1
    else:
        while i < length2:
            if j < length1 and mention[i] == menu_item[j]:
                j += 1
                count += 1
            else:
                if big < count:
                    big = count
                j = 0
                count = 0
            i += 1

    return big


def PercentMatch(mention, menu_item, percent):
    '''
        counts the number of chars matched and should be above
        certain percent of the smaller
    '''
    matched = CharMatch(mention, menu_item)
    if len(mention) <= len(menu_item):
        if percent < matched /len(mention):
            return True
        else:
            return False
    else:
        if percent < matched /len(menu_item):
            return True
        else:
            return False


def PartialMatch(mention, menu_item):
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

	if words_matched >= (len(words_mention)/2) :
		return True
	else:
		return False

def FuzzyMatch(mention, menu_item, edit):
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
            if mention[j-1] == menu_item[i-1]:
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

def SubstringMatch(mention, menu_item):
    '''
        Checks if either of strings part of the other
    '''
    if mention in menu_item or menu_item in mention:
        return True
    else:
        return False
