# Panda Bamboo Scheduling

An algorithms project for the Bamboo Garden Trimming problem: choose a repeating cutting schedule that maximises the harvest guaranteed across bamboo plots with different growth rates.

The repository contains several problem instances and candidate schedules, plus a simulator that evaluates the minimum harvest over repeated cycles.

## Run an example

```bash
python3 pandaPrecision.py
```

Results are written to `panda-results.json` by default. A coursework username can optionally be set in `config.py`.

## Test

```bash
python3 -m unittest discover -s tests
```

## What this demonstrates

- periodic scheduling and greedy heuristics
- simulation of worst-case guarantees
- Python collections, type hints and JSON result persistence

This is an academic algorithms project; the included PDFs preserve the original problem context.
