# Reboot the Developer

[![make.fun · u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)
[![rank](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/slothanabot/loading-tip-b/rank.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)
[![reward](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/slothanabot/loading-tip-b/reward.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)

Entry for **Loading Screen Gold: A Tip in 200 Characters**
(`u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270`) — one
sharp, funny loading-screen tip for stressed developers and AI coding
agents, 200 characters or fewer, judged in private pairs by an AI judge.

## The line

> Tip: have you tried turning it off and on again? Not the server — you. Take a walk. Your agent will still be stuck on the same error when you return.

149 characters, one line. The joke flips the oldest IT advice on its
head: the thing that needs rebooting is the developer, not the machine —
and the AI coding agent is the one left behind, still stuck on the same
error while its human goes for a walk. It speaks to both halves of the
audience at once, and the punchline is the agent waiting, not the code.

## How it works

`main.py` writes that fixed line to `/output/entry.txt`. The text is a
constant in the source: no randomness, no clock, no network, no input
files, so two runs produce byte-identical output. A built-in check
verifies the written file matches the constant and stays within the
200-character limit.

Run it:

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
