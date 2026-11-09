# A001246

> Squares of Catalan numbers.
> — [OEIS A001246](https://oeis.org/A001246)

Offset 0: 1, 1, 4, 25, 196, 1764, 17424, 184041, 2044900, 23639044, …

### Python 3 — 41 bytes

```python
c=n=1
while[print(c*c)]:n+=1;c=4*c-6*c//n
```

**How it works**

- The Catalan loop of [A000108](../../A000xxx/A000108/), printing `c*c`.
  Consecutive Catalan numbers satisfy C(m) = C(m−1)·2(2m−1)/(m+1); with
  n = m + 1 the step from C(n−2) to C(n−1) is a multiplication by
  (4n − 6)/n.
- `c` holds the Catalan number just squared and printed, and `n` its index
  plus 2 after the increment. The loop starts at c = C(0) = 1 and n = 1.
- c·(4n−6)/n is split as 4c − 6c/n. Both 4c and the new term are
  integers, so 6c/n is an integer too and `6*c//n` is exact.
- `print` returns `None` and `[None]` is a non-empty list, so the loop
  never ends.

**Notes**

- Updating the square directly, a(n) = a(n−1)·(4n − 6)²/n² in the same
  indexing, needs `a=a*(4*n-6)**2//n//n` and is longer than squaring at
  the print.
- Exact integer arithmetic, so the program is right for every n. a(3581)
  is the first term with more than 4300 digits, so Python 3.11+ stops
  there with a `ValueError` from the int-to-str limit, which is not counted
  as a failure.
- The b-file has 101 terms (n = 0 to 100); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 41 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001246), CC BY-SA 4.0.
