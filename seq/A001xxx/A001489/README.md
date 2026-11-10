# A001489

> a(n) = -n.
> — [OEIS A001489](https://oeis.org/A001489)

Offset 0: 0, −1, −2, −3, −4, −5, …

### Python 3 — 24 bytes

```python
n=0
while[print(n)]:n-=1
```

**How it works**

- `print(n)` runs in the loop condition. It returns `None`, and `[None]` is a
  non-empty list, so the condition is always true.
- The body subtracts 1 from `n`, so the loop prints 0, −1, −2, … forever: the
  counter of [A001477](../A001477/) run backwards.

**Notes**

- `n=0` + `while 1:print(n);n-=1` and `n=0` + `while[print(-n)]:n+=1` are
  25 bytes.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file in
  60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 24 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001489), CC BY-SA 4.0.
