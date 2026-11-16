# A001879

> a(n) = (2n+2)!/(n!*2^(n+1)).
> — [OEIS A001879](https://oeis.org/A001879)

Offset 0: 1, 6, 45, 420, 4725, 62370, 945945, 16216200, 310134825, 6547290750, 151242416325, 3794809718700, …

### Python 3 — 36 bytes

```python
b=m=1
while[print(m*b)]:b*=m-~m;m+=1
```

**How it works**

- **The formula.** (2n + 2)! = 2^(n+1)·(n + 1)!·(2n + 1)!!, so
  a(n) = (2n + 2)!/(n!·2^(n+1)) = (n + 1)·(2n + 1)!!.
- **The program.** `m` is n + 1 and `b` is (2m − 1)!! = (2n + 1)!!; it
  prints m·b, then multiplies b by `m-~m` = 2m + 1 before raising m.

**Notes**

- Checked against (2n + 2)!/(n!·2^(n+1)) for n < 150, and against the b-file.
- Exact integer arithmetic, so the program is right for every n; it stops at
  the 4300-digit int-to-str limit of Python 3.11+ near n = 1422.
- The b-file has 201 terms (n = 0 to 200); the bar is the whole b-file in
  60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 36 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001879), CC BY-SA 4.0.
