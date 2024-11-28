import unittest
import subprocess


class TestCSRA(unittest.TestCase):
    def run_cli(self, *args):
        result = subprocess.run(["csra"] + list(args), capture_output=True, text=True)
        return result

    def test_success_single_word_query(self):
        single_word_query = "rheumatism"
        result = self.run_cli("--query", single_word_query)
        self.assertEqual(0, result.returncode)
        self.assertIn(f"Received query: {single_word_query}", result.stdout)

    def test_success_multiword_query(self):
        multiword_query = '"multiple sclerosis"'
        result = self.run_cli("--query", multiword_query)
        self.assertEqual(0, result.returncode)
        self.assertIn(f"Received query: {multiword_query}", result.stdout)

    def test_fail_multiword_query_not_quoted(self):
        not_quoted_multiword_query = "liver cirrhosis"
        result = self.run_cli("--query", not_quoted_multiword_query)
        self.assertEqual(0, result.returncode)
        self.assertIn("Error: It looks like your query isn\'t quoted.\nUsage: csra \"your query here\"", result.stderr)

    def test_version(self):
        result = self.run_cli("--version")
        self.assertEqual(0, result.returncode)
        self.assertIn("csra version 0.1.0", result.stdout)


if __name__ == "__main__":
    unittest.main()
