#test_blood_calculator.py
import pytest

@pytest.mark.parametrize("input_HDL, expected", [
	[70, "Normal"],
	[45, "Borderline low"],
	[20, "Low"]
	])
	
def test_check_HDL(input_HDL, expected):
	from blood_calculator import check_HDL
	
	result = check_HDL(input_HDL)
	assert result == expected
	
def test_check_LDL():
	from blood_calculator import check_LDL
	
	result = check_LDL(70)
	assert result == "Normal"

def test_check_TC():
	from blood_calculator import check_TC
	
	result = check_TC(70)
	assert result == "Normal"
	