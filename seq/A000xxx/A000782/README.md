# A000782

> a(n) = 2*Catalan(n) - Catalan(n-1).
> — [OEIS A000782](https://oeis.org/A000782)

Offset 1: 1, 3, 8, 23, 70, 222, 726, 2431, 8294, 28730, 100776, 357238, 1277788, …

### Python 3 — 46 bytes

```python
c=n=1
while 1:n+=1;print(-c+2*(c:=4*c-6*c//n))
```

**How it works**

- The Catalan numbers satisfy C_m = C_{m−1}·2(2m−1)/(m+1); with n = m + 1
  that is 4·C_{m−1} − 6·C_{m−1}/n, the update of [A000108](../A000108/),
  and the division is exact because C_m and 4·C_{m−1} are integers.
- `-c` is read while `c` is still C_{m−1}; then the walrus steps `c` to
  C_m, so `-c+2*(c:=…)` is 2·C_m − C_{m−1} and leaves C_m for the next
  round. Python evaluates operands left to right, which is what makes the
  two `c`s differ.
- Starting at `c=n=1`, the first round has n = 2 and C_0 = 1, so it prints
  a(1) = 2·1 − 1 = 1. `while 1:` with `n+=1` first is 1 byte under
  `c=1;n=2` / `while[print(…)]:n+=1` (47).

**Notes**

- The closed form a(m) = (7m−5)/(m+1)·C_{m−1} = 7·C_{m−1} − 12·C_{m−1}/n
  (n = m + 1 as above) needs a separate step for `c` and is longer than
  the walrus.
- [A000781](../A000781/) is the same program with `~c+3*`.
- Exact integer arithmetic, correct for every n.
- The b-file has 1000 terms (up to a(1000)); the bar is the whole b-file
  in 60 s. It prints them in a fraction of a second.
- a(n) first has more than 4300 digits at n = 7152, so printing stops
  there with a ValueError (about a second).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 46 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000782), CC BY-SA 4.0.
