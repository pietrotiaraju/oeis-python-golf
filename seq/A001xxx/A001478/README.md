# A001478

> The negative integers.
> — [OEIS A001478](https://oeis.org/A001478)

Offset 1: −1, −2, −3, −4, −5, …

### Python 3 — 25 bytes

```python
n=-1
while[print(n)]:n-=1
```

**How it works**

- a(n) = −n for n ≥ 1. `print(n)` runs in the loop condition; it returns
  `None`, and `[None]` is a non-empty list, so the condition is always true.
- The body subtracts 1, so the loop prints −1, −2, −3, … forever: the
  [A000027](../../A000xxx/A000027/) loop counting down from −1.

**Notes**

- `n=0` + `while 1:n-=1;print(n)` and `n=0` + `while[print(~n)]:n+=1`
  (~n = −n − 1) are also 25 bytes: the minus sign costs one byte over the
  24-byte counter of [A001489](../A001489/), which starts at 0.
- The b-file has 10 000 terms (n = 1 to 10 000); the bar is the whole b-file
  in 60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 25 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001478), CC BY-SA 4.0.
