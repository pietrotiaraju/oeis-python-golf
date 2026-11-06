# A000486

> One half of the number of permutations of [n] such that the differences have 4 runs with the same signs.
> — [OEIS A000486](https://oeis.org/A000486)

Offset 5: 16, 150, 926, 4788, 22548, 100530, 433162, 1825296, 7577120, 31130190, …

### Python 3 — 114 bytes

```python
a=[16,150,926,4788,22548,100530]
while[print(a[0])]:a=a[1:]+[sum(x*y for x,y in zip(a,(-48,172,-244,175,-67,13)))]
```

**How it works**

- The sign sequence consists of successive differences of a permutation.
  A sign run is a maximal block of consecutive differences having
  the same sign. Four such runs first fit when n=5.
- The ordinary generating function on the OEIS page is
  2x⁵(24x²−29x+8)/Q(x), where
  Q(x)=(1−x)²(1−2x)²(1−3x)(1−4x).
  Expanding gives
  Q(x)=1−13x+67x²−175x³+244x⁴−172x⁵+48x⁶.
- Beyond the numerator's degree, multiplying by Q gives

  a(n)=13a(n−1)−67a(n−2)+175a(n−3)−244a(n−4)
  +172a(n−5)−48a(n−6).

- The list initially holds a(5) through a(10), obtained by expanding
  that rational function. Its entries are in oldest-to-newest order,
  so `zip` uses the reversed coefficient order
  (−48,172,−244,175,−67,13).
- Print the oldest entry, drop it with `a[1:]`, and append the new
  recurrence value. Each list remains a six-term consecutive window;
  the recurrence applies to every appended term, starting at n=11.

**Notes**

- Exact integer arithmetic. The six seeds are the initial conditions
  of a proved generating-function recurrence, rather than an embedded
  reference file; they determine all later coefficients.
- Reversing a permutation exchanges its initial direction while
  preserving the number of sign runs, explaining the factor one half
  in the definition. At n=5 the full alternating count is 32,
  and this sequence prints 16.
- Six stored terms and six products per update suffice. Exponential
  growth eventually reaches Python 3.11+'s default 4300-digit output
  conversion limit, an interpreter limit.
- The b-file has 996 terms (indices 5 through 1000). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 114 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000486), CC BY-SA 4.0.
