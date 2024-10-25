
def test_frist_step():
	assert first_step(4388576018402626) ==  37

 def test_second_step():
	assert first_step(4388576018402626) ==  38

def test_check_for_visa():
	assert card_check(4388576018402626) == "Visa Card"

def test_check_for_master():
	assert card_check(5388576018402626) == "Master Card"

def test_check_for_american_express_card():
	assert card_check(3788576018402626) == "American Express Card"

def test_check_for_Discover_card():
	assert card_check(3788576018402626) == "Discover Card"

def test_check_for_invalid_card():
	assert card_check(2288576018402626) == "Invalid Card"

def test_check_for_validation_of_card():
	assert card_check [] (4388576018410707) == ["Visa Card", "4388576018402626", "16", "Valid"]

def test_check_for_Invalidation_of_card():
	assert card_check [] (4388576018402626") == ["Visa Card", "4388576018402626", "16", "Invalid"]









 



