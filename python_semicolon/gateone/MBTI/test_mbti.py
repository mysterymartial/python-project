import mbti

def test_get_first_response_E():
	assert mbti.get_first_response(["A","B","B","A","A","A","A","B","A","B","B","B","A","A","B","A","B","A","A","A"]) == "E" 

def test_get_first_response_I():
	assert mbti.get_first_response(["B","B","B","A","B","A","A","B","B","B","B","B","B","A","B","A","B","A","A","A"]) ==  "I"

def test_get_second_response_S():
	assert mbti.get_second_response(["B","A","B","A","B","A","A","B","B","A","B","B","B","A","B","A","B","A","A","A"]) == "S"

def test_get_second_response_N():
	assert mbti.get_second_response(["B","B","B","A","B","B","A","B","B","B","B","B","B","B","B","A","B","A","A","A"]) == "N"

def test_get_third_response_T():
	assert mbti.get_third_response(["B","B","A","A","B","B","A","B","B","B","A","B","B","B","A","A","B","A","A","A"]) == "T"

def test_get_third_response_F():
	assert mbti.get_third_response(["B","B","B","A","B","B","B","B","B","B","B","B","B","B","B","A","B","A","A","A"]) == "F"

def test_get_fourth_response_J():
	assert mbti.get_fourth_response(["B","B","B","A","B","B","A","A","B","B","B","A","B","B","B","A","B","A","A","A"]) == "J"

def test_get_fourth_response_P():
	assert mbti.get_fourth_response(["B","B","B","B","B","B","A","B","B","B","B","B","B","B","B","B","B","A","A","A"]) == "P"

def test_get_personality():
	result = mbti.get_personality("E", "S", "T", "J")
	expected = "The Supervisor (ESTJ)ESTJs are organized and governed by the zeal to do what is right and socially acceptable. They epitomize the ideal individual who is on the track toward doing what is good and right. They are happy to be of help.Their dominant cognitive function is extraverted thinking which makes them quite practical when compared to other personality types. The auxiliary cognitive functions are introverted sensing which makes them very keen on details and stability.The ESTJs like to work in management positions where they can oversee operations and put in structures. In relationships, they love routines and their loved ones know that they can always be depended on for anything."
	assert result == expected
