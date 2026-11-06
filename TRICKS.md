# Golf tricks

Each sequence page explains its own program. This page collects the
techniques that come up again and again, so you can learn them in one place
and try them on a new sequence. Each entry has a short example and links to
pages that use it. Those pages have the full explanation and, where the trick
needs one, the proof that it is exact.

Byte counts are those of the records on 2026-11-06. Records only get shorter,
so a linked page may already show a smaller number. Every program here is the
shortest known, not a proven minimum: see
[why "shortest known"](README.md#why-shortest-known).

- [Loop frames](#loop-frames)
- [Arithmetic and bit identities](#arithmetic-and-bit-identities)
- [Recurrences and running products](#recurrences-and-running-products)
- [Primes and divisors without imports](#primes-and-divisors-without-imports)
- [Lists, slices and transforms](#lists-slices-and-transforms)
- [Power series in one big integer](#power-series-in-one-big-integer)
- [Burnside and cycle indices](#burnside-and-cycle-indices)
- [Exact floors and rounding of real numbers](#exact-floors-and-rounding-of-real-numbers)
- [Digits, strings and bytes](#digits-strings-and-bytes)
- [Searching and canonical forms](#searching-and-canonical-forms)
- [Syntax savings](#syntax-savings)
- [Searches behind the records](#searches-behind-the-records)

## Loop frames

### Print in the loop condition

`print` returns `None`, and `[None]` is a non-empty list, so `while[print(…)]:`
is always true. It prints a term before every pass and leaves the body for the
update. It is one byte under `while 1:print(…);`, and most records here use it.

```python
n=1
while[print(n)]:n+=1
```

[A000027](seq/A000xxx/A000027/) (24 bytes). When the body would be empty, the
plain form wins: `while 1:print(1)` is 16 bytes and the list form 17
([A000012](seq/A000xxx/A000012/)).

### Name the working value in the condition

A walrus in the `while` header sets up each pass for free, as long as the value
can never be false: a non-empty range, list or set, or an int that is never 0.
It is one byte under the same assignment at the start of the body
([A000091](seq/A000xxx/A000091/), [A000099](seq/A000xxx/A000099/)).

- `while r:=range(2<<n//2):` gives one range for both x and y
  ([A000018](seq/A000xxx/A000018/) (92 bytes),
  [A000205](seq/A000xxx/A000205/)).
- `while B:=4**m:` sets the base of a packed series
  ([A000200](seq/A000xxx/A000200/) (163 bytes),
  [A000022](seq/A000xxx/A000022/)).
- `while F:={r:=n**49}:` and `while V:=[M:=n**200]:` reset a set or a list and
  a scale at once ([A000158](seq/A000xxx/A000158/) (172 bytes),
  [A000160](seq/A000xxx/A000160/) (188 bytes)).
- `while u:=p:` works because p is ±1 ([A000134](seq/A000xxx/A000134/)), and
  `while f:=…:` because f is proved never to be 0
  ([A000186](seq/A000xxx/A000186/)).

A walrus cannot be the iterable of a comprehension, which is one more reason
to name the range in the header ([A000091](seq/A000xxx/A000091/)).

### Print only on some passes

In `a<b==print(x)` Python calls `print` only when `a<b` holds, so a chained
comparison is a one-line `if`. Inside `while[…]` the list keeps the loop going
either way.

```python
P=k=1
while[-P%k==1==print(k)]:P*=k;k+=1
```

The primes, [A000040](seq/A000xxx/A000040/) (40 bytes). Because `print`
returns `None`, a final `!=print(…)` link is always true: `n+=a==b!=print(a-1)`
prints and steps n exactly when `a==b` ([A000135](seq/A000xxx/A000135/)).
Others: `W%n>0==print(n)` is 1 byte under `W%n and print(n)`
([A000057](seq/A000xxx/A000057/)), `0<d==print(p:=n)` is 2 bytes under
`if d>0:` ([A000092](seq/A000xxx/A000092/)), and
[A000028](seq/A000xxx/A000028/), [A000173](seq/A000xxx/A000173/),
[A000193](seq/A000xxx/A000193/), [A000396](seq/A000xxx/A000396/).

### Start one step early

If the update turns any seed into a(0), start one step before 0 and put the
update inside `print`:

```python
a=n=0
while[print(a:=a*n^1)]:n+=1
```

Derangements, [A000166](seq/A000xxx/A000166/) (33 bytes): at n = 0 the
product is 0 and `0^1` is 1. That is a byte under `a=n=1` /
`while[print(a)]:a=a*n^1;n+=1`. With `n+=3` the same frame is
[A000180](seq/A000xxx/A000180/) (33 bytes), 3 bytes under the form without the
walrus. Also [A000274](seq/A000xxx/A000274/) and the phantom pass of
[A000207](seq/A000xxx/A000207/).

Running a recurrence backwards can also make the seeds equal, so one chained
assignment sets them all: `a=b=-1` is a byte under `a,b=0,1`
([A000283](seq/A000xxx/A000283/) (35 bytes)), and `a=b=c=1` two bytes under
`a=b=0;c=1` ([A000213](seq/A000xxx/A000213/) (39 bytes)). Also
[A000126](seq/A000xxx/A000126/), [A000271](seq/A000xxx/A000271/).

### A list that grows while a for loop reads it

A list iterator checks the length at every step, so `for x in q:` never ends
if the body appends to `q`. The loop variable walks the sequence itself, and
`len(q)` is a free counter.

```python
q=[s:=1]
for x in q:print(s);s+=x;q+=s,s
```

[A000123](seq/A000xxx/A000123/) (40 bytes). Indexing into the list instead is
44 bytes, and `q.pop(0)` is 43 and slower.

- σ(n), [A000203](seq/A000xxx/A000203/) (56 bytes):
  `for n in r:r+=n+1,;print(sum(d*(n%d<1)for d in r))`. The appended n + 1
  never divides n, so the sum can run over all of `r`, 2 bytes under `while`
  with `range(1,n+1)`.
- ⌊nφ⌋, [A000201](seq/A000xxx/A000201/) (42 bytes):
  `for d in l:l+=(1,0)[d:print(len(l))]` grows the Fibonacci word while reading
  it. `len(l)` is the term, and the `None` from `print` works as the end of the
  slice, a byte under a separate `print(len(l));`.
- Also [A000150](seq/A000xxx/A000150/), [A000248](seq/A000xxx/A000248/),
  [A035513](seq/A035xxx/A035513/).

### Several terms per print

- `while 1:print('1\n2')` prints a whole period per pass
  ([A000034](seq/A000xxx/A000034/) (21 bytes)).
- `while[*map(print,l[c:])]:` prints a whole block of terms per pass
  ([A000121](seq/A000xxx/A000121/), [A139569](seq/A139xxx/A139569/)).
- `print('12'[k>0]+'\n0'*k)` prints a term and the k zeros after it
  ([A000122](seq/A000xxx/A000122/) (40 bytes)).

### Repeat a statement with exec

`exec("…;"*k)` runs a statement k times without a loop variable. The
Lucas–Lehmer test in [A000043](seq/A000xxx/A000043/) (65 bytes) is
`s=4;exec('s=s*s%~-(4<<k)-2;'*k)`. Also [A000039](seq/A000xxx/A000039/) and
[A000082](seq/A000xxx/A000082/).

## Arithmetic and bit identities

### `-~x`, `~-x` and `~k*~k`

`~x` is −x−1, so `-~x` is x + 1 and `~-x` is x − 1, with no parentheses:
`n**~-n` is n^(n−1) ([A000169](seq/A000xxx/A000169/) (29 bytes)), and `-~k`
lets `range(n)` stand for 1…n, 2 bytes under `range(1,n+1)`
([A000005](seq/A000xxx/A000005/) (52 bytes)).

`~k*~k` is (k + 1)² in 5 bytes, which gives an integer square root that only
counts up:

```python
n=k=0
while[print(k)]:n+=1;k+=~k*~k<=n
```

⌊√n⌋, [A000196](seq/A000xxx/A000196/) (38 bytes): one byte under `k*k+2*k<n`
and three under `(k+1)**2<=n`. Counting like this replaces `isqrt` and its
import in [A000006](seq/A000xxx/A000006/), [A000037](seq/A000xxx/A000037/)
(round √n with `r+=r*r+r<n`), [A000194](seq/A000xxx/A000194/),
[A000267](seq/A000xxx/A000267/) and [A000277](seq/A000xxx/A000277/). Floats are
not an option: `round(n**.5)` is wrong at n = 1125900007505922
([A000037](seq/A000xxx/A000037/)).

### `^1` adds (−1)ⁿ

When `a*n` always has the parity of n, adding (−1)ⁿ just flips the last bit,
so a·n + (−1)ⁿ is `a*n^1` (`*` binds tighter than `^`). Derangements are
`a=a*n^1` ([A000166](seq/A000xxx/A000166/)); also
[A000167](seq/A000xxx/A000167/), [A000180](seq/A000xxx/A000180/),
[A000240](seq/A000xxx/A000240/), [A000255](seq/A000xxx/A000255/),
[A000274](seq/A000xxx/A000274/). [A000155](seq/A000xxx/A000155/) (50 bytes)
uses the next bit: `b^m&2` flips bit 1 of b when n is even, which adds +2 or
−2 depending on b mod 4, exactly the correction its recurrence needs.

### Booleans and shifts as switches

Comparisons are 0 or 1, so they count and select: `sum(n%-~k<1for k in range(n))`
counts divisors ([A000005](seq/A000xxx/A000005/)), and `d*(n%d<1)` is d when d
divides n ([A000203](seq/A000xxx/A000203/)). A right shift does the same,
since `c>>s` is 0 once s reaches the bit length of c:

- `J[d>>n%d*n]` reads `J[d]` when d divides n and the 0 in `J[0]` otherwise, a
  byte under `J[d]for … if n%d<1` ([A000114](seq/A000xxx/A000114/) (86 bytes)).
- `2>>n%2+n%g` is 2 − n%2 when g divides n and 0 otherwise, 3 bytes under
  `(n%g<1)*(2-n%2)` ([A000208](seq/A000xxx/A000208/) (107 bytes));
  [A000206](seq/A000xxx/A000206/) has `2-n%2>>n%g`.
- `-k|n` is n when k = 0 and −1 when k = 1 ([A000138](seq/A000xxx/A000138/)).

### XOR and OR as addition

When two numbers have no set bits in common, `^` and `|` add them, and they
bind more loosely than `+`, which can save parentheses. In
[A000187](seq/A000xxx/A000187/) (88 bytes), (−4)ⁿ + (−16)ⁿ is
`(p:=p*-4)*p^p` with p = (−4)ⁿ, 5 bytes under `p+p*abs(p)` (the page shows
why it also holds for negative p). [A000231](seq/A000xxx/A000231/) (42 bytes)
adds 2ᴺ and (N − 1)·2^(N/2) as `2**N|N-1<<N//2`.

### Complete the square

A quadratic term is often one square plus a shift. Since (2n + 1)² = 8·T(n) + 1,
the triangular numbers are `m*m>>3` over odd m:

```python
m=1
while[print(m*m>>3)]:m+=2
```

[A000217](seq/A000xxx/A000217/) (29 bytes), 2 bytes under `n*n+n>>1`. Also
`m*m//8-1` ([A000096](seq/A000xxx/A000096/) (31 bytes)). Stepping the whole
numerator saves a multiplication: ⌊(13n − 1)/8⌋ is `n=12` /
`while[print(n//8)]:n+=13` ([A000202](seq/A000xxx/A000202/) (29 bytes)).

### Exact division in two pieces

With n one more than the index, each Catalan number is the one before times
(4n − 6)/n. Written as `4*c-6*c//n` the division is still exact, and it saves
the parentheses: 2 bytes under `c*=4*n-6;c//=n`.

```python
c=n=1
while[print(c)]:n+=1;c=4*c-6*c//n
```

Catalan numbers, [A000108](seq/A000xxx/A000108/) (39 bytes). The same split is
`a=12*a-30*a//m` ([A000168](seq/A000xxx/A000168/) (43 bytes)) and `4*v+6*v//n`
([A000184](seq/A000xxx/A000184/) (48 bytes)); also
[A000131](seq/A000xxx/A000131/), [A000150](seq/A000xxx/A000150/),
[A000207](seq/A000xxx/A000207/). Chained floor divisions `x//p//q` equal
`x//(p*q)`, and a walrus in the divisor can step the counter:
`a*27*m*~-m//-~(m:=m+3)//(4*m-2)` is a byte under ending with `;m+=3`
([A000139](seq/A000xxx/A000139/) (55 bytes)).

### Lowest set bit

`n&-n` is the largest power of 2 that divides n. The odd part of n is
`n//(n&-n)` ([A000265](seq/A000xxx/A000265/) (32 bytes); `//` binds tighter
than `&`, so the parentheses are needed), and gcd(m, 8) is `min(m&-m,8)`
([A276805](seq/A276xxx/A276805/) (41 bytes)).

### Factorials and imports

- `math.perm` with one argument is the factorial, 4 bytes under `factorial`:
  [A000197](seq/A000xxx/A000197/) (54 bytes) prints `perm(perm(n))`.
- When a `math` function is used once, `import math` with `math.gcd` is a byte
  under `from math import*` with `gcd` ([A000029](seq/A000xxx/A000029/),
  [A000088](seq/A000xxx/A000088/)).

## Recurrences and running products

### Tuple windows

`a,b,c=b,c,a+b+c` moves a window of terms in one statement. For a sum of the
last k terms, `a,*l=*l,sum(l)` drops the oldest and appends the sum
([A000078](seq/A000xxx/A000078/) (41 bytes),
[A000102](seq/A000xxx/A000102/) (63 bytes)). For tribonacci
([A000213](seq/A000xxx/A000213/) (39 bytes)) a search over chains of up to four
`x+=y`-style statements of at most 16 bytes found none with the right
characteristic polynomial, so the tuple stays.

### Two plain steps instead of a pair

A change of variable can split a second-order recurrence into two plain
assignments. [A000153](seq/A000xxx/A000153/) (46 bytes) keeps
s = a(n) + a(n+1) and runs `a=s-a;s=n*s+3*a`, 2 bytes under the tuple form (48);
[A000262](seq/A000xxx/A000262/) runs `c=a+n*c;a=c+n*a` (46 bytes against 51),
and [A000261](seq/A000xxx/A000261/) is like A000153.

### Read a value, then overwrite it

Python evaluates left to right, so `b+(b:=…)` uses the old b and stores the new
one in the same expression: `print(a:=b+(b:=a*a))`, a byte under the tuple
swap `a,b=b,a*a+b*b` ([A000283](seq/A000xxx/A000283/) (35 bytes)).
[A000245](seq/A000xxx/A000245/) (45 bytes) prints the difference of two
consecutive terms with `-c+(c:=c*4*m//(m+3))`.

### Shift the variable to absorb a constant

Storing a(n) − 1 turns a(n) = a(n−1)² − a(n−1) + 1 into `b*=b+1`, three bytes
shorter than `a=a*a-a+1` ([A000058](seq/A000xxx/A000058/) (28 bytes)), and
storing 2^(2ⁿ) makes the step `b*=b` ([A000215](seq/A000xxx/A000215/)
(26 bytes)). `a-~b` is a + b + 1, a byte under `a+b+1`
([A000071](seq/A000xxx/A000071/) (32 bytes)).

### Patch the first term

When a(0) breaks the pattern, a short expression fixes it: `1//n` is 1 only
at n = 1 (`print(a+b-1//n)` in [A000179](seq/A000xxx/A000179/)), `(n*4or 1)`
avoids dividing by 0 at n = 0 ([A000011](seq/A000xxx/A000011/)),
`n**max(0,n-2)` gives 1 at n = 0 and 1 ([A000272](seq/A000xxx/A000272/)
(36 bytes)), and `abs(…)` replaces a sign when the count is known to be
non-negative ([A000159](seq/A000xxx/A000159/),
[A000181](seq/A000xxx/A000181/), [A000185](seq/A000xxx/A000185/)).

### Running products in a comprehension

A walrus keeps a running product inside a comprehension.

- `(c:=c*(m-j)//j)` walks a row of binomial coefficients and ends back at 1,
  so it needs no reset ([A000279](seq/A000xxx/A000279/) (74 bytes));
  [A000146](seq/A000xxx/A000146/) and [A000275](seq/A000xxx/A000275/) do the
  same with signs.
- `max(w:=a[k]*a[-k],*[w:=w*r**(k%r>n%r)for r in range(1,n)])` is a product
  without `math.prod`: every factor is at least 1, so the maximum of the
  running products is the last one, and `r**(…)` instead of an `if` keeps the
  list non-empty. That is 3 bytes under `import math` with `math.prod(…)`
  ([A000175](seq/A000xxx/A000175/) (119 bytes)).

## Primes and divisors without imports

### Wilson's theorem

For k ≥ 2, (k − 1)! ≡ −1 (mod k) exactly when k is prime, and the factorial
can be kept up to date as k grows:

```python
P=k=1
while[-P%k==1==print(k)]:P*=k;k+=1
```

[A000040](seq/A000xxx/A000040/) (40 bytes); trial division is 57 bytes, and
Fermat's test fails at 341. With `P*=k*k`, (k − 1)!² mod k is 1 for primes and
0 for every other k, so `P%k` is a 0/1 flag ([A000006](seq/A000xxx/A000006/),
[A000101](seq/A000xxx/A000101/), [A000232](seq/A000xxx/A000232/)), and
`P%k>n%k` is true exactly for the primes that divide n
([A000082](seq/A000xxx/A000082/)).

### Negative moduli

`x%~d` divides by −(d+1), and the result is −1 exactly when d + 1 divides
x + 1. [A000068](seq/A000xxx/A000068/) (60 bytes) tests k⁴ + 1 for primality
with `-1in(k**4%~d for d in range(k*k))`, a byte under the direct
`1in(-k**4%d for d in range(2,k*k))`. Also [A000059](seq/A000xxx/A000059/).

### Coprimality by Euler's theorem

With F = n!, `1%n==pow(k,F,n)` is true exactly when gcd(k, n) = 1, so Euler's
φ needs no gcd ([A000010](seq/A000xxx/A000010/) (67 bytes)). `1%n` is 0 for
n = 1, which handles that case, and writing it first saves the space before
`for`.

### Unitary divisors by lcm

`math.lcm(d,m//d)//m*d` is d when d is a unitary divisor of m and 0
otherwise, with no divisibility test ([A000173](seq/A000xxx/A000173/)
(135 bytes)).

## Lists, slices and transforms

### Euler transform with negative slices

```python
*a,n=1,0
while[print(a[-1])]:n-=1;a+=sum(d*sum(a[d::d])for d in range(n,0))//n,
```

Partitions, [A000041](seq/A000xxx/A000041/) (79 bytes). The counter n runs
through −1, −2, …. For d from −N to −1 the slice `a[d::d]` walks
a(N−|d|), a(N−2|d|), … and stops by itself at index 0, so the double sum is
−Σ σ(k)·a(N−k), and `//n` with the negative n undoes the sign. Counting up
instead is 81 bytes. The same loop with other weights gives rooted trees
([A000081](seq/A000xxx/A000081/) (87 bytes)), weights as shifts `<<(d>-3)`
([A000097](seq/A000xxx/A000097/) (87 bytes)), `d*d` for plane partitions
([A000219](seq/A000xxx/A000219/) (82 bytes)), two series in one list
([A000235](seq/A000xxx/A000235/), [A000242](seq/A000xxx/A000242/)), and the
tree counts [A000055](seq/A000xxx/A000055/), [A000151](seq/A000xxx/A000151/),
[A000220](seq/A000xxx/A000220/), [A000226](seq/A000xxx/A000226/),
[A000243](seq/A000xxx/A000243/).

### Dot products with map

`sum(map(int.__mul__,F,F[::-1]))` is a convolution with no import, and `map`
stops at the shorter list ([A000106](seq/A000xxx/A000106/) (112 bytes),
[A000107](seq/A000xxx/A000107/), [A000137](seq/A000xxx/A000137/),
[A000238](seq/A000xxx/A000238/), [A000243](seq/A000xxx/A000243/)).
`math.sumprod` (Python 3.12) is 13 bytes shorter, but `from math import*` costs
18, so it only pays when the program imports `math` anyway
([A000083](seq/A000xxx/A000083/)).

### Multiply by 1 + xᵏ with zip

`p=[*map(sum,zip(p+[0]*k,[0]*k+p))]` multiplies a list of coefficients by
1 + xᵏ ([A000009](seq/A000xxx/A000009/) (68 bytes)); the same loop with
`[a+b for a,b in zip(…)]` is 73 bytes.

### Triangle rows from a running sum

`[t:=t+x for x in row]` builds the next row of a triangle in which each entry
is the one before it plus a neighbour (Seidel and boustrophedon triangles):

```python
t,*r=1,
while[print(t)]:r=[t:=t+x for x in[0]+r]
```

Bell numbers, [A000110](seq/A000xxx/A000110/) (48 bytes). Reading the row
backwards gives the zigzag numbers, `r=[t:=t+x for x in[-t]+r[::-1]]`
([A000111](seq/A000xxx/A000111/) (56 bytes)), and
[A000182](seq/A000xxx/A000182/) (66 bytes) prints only every other row,
telling them apart by the parity of the term: `r<[t%2]or print(t)`. In [A000187](seq/A000xxx/A000187/) the loop
`for s in 0,…:` makes `s` the first entry of each row, 4 bytes under
`r=[s:=u]+[s:=s+5*x for x in r[::-1]]`; also [A000191](seq/A000xxx/A000191/)
and [A000192](seq/A000xxx/A000192/).

### Start values inside the list

A walrus in a list display sets a counter with the list: `r=[n:=0,1]`
([A000081](seq/A000xxx/A000081/)), `s=[n:=0]` ([A000161](seq/A000xxx/A000161/)),
and `q=[s:=1]`, a byte under `s=1;q=[1]` ([A000123](seq/A000xxx/A000123/)).
Leading zeros make negative lags exist from the start: `L=[0]*6+[n:=1]` stands
for a(−6) … a(−1) = 0 in [A000198](seq/A000xxx/A000198/) (84 bytes). A
sentinel −1 at index 0 adds a correction term for free in
[A000060](seq/A000xxx/A000060/) and [A000220](seq/A000xxx/A000220/).

### Spaced lists

Keep values several places apart with zeros between, and one index covers
several cases. [A000207](seq/A000xxx/A000207/) (94 bytes) stores the Catalan
numbers three apart (`L+=0,0,c`), so `4*L[m]` replaces `n%3%2*4*L[n//3]`
(−7 bytes). [A000220](seq/A000xxx/A000220/) stores its series at the even
positions only, so that `R[e]` reads the same series at x² with no parity
test.

### Newest-first tuples

`a=sum(a[:11:2]),*a` puts the new term in front. While the tuple is short, the
slice simply stops early, which supplies the zero terms for n < 0
([A000044](seq/A000xxx/A000044/) (42 bytes); the list version is 45).

## Power series in one big integer

### Evaluate at q = 2^m and read one digit

A series with small non-negative coefficients, evaluated at q = 2^m, is one
big integer whose m-bit digits are the coefficients. A power of the series is
then a single `**`:

```python
m=5
while[print(sum(1<<j*j*m+m for j in range(-m,m))**5>>m*m&2**m-1)]:m+=1
```

Sums of 5 squares, [A000132](seq/A000xxx/A000132/) (74 bytes). The sum is
2^m·θ(2^m) cut to |j| ≤ m, the fifth power puts a(k) in digit k + 5, and
`>>m*m&2**m-1` reads digit m. Reading digit m − 5 directly with `>>m*(m-5)`
would be 4 bytes longer; the `+m` in the exponent costs 2. The page proves the
digits never carry. Changing the 5 gives other numbers of squares:
[A000141](seq/A000xxx/A000141/), [A000143](seq/A000xxx/A000143/),
[A000144](seq/A000xxx/A000144/), [A000145](seq/A000xxx/A000145/),
[A000152](seq/A000xxx/A000152/), [A000156](seq/A000xxx/A000156/).

### Kronecker substitution in tree recursions

In [A000200](seq/A000xxx/A000200/) (163 bytes) and
[A000022](seq/A000xxx/A000022/) (200 bytes), `V[k]` holds the series T(xᵏ) as
one integer in base B = 4^m, so `V[2*k]` and `V[3*k]` are T(x²) and T(x³)
with no substitution step, and `%B**m` drops the high digits. A digit of a
power gives a binomial coefficient: `(B+k)**n//B**k%B`
([A000248](seq/A000xxx/A000248/) (73 bytes)).

### Series division with pow

`pow(x,-1,M)` inverts a series modulo B^n, so a quotient of series is one call:
`pow(2-Q,-3,M:=8**n**2)` in [A000163](seq/A000xxx/A000163/), `pow(1-b,-1,M)`
in [A000251](seq/A000xxx/A000251/), and a negative power `1-2*n` in
[A000264](seq/A000xxx/A000264/).

### Divide by 1 + qᵏ in place

`for j in range(k,m):r[j]-=r[j-k]` divides a list of coefficients by 1 + qᵏ
when j runs upwards. The mock theta functions use it level by level
([A000199](seq/A000xxx/A000199/) (106 bytes),
[A000025](seq/A000xxx/A000025/) (118 bytes)).

## Burnside and cycle indices

### Necklaces: one sum over rotations

Rotating an n-bead necklace by j leaves gcd(j, n) cycles, so Burnside's lemma
is one sum:

```python
import math
print(n:=1)
while[print(sum(2**math.gcd(j,n)for j in range(n))//n)]:n+=1
```

[A000031](seq/A000xxx/A000031/) (84 bytes). Turning over adds
`2**(n-j%2>>1)` and halves the rotation weight with `2**~-math.gcd(j,n)`
([A000029](seq/A000xxx/A000029/) (98 bytes)). Weights that depend on the
cycles use the walrus inside the sum, as in `1<<(g:=math.gcd(j,n))-n//g%2`
([A000013](seq/A000xxx/A000013/) (96 bytes)): g is assigned before `n//g`
reads it, since the left operand of `-` is evaluated first. Also
[A000011](seq/A000xxx/A000011/), [A000016](seq/A000xxx/A000016/),
[A000046](seq/A000xxx/A000046/), [A000116](seq/A000xxx/A000116/),
[A000117](seq/A000xxx/A000117/), [A000206](seq/A000xxx/A000206/),
[A000208](seq/A000xxx/A000208/).

### Cycle types, divided at every level

To average over a symmetric group, recurse on the cycle through one point and
divide by the number of points left at every level, instead of by r! at the
end:

```python
import math
f=lambda r,*L:r<1or sum(f(r+k,*L,k)<<~k+2*sum(map(math.gcd,L,[k]*n))for k in range(-r,0))//r
n=0
while[print(+f(n))]:n+=1
```

Digraphs, [A000273](seq/A000xxx/A000273/) (133 bytes). Cycle lengths are
stored negated, so `range(-r,0)` and `~k` need no `-~` (gcd ignores the sign),
`[k]*n` pads the second argument of `map`, and `+` turns the `True` of n = 0
into 1. The pages explain why each `//r` is exact. Same frame:
[A000171](seq/A000xxx/A000171/) (146 bytes), [A000250](seq/A000xxx/A000250/)
(137 bytes); [A000088](seq/A000xxx/A000088/) (graphs, 172 bytes) recurses over
partitions instead.

### Brute force over the group

When the group is small, walk all of it. [A000157](seq/A000xxx/A000157/)
(239 bytes) starts the point map as a one-element list with the starred target
`for*m,p in product(…)` and walks each cycle with `while~m[x]:`.
[A000214](seq/A000xxx/A000214/) (197 bytes) reads the group elements off the
digits of one integer instead of `itertools.product` (226 bytes), and walks
cycles with `while~x:m[x],x=-1,m[x];r<<=x<0`.

### Count pairs instead of canonical forms

Counting up to isomorphism, it can be shorter to count (object, symmetry)
pairs and divide by the size of the group than to compute a canonical form:
groups of order n in [A000001](seq/A000xxx/A000001/) (255 bytes) count pairs
(table, automorphism), and [A000019](seq/A000xxx/A000019/) does the same for
permutation groups.

## Exact floors and rounding of real numbers

Records must be right for every n, so floats are out: `math.log` returns
exactly 33.0 at n = ⌊e³³⌋ = 214643579785916, where ⌊ln n⌋ is 32
([A000195](seq/A000xxx/A000195/)). These are the exact methods the pages use.

### Stop when the gap beats the tail

Sum a series over a common denominator as N/F, and stop once the distance up
to the next integer is larger than what the rest of the series can add:

```python
n=0
while 1:
 N=F=d=1
 while-N%F<n**d:N=N*d+n**d;F*=d;d+=1
 print(N//F);n+=1
```

⌊eⁿ⌋, [A000149](seq/A000xxx/A000149/) (76 bytes). `-N%F` is F times the gap
from N/F up to the next integer. The test `N%F+n**d>=F` would be two bytes
longer and need a space after `while`. [A000193](seq/A000xxx/A000193/)
(97 bytes) reuses the loop for round(ln n).

### Truncate where the floor is already right

For K ≥ n, ⌊n·e⌋ equals ⌊n·S_K⌋, where S_K is the sum of 1/k! up to K, by the
argument that proves e irrational. So [A000210](seq/A000xxx/A000210/) (44 bytes)
uses integers only: `n=M=F=1` / `while[print(M//F)]:F*=n;n+=1;M=M*n+1`.

### Correctly rounded decimal

The `decimal` module documents `ln` and `exp` as correctly rounded, and the
methods of a `Context` take an int directly. With a precision that grows
with n:

- `Context(n).ln(n)//1` is ⌊ln n⌋ ([A000195](seq/A000xxx/A000195/) (63 bytes)),
  9 bytes under `Decimal(n).ln(Context(n))`;
- `round(Context(1<<n).exp(n))` is the nearest integer to eⁿ
  ([A000227](seq/A000xxx/A000227/) (71 bytes)).

Correct rounding alone is not a proof: both pages use Hermite's integral to
bound how close e^b can come to an integer or a half-integer, which shows the
precision is enough.

### Continued fractions

[A000209](seq/A000xxx/A000209/) (125 bytes) rounds tan n with the convergents
of Lambert's continued fraction. It tracks 2A + B and 2B, so that `b//d` is
the rounding, and one test, `-b%(d or 1)*(2*c-k*d)<=n**k`, keeps going until
the rounding is certain.

### Integer roots with a proven gap

`while r**3>N:r=(2*r+N//r//r)//3`, started above the root, ends at ⌊∛N⌋
exactly. Scaling by a large M and comparing sums of such floors decides
questions about sums of cube roots. [A000160](seq/A000xxx/A000160/)
(188 bytes) and [A000158](seq/A000xxx/A000158/) fix M in advance, because a
nonzero algebraic integer of bounded degree and size cannot be too close to 0.
[A000135](seq/A000xxx/A000135/) and [A000234](seq/A000xxx/A000234/) instead
double M until a lower and an upper count agree (A000234 starts again on
`except:`).

### π without floats

`s=lambda t,d=3:t and t+s(t*~-d//4//d,d+2)` sums Σ k!²/(2k+1)! = 2π/(3√3)
with floored terms ([A000092](seq/A000xxx/A000092/),
[A000223](seq/A000xxx/A000223/)). [A000036](seq/A000xxx/A000036/) and
[A000099](seq/A000xxx/A000099/) sum Euler's series for π/2 with
`x=x*i//(i-~i)`, and [A000796](seq/A000xxx/A000796/) (85 bytes) prints the
digits of π with a spigot.

## Digits, strings and bytes

### Digit squares mod 96

`b'%d'%n` is the decimal expansion as bytes, and iterating it gives the ASCII
codes c = 48 + d. Since c² ≡ d² (mod 96) and d² ≤ 81, `d*d%96` is the square
of the digit:

```python
n=3
while[print(n)]:n=sum(d*d%96for d in b'%d'%n)
```

[A000218](seq/A000xxx/A000218/) (49 bytes) and
[A000221](seq/A000xxx/A000221/) (49 bytes). The usual
`n=sum(int(d)**2for d in str(n))` is 51 bytes.

### Byte tables

Indexing a bytes literal gives an int, so a short orbit can be stored as a
table of successors. [A000216](seq/A000xxx/A000216/) (44 bytes) is
`n=b'\x91:\4*\20Y\24%'[n%53%9]` with the three control bytes written raw
instead of escaped (49 bytes as shown). A search over index expressions found
nothing shorter than `n%53%9`; for [A000218](seq/A000xxx/A000218/) and
[A000221](seq/A000xxx/A000221/) no table beats the mod-96 sum.

### First digit

`"%.1s"%n` is the first character of `str(n)`, a byte under `str(n)[0]`
([A000030](seq/A000xxx/A000030/) (31 bytes)).

### Regular expressions and Unicode names

Look-and-say is one `re.sub`:
`s=re.sub(r'(.)\1*',lambda m:str(len(m[0]))+m[1],s)`
([A005150](seq/A005xxx/A005150/) (82 bytes); `itertools.groupby` is 94).
Keeping the term a string also avoids the 4300-digit limit on `str` of an int.
[A000052](seq/A000xxx/A000052/) gets English number words from the Unicode
names of number characters (`name` from `unicodedata`).

## Searching and canonical forms

### Bitmask backtracking

N queens with three bitmasks (columns and both diagonals), where `c+1>>n` is 1
exactly on a full board:
`f=lambda c,d,e:c+1>>n or sum(f(c|b,(d|b)*2,(e|b)//2)for i in range(n)if(b:=1<<i)&~(c|d|e))`
([A000170](seq/A000xxx/A000170/) (122 bytes)).

### Sets as state

`f=lambda c:c<{0}or sum(f(c-{j})for j in c if(j+len(c))%n>2)` counts
permutations with forbidden positions. `c<{0}` (a proper subset of {0}) is
true only for the empty set, a byte under `not c`, and `len(c)` is the current
row ([A000183](seq/A000xxx/A000183/) (98 bytes)).

### Partitions with the part count folded in

[A000174](seq/A000xxx/A000174/) (89 bytes) adds m to every part, so one
argument t carries both the sum still to fill (`t%m`) and whether parts are
left (`t%m<t`): `g=lambda t,i=0:t<1or i*i<=t%m<t and g(t-i*i-m,i)+g(t,i+1)`.
[A000177](seq/A000xxx/A000177/) (94 bytes) stops at k = 0 parts with
`range(i,n*k)`, which is empty when k = 0, 4 bytes under `k and`.

### Sums of squares from a growing list

`s=[n:=0]` and `n+=1;s+=n*n,` keep the squares, and a chained `in` only scans
the list once the cheap comparison holds: `sum(k<=n-k in s for k in s)`
([A000161](seq/A000xxx/A000161/) (63 bytes)) and
`sum(j<=k<=n-j-k in s for j in s for k in s)`
([A000164](seq/A000xxx/A000164/) (79 bytes)).

### Values up to 2ⁿ of a quadratic form

Clamp every value above the limit to one cap, and subtract it at the end:
`len({min(x*x+16*y*y,2**n+1)for x in r for y in r})-2`
([A000018](seq/A000xxx/A000018/) (92 bytes)), 4 bytes under filtering with a
walrus. Many forms use the same frame, for example
[A000049](seq/A000xxx/A000049/), [A000075](seq/A000xxx/A000075/),
[A000205](seq/A000xxx/A000205/).

### Polyforms as sets of complex numbers

Cells are Gaussian integers, `len(Q)*z-sum(Q)` puts a shape around its centre
of mass with integer coordinates, and a frozenset of all its images is the
canonical key: polyominoes in [A000105](seq/A000xxx/A000105/) (209 bytes), with
holes in [A000104](seq/A000xxx/A000104/), and polyhexes in
[A000228](seq/A000xxx/A000228/), where `u-v in D` picks out the 12 symmetries.

### Inserting into a pile

[A000136](seq/A000xxx/A000136/) (145 bytes) folds stamps with heights stored
as lists and compared lexicographically, so `x+[-len(q)]` sits just above `x`
and nothing has to be renumbered.

## Syntax savings

- A number followed by a keyword needs no space: `n%-~k<1for`, `(n*4or 1)`,
  `d*d%96for`, `2**n-1in`. CPython 3.12 prints a `SyntaxWarning` to stderr,
  which the rules ignore ([A000005](seq/A000xxx/A000005/),
  [A000011](seq/A000xxx/A000011/), [A000218](seq/A000xxx/A000218/),
  [A000080](seq/A000xxx/A000080/)).
- `a+=x,` appends one value as a one-tuple, with no brackets
  ([A000041](seq/A000xxx/A000041/)).
- `(*…,)` is three bytes under `tuple(…)` ([A000162](seq/A000xxx/A000162/)).
- `+f(n)` prints a recursion's `True` or `False` as 1 or 0
  ([A000273](seq/A000xxx/A000273/), [A384128](seq/A384xxx/A384128/)).

## Searches behind the records

"Shortest known" means nobody has found a shorter program. Some pages back
their record with a search over a family of programs; each search rules out
that family only.

- [A000096](seq/A000xxx/A000096/): every integer expression in m of up to
  7 bytes, with any start value and any step from −19 to 19.
- [A000124](seq/A000xxx/A000124/): the same, up to 8 bytes.
- [A000125](seq/A000xxx/A000125/): expressions in n of up to 9 bytes, and
  13-byte combinations of smaller pieces.
- [A000213](seq/A000xxx/A000213/): chains of up to four in-place updates of
  at most 16 bytes.
- [A000100](seq/A000xxx/A000100/): every update with 8 terms; 240 have the
  right characteristic polynomial, and none prints the sequence.
- [A000216](seq/A000xxx/A000216/), [A000218](seq/A000xxx/A000218/) and
  [A000221](seq/A000xxx/A000221/): index expressions for byte tables, up to
  8.5 million expressions of up to 7 characters for A000221.
- [A000198](seq/A000xxx/A000198/): every set of lag terms c·a(n−k) with
  c ≤ a(k) and k ≤ 9.
- [A000253](seq/A000xxx/A000253/) and [A000270](seq/A000xxx/A000270/): small
  in-place and tuple updates of the state.
- [A000271](seq/A000xxx/A000271/): no recurrence on two terms of state with
  polynomial coefficients of degree ≤ 4, which is why the record keeps three.
