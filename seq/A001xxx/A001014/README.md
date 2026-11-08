# A001014

> Sixth powers: a(n) = n^6.
> — [OEIS A001014](https://oeis.org/A001014)

Offset 0: 0, 1, 64, 729, 4096, 15625, 46656, 117649, 262144, 531441, …

### Python 3 — 27 bytes

```python
n=0
while[print(n**6)]:n+=1
```

**How it works**

- `n**6` is n⁶, printed for n = 0, 1, 2, …: the
  [A000027](../../A000xxx/A000027/) counter, and
  [A000584](../../A000xxx/A000584/) with 6 in place of 5.
- `print(n**6)` runs in the loop condition. It returns `None`, and `[None]` is
  a non-empty list, so the condition is always true and the body `n+=1` moves
  to the next n.

**Notes**

- `while 1:print(n**6);n+=1` is 28 bytes, and a walrus counter `n=-1` /
  `while[print((n:=n+1)**6)]:0` is 32. Unlike 8ⁿ in [A001018](../A001018/), n⁶
  has no one-operation update of its own value, so the counter stays.
- Exact integers, so every term is right; for n ≥ 1, a(n) has ⌊6·log₁₀ n⌋ + 1
  digits, so the 4300-digit int-to-str limit would only be reached near
  n = 10^717.
- The b-file has 501 terms (n = 0 to 500) and all of them print at once; the
  bar is the whole b-file in 60 s.
- The same loop with another exponent: [A000290](../../A000xxx/A000290/) n²,
  [A000578](../../A000xxx/A000578/) n³, [A000583](../../A000xxx/A000583/) n⁴,
  [A000584](../../A000xxx/A000584/) n⁵, [A001015](../A001015/) n⁷,
  [A001016](../A001016/) n⁸, [A001017](../A001017/) n⁹.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 27 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001014), CC BY-SA 4.0.
