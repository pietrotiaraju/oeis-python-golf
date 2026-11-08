# A001203

> Simple continued fraction expansion of Pi.
> — [OEIS A001203](https://oeis.org/A001203)

Offset 0: 3, 7, 15, 1, 292, 1, 1, 1, 2, 1, 3, 1, 14, 2, 1, 1, 2, 2, 2, 2, 1, 84, …

### Python 3 — 116 bytes

```python
a=4;b=2;c=d=k=1
while a//c-b//d or[print(a//c),c:=a%(a:=c),d:=b%(b:=d)]:exec("a,b,c,d=c,d,2*k*a+b,k*a-~k*b;"*2);k+=1
```

**How it works**

This is the spigot of [A000796](../../A000xxx/A000796/) (Gibbons' unbounded
spigot), with the output changed from decimal digits to partial quotients, in
the spirit of Gosper's continued-fraction arithmetic.

- The series is the same: π = 2 + 1/3·(2 + 2/5·(2 + 3/7·(2 + …))), step k
  being x ↦ 2 + k·x/(2k + 1). Every tail 2 + (k+1)/(2k+3)·(2 + …) is a
  positive series whose ratios are below 1/2, so it lies in [2, 4].
- The tail is written as x = (4z + 2)/(z + 1), so that z ∈ [0, ∞] covers
  x ∈ [2, 4]. In z, step k becomes z ↦ (2k·z + k)/(z + k + 1), the matrix
  [[2k, k], [1, k+1]], which sends [0, ∞] to [k/(k+1), 2k], strictly inside.
- The state is f(z) = (a·z + b)/(c·z + d), chosen so that the partial
  quotients still to be printed are those of f(z), where z is the rest of
  the series. At the start f(z) = (4z + 2)/(z + 1), that is x itself.
- All four entries stay ≥ 0 with c, d > 0, so f is monotone on [0, ∞] and
  f(z) lies between f(∞) = a/c and f(0) = b/d. When `a//c` equals `b//d`,
  that common value n is certainly the next partial quotient. Printing it
  replaces f by 1/(f − n): (a, b, c, d) → (c, d, a − n·c, b − n·d), and
  a − n·c is just `a%c`. In the list, `c:=a%(a:=c)` reads the old a, then
  sets a to c, so it is the tuple swap a, c = c, a % c done with walrus.
- The body takes in one more term: f becomes f∘step k, a column operation
  that maps each row (a, b) to (2k·a + b, k·a + (k+1)·b), with
  `k*a-~k*b` = k·a + (k+1)·b. The `exec` runs the row update twice,
  rotating the rows each time (`a,b,c,d=c,d,…`), so each row is updated once
  and they end in their original order.
- As in A000796, the `while` condition prints when it is safe (the list is
  non-empty, so the condition is always true) and the body always takes in a
  term. A term narrows the interval by a factor of about 2, and a partial
  quotient costs on average π²/(6 ln² 2) ≈ 3.42 bits (Lévy's constant); the
  program uses 3.40 terms per partial quotient over the first 8000, so one
  chance to print per term keeps up easily.

**Notes**

- It is exact: a partial quotient is printed only when both ends of the
  interval agree on it, and since π is irrational its complete quotients are
  never whole numbers, so the interval always ends up inside one integer
  and no partial quotient is held back forever.
- The order "test, then always take a term" is what keeps it from dividing
  by zero. Right after a print, f(0) or f(∞) may be exactly n, and then
  1/(f − n) has a pole at that end (d or c is 0). Testing again at once
  would crash; taking a term first moves both ends strictly inside [0, ∞],
  so c and d are positive again before the next test. This is not
  hypothetical: written with the tail interval [3, 4] instead, the image
  after one term is [3, 10/3] and printing 3 leaves exactly such a pole. With
  the interval [2, 4] used here no exact hit occurs in the first 8000
  partial quotients, but the program does not rely on that.
- Each printed value is small, so the 4300-digit int-to-str limit never
  applies. The integers are never reduced and grow by about log₂(2k) bits
  per term: after 8000 partial quotients (27 169 terms) c has some 375 000
  bits, and the program slows down roughly quadratically. 10 000 partial
  quotients take about 15 s and the whole b-file (20 000) 50–60 s; the
  bar is 10 000 terms in 60 s.
- Writing out both rows instead of the `exec`,
  `a,b,c,d=2*k*a+b,k*a-~k*b,2*k*c+d,k*c-~k*d;k+=1`, is 118 bytes and about
  1.5 times faster. Putting everything in one `exec`,
  `while 1:exec("print(a//c);a,b,c,d=c,d,a%c,b%d;"*(a//c==b//d)+"a,b,c,d=c,d,2*k*a+b,k*a-~k*b;"*2);k+=1`
  (same start), is also 116 bytes.
- With the tail coordinate w = (x − 2)/2 ∈ [0, 1] the step is simpler,
  [[k, k], [0, 2k+1]], but the ends are f(0) = b/d and f(1) =
  (a + b)/(c + d), and the update needs a − n·c: 124 bytes. Evaluating at 0
  and ∞ is what makes both the test and the update `%`-cheap.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 116 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001203), CC BY-SA 4.0.
