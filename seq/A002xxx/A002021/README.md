# A002021

> Pile of coconuts problem: (n-1)*(n^n - 1), n even; n^n - n + 1, n odd.
> — [OEIS A002021](https://oeis.org/A002021)

Offset 1: 1, 3, 25, 765, 3121, 233275, 823537, 117440505, 387420481, …

### Python 3 — 42 bytes

```python
n=1
while[print((n%2or~-n)*n**n-n+1)]:n+=1
```

**How it works**

- The name gives the formula: (n − 1)(nⁿ − 1) for even n and nⁿ − n + 1
  for odd n. Both are c·nⁿ − n + 1, with c = n − 1 for even n and c = 1
  for odd n, and `(n%2or~-n)` is that c: n % 2 = 1 for odd n, otherwise
  `~-n` = n − 1.
- Why this is the least pile: a share takes a pile x to (n − 1)(x − 1)/n,
  so y = x + n − 1 is multiplied by (n − 1)/n. All n shares come out even
  exactly when nⁿ divides y₀ (n − 1 is prime to n), say y₀ = c·nⁿ, and
  then y after the shares is c·(n − 1)ⁿ ≡ c·(−1)ⁿ (mod n). The final pile
  y − (n − 1) is a multiple of n when that is ≡ −1, so the least c ≥ 1 is
  1 for odd n and n − 1 for even n, which is the formula.

**Notes**

- Exact integer arithmetic, so the program is right for every n; Python's
  4300-digit int-to-str limit stops the output near n = 1370.
- The b-file has 100 terms (n = 1 to 100); the bar is the whole b-file in
  60 s, which takes a few milliseconds.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 42 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002021), CC BY-SA 4.0.
