# A002066

> a(n) = 10*4^n.
> — [OEIS A002066](https://oeis.org/A002066)

Offset 0: 10, 40, 160, 640, 2560, 10240, 40960, 163840, 655360, 2621440, …

### Python 3 — 25 bytes

```python
n=10
while[print(n)]:n*=4
```

**How it works**

- Start at a(0) = 10 and multiply by 4 at every step: a(n) = 10·4ⁿ.
- `while[print(n)]:` prints the term; the list `[None]` is true, so the
  loop never ends.

**Notes**

- `10<<2*n` with a counter is longer; so is `while 1:print(n);n*=4`.
- Exact integer arithmetic, right for every n; Python's 4300-digit
  int-to-str limit stops the output near n = 7100. The b-file has 501
  terms (n = 0 to 500); the bar is the whole b-file in 60 s, a few
  milliseconds.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 25 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002066), CC BY-SA 4.0.
