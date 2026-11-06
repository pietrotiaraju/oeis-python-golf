# A000270

> For n >= 2, a(n) = b(n+1)+b(n)+b(n-1), where the b(i) are the ménage numbers A000179; a(0)=a(1)=1.
> — [OEIS A000270](https://oeis.org/A000270)

Offset 0: 1, 1, 0, 3, 16, 95, 672, 5397, 48704, 487917, 5373920, …

### Python 3 — 58 bytes

```python
p=t=n=r=1;q=0
while[print(t)]:p,q,r=(t:=n*p)-r,p,-t-q;n+=1
```

**How it works**

- a(n) = n·S_n for n ≥ 1, where S_n = [A127548](https://oeis.org/A127548)(n)
  has o.g.f. S(x) = f(t) = Σ m!·t^m with t = x/(1+x)². Proof: Jovovic's
  g.f. in the entry is A(x) = 1 + (1−x)/(1+x)·Σ m·m!·t^m, and
  x·t′/t = (1−x)/(1+x), so the sum times (1−x)/(1+x) is x·d/dx f(t(x)) =
  x·S′(x). Hence A(x) = 1 + x·S′(x): a(n) = n·S_n for n ≥ 1, and a(0) = 1.
  (The formula n·S_n alone gives 0 at n = 0, the value Orrick gets from
  Touchard's 1934 equation; the entry keeps the table's a(0) = 1.)
- With W_n = [A000271](https://oeis.org/A000271)(n), Σ W_n xⁿ = f(t)/(1+x)
  (Gessel), so S_n = W_n + W_{n−1}. Put also D_n = W_n + W_{n−2}, and use
  Somos's extension W_{−1} = −1, W_{−2} = 0, with which
  W_{n+1} = n(W_n + W_{n−1}) + W_{n−2} = n·S_n + W_{n−2} holds at every
  step from n = 0 (proof on the [A000179](../A000179/) page). Adding W_n,
  resp. W_{n−1}, to both sides:

  S_{n+1} = n·S_n + D_n,   D_{n+1} = n·S_n + S_{n−1}.

  So both new values are the same t = n·S_n = a(n) plus an old value.
  (S_0 = 0 here, not A127548(0) = 1, because of W_{−1} = −1; it only feeds
  D_2.)
- The state at the start of pass n ≥ 1 is p = S_n, q = S_{n−1}, r = −D_n,
  and t = a(n−1) from the pass before. The update is
  `p,q,r=(t:=n*p)-r,p,-t-q`: the walrus computes t = a(n) inside the first
  element and the third one reuses it.
- The seeds at n = 1 are S_1 = 1, S_0 = 0, D_1 = W_1 + W_{−1} = −1, and
  t = a(0) = 1. Storing −D makes them p = t = n = r = 1 and q = 0, one
  chain plus `q=0` (3 bytes under `r=-1`, for one more `-` in the update).
- Printing t one pass late is what gives a(0) = 1: any value printed from
  the state itself carries the factor n and is 0 at n = 0, so the first
  print shows the seed t = 1 and pass n prints a(n) on the next turn.

**Notes**

- Each term is a few big-integer operations. The whole b-file
  (176 terms) prints at once; the bar is the whole b-file in 60 s.
- Python's 4300-digit limit for printing ints stops the program after
  a(1557) (4299 digits); a(1558) has 4302. All terms up to a(1558) agree
  with van Hoeij's sum in the entry.
- A search over this template (three state variables, each new value a
  sum of at most two signed terms, the walrus in any element, integer
  seeds, start index −1 to 2) finds nothing under 58 bytes; the 58-byte hits are
  this program with variables renamed or negated.
- Longer routes: the same delayed print with the state W_{n−2}, W_{n−1},
  W_n (sign of W_{n−2} flipped) is 60 bytes,
  `a=b=t=n=1;c=0` / `while[print(t)]:a,b,c=-b,c,(t:=n*(b+c))-a;n+=1`;
  printing n·(W_{n−1} + W_n) directly needs `+0**n` for a(0) and is 63.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 58 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000270), CC BY-SA 4.0.
