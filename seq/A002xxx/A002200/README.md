# A002200

> Primes of the form 2^q*3^r*5^s + 1.
> — [OEIS A002200](https://oeis.org/A002200)

Offset 1: 2, 3, 5, 7, 11, 13, 17, 19, 31, 37, 41, 61, …

### Python 3 — 133 bytes

```python
h={1}
while 1:
 h=h-{x:=min(h)}|{2*x,3*x,5*x};n=x+1;a=1
 while any(pow(a,x//q,n)+x%q==1for q in(2,3,5)):a+=1
 pow(a,x,n)-1or print(n)
```

**How it works**

The program walks the 5-smooth numbers x = 2^q·3^r·5^s in increasing
order and proves or disproves that n = x + 1 is prime with Lucas's test,
which is exact here because n − 1 = x comes fully factored.

- **5-smooth numbers in order.** `h` starts as {1}; each pass takes out
  its least element x and puts in 2x, 3x and 5x (a set, so a number
  reached twice is kept once). Every 5-smooth y > 1 is 2, 3 or 5 times a
  smaller 5-smooth number, which is taken out first and puts y in; and
  everything in `h` is larger than the x just taken out. So the x come
  out exactly once each, in increasing order (a(10000) has 52 digits, so
  a scan of all integers would be hopeless).
- **Lucas's test.** If some a has a^x ≡ 1 (mod n) but a^(x/q) ≢ 1 for
  every prime q | x, then a has order exactly x = n − 1 in the units
  mod n, so n − 1 ≤ φ(n) and n is prime. The `while` tries a = 1, 2, …
  as long as some q in {2, 3, 5} with q | x has a^(x/q) ≡ 1; when it
  stops, n is printed if a^x ≡ 1 (`pow(a,x,n)-1or print(n)`). For q ∤ x
  the term `pow(a,x//q,n)+x%q` is at least 2 unless the power is 0, so
  `==1` tests q | x and a^(x/q) ≡ 1 at once.
- **Why it decides every n.**
  - *n prime:* for 1 ≤ a < n no power is 0, so the loop stops exactly at
    the first primitive root a (which exists and is below n), and
    a^x ≡ 1: printed. n = 2 (x = 1, no prime factor) stops at a = 1.
  - *n composite:* when the loop stops, a^(x/q) ≢ 1 for every q | x, so
    a^x ≡ 1 would make n prime: never printed. And it stops: if n is
    not a prime power, at the latest at its least prime factor r, whose
    powers mod n are never 1 (r | n) and never 0 (another prime divides
    n); if n = r^j with j ≥ 2, at the latest at a = 1 + r^(j−1), a unit
    of order r, with a^x ≢ 1 because r ∤ x = r^j − 1 (and since a^x ≢ 1,
    no a^(x/q) is 1 either). Fermat liars, even Carmichael numbers such
    as 1729 = 2^6·3^3 + 1, cannot fool it.

**Notes**

- Exact integers and a proven primality test: right for every n.
- About 223000 smooth numbers lie below a(10000) and `min` scans a set
  of a few thousand each time: 5000 terms come in about 29 s here and
  6000 in 43 s. The b-file has 10000 terms; the bar is 5000 terms in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-23 | Python 3 | 133 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002200), CC BY-SA 4.0.
