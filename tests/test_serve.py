"""Unit tests for ple-engineer-harness."""

from __future__ import annotations

import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import serve  # noqa: E402


class TestServeHelpers(unittest.TestCase):
  """Tests for verdict parsing and verifier configuration."""

  def test_parse_verdict_pass(self) -> None:
    passed, text = serve.parse_verdict("All checks passed.\nVERDICT: PASS")
    self.assertTrue(passed)
    self.assertIn("VERDICT: PASS", text)

  def test_parse_verdict_fail(self) -> None:
    passed, text = serve.parse_verdict("VERDICT: FAIL\n1. Missing output.zip")
    self.assertFalse(passed)
    self.assertIn("Missing output.zip", text)

  def test_parse_verdict_fail_takes_precedence(self) -> None:
    passed, _ = serve.parse_verdict("VERDICT: PASS? No, VERDICT: FAIL")
    self.assertFalse(passed)

  def test_parse_verdict_ambiguous_defaults_to_fail(self) -> None:
    passed, _ = serve.parse_verdict("Looks okay maybe.")
    self.assertFalse(passed)

  def test_tools_include_core_four(self) -> None:
    names = {t["function"]["name"] for t in serve.TOOLS}
    self.assertEqual(names, {"bash", "read_file", "write_file", "edit_file"})


if __name__ == "__main__":
  unittest.main()
