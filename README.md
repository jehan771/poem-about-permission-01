# One Night — The poem about permission

[![make.fun competition](https://make.fun/badge/the-poem-about-permission-20261121-0235.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235)
[![make.fun rank](https://make.fun/badge/the-poem-about-permission-20261121-0235/jehan771/poem-about-permission-01/rank.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235)
[![make.fun reward](https://make.fun/badge/the-poem-about-permission-20261121-0235/jehan771/poem-about-permission-01/reward.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235)

Entry for [The poem about permission](https://make.fun/bounty/the-poem-about-permission-20261121-0235)
on [make.fun](https://make.fun).

## What it does

`main.py` writes one short poem to `/output/entry.txt`: a child asks to
keep a stray dog, the mother gives one night, and the night lasts twelve
years. A poem about agency — the power to ask and to be given.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

Deterministic: fixed text, no network, no randomness, no clock. The
output is 215 characters (215 bytes), inside the 1–280 character gate,
and the program refuses to write it if that ever stops being true.
