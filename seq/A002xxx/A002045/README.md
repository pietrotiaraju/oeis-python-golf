# A002045

> MacMahon's solid partitions of n in which 4 is the smallest summand.
> — [OEIS A002045](https://oeis.org/A002045)

Offset 4: 10, 0, 0, 0, 55, 150, 210, 280, 580, 1275, 2905, 5350, 9985, 17965, 33665, 62895, 117287, …

### Python 3 — 123 bytes

```python
L=[1,1]+[0]*6;n=-8
while 1:
 for K in-3,-4:L+=sum(d*d*~-d*sum(L[2*d::2*d])for d in range(n,K))//n,
 print(L[-2]-L[-1]);n-=2
```

**How it works**

- These are MacMahon's counts, not the true solid partitions
  ([A000293](../../A000xxx/A000293/)): his tables come from his guessed
  generating function Π_{i≥1} (1 − xⁱ)^(−i(i+1)/2)
  ([A000294](../../A000xxx/A000294/)), which first goes wrong at n = 6.
  In that model a part i comes in C(i + 1, 2) kinds, so "smallest summand
  4" means parts ≥ 4 with at least one 4: the g.f. is
  (Π_{i≥4} − Π_{i≥5}) (1 − xⁱ)^(−C(i+1,2)), the entry's formula
  (Rascoe). It reproduces every term: 10 = C(5, 2) kinds of a lone 4,
  then 0, 0, 0 for n = 5, 6, 7.
- The program builds both products, A = Π_{i≥4} and B = Π_{i≥5}, with the
  [A000294](../../A000xxx/A000294/) recurrence
  2m·A(m) = Σ_{i≥4} i²(i + 1)·Σⱼ A(m − ji) (n = −2m, d = −i,
  `d*d*~-d`), and prints A(m) − B(m). `range(n,K)` with K = −3 or −4
  stops at d = −4 or −5.
- One list holds both, interleaved: A(0), B(0), A(1), B(1), …. With two
  entries per m, A(m − i) sits 2i places from the end while A(m) is being
  computed, and so does B(m − i) once A(m) has been appended, so the same
  slice `L[2*d::2*d]` serves both passes of `for K in-3,-4`.
- `L` starts with A and B for m = 0, …, 3 (1, 0, 0, 0 each) and n = −8,
  so the first pass makes m = 4 and prints a(4).

**Notes**

- Writing the second product as A·(1 − x⁴)¹⁰ and printing
  A(m) − Σⱼ (−1)ʲC(10, j)·A(m − 4j) takes more bytes than the second list;
  for [A002043](../A002043/) (three terms) it is the other way round.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 35 terms (n = 4 to 38); the bar is the whole b-file in
  60 s, which takes a fraction of a second. The program prints a thousand
  terms in about 1.5 s, and its terms up to n = 150 agree with a direct
  expansion of the two products.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 123 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002045), CC BY-SA 4.0.
