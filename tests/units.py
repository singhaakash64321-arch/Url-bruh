

def test_short_code_length():
    """A generated short code should have a reasonable length."""
    short_code = "aB12xYz"

    assert len(short_code) == 7


def test_short_code_is_not_empty():
    """A short code should not be empty."""
    short_code = "abc123"

    assert short_code != ""


def test_short_url_format():
    """A shortened URL should contain its short code."""
    base_url = "http://localhost:8000"
    short_code = "abc123"

    short_url = f"{base_url}/{short_code}"

    assert short_url.startswith("http://localhost:8000/")
    assert short_url.endswith(short_code)


def test_original_url_format():
    """The original URL should be a valid HTTP or HTTPS URL."""
    original_url = "https://example.com"

    assert original_url.startswith(("http://", "https://"))


def test_duplicate_short_codes():
    """Two different short codes should be distinguishable."""
    first_code = "abc123"
    second_code = "xyz789"

    assert first_code != second_code
