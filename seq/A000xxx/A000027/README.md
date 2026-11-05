# A000027

> The positive integers. Also called the natural numbers, the whole numbers or
> the counting numbers, but these terms are ambiguous.
> — [OEIS A000027](https://oeis.org/A000027)

Offset 1: 1, 2, 3, 4, 5, …

### Python 3 — 24 bytes

```python
n=1
while[print(n)]:n+=1
```

**How it works**

- `print(n)` runs in the loop condition. It returns `None`, and `[None]` is a
  non-empty list, so the condition is always true.
- The body adds 1 to `n`, so the loop prints 1, 2, 3, … forever. It is the
  [A000007](../A000007/) loop with `n=0` replaced by `n+=1`.

**Notes**

- `n=1` + `while 1:print(n);n+=1`, `n=0` + `while 1:print(n:=n+1)` and
  `n=0` + `while n:=n+1:print(n)` are all 25 bytes.
- `for n in range(1,9**99):print(n)` (32 bytes) would stop eventually, which
  the rules do not allow for an infinite sequence.
- The b-file has 500 000 terms and the whole of it prints in a few seconds;
  the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 24 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000027), CC BY-SA 4.0.
