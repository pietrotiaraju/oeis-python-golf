# A000778

> a(n) = Catalan(n) + Catalan(n+1) - 1.
> — [OEIS A000778](https://oeis.org/A000778)

Offset 0: 1, 2, 6, 18, 55, 173, 560, 1858, 6291, 21657, 75581, 266797, 950911, …

### Python 3 — 45 bytes

```python
c=n=1
while 1:n+=1;print(c+(c:=4*c-6*c//n)-1)
```

**How it works**

- The Catalan numbers satisfy C_{m+1} = C_m·2(2m+1)/(m+2); with n = m + 2
  that is 4·C_m − 6·C_m/n, the update of [A000108](../A000108/), and
  6·C_m/n is an integer because C_{m+1} and 4·C_m are.
- Python evaluates `c+(c:=…)` left to right: the first `c` is still C_m,
  the walrus then computes C_{m+1} and stores it for the next round, so
  one expression both prints C_m + C_{m+1} − 1 and steps the sequence.
- Starting at `c=n=1`, the first round has n = 2: C_0 + C_1 − 1 = 1.
  `while 1:` with `n+=1` first is 1 byte under `c=1;n=2` /
  `while[print(…)]:n+=1` (46).

**Notes**

- Printing 5·C_m − 6·C_m/n − 1 and stepping `c` in a separate statement
  repeats `6*c//n` and is longer; carrying the pair (C_m, C_{m+1}) is 50.
- Exact integer arithmetic, correct for every n.
- The b-file has 201 terms (up to a(200)); the bar is the whole b-file in
  60 s. It prints them at once.
- a(n) first has more than 4300 digits at n = 7152, so printing stops
  there with a ValueError (about a second).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 45 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000778), CC BY-SA 4.0.
