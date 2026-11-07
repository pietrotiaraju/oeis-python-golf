# A000924

> Class number of Q(sqrt(-n)), n squarefree.
> — [OEIS A000924](https://oeis.org/A000924)

Offset 1: 1, 1, 1, 2, 2, 1, 2, 1, 2, 4, 2, 4, 1, 4, 2, 3, 6, 6, 4, 3, …

### Python 3 — 161 bytes

```python
n=0
while[d:=(n:=n+1)<<(n%4<3)*2]:all(n%k**2for k in range(2,n))and print(sum(0==r<c+(b<1)-a for a in range(d)for b in range(-a,a)for c,r in[divmod(b*b+d,4*a)]))
```

**How it works**

- For squarefree n the field Q(√−n) has discriminant D = −n when
  n ≡ 3 (mod 4) and D = −4n otherwise; `n<<(n%4<3)*2` is d = |D|. Its class
  number is the number of reduced forms ax² + Bxy + cy² with
  B² − 4ac = D, that is |B| ≤ a ≤ c, with B ≥ 0 when |B| = a or a = c
  (Gauss). D is a fundamental discriminant, so every such form is
  primitive and no gcd test is needed (a common factor g would need
  g² | D with D/g² again a discriminant).
- The loop variable `b` is −B, so `range(-a,a)` gives B from −a+1 to a: B = a
  is kept and B = −a dropped. `divmod(b*b+d,4*a)` gives c and a remainder
  `r`; the form exists when r = 0.
- The rest of the reduction rule, "c > a, or c = a and B ≥ 0", is
  c + [b ≤ 0] > a, and it joins the remainder test in one chain:
  `0==r<c+(b<1)-a`.
- `a` starts at 0, where the empty `range(0,0)` keeps the division by zero
  from ever happening; it runs up to d, far past the real bound
  a ≤ √(d/3), and those extra values never pass the test.
- `all(n%k**2for k in range(2,n))and print(...)` skips the n that are not
  squarefree. The loop condition `[d:=(n:=n+1)<<(n%4<3)*2]` steps n and
  sets d (a one-element list is always true), so the whole body fits on
  the `while` line.

**Notes**

- Exact integer arithmetic; the only theorem used is the
  reduction theory of binary quadratic forms.
- Running a up to d makes term n cost about d² ≤ 16n² steps: about 240
  terms in 60 s. The b-file has 10000 terms; the bar is 180 terms in 60 s.
- Adding `if a*a<d` after `range(d)` (169 bytes) skips the useless a and
  gives about 6400 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 161 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000924), CC BY-SA 4.0.
