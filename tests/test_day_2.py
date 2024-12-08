from src.day_2 import report_safe, report_safe_with_dampener

def test_report_safe():
    assert report_safe([7, 6, 4, 2, 1]) == True
    assert report_safe([1, 2, 7, 8, 9]) == False
    assert report_safe([9, 7, 6, 2, 1]) == False
    assert report_safe([1, 3, 2, 4, 5]) == False
    assert report_safe([8, 6, 4, 4, 1]) == False
    assert report_safe([1, 3, 6, 7, 9]) == True

def test_report_safe_with_dampener():
    assert report_safe_with_dampener([7, 6, 4, 2, 1]) == True
    assert report_safe_with_dampener([1, 2, 7, 8, 9]) == False
    assert report_safe_with_dampener([9, 7, 6, 2, 1]) == False
    assert report_safe_with_dampener([1, 3, 2, 4, 5]) == True
    assert report_safe_with_dampener([8, 6, 4, 4, 1]) == True
    assert report_safe_with_dampener([1, 3, 6, 7, 9]) == True
