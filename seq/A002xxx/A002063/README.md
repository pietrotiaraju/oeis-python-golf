# A002063

> a(n) = 9*4^n.
> — [OEIS A002063](https://oeis.org/A002063)

Offset 0: 9, 36, 144, 576, 2304, 9216, 36864, 147456, 589824, 2359296, 9437184, …

### Python 3 — 24 bytes

```python
n=9
while[print(n)]:n*=4
```

**How it works**

- Start at a(0) = 9 and multiply by 4 at every step: a(n) = 9·4ⁿ.
- `while[print(n)]:` prints the term; the list `[None]` is true, so the
  loop never ends.

**Notes**

- `9<<2*n` with a counter is longer; so is `while 1:print(n);n*=4`.
- Exact integer arithmetic, right for every n; Python's 4300-digit
  int-to-str limit stops the output near n = 7100. The b-file has 501
  terms (n = 0 to 500); the bar is the whole b-file in 60 s, a few
  milliseconds.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 24 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002063), CC BY-SA 4.0.
