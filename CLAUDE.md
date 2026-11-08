# ets2-modhelper

Python 3.12 CLI that finds the mod crashing ETS2/ATS by bisecting the active mod list.
Public repository. Architecture: see `docs/architecture.md`.

## Commands

```bash
uv sync                      # install deps
uv run ets2-modhelper --help
uv run pytest                # tests
uv run ruff check --fix      # lint
uv run ruff format           # format
```

## Rules

- **Never modify real game files** (profile.sii, config.cfg, mod folder) during
  development. Work only against copies in `tests/fixtures/`.
- `core/` stays platform-independent and side-effect free: no real file system access
  to game directories, no subprocesses. OS specifics go into `platforms/`.
- No hard-coded user paths. Paths are discovered (Steam registry, libraryfolders.vdf,
  Known Folders incl. OneDrive redirection) or passed in by the user.
- Every feature must work for both ETS2 and ATS (see `games.py`).
- Fixtures must be anonymized (profile names, hex profile IDs, user paths, Steam IDs)
  and must never contain mod archives. See `tests/fixtures/README.md`.
- Verify file formats against fixtures and document them in `docs/formats.md`
  before writing a parser.
- Standard library first; add a dependency only with a clear reason.
- Code, comments, docs and commit messages in English (public repo).

## Build order

Log parser → profile.sii read/write → backup/restore → game start + crash
detection → bisection → report.
