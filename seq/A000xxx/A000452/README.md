# A000452

> The greedy sequence of integers which avoids 3-term geometric progressions.
> — [OEIS A000452](https://oeis.org/A000452)

Offset 1: 1, 2, 3, 5, 6, 7, 8, 10, 11, 13, …

### Python 3 — 156 bytes

```python
def f(n):
 p=2
 while p*p<=n:
  e=0
  while n%p<1:n//=p;e+=1
  while e:
   if e%3==2:return 0
   e//=3
  p+=1
 return 1
n=1
while 1:
 if f(n):print(n)
 n+=1
```

**How it works**

- Rankin's set, identified with the greedy set by Brown and Gordon
  (references on the OEIS page), consists of integers whose prime
  exponents have only digits 0 and 1 in base 3.
- To see why it avoids progressions, a geometric progression would
  make the three exponents of every prime an arithmetic progression.
  Three numbers with only 0/1 ternary digits cannot form a nonconstant
  arithmetic progression: reducing a+c=2b modulo 3 forces their
  last digits to agree, and removing that digit repeats the argument.
- Conversely, for an excluded integer, let δ_p be the sum of the
  powers of 3 at the digit-2 positions of each prime exponent e_p.
  Both e_p−δ_p and e_p−2δ_p have only 0/1 digits. The two
  smaller integers with those exponents are already accepted and,
  together with the excluded integer, form a geometric progression.
- In `f`, trial division extracts e, the exponent of each p.
  `e%3==2` rejects a forbidden digit; `e//=3` shifts to the
  next digit. The function returns 1 only after every extracted
  exponent has passed.
- Once p²>n, the remaining factor is 1 or a prime with exponent 1,
  which is allowed. The n modified inside f is local; the outer
  increasing candidate counter is unchanged.

**Notes**

- Exact integer factorization and digit tests, with no conjectural
  shortcut. For example 4=2² fails, 8=2³ passes (3=10 in base 3),
  and 16=2⁴ passes (4=11 in base 3).
- The value 1 has no prime factors, so the tests are vacuously true
  and it is printed first. Squarefree integers also pass because
  their nonzero exponents are all 1.
- Testing all possible divisors, including composites, costs at most
  O(√n) trial steps per candidate. After smaller factors are removed,
  a composite trial divisor extracts no additional prime factors.
- Only the current candidate and its temporary factorization state
  are stored; the program does not retain earlier accepted integers
  or test every pair for a geometric progression.
- The b-file has 10000 terms (indices 1 through 10000). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 156 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000452), CC BY-SA 4.0.
