# A000032

> Lucas numbers beginning at 2: L(n) = L(n-1) + L(n-2), L(0) = 2, L(1) = 1.
> — [OEIS A000032](https://oeis.org/A000032)

Offset 0: 2, 1, 3, 4, 7, 11, 18, 29, 47, …

### Python 3 — 33 bytes

```python
a,b=2,1
while[print(a)]:a,b=b,a+b
```

**How it works**

- `a` and `b` hold two consecutive Lucas numbers, L(n) and L(n+1), starting
  from L(0) = 2 and L(1) = 1.
- `print(a)` runs in the loop condition, as in [A000027](../A000027/): it
  returns `None`, and `[None]` is a non-empty list, so the loop never ends.
- `a,b=b,a+b` moves one step along the recurrence: the new pair is
  L(n+1), L(n) + L(n+1) = L(n+2). Integers are exact, so every term is right.

**Notes**

- `a,b=2,1` + `while 1:print(a);a,b=b,a+b` is 34 bytes, and `a=2;b=1` is no
  shorter than `a,b=2,1`.
- Starting one step earlier, from L(-1) = -1 and L(0) = 2, needs `a,b=2,-1`
  (with `b,a=a,a+b`, so `a` is still printed first), one byte more.
- `from sympy import*` + `n=0` + `while[print(lucas(n))]:n+=1` is 50 bytes,
  longer than the plain loop, so there is no sympy entry.
- Python's 4300-digit limit on int-to-str conversion stops the program at
  L(20576), the first Lucas number with 4301 digits, after printing L(0) to
  L(20575). The limit is not counted as a failure.
- The b-file has 4776 terms (n = 0 to 4775, the last one has 998 digits) and
  the whole of it prints instantly; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 33 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000032), CC BY-SA 4.0.
