# A002050

> Number of simplices in barycentric subdivision of n-simplex.
> — [OEIS A002050](https://oeis.org/A002050)

Offset 0: 0, 1, 5, 25, 149, 1081, 9365, 94585, 1091669, 14174521, 204495125, 3245265145, 56183135189, …

### Python 3 — 58 bytes

```python
r=[t:=1]
while[print(t-1)]:r=[t:=t+x for x in[sum(r)-t]+r]
```

**How it works**

- a(n) = A000629(n) − 1 (entry formula; the e.g.f.
  (e^{2x} − eˣ)/(2 − eˣ) is eˣ/(2 − eˣ) − 1). The loop is the
  [A000629](../../A000xxx/A000629/) program, which runs the Fubini array:
  each row is the running sums of s = the sum of the row above, followed
  by the row above, and the last entry `t` of row n is A000629(n).
- The only change is `print(t-1)`.

**Notes**

- Starting from `r=[t:=0]` and putting `sum(r,1)-t` (one more) in front of
  each row prints a(n) directly, also in 58 bytes.
- a(n) also equals Σ_{k=1}^{n} C(n, k)·A000670(k) (Critzer).
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 425 terms (n = 0 to 424); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 58 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002050), CC BY-SA 4.0.
