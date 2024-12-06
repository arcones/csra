import subprocess

def run_cli(*args):
    """Helper function to run the csra CLI and return the result."""
    result = subprocess.run(["csra"] + list(args), capture_output=True, text=True)
    return result


def test_success_single_word_query():
    single_word_query = "rheumatism"
    result = run_cli("--query", single_word_query)
    assert result.returncode == 0
    assert f"Received query: {single_word_query}" in result.stdout


def test_success_multiword_query():
    multiword_query = '"multiple sclerosis"'
    result = run_cli("--query", multiword_query)
    assert result.returncode == 0
    assert f"Received query: {multiword_query}" in result.stdout


def test_fail_multiword_query_not_quoted():
    result = run_cli("--query", "liver", "cirrhosis")
    assert result.returncode == 1
    assert "Error: It looks like your query isn't quoted.\nUsage: csra \"your query here\"" in result.stderr


def test_version():
    result = run_cli("--version")
    assert result.returncode == 0
    assert "csra version 0.0.10" in result.stdout
