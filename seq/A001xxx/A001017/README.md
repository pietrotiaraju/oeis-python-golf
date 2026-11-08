# A001017

> Ninth powers: a(n) = n^9.
> — [OEIS A001017](https://oeis.org/A001017)

Offset 0: 0, 1, 512, 19683, 262144, 1953125, 10077696, 40353607, 134217728, 387420489, …

### Python 3 — 27 bytes

```python
n=0
while[print(n**9)]:n+=1
```

**How it works**

- `n**9` is n⁹, printed for n = 0, 1, 2, …: the
  [A000027](../../A000xxx/A000027/) counter, and [A001016](../A001016/) with 9
  in place of 8.
- `print(n**9)` runs in the loop condition. It returns `None`, and `[None]` is
  a non-empty list, so the condition is always true and the body `n+=1` moves
  to the next n.

**Notes**

- `while 1:print(n**9);n+=1` is 28 bytes, and a walrus counter `n=-1` /
  `while[print((n:=n+1)**9)]:0` is 32. Unlike 8ⁿ in [A001018](../A001018/), n⁹
  has no one-operation update of its own value, so the counter stays.
- Exact integers, so every term is right; for n ≥ 1, a(n) has ⌊9·log₁₀ n⌋ + 1
  digits, so the 4300-digit int-to-str limit would only be reached near
  n = 10^478.
- The b-file has 10001 terms (n = 0 to 10000) and all of them print at once;
  the bar is the whole b-file in 60 s.
- The same loop with another exponent: [A000290](../../A000xxx/A000290/) n²,
  [A000578](../../A000xxx/A000578/) n³, [A000583](../../A000xxx/A000583/) n⁴,
  [A000584](../../A000xxx/A000584/) n⁵, [A001014](../A001014/) n⁶,
  [A001015](../A001015/) n⁷, [A001016](../A001016/) n⁸.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 27 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001017), CC BY-SA 4.0.
