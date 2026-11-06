# A000204

> Lucas numbers (beginning with 1): L(n) = L(n-1) + L(n-2) with L(1) = 1, L(2) = 3.
> — [OEIS A000204](https://oeis.org/A000204)

Offset 1: 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, …

### Python 3 — 33 bytes

```python
a,b=1,3
while[print(a)]:a,b=b,a+b
```

**How it works**

- `a` and `b` hold two consecutive Lucas numbers, L(n) and L(n+1), starting
  from L(1) = 1 and L(2) = 3.
- `print(a)` runs in the loop condition, as in [A000027](../A000027/): it
  returns `None`, and `[None]` is a non-empty list, so the loop never ends.
- `a,b=b,a+b` moves one step along the recurrence. Integers are exact, so
  every term is right.

**Notes**

- This is [A000032](../A000032/) without its first term L(0) = 2, and the
  same 33 bytes. Starting that program's pair one step later is all it takes;
  printing `b` from `a,b=2,1` is the same length.
- Nothing shorter turned up for the seed: `a=b=1` saves two bytes, but from a
  pair of equal numbers the recurrence gives Fibonacci numbers, and getting
  back to Lucas (`print(b+b-a)`) costs four. The walrus form
  `while 1:print(b:=a+(a:=b))` needs the seed `a,b=-1,2`.
- Python's 4300-digit limit on int-to-str conversion stops the program at
  L(20576), the first Lucas number with 4301 digits, after printing L(1) to
  L(20575). The limit is not counted as a failure.
- The b-file has 4780 terms (n = 1 to 4780, the last one has 999 digits) and
  the whole of it prints instantly; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 33 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000204), CC BY-SA 4.0.
