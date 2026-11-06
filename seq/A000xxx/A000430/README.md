# A000430

> Primes and squares of primes.
> — [OEIS A000430](https://oeis.org/A000430)

Offset 1: 2, 3, 4, 5, 7, 9, 11, 13, 17, 19, …

### Python 3 — 74 bytes

```python
s=set();n=p=1
while 1:
 p*=n*n;n+=1
 if p%n:s|={n,n*n}
 if n in s:print(n)
```

**How it works**

- Immediately before the primality test, p=((n−1)!)². Starting
  from n=p=1, `p*=n*n;n+=1` maintains that invariant for the
  next candidate.
- For prime n, Wilson's theorem gives (n−1)!≡−1 mod n, so p%n=1.
  For composite n=ab with 2≤a,b<n, both factors occur in (n−1)!
  if distinct; if equal, squaring supplies both copies. Thus n divides
  ((n−1)!)² for every composite, including the exceptional Wilson
  case n=4.
- Consequently `if p%n` detects primes exactly. On discovery,
  `s|={n,n*n}` marks the prime and its square. Increasing n then
  prints exactly the marked values when their turn arrives.
- A prime square is marked well before it is tested. For example 4
  is inserted on discovering 2; 4 later fails the prime test but still
  passes `n in s`, so it is printed.

**Notes**

- Exact integer primality testing; the residue test works at every
  candidate, rather than only over the b-file range. Neither 1 nor
  products of two different primes are marked.
- Squaring the factorial avoids a separate branch for n=4, at the
  cost of larger integers. The program retains the full factorial
  square because a residue for one modulus cannot be reused for the
  next modulus.
- Factorial-size integers and repeated remainder operations eventually
  dominate the runtime. The set also retains the prime squares that
  have been scheduled for later output.
- The b-file has 1000 terms (indices 1 through 1000). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 74 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000430), CC BY-SA 4.0.
