# Architecture

## Goal

When ETS2/ATS crashes reproducibly (on start or while loading a profile), find the
mod — or combination of mods — that causes it, by automatically bisecting the active
mod list instead of guessing.

## Layers

```
cli.py            argument parsing, user interaction
core/             platform-independent, pure logic
  logparse        read game.log.txt / crash logs, flag outdated mods
  sii             read/write profile.sii (plain-text SII), keep load order
  bisect          bisection incl. detection of mod combinations
  report          result + log of all runs
platforms/        OS adapters behind one interface
  windows         Steam/registry/libraryfolders.vdf, Known Folders (OneDrive!),
                  start/stop eurotrucks2.exe, crash detection
  macos           later
games.py          ETS2 / ATS definitions
```

### Key design rule

`core.bisect` talks to the game only through an interface like
`run(mods) -> Outcome(CRASH | OK)`. Tests replace the game with a simulator
(e.g. "mods 17 and 42 together crash"), so the whole algorithm can be developed and
tested on any OS without the game.

## Safety

The tool changes other people's files.

- Back up `profile.sii` and `config.cfg` before any change.
- Always restore — also on Ctrl+C, exceptions and crashes of the tool itself.
- `--dry-run` must never write anything.
- Warn about Steam Cloud profiles (the cloud may overwrite changed files).

## Workflow (planned)

1. Detect game, user directory and profiles; user picks a profile.
2. Baseline: all mods (must crash) and no mods. If it also crashes with no mods →
   report "profile references missing mod content" and stop.
3. Bisect until the culprit (or combination) is found.
4. Restore everything, print report.

Only reproducible crashes are supported, not random crashes while driving.
