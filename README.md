# ets2-modhelper

Find the mod that crashes **Euro Truck Simulator 2** or **American Truck Simulator** —
automatically, by bisecting your active mod list instead of guessing.

> 🚧 Early development. Not usable yet.

## How it works (planned)

1. Backs up your profile and config.
2. Checks that the game crashes with all mods and starts without mods.
3. Repeatedly enables half of the suspicious mods, starts the game and watches for a crash.
4. Reports the mod (or combination of mods) causing the crash and restores everything.

Works for crashes that happen **reproducibly** on start or while loading a profile —
not for random crashes while driving.

## Platforms

- Windows — first target
- macOS — planned

## Development

Requires [uv](https://docs.astral.sh/uv/).

```bash
uv sync
uv run ets2-modhelper --help
uv run pytest
```

See [docs/architecture.md](docs/architecture.md).

## Disclaimer

Not affiliated with or endorsed by SCS Software. Use at your own risk — the tool modifies
your profile files, but always creates a backup first.

## License

[MIT](LICENSE)
