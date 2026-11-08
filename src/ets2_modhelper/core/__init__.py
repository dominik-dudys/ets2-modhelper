"""Platform-independent logic: log parsing, SII read/write, bisection, reporting.

Nothing in this package may touch the real file system of a game installation
or start processes. Everything here must be testable with fixtures alone.
"""
