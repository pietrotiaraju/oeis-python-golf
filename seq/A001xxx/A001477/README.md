# A001477

> The nonnegative integers.
> — [OEIS A001477](https://oeis.org/A001477)

Offset 0: 0, 1, 2, 3, 4, 5, …

### Python 3 — 24 bytes

```python
n=0
while[print(n)]:n+=1
```

**How it works**

- `print(n)` runs in the loop condition. It returns `None`, and `[None]` is a
  non-empty list, so the condition is always true.
- The body adds 1 to `n`, so the loop prints 0, 1, 2, … forever. It is the
  [A000027](../../A000xxx/A000027/) program started at 0 instead of 1.

**Notes**

- `n=0` + `while 1:print(n);n+=1` is 25 bytes, and `n=-1` +
  `while 1:print(n:=n+1)` 26.
- A `range` with a huge bound would stop eventually, which the rules do not
  allow for an infinite sequence.
- The b-file has 500 001 terms (n = 0 to 500 000) and the whole of it prints
  in a few seconds; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 24 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001477), CC BY-SA 4.0.
