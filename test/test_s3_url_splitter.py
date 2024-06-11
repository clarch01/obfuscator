from src.s3_url_splitter import s3_url_splitter
import pytest


def test_function_should_accept_one_argument():
    with pytest.raises(TypeError):
        s3_url_splitter()
    with pytest.raises(TypeError):
        s3_url_splitter("x", "y")


def test_returns_a_dictionary_with_2_key_value_pairs():
    url = "s3://obfuscator-bucket/test-file"
    assert type(s3_url_splitter(url)) == dict
    assert len(s3_url_splitter(url)) == 2
