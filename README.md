# TRPP

This repository contains a Python script to fetch champion win rates from [u.gg](https://u.gg).

## Usage

```bash
python3 winrate_parser.py <champion_slug>
```

Before running the script make sure the required Python packages are installed:

You can install them individually or via the provided `requirements.txt`:

```bash
pip install -r requirements.txt
```

Example:

```bash
python3 winrate_parser.py ahri
```

This will print the role with the highest pick rate on u.gg and the corresponding win rate.
