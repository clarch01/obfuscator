from src.redactor import redactor
import pandas as pd
import pytest

d = {"student_id": 1234,
     "name": 'John Smith',
     "course": 'Software',
     "cohort": 'March',
     "graduation_date": '2024-03-31',
     "email_address": 'j.smith@email.com'
     }
test_df = pd.DataFrame(data=d, index=[1])


def test_should_censor_selected_fields():
    test = redactor(test_df, ["name"])
    assert test.at[1, 'name'] == 'xxx'


def test_should_raise_error_if_given_incorrect_column():
    with pytest.raises(Exception):
        redactor(test_df, ['names'])
