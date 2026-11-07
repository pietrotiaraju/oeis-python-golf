# A000597

> Central factorial numbers: A008955(n,3).
> — [OEIS A000597](https://oeis.org/A000597)

Offset 4: 36, 820, 7645, 44473, 191620, 669188, 1999370, 5293970, 12728936, 28285400, …

a(n) = Σ_{0<i<j<k<n} i²·j²·k², the third elementary symmetric function of
the squares 1², 2², …, (n−1)² (Roudy El Haddad's formula on the entry).

### Python 3 — 61 bytes

```python
n=3;a=5;b=4;c=0
while[print(c:=c+n*n*b)]:b+=n*n*a;a+=n*n;n+=1
```

**How it works**

- When the condition runs, `a`, `b` and `c` are the first three elementary
  symmetric functions of 1², …, (n−1)². Adding the square n² adds n² times
  the next lower function to each of them, so the new values are c + n²·b,
  b + n²·a and a + n², each from the old values. The condition does the
  first update and prints it: c is then e₃(1², …, n²) = a(n+1).
- `n=3;a=5;b=4;c=0` are the functions of 1² and 2² (5 = 1 + 4, 4 = 1·4), so
  the first line is 9·4 = 36 = a(4).
- `print` returns `None` and `[None]` is a non-empty list, so the loop never
  ends (the [A000007](../A000007/) loop).

**Notes**

- Other versions that print the same terms:
  - the first version of this page, all three updates in the body and
    `print(c)` at its end, `while 1:`: 62 bytes;
  - the closed form a(n) = C(2n, 7)·(35n² + 21n + 4)/144 from the entry,
    `import math` / `n=4` /
    `while[print(math.comb(2*n,7)*(35*n*n+21*n+4)//144)]:n+=1`: 72 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 997 terms (up to a(1000)) and all of them print at once; the
  bar is the whole b-file in 60 s.
- a(n) < n⁹, so the 4300-digit int-to-str limit is out of reach.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 62 | first entry |
| 2026-11-07 | Python 3 | 61 | first update as a walrus print in the loop condition |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000597), CC BY-SA 4.0.
