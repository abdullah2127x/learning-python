 # I ran Ruff on messy Python code with unused imports, inconsistent spacing, and mixed quotes. The output shows error codes like
 #   F401, E501 with [*] markers for some. Explain the difference between formatting and linting, what the error code letters mean
 #   (F, E, W, I, N), how Ruff knows which errors are auto-fixable, and the difference between ruff format vs ruff check.


  # Common Commands Cheatsheet

  # uv run ruff check .              # lint entire project
  # uv run ruff check --fix .        # lint + auto fix
  # uv run ruff format .             # format entire project
  # uv run ruff format --check .     # check format (no changes)
  # uv run ruff check src/main.py    # lint single file
  # 
  # 
  # 
  # 
  #   ---
  # What the Error Code Letters Mean

  # F — Pyflakes (logic/correctness problems)
  # F401  →  import os  (imported but unused)
  # F821  →  undefined name 'foo'
  # F841  →  local variable assigned but never used

  # E — pycodestyle Errors (style violations)
  # E501  →  line too long (> 88 chars)
  # E711  →  comparison to None (use `is` not `==`)
  # E302  →  expected 2 blank lines before function

  # W — pycodestyle Warnings (softer style issues)
  # W291  →  trailing whitespace
  # W293  →  whitespace before blank line
  # W605  →  invalid escape sequence '\d' (use r'\d')

  # I — isort (import organization)
  # I001  →  imports are not sorted/organized correctly

  # N — pep8-naming (naming conventions)
  # N801  →  class name should use CapWords  →  class my_class
  # N802  →  function name should be lowercase  →  def MyFunc()
  # N803  →  argument name should be lowercase