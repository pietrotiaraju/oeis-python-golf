# A000596

> Central factorial numbers: A008955(n,2).
> — [OEIS A000596](https://oeis.org/A000596)

Offset 3: 4, 49, 273, 1023, 3003, 7462, 16422, 32946, 61446, 108031, …

a(n) = Σ_{0<i<j<n} i²·j², the second elementary symmetric function of the
squares 1², 2², …, (n−1)² (Roudy El Haddad's formula on the entry).

### Python 3 — 47 bytes

```python
n=a=1;b=0
while 1:n+=1;b+=n*n*a;a+=n*n;print(b)
```

**How it works**

- After the step for n, `a` = 1² + 2² + … + n² and `b` = Σ_{i<j≤n} i²·j²,
  which is a(n+1). Adding the square n² to the set adds n² times the sum of
  the earlier squares to the second symmetric function, so the update is
  b += n²·a with the old a, and then a += n².
- `n=a=1;b=0` is the state after n = 1 (a = 1, b = 0); the first pass, n = 2,
  prints b = 4 = a(3).

**Notes**

- Other versions that print the same terms:
  - the print as a walrus in the loop condition,
    `n=2;a=1;b=0` / `while[print(b:=b+n*n*a)]:a+=n*n;n+=1`: 48 bytes (the
    longer start costs the byte that the loop saves);
  - the closed form a(n) = C(2n, 5)·(5n + 1)/24 from the entry,
    `import math` / `n=3` / `while[print(math.comb(2*n,5)*(5*n+1)//24)]:n+=1`:
    63 bytes;
  - the polynomial n(n−1)(n−2)(2n−1)(2n−3)(5n+1)/360: 65 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 9998 terms (up to a(10000)) and all of them print at once;
  the bar is the whole b-file in 60 s.
- a(n) < n⁶, so the 4300-digit int-to-str limit is out of reach.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 47 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000596), CC BY-SA 4.0.
