# A001105

> a(n) = 2*n^2.
> — [OEIS A001105](https://oeis.org/A001105)

Offset 0: 0, 2, 8, 18, 32, 50, 72, 98, 128, 162, 200, 242, 288, 338, 392, …

### Python 3 — 28 bytes

```python
n=0
while[print(2*n*n)]:n+=1
```

**How it works**

- The [A000290](../../A000xxx/A000290/) squares loop, printing 2·n·n instead
  of n·n.
- `print(…)` runs in the loop condition. It returns `None`, and `[None]` is a
  non-empty list, so the condition is always true and the body `n+=1` moves
  to the next n.

**Notes**

- Other versions that print the same terms: stepping m = 2n and halving its
  square, `m=0` / `while[print(m*m>>1)]:m+=2`: 29 bytes; adding the first
  differences 4n + 2, `a=0;d=2` / `while[print(a)]:a+=d;d+=4`: 33 bytes.
  `n*n*2` and `n*n<<1` tie with or lose to `2*n*n`.
- Exact integer arithmetic, so every term is right; the 4300-digit
  int-to-str limit would only be reached near n = 10^2150.
- The b-file has 1001 terms (n = 0 to 1000) and all of them print at once;
  the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 28 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001105), CC BY-SA 4.0.
