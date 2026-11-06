# A000247

> a(n) = 2^n - n - 2.
> — [OEIS A000247](https://oeis.org/A000247)

Offset 2: 0, 3, 10, 25, 56, 119, 246, 501, 1012, 2035, …

### Python 3 — 31 bytes

```python
n=2
while[print(2**n-n-2)]:n+=1
```

**How it works**

- It prints the formula itself for n = 2, 3, 4, …, starting at the OEIS
  offset.
- `print(…)` runs in the loop condition and returns `None`; `[None]` is a
  non-empty list, so the loop never stops (one byte under `while 1:` with
  the `print` moved into the body).
- Python integers are unbounded, so every term is exact.

**Notes**

- The recurrence a(n) = 2a(n−1) + n needs a second variable and a seed
  a(1) = −1: `a=-1;n=2` + `while[print(a:=2*a+n)]:n+=1` is 36 bytes, and
  so is `a=0;n=2` + `while[print(a)]:a-=~a-n;n+=1` (`a-=~a-n` is
  a + a + 1 + n).
- Moving the increment into the header, `n=1` + `while n:=n+1:print(2**n-n-2)`,
  is 32 bytes.
- `2**n+~n` is 2^n − n − 1 ([A000295](https://oeis.org/A000295)), one short
  of the target; shifting the counter to n + 1 or n + 2 turns `2**n` into
  `2**k//2` or `2**k//4` and costs more than it saves.
- The b-file has 299 terms (n = 2 to 300) and the whole of it prints
  instantly; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 31 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000247), CC BY-SA 4.0.
