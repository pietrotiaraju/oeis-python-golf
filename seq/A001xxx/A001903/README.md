# A001903

> Final digit of 7^n.
> — [OEIS A001903](https://oeis.org/A001903)

Offset 0: 1, 7, 9, 3, 1, 7, 9, 3, 1, 7, 9, 3, 1, 7, 9, 3, 1, 7, 9, 3, 1, 7, 9, 3, 1, 7, …

### Python 3 — 27 bytes

```python
n=1
while[print(n%10)]:n*=7
```

**How it works**

- `n` holds the power 7ⁿ itself (`n*=7` after each term) and `n%10` is its
  last digit. The digits repeat 1, 7, 9, 3 because 7⁴ = 2401 ≡ 1 (mod 10),
  but the program does not rely on that: it reads the digit off the exact
  power every time.
- Exact integer arithmetic, so the program is right for every n. Only
  n % 10 is converted to a string, so the 4300-digit int-to-str limit never
  applies; the power gains under one digit per term (7ⁿ has about 0.85·n
  digits), which keeps the run fast long after the b-file.

**Notes**

- Reducing as it goes, `n=n*7%10` with `print(n)`, is 28 bytes; keeping
  the whole power lets the update be `n*=7`, one byte shorter overall.
  The cycle written out, `while 1:print('1\n7\n9\n3')`, is 27 bytes as
  well.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file in
  60 s, which prints instantly.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 27 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001903), CC BY-SA 4.0.
