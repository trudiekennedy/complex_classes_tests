from lib.most_often import *

# Test for the starting list
def test_initial_starting_list():
    initial_list = MostOften(["apple", "banana"])
    assert initial_list.starting_list == ["apple", "banana"]

# Test for adding a new item
def test_add_new_item():
    initial_list = MostOften(["apple", "banana"])
    initial_list.add_new("pear")
    assert initial_list.starting_list == ["apple", "banana", "pear"]

# Test to see if we get a set
def test_where_one_item_occurs_more():
    initial_list = MostOften(["hello", "hello", "goodbye"])
    highest_letter = initial_list.get_most_often()
    assert highest_letter == "hello"

# Test where there's no winner
def test_no_clear_winner():
    initial_list = MostOften(["apple", "banana", "pear"])
    highest_letter = initial_list.get_most_often()
    assert highest_letter == "no clear winner"

# Test a string with multiple unique characters
def test_strings_with_multiple_unique_chars():
    initial_list = MostOften("Hello")
    highest_letter = initial_list.get_most_often()
    assert highest_letter == "l"

# Test a with a list of numbers 
def test_with_numbers_list():
    initial_list = MostOften([1, 2, 3, 4, 1, 1])
    highest_number = initial_list.get_most_often()
    assert highest_number == 1

# Test with a mixed string input
def test_with_mixed_string():
    initial_list = MostOften("HGFIOHF444T0438U30GUEP44E-IF=Q!!")
    highest_char = initial_list.get_most_often()
    assert highest_char == "4"