# A001672

> a(n) = floor(Pi^n).
> — [OEIS A001672](https://oeis.org/A001672)

Offset 0: 1, 3, 9, 31, 97, 306, 961, 3020, 9488, 29809, 93648, 294204, 924269, …

### Python 3 — 97 bytes

```python
t=l=1;q=z=2;n=0
while z**n//t**n<(a:=(z+q)**n//t**n)or[print(a),n:=n+1]:l+=2;q*=l//2;z=z*l+q;t*=l
```

**How it works**

- **A shrinking interval around π.** The state is the one of Gibbons'
  spigot in [A000796](../../A000xxx/A000796/), in its halved form
  π = 2u, u = 1 + 1/3·(1 + 2/5·(1 + 3/7·(1 + …))). After k terms
  π = (q·x + z − q)/t, where x is the value of the rest of the series, and
  every such tail lies in [1, 2] (each factor k/(2k+1) is below ½). So π
  lies in the interval [z/t, (z+q)/t], and since π is irrational it lies
  strictly inside. At the start q = z = 2, t = 1: π = 2x, π ∈ [2, 4].
- **Taking in a term.** With l = 2k+1, substituting x = 1 + k·x′/l gives
  q → q·k, t → t·l and z → z·l + q·k: in the code `q*=l//2` comes first,
  so `z=z*l+q` adds the new q. The width q/t is multiplied by
  k/(2k+1) < ½, so it tends to 0.
- **Deciding a term.** Raising the bounds to the n-th power keeps the order,
  so πⁿ lies in [zⁿ/tⁿ, (z+q)ⁿ/tⁿ], and `//` gives the integer parts of
  both. When both ends have the same integer part a, so does πⁿ: then `<` is false, the list prints a = ⌊πⁿ⌋ and
  steps n (a non-empty list is true, so the body still runs). Otherwise
  the body takes in the next term and the same n is tried again.
- **It never stalls.** πⁿ is irrational for n ≥ 1 (π is transcendental), so
  it is not an integer, and once the interval is narrow enough both ends
  fall between the same two integers. For n = 0 both powers are 1 and
  a(0) = 1 is printed at once. Each term of the series gains one bit, a
  new n needs about log₂ π ≈ 1.65 bits more, and the loop gets one chance
  to print per term, so it keeps up.

**Notes**

- Exact integer arithmetic throughout: every printed value is certified by
  the bounds, so the program is right for every n.
- t is the product 1·3·5⋯(2k+1), so the numbers raised to the n-th power
  have about k·log₂(2k) bits and the run slows down as it goes; still, the
  whole b-file (301 terms) comes in about 20 reference seconds. The bar is
  280 of them, in 60 s.
- Computing tⁿ once, `z**n//(T:=t**n)<(a:=(z+q)**n//T)`, is faster and two
  bytes longer.
- Scaling the interval down to 2ˡ before powering, with
  `((z<<l)//t)**n>>l*n` and `((z+q<<l)//t+1)**n>>l*n`, prints the whole
  b-file in a few seconds but costs some 25 bytes.
- The original form of the spigot (`q=t=l=1;y=4`, π in [(y−q)/t, y/t],
  `y=y*l-2*q`) is one byte longer: in the halved form z = y − q updates by
  just adding the new q.
- Python prints numbers of up to 4300 digits, about π^8650, far beyond
  what the program reaches.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 97 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001672), CC BY-SA 4.0.
