# A000781

> a(n) = 3*Catalan(n) - Catalan(n-1) - 1.
> — [OEIS A000781](https://oeis.org/A000781)

Offset 1: 1, 4, 12, 36, 111, 353, 1154, 3860, 13155, 45525, 159561, 565249, 2020687, …

### Python 3 — 46 bytes

```python
c=n=1
while 1:n+=1;print(~c+3*(c:=4*c-6*c//n))
```

**How it works**

- The Catalan numbers satisfy C_m = C_{m−1}·2(2m−1)/(m+1); with n = m + 1
  that is 4·C_{m−1} − 6·C_{m−1}/n, the update of [A000108](../A000108/),
  and the division is exact because C_m and 4·C_{m−1} are integers.
- `~c` is −c − 1, read while `c` is still C_{m−1}; then the walrus steps
  `c` to C_m, so `~c+3*(c:=…)` is 3·C_m − C_{m−1} − 1 and also leaves C_m
  for the next round. Left-to-right evaluation makes the order right; the
  `~` saves the `-1`.
- Starting at `c=n=1`, the first round has n = 2 and C_0 = 1, so it prints
  a(1) = 3·1 − 1 − 1 = 1. `while 1:` with `n+=1` first is 1 byte under
  `c=1;n=2` / `while[print(…)]:n+=1`.

**Notes**

- The same term is C_{m−1}·(11m − 7)/(m+1) = 11·C_{m−1} − 18·C_{m−1}/n,
  but printing that and stepping `c` separately is longer than the walrus.
- Exact integer arithmetic, correct for every n.
- The b-file has 1657 terms (up to a(1657)); the bar is the whole b-file
  in 60 s. It prints them in a fraction of a second.
- a(n) first has more than 4300 digits at n = 7152, so printing stops
  there with a ValueError (about a second).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 46 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000781), CC BY-SA 4.0.
