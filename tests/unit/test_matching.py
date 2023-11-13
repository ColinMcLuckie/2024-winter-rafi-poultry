import pandas as pd
from pipeline import match_farms

def test_name_match_works_with_empty_input():
    """Checks that no errors are thrown for empty dataframe inputs"""
    mock_counterglow = pd.DataFrame({
        "Name": [],
        "State": []
    })
    mock_cafomaps = pd.DataFrame({
        "name": [],
        "state": []
    })
    df = match_farms.name_match(mock_counterglow, mock_cafomaps)
    assert True

def test_name_match_works_with_simple_input():
    """"""
    mock_counterglow = pd.DataFrame({
        "Name": ["Grngotts", "Stark Industries", "Python Corp", "Wonka Co"],
        "State": ["California", "Ontario", "Detroit", "Quebed"]
    })
    mock_cafomaps = pd.DataFrame({
        "name": ["Gringotts", "Wonka Co"],
        "state": ["California", "Hyde Park"]
    })
    df = match_farms.name_match(mock_counterglow, mock_cafomaps)
    matched_records = list(df[~df["No Match"]]["name"])
    missing_records = list(df[df["No Match"]]["name"])
    assert "Gringotts" in  matched_records
    assert "Wonka Co" in missing_records
