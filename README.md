# OEIS Python Golf

Shortest known Python programs that generate sequences from the
[OEIS](https://oeis.org/). Every record is run and checked against the
sequence's OEIS b-file, locally and in CI.

New to golfing these? The [golf tricks](TRICKS.md) page collects the
techniques that come up again and again across the sequence pages, each with a
short example and links to the sequences that use it.

## Records

Size in bytes. The last column is how many terms every program for that
sequence must reproduce within its time limit. Click a sequence for the code
and how it works. Where the bar forces a fast but long method, the shortest
correct program that only reaches the first few terms in time is a separate
record: see [Short-bar records](#short-bar-records) below the table.

<!-- records:start -->

| Sequence | Name | Python 3 | Terms checked |
|---|---|---|---|
| [A000001](seq/A000xxx/A000001/) | Number of groups of order n. | **221** | 6 |
| [A000002](seq/A000xxx/A000002/) | Kolakoski sequence: a(n) is length of n-th run; a(1) = 1; sequence… | **53** | 10502 |
| [A000003](seq/A000xxx/A000003/) | Number of classes of primitive positive definite binary quadratic… | **141** | 300 |
| [A000004](seq/A000xxx/A000004/) | The zero sequence. | **16** | 1001 |
| [A000005](seq/A000xxx/A000005/) | d(n) (also called tau(n) or sigma\_0(n)), the number of divisors of n. | **52** | 10000 |
| [A000006](seq/A000xxx/A000006/) | Integer part of square root of n-th prime. | **56** | 5000 |
| [A000007](seq/A000xxx/A000007/) | The characteristic function of {0}: a(n) = 0^n. | **23** | 1001 |
| [A000008](seq/A000xxx/A000008/) | Number of ways of making change for n cents using coins of 1, 2, 5,… | **67** | 10001 |
| [A000009](seq/A000xxx/A000009/) | Expansion of Product\_{m >= 1} (1 + x^m); number of partitions of n… | **68** | 500 |
| [A000010](seq/A000xxx/A000010/) | Euler totient function phi(n): count numbers <= n and prime to n. | **67** | 500 |
| [A000011](seq/A000xxx/A000011/) | Number of n-bead necklaces (turning over is allowed) where… | **110** | 3336 |
| [A000012](seq/A000xxx/A000012/) | The simplest sequence of positive numbers: the all 1's sequence. | **16** | 10001 |
| [A000013](seq/A000xxx/A000013/) | Definition (1): Number of n-bead binary necklaces with beads of 2… | **96** | 3335 |
| [A000014](seq/A000xxx/A000014/) | Number of series-reduced trees with n nodes. | **161** | 1001 |
| [A000015](seq/A000xxx/A000015/) | Smallest prime power >= n. | **82** | 10000 |
| [A000016](seq/A000xxx/A000016/) | a(n) is the number of distinct (infinite) output sequences from… | **96** | 3335 |
| [A000018](seq/A000xxx/A000018/) | Number of positive integers <= 2^n of form x^2 + 16\*y^2. | **92** | 24 |
| [A000019](seq/A000xxx/A000019/) | Number of primitive permutation groups of degree n. | **468** | 5 |
| [A000020](seq/A000xxx/A000020/) | Number of primitive polynomials of degree n over GF(2) (version 2). | **83** | 24 |
| [A000021](seq/A000xxx/A000021/) | Number of positive integers <= 2^n of form x^2 + 12 y^2. | **92** | 24 |
| [A000022](seq/A000xxx/A000022/) | Number of centered hydrocarbons with n atoms. | **200** | 40 |
| [A000023](seq/A000xxx/A000023/) | a(n) is the number of permutations on {1,2,...,n} with an even number… | **40** | 251 |
| [A000024](seq/A000xxx/A000024/) | Number of positive integers <= 2^n of form x^2 + 10 y^2. | **92** | 24 |
| [A000025](seq/A000xxx/A000025/) | Coefficients of the 3rd-order mock theta function f(q). | **118** | 400 |
| [A000026](seq/A000xxx/A000026/) | Mosaic numbers or multiplicative projection of n: if n = Product… | **95** | 10000 |
| [A000027](seq/A000xxx/A000027/) | The positive integers. Also called the natural numbers, the whole… | **24** | 500000 |
| [A000028](seq/A000xxx/A000028/) | Let k = p\_1^e\_1 p\_2^e\_2 p\_3^e\_3 ... be the prime factorization of n.… | **88** | 10000 |
| [A000029](seq/A000xxx/A000029/) | Number of necklaces with n beads of 2 colors, allowing turning over… | **98** | 301 |
| [A000030](seq/A000xxx/A000030/) | Initial digit of n. | **31** | 10001 |
| [A000031](seq/A000xxx/A000031/) | Number of n-bead necklaces with 2 colors when turning over is not… | **84** | 3334 |
| [A000032](seq/A000xxx/A000032/) | Lucas numbers beginning at 2: L(n) = L(n-1) + L(n-2), L(0) = 2, L(1)… | **33** | 4776 |
| [A000033](seq/A000xxx/A000033/) | a(n) = A058087(n,n-2). | **67** | 100 |
| [A000034](seq/A000xxx/A000034/) | Period 2: repeat [1, 2]; a(n) = 1 + (n mod 2). | **21** | 10000 |
| [A000035](seq/A000xxx/A000035/) | Period 2: repeat [0, 1]; a(n) = n mod 2; parity of n. | **21** | 1001 |
| [A000036](seq/A000xxx/A000036/) | Let A(n) = #{(i,j): i^2 + j^2 <= n}, V(n) = Pi\*n, P(n) = A(n) - V(n);… | **204** | 50 |
| [A000037](seq/A000xxx/A000037/) | Numbers that are not squares (or, the nonsquares). | **39** | 10000 |
| [A000038](seq/A000xxx/A000038/) | Twice A000007. | **23** | 10001 |
| [A000039](seq/A000xxx/A000039/) | Coefficient of q^(2n) in the series expansion of Ramanujan's mock… | **96** | 200 |
| [A000040](seq/A000xxx/A000040/) | The prime numbers. | **40** | 10000 |
| [A000041](seq/A000xxx/A000041/) | a(n) is the number of partitions of n (the partition numbers). | **79** | 5000 |
| [A000042](seq/A000xxx/A000042/) | Unary representation of natural numbers. | **28** | 1000 |
| [A000043](seq/A000xxx/A000043/) | Mersenne exponents: primes p such that 2^p - 1 is prime. Then 2^p - 1… | **65** | 15 |
| [A000044](seq/A000xxx/A000044/) | Dying rabbits: a(0) = 1; for 1 <= n <= 12, a(n) = Fibonacci(n); for n… | **42** | 1001 |
| [A000045](seq/A000xxx/A000045/) | Fibonacci numbers: F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1. | **31** | 2001 |
| [A000046](seq/A000xxx/A000046/) | Number of primitive n-bead necklaces (turning over is allowed) where… | **132** | 1001 |
| [A000047](seq/A000xxx/A000047/) | Number of integers <= 2^n of form x^2 - 2y^2. | **95** | 25 |
| [A000048](seq/A000xxx/A000048/) | Number of n-bead necklaces with beads of 2 colors and primitive… | **92** | 3321 |
| [A000049](seq/A000xxx/A000049/) | Number of positive integers <= 2^n of the form 3\*x^2 + 4\*y^2. | **93** | 24 |
| [A000050](seq/A000xxx/A000050/) | Number of positive integers <= 2^n of form x^2 + y^2. | **91** | 25 |
| [A000051](seq/A000xxx/A000051/) | a(n) = 2^n + 1. | **26** | 101 |
| [A000052](seq/A000xxx/A000052/) | 1-digit numbers arranged in alphabetical order, then the 2-digit… | **389** | 10000 |
| [A000053](seq/A000xxx/A000053/) | Local stops on New York City 1 Train (Broadway-7 Avenue Local) subway. | **62** | 29 |
| [A000054](seq/A000xxx/A000054/) | Local stops on New York City A line subway. | **58** | 25 |
| [A000055](seq/A000xxx/A000055/) | Number of trees with n unlabeled nodes. | **137** | 1001 |
| [A000056](seq/A000xxx/A000056/) | Order of the group SL(2,Z\_n). | **81** | 1000 |
| [A000057](seq/A000xxx/A000057/) | Primes that divide at least one term in every Fibonacci sequence. | **54** | 100 |
| [A000058](seq/A000xxx/A000058/) | Sylvester's sequence: a(n+1) = a(n)^2 - a(n) + 1, with a(0) = 2. | **28** | 13 |
| [A000059](seq/A000xxx/A000059/) | Numbers k such that (2k)^4 + 1 is prime. | **63** | 120 |
| [A000060](seq/A000xxx/A000060/) | Number of signed trees with n nodes. | **131** | 500 |
| [A000061](seq/A000xxx/A000061/) | Generalized tangent numbers d(n,1). | **158** | 1000 |
| [A000062](seq/A000xxx/A000062/) | A Beatty sequence: a(n) = floor(n/(e-2)). | **53** | 1000 |
| [A000063](seq/A000xxx/A000063/) | Symmetrical dissections of an n-gon. | **91** | 996 |
| [A000064](seq/A000xxx/A000064/) | Partial sums of (unordered) ways of making change for n cents using… | **69** | 1001 |
| [A000065](seq/A000xxx/A000065/) | -1 + number of partitions of n. | **81** | 1001 |
| [A000066](seq/A000xxx/A000066/) | Smallest number of vertices in trivalent graph with girth (shortest… | **225** | 6 |
| [A000067](seq/A000xxx/A000067/) | Number of positive integers <= 2^n of form x^2 + 2 y^2. | **89** | 24 |
| [A000068](seq/A000xxx/A000068/) | Numbers k such that k^4 + 1 is prime. | **60** | 120 |
| [A000069](seq/A000xxx/A000069/) | Odious numbers: numbers with an odd number of 1's in their binary… | **41** | 10001 |
| [A000070](seq/A000xxx/A000070/) | a(n) = Sum\_{k=0..n} p(k) where p(k) = number of partitions of k… | **80** | 1001 |
| [A000071](seq/A000xxx/A000071/) | a(n) = Fibonacci(n) - 1. | **32** | 500 |
| [A000072](seq/A000xxx/A000072/) | Number of positive integers <= 2^n of form x^2 + 4 y^2. | **98** | 25 |
| [A000073](seq/A000xxx/A000073/) | Tribonacci numbers: a(n) = a(n-1) + a(n-2) + a(n-3) for n >= 3 with… | **39** | 3001 |
| [A000074](seq/A000xxx/A000074/) | Number of odd integers <= 2^n of form x^2 + y^2. | **100** | 25 |
| [A000075](seq/A000xxx/A000075/) | Number of positive integers <= 2^n of form 2\*x^2 + 3\*y^2. | **93** | 24 |
| [A000076](seq/A000xxx/A000076/) | Number of integers <= 2^n of form 4 x^2 + 4 x y + 5 y^2. | **97** | 24 |
| [A000077](seq/A000xxx/A000077/) | Number of positive integers <= 2^n of form x^2 + 6 y^2. | **91** | 24 |
| [A000078](seq/A000xxx/A000078/) | Tetranacci numbers: a(n) = a(n-1) + a(n-2) + a(n-3) + a(n-4) for n >=… | **41** | 3506 |
| [A000079](seq/A000xxx/A000079/) | Powers of 2: a(n) = 2^n. | **24** | 1001 |
| [A000080](seq/A000xxx/A000080/) | Number of nonisomorphic minimal triangle graphs. | **339** | 6 |
| [A000081](seq/A000xxx/A000081/) | Number of unlabeled rooted trees with n nodes (or connected functions… | **87** | 1001 |
| [A000082](seq/A000xxx/A000082/) | a(n) = n^2\*Product\_{p\|n} (1 + 1/p). | **75** | 1000 |
| [A000083](seq/A000xxx/A000083/) | Number of mixed Husimi trees with n nodes; or polygonal cacti with… | **260** | 501 |
| [A000084](seq/A000xxx/A000084/) | Number of series-parallel networks with n unlabeled edges. Also… | **91** | 1001 |
| [A000085](seq/A000xxx/A000085/) | Number of self-inverse permutations on n letters, also known as… | **40** | 801 |
| [A000086](seq/A000xxx/A000086/) | Number of solutions to x^2 - x + 1 == 0 (mod n). | **56** | 2000 |
| [A000087](seq/A000xxx/A000087/) | Number of unrooted nonseparable planar maps with n edges and a… | **160** | 200 |
| [A000088](seq/A000xxx/A000088/) | Number of simple graphs on n unlabeled nodes. | **169** | 40 |
| [A000089](seq/A000xxx/A000089/) | Number of solutions to x^2 + 1 == 0 (mod n). | **54** | 10000 |
| [A000090](seq/A000xxx/A000090/) | Expansion of e.g.f. exp((-x^3)/3)/(1-x). | **58** | 101 |
| [A000091](seq/A000xxx/A000091/) | Multiplicative with a(2^e) = 2 for k >= 1; a(3) = 2, a(3^e) = 0 for k… | **88** | 2000 |
| [A000092](seq/A000xxx/A000092/) | Let A(n) = #{(i,j,k): i^2 + j^2 + k^2 <= n}, V(n) = (4/3)\*Pi\*n^(3/2),… | **270** | 30 |
| [A000093](seq/A000xxx/A000093/) | a(n) = floor(n^(3/2)). | **41** | 501 |
| [A000094](seq/A000xxx/A000094/) | Number of trees of diameter 4. | **86** | 500 |
| [A000095](seq/A000xxx/A000095/) | Number of fixed points of Gamma\_0 (n) of type i. | **57** | 10000 |
| [A000096](seq/A000xxx/A000096/) | a(n) = n\*(n+3)/2. | **31** | 10001 |
| [A000097](seq/A000xxx/A000097/) | Number of partitions of n if there are two kinds of 1's and two kinds… | **87** | 5000 |
| [A000098](seq/A000xxx/A000098/) | Number of partitions of n if there are two kinds of 1, two kinds of 2… | **87** | 1001 |
| [A000099](seq/A000xxx/A000099/) | Let A(n) = #{(i,j): i^2 + j^2 <= n}, V(n) = Pi\*n, P(n) = A(n) - V(n);… | **176** | 50 |
| [A000100](seq/A000xxx/A000100/) | a(n) is the number of compositions of n in which the maximal part is… | **57** | 201 |
| [A000101](seq/A000xxx/A000101/) | Record gaps between primes (upper end) (compare A002386, which gives… | **67** | 14 |
| [A000102](seq/A000xxx/A000102/) | a(n) = number of compositions of n in which the maximum part size is… | **63** | 201 |
| [A000103](seq/A000xxx/A000103/) | Number of n-node triangulations of sphere in which every node has… | **425** | 7 |
| [A000104](seq/A000xxx/A000104/) | Number of n-celled free polyominoes without holes. | **285** | 12 |
| [A000105](seq/A000xxx/A000105/) | Number of free polyominoes (or square animals) with n cells. | **217** | 13 |
| [A000106](seq/A000xxx/A000106/) | 2nd power of rooted tree enumerator; number of linear forests of 2… | **111** | 999 |
| [A000107](seq/A000xxx/A000107/) | Number of rooted trees with n nodes and a single labeled node;… | **120** | 1001 |
| [A000108](seq/A000xxx/A000108/) | Catalan numbers: C(n) = binomial(2n,n)/(n+1) = (2n)!/(n!(n+1)!). | **39** | 1001 |
| [A000109](seq/A000xxx/A000109/) | Number of simplicial polyhedra with n vertices; simple planar graphs… | **415** | 8 |
| [A000110](seq/A000xxx/A000110/) | Bell or exponential numbers: number of ways to partition a set of n… | **48** | 501 |
| [A000111](seq/A000xxx/A000111/) | Euler or up/down numbers: e.g.f. sec(x) + tan(x). Also for n >= 2,… | **56** | 486 |
| [A000112](seq/A000xxx/A000112/) | Number of partially ordered sets ("posets") with n unlabeled elements. | **228** | 7 |
| [A000113](seq/A000xxx/A000113/) | Number of transformation groups of order n. | **116** | 10000 |
| [A000114](seq/A000xxx/A000114/) | Number of cusps of principal congruence subgroup Gamma^{hat}(n). | **86** | 9999 |
| [A000115](seq/A000xxx/A000115/) | Denumerants: Expansion of 1/((1-x)\*(1-x^2)\*(1-x^5)). | **34** | 10001 |
| [A000116](seq/A000xxx/A000116/) | Number of even sequences with period 2n (bisection of A000013). | **92** | 1001 |
| [A000117](seq/A000xxx/A000117/) | Number of even sequences with period 2n (bisection of A000011). | **107** | 501 |
| [A000118](seq/A000xxx/A000118/) | Number of ways of writing n as a sum of 4 squares; also theta series… | **67** | 10000 |
| [A000119](seq/A000xxx/A000119/) | Number of representations of n as a sum of distinct Fibonacci numbers. | **75** | 6766 |
| [A000120](seq/A000xxx/A000120/) | Ones-counting sequence: number of 1's in binary expansion of n (or… | **36** | 10001 |
| [A000121](seq/A000xxx/A000121/) | Number of representations of n as a sum of Fibonacci numbers (1 is… | **74** | 6766 |
| [A000122](seq/A000xxx/A000122/) | Expansion of Jacobi theta function theta\_3(x) = Sum\_{m =-oo..oo}… | **40** | 10001 |
| [A000123](seq/A000xxx/A000123/) | Number of binary partitions: number of partitions of 2n into powers… | **40** | 65537 |
| [A000124](seq/A000xxx/A000124/) | Central polygonal numbers (the Lazy Caterer's sequence): n(n+1)/2 +… | **31** | 1001 |
| [A000125](seq/A000xxx/A000125/) | Cake numbers: maximal number of pieces resulting from n planar cuts… | **37** | 1001 |
| [A000126](seq/A000xxx/A000126/) | A nonlinear binomial sum. | **40** | 201 |
| [A000127](seq/A000xxx/A000127/) | Maximal number of regions obtained by joining n points around a… | **41** | 1000 |
| [A000128](seq/A000xxx/A000128/) | A nonlinear binomial sum. | **47** | 201 |
| [A000129](seq/A000xxx/A000129/) | Pell numbers: a(0) = 0, a(1) = 1; for n > 1, a(n) = 2\*a(n-1) + a(n-2). | **35** | 1001 |
| [A000130](seq/A000xxx/A000130/) | One-half the number of permutations of length n with exactly 1 rising… | **88** | 201 |
| [A000131](seq/A000xxx/A000131/) | Number of asymmetrical dissections of n-gon. | **117** | 994 |
| [A000132](seq/A000xxx/A000132/) | Number of ways of writing n as a sum of 5 squares. | **74** | 100 |
| [A000133](seq/A000xxx/A000133/) | Number of Boolean functions of n variables. | **41** | 11 |
| [A000134](seq/A000xxx/A000134/) | Positive zeros of Bessel function of order 0 rounded to nearest… | **92** | 200 |
| [A000135](seq/A000xxx/A000135/) | Number of partitions into non-integral powers. | **211** | 38 |
| [A000136](seq/A000xxx/A000136/) | Number of ways of folding a strip of n labeled stamps. | **141** | 10 |
| [A000137](seq/A000xxx/A000137/) | Series-parallel numbers. | **132** | 1000 |
| [A000138](seq/A000xxx/A000138/) | Expansion of e.g.f. exp(-x^4/4)/(1-x). | **54** | 101 |
| [A000139](seq/A000xxx/A000139/) | a(n) = 2\*(3\*n)! / ((2\*n+1)!\*(n+1)!). | **55** | 201 |
| [A000140](seq/A000xxx/A000140/) | Kendall-Mann numbers: the most common number of inversions in a… | **78** | 400 |
| [A000141](seq/A000xxx/A000141/) | Number of ways of writing n as a sum of 6 squares. | **74** | 100 |
| [A000142](seq/A000xxx/A000142/) | Factorial numbers: n! = 1\*2\*3\*4\*...\*n (order of symmetric group S\_n,… | **31** | 101 |
| [A000143](seq/A000xxx/A000143/) | Number of ways of writing n as a sum of 8 squares. | **74** | 80 |
| [A000144](seq/A000xxx/A000144/) | Number of ways of writing n as a sum of 10 squares. | **76** | 75 |
| [A000145](seq/A000xxx/A000145/) | Number of ways of writing n as a sum of 12 squares. | **76** | 70 |
| [A000146](seq/A000xxx/A000146/) | From von Staudt-Clausen representation of Bernoulli numbers: a(n) =… | **101** | 150 |
| [A000147](seq/A000xxx/A000147/) | Number of trees of diameter 5. | **129** | 1000 |
| [A000148](seq/A000xxx/A000148/) | Number of partitions into non-integral powers. | **102** | 40 |
| [A000149](seq/A000xxx/A000149/) | a(n) = floor(e^n). | **76** | 301 |
| [A000150](seq/A000xxx/A000150/) | Number of dissections of an n-gon, rooted at an exterior edge,… | **61** | 201 |
| [A000151](seq/A000xxx/A000151/) | Number of oriented rooted trees with n nodes. Also rooted trees with… | **88** | 1300 |
| [A000152](seq/A000xxx/A000152/) | Number of ways of writing n as a sum of 16 squares. | **76** | 60 |
| [A000153](seq/A000xxx/A000153/) | a(n) = n\*a(n-1) + (n-2)\*a(n-2), with a(0) = 0, a(1) = 1. | **46** | 251 |
| [A000155](seq/A000xxx/A000155/) | Nearest integer to modified Bessel function K\_n(1). | **50** | 201 |
| [A000156](seq/A000xxx/A000156/) | Number of ways of writing n as a sum of 24 squares. | **76** | 45 |
| [A000157](seq/A000xxx/A000157/) | Number of Boolean functions of n variables. | **226** | 6 |
| [A000158](seq/A000xxx/A000158/) | Number of partitions into non-integral powers. | **172** | 35 |
| [A000159](seq/A000xxx/A000159/) | a(n) = A058087(n,n-3). | **77** | 248 |
| [A000160](seq/A000xxx/A000160/) | Number of partitions into non-integral powers. | **188** | 38 |
| [A000161](seq/A000xxx/A000161/) | Number of partitions of n into 2 squares. | **63** | 8000 |
| [A000162](seq/A000xxx/A000162/) | Number of 3-dimensional polyominoes (or polycubes) with n cells. | **273** | 7 |
| [A000163](seq/A000xxx/A000163/) | Series-parallel numbers. | **160** | 160 |
| [A000164](seq/A000xxx/A000164/) | Number of partitions of n into 3 squares (allowing part zero). | **79** | 800 |
| [A000165](seq/A000xxx/A000165/) | Double factorial of even numbers: (2n)!! = 2^n\*n!. | **33** | 404 |
| [A000166](seq/A000xxx/A000166/) | Subfactorial or rencontres numbers, or derangements: number of… | **33** | 451 |
| [A000167](seq/A000xxx/A000167/) | Nearest integer to modified Bessel function K\_n(2). | **69** | 201 |
| [A000168](seq/A000xxx/A000168/) | a(n) = 2\*3^n\*(2\*n)!/(n!\*(n+2)!). | **43** | 926 |
| [A000169](seq/A000xxx/A000169/) | Number of labeled rooted trees with n nodes: n^(n-1). | **29** | 100 |
| [A000170](seq/A000xxx/A000170/) | Number of ways of placing n nonattacking queens on an n X n board. | **122** | 13 |
| [A000171](seq/A000xxx/A000171/) | Number of self-complementary graphs with n nodes. | **146** | 65 |
| [A000172](seq/A000xxx/A000172/) | The Franel number a(n) = Sum\_{k = 0..n} binomial(n,k)^3. | **68** | 1001 |
| [A000173](seq/A000xxx/A000173/) | Unitary-sociable numbers (smallest member of each cycle). | **135** | 3 |
| [A000174](seq/A000xxx/A000174/) | Number of partitions of n into 5 squares. | **89** | 1000 |
| [A000175](seq/A000xxx/A000175/) | Related to zeros of Bessel function. | **119** | 100 |
| [A000176](seq/A000xxx/A000176/) | Generalized tangent numbers d\_(n,2). | **126** | 4500 |
| [A000177](seq/A000xxx/A000177/) | Number of partitions of n into 6 squares. | **94** | 200 |
| [A000178](seq/A000xxx/A000178/) | Superfactorials: product of first n factorials. | **38** | 47 |
| [A000179](seq/A000xxx/A000179/) | Ménage numbers: a(0) = 1, a(1) = -1, and for n >= 2, a(n) = number of… | **60** | 451 |
| [A000180](seq/A000xxx/A000180/) | Expansion of E.g.f. exp(-x)/(1-3x). | **33** | 101 |
| [A000181](seq/A000xxx/A000181/) | a(n) = A058087(n,n-4). | **89** | 247 |
| [A000182](seq/A000xxx/A000182/) | Tangent (or "Zag") numbers: e.g.f. tan(x), also (up to signs) e.g.f.… | **66** | 243 |
| [A000183](seq/A000xxx/A000183/) | Number of discordant permutations of length n. | **98** | 11 |
| [A000184](seq/A000xxx/A000184/) | Number of genus 0 rooted maps with 3 faces with n vertices. | **48** | 499 |
| [A000185](seq/A000xxx/A000185/) | a(n) = A058087(n,n-5). | **90** | 246 |
| [A000186](seq/A000xxx/A000186/) | Number of 3 X n Latin rectangles in which the first row is in order. | **77** | 208 |
| [A000187](seq/A000xxx/A000187/) | Generalized Euler numbers, c(5,n). | **87** | 251 |
| [A000188](seq/A000xxx/A000188/) | (1) Number of solutions to x^2 == 0 (mod n). (2) Also square root of… | **52** | 10000 |
| [A000189](seq/A000xxx/A000189/) | Number of solutions to x^3 == 0 (mod n). | **53** | 10000 |
| [A000190](seq/A000xxx/A000190/) | Number of solutions to x^4 == 0 (mod n). | **53** | 10000 |
| [A000191](seq/A000xxx/A000191/) | Generalized tangent numbers d(3, n). | **79** | 251 |
| [A000192](seq/A000xxx/A000192/) | Generalized Euler numbers c(6,n). | **88** | 251 |
| [A000193](seq/A000xxx/A000193/) | Nearest integer to log n. | **97** | 10000 |
| [A000194](seq/A000xxx/A000194/) | n appears 2n times, for n >= 1; also nearest integer to square root… | **37** | 1001 |
| [A000195](seq/A000xxx/A000195/) | a(n) = floor(log(n)). | **63** | 1200 |
| [A000196](seq/A000xxx/A000196/) | Integer part of square root of n. Or, number of positive squares <=… | **38** | 10001 |
| [A000197](seq/A000xxx/A000197/) | a(n) = (n!)!. | **54** | 6 |
| [A000198](seq/A000xxx/A000198/) | Largest order of automorphism group of a tournament with n nodes. | **84** | 1000 |
| [A000199](seq/A000xxx/A000199/) | Coefficient of q^(2n-1) in the series expansion of Ramanujan's mock… | **106** | 500 |
| [A000200](seq/A000xxx/A000200/) | Number of bicentered hydrocarbons with n atoms. | **163** | 50 |
| [A000201](seq/A000xxx/A000201/) | Lower Wythoff sequence (a Beatty sequence): a(n) = floor(n\*phi),… | **42** | 10000 |
| [A000202](seq/A000xxx/A000202/) | a(8i+j) = 13i + a(j), where 1<=j<=8. | **29** | 10000 |
| [A000203](seq/A000xxx/A000203/) | a(n) = sigma(n), the sum of the divisors of n. Also called sigma\_1(n). | **56** | 15000 |
| [A000204](seq/A000xxx/A000204/) | Lucas numbers (beginning with 1): L(n) = L(n-1) + L(n-2) with L(1) =… | **33** | 4780 |
| [A000205](seq/A000xxx/A000205/) | Number of positive integers <= 2^n of form x^2 + 3 y^2. | **91** | 24 |
| [A000206](seq/A000xxx/A000206/) | Even sequences with period 2n. | **122** | 1001 |
| [A000207](seq/A000xxx/A000207/) | Number of inequivalent ways of dissecting a regular (n+2)-gon into n… | **94** | 200 |
| [A000208](seq/A000xxx/A000208/) | Number of even sequences with period 2n. | **107** | 1001 |
| [A000209](seq/A000xxx/A000209/) | Nearest integer to tan n. | **125** | 900 |
| [A000210](seq/A000xxx/A000210/) | A Beatty sequence: floor(n\*(e-1)). | **44** | 1000 |
| [A000211](seq/A000xxx/A000211/) | a(n) = a(n-1) + a(n-2) - 2, a(0) = 4, a(1) = 3. | **35** | 501 |
| [A000212](seq/A000xxx/A000212/) | a(n) = floor(n^2/3). | **29** | 5001 |
| [A000213](seq/A000xxx/A000213/) | Tribonacci numbers: a(n) = a(n-1) + a(n-2) + a(n-3) with… | **39** | 3773 |
| [A000214](seq/A000xxx/A000214/) | Number of equivalence classes of Boolean functions of n variables… | **197** | 4 |
| [A000215](seq/A000xxx/A000215/) | Fermat numbers: a(n) = 2^(2^n) + 1. | **26** | 12 |
| [A000216](seq/A000xxx/A000216/) | Take sum of squares of digits of previous term, starting with 2. | **44** | 100 |
| [A000217](seq/A000xxx/A000217/) | Triangular numbers: a(n) = binomial(n+1,2) = n\*(n+1)/2 = 0 + 1 + 2 +… | **29** | 30001 |
| [A000218](seq/A000xxx/A000218/) | Take sum of squares of digits of previous term; start with 3. | **49** | 100 |
| [A000219](seq/A000xxx/A000219/) | Number of plane partitions (or planar partitions) of n. | **82** | 6501 |
| [A000220](seq/A000xxx/A000220/) | Number of asymmetric trees with n nodes (also called identity trees). | **143** | 1000 |
| [A000221](seq/A000xxx/A000221/) | Take sum of squares of digits of previous term; start with 5. | **49** | 100 |
| [A000222](seq/A000xxx/A000222/) | a(n) = A058057(n,n-2). | **66** | 151 |
| [A000223](seq/A000xxx/A000223/) | Let A(n) = #{(i,j,k): i^2 + j^2 + k^2 <= n}, V(n) = (4/3)Pi\*n^(3/2),… | **293** | 20 |
| [A000224](seq/A000xxx/A000224/) | Number of squares mod n. | **53** | 10000 |
| [A000225](seq/A000xxx/A000225/) | a(n) = 2^n - 1. (Sometimes called Mersenne numbers, although that… | **25** | 1001 |
| [A000226](seq/A000xxx/A000226/) | Number of n-node unlabeled connected graphs with one cycle of length… | **167** | 500 |
| [A000227](seq/A000xxx/A000227/) | Nearest integer to e^n. | **71** | 15 |
| [A000228](seq/A000xxx/A000228/) | Number of hexagonal polyominoes (or hexagonal polyforms, or planar… | **229** | 10 |
| [A000229](seq/A000xxx/A000229/) | a(n) is the least number m such that the n-th prime is the least… | **133** | 15 |
| [A000230](seq/A000xxx/A000230/) | a(0)=2; for n>=1, a(n) = smallest prime p such that there is a gap of… | **71** | 24 |
| [A000231](seq/A000xxx/A000231/) | Number of inequivalent Boolean functions of n variables under action… | **42** | 12 |
| [A000232](seq/A000xxx/A000232/) | Construct a triangle as in A036262. Sequence is one less than the… | **110** | 50 |
| [A000233](seq/A000xxx/A000233/) | Generalized class numbers c\_(n,1). | **115** | 6500 |
| [A000234](seq/A000xxx/A000234/) | Partitions into non-integral powers (see Comments for precise… | **157** | 26 |
| [A000235](seq/A000xxx/A000235/) | Number of n-node rooted trees of height 3. | **113** | 200 |
| [A000236](seq/A000xxx/A000236/) | Maximum m such that there are no two adjacent elements belonging to… | **216** | 4 |
| [A000237](seq/A000xxx/A000237/) | Number of mixed Husimi trees with n nodes; or rooted polygonal cacti… | **165** | 501 |
| [A000238](seq/A000xxx/A000238/) | Number of oriented trees with n nodes. | **119** | 1000 |
| [A000239](seq/A000xxx/A000239/) | One-half of number of permutations of [n] with exactly one run of… | **100** | 40 |
| [A000240](seq/A000xxx/A000240/) | Rencontres numbers: number of permutations of [n] with exactly one… | **36** | 100 |
| [A000241](seq/A000xxx/A000241/) | Crossing number of complete graph with n nodes. | **39** | 15 |
| [A000242](seq/A000xxx/A000242/) | 3rd power of rooted tree enumerator; number of linear forests of 3… | **107** | 198 |
| [A000243](seq/A000xxx/A000243/) | Number of trees with n nodes, 2 of which are labeled. | **124** | 199 |
| [A000244](seq/A000xxx/A000244/) | Powers of 3: a(n) = 3^n. | **24** | 201 |
| [A000245](seq/A000xxx/A000245/) | a(n) = 3\*(2\*n)!/((n+2)!\*(n-1)!). | **45** | 101 |
| [A000246](seq/A000xxx/A000246/) | Number of permutations in the symmetric group S\_n that have odd order. | **35** | 451 |
| [A000247](seq/A000xxx/A000247/) | a(n) = 2^n - n - 2. | **31** | 299 |
| [A000248](seq/A000xxx/A000248/) | Expansion of e.g.f. exp(x\*exp(x)). | **73** | 125 |
| [A000249](seq/A000xxx/A000249/) | Nearest integer to modified Bessel function K\_n(5). | **239** | 300 |
| [A000250](seq/A000xxx/A000250/) | Number of symmetric reflexive relations on n nodes: (1/2)\*A000666. | **137** | 18 |
| [A000251](seq/A000xxx/A000251/) | Number of trees of diameter 6. | **127** | 70 |
| [A000252](seq/A000xxx/A000252/) | Number of invertible 2 X 2 matrices mod n. | **95** | 1000 |
| [A000253](seq/A000xxx/A000253/) | a(n) = 2\*a(n-1) - a(n-2) + a(n-3) + 2^(n-1). | **49** | 1001 |
| [A000254](seq/A000xxx/A000254/) | Unsigned Stirling numbers of first kind, s(n+1,2): a(n+1) =… | **43** | 450 |
| [A000255](seq/A000xxx/A000255/) | a(n) = n\*a(n-1) + (n-1)\*a(n-2), a(0) = 1, a(1) = 1. | **39** | 101 |
| [A000256](seq/A000xxx/A000256/) | Number of simple triangulations of the plane with n nodes. | **92** | 198 |
| [A000257](seq/A000xxx/A000257/) | Number of rooted bicubic maps: a(n) = (8\*n-4)\*a(n-1)/(n+2) for n >=… | **41** | 201 |
| [A000258](seq/A000xxx/A000258/) | Expansion of e.g.f. exp(exp(exp(x)-1)-1). | **84** | 476 |
| [A000259](seq/A000xxx/A000259/) | Number of certain rooted planar maps. | **67** | 350 |
| [A000260](seq/A000xxx/A000260/) | Number of rooted simplicial 3-polytopes with n+3 nodes; or rooted… | **62** | 201 |
| [A000261](seq/A000xxx/A000261/) | a(n) = n\*a(n-1) + (n-3)\*a(n-2), with a(1) = 0, a(2) = 1. | **46** | 102 |
| [A000262](seq/A000xxx/A000262/) | Number of "sets of lists": number of partitions of {1,...,n} into any… | **46** | 445 |
| [A000263](seq/A000xxx/A000263/) | Number of partitions into non-integral powers. | **60** | 36 |
| [A000264](seq/A000xxx/A000264/) | Number of 3-edge-connected rooted cubic maps with 2n nodes and a… | **132** | 120 |
| [A000265](seq/A000xxx/A000265/) | Remove all factors of 2 from n; or largest odd divisor of n; or odd… | **32** | 100000 |
| [A000266](seq/A000xxx/A000266/) | Expansion of e.g.f. exp(-x^2/2) / (1-x). | **48** | 451 |
| [A000267](seq/A000xxx/A000267/) | Integer part of square root of 4n+1. | **37** | 10001 |
| [A000268](seq/A000xxx/A000268/) | E.g.f.: -log(1+log(1+log(1-x))). | **85** | 400 |
| [A000269](seq/A000xxx/A000269/) | Number of trees with n nodes, 3 of which are labeled. | **147** | 198 |
| [A000270](seq/A000xxx/A000270/) | For n >= 2, a(n) = b(n+1)+b(n)+b(n-1), where the b(i) are the ménage… | **58** | 176 |
| [A000271](seq/A000xxx/A000271/) | Sums of ménage numbers. | **53** | 451 |
| [A000272](seq/A000xxx/A000272/) | Number of trees on n labeled nodes: n^(n-2) with a(0)=1. | **36** | 389 |
| [A000273](seq/A000xxx/A000273/) | Number of unlabeled simple digraphs with n nodes. | **133** | 20 |
| [A000274](seq/A000xxx/A000274/) | Number of permutations of length n with 2 consecutive ascending pairs. | **40** | 150 |
| [A000275](seq/A000xxx/A000275/) | Coefficients of a Bessel function (reciprocal of J\_0(z)); also pairs… | **94** | 262 |
| [A000276](seq/A000xxx/A000276/) | Associated Stirling numbers. | **47** | 447 |
| [A000277](seq/A000xxx/A000277/) | 3\*n - 2\*floor(sqrt(4\*n+5)) + 5. | **46** | 1001 |
| [A000278](seq/A000xxx/A000278/) | a(n) = a(n-1) + a(n-2)^2 for n >= 2 with a(0) = 0 and a(1) = 1. | **35** | 26 |
| [A000279](seq/A000xxx/A000279/) | Card matching: coefficients B[n,1] of t in the reduced hit polynomial… | **74** | 300 |
| [A000280](seq/A000xxx/A000280/) | a(n) = a(n-1) + a(n-2)^3. | **36** | 18 |
| [A000281](seq/A000xxx/A000281/) | Expansion of cos(x)/cos(2x). | **75** | 216 |
| [A000282](seq/A000xxx/A000282/) | Finite automata. | **271** | 16 |
| [A000283](seq/A000xxx/A000283/) | a(n) = a(n-1)^2 + a(n-2)^2 for n >= 2 with a(0) = 0 and a(1) = 1. | **35** | 15 |
| [A000284](seq/A000xxx/A000284/) | a(n) = a(n-1)^3 + a(n-2) with a(0)=0, a(1)=1. | **36** | 11 |
| [A000285](seq/A000xxx/A000285/) | a(0) = 1, a(1) = 4, and a(n) = a(n-1) + a(n-2) for n >= 2. | **33** | 501 |
| [A000286](seq/A000xxx/A000286/) | Number of positive integers <= 2^n of form 2 x^2 + 5 y^2. | **80** | 12 |
| [A000287](seq/A000xxx/A000287/) | Number of rooted polyhedral graphs with n edges. | **77** | 995 |
| [A000288](seq/A000xxx/A000288/) | Tetranacci numbers: a(n) = a(n-1) + a(n-2) + a(n-3) + a(n-4) with… | **39** | 3504 |
| [A000289](seq/A000xxx/A000289/) | A nonlinear recurrence: a(n) = a(n-1)^2 - 3\*a(n-1) + 3 (for n>1). | **32** | 13 |
| [A000290](seq/A000xxx/A000290/) | The squares: a(n) = n^2. | **26** | 10001 |
| [A000291](seq/A000xxx/A000291/) | Number of bipartite partitions of n white objects and 2 black ones. | **99** | 5000 |
| [A000292](seq/A000xxx/A000292/) | Tetrahedral (or triangular pyramidal) numbers: a(n) = C(n+2,3) =… | **34** | 10001 |
| [A000293](seq/A000xxx/A000293/) | a(n) = number of solid (i.e., three-dimensional) partitions of n. | **135** | 16 |
| [A000294](seq/A000xxx/A000294/) | Expansion of g.f. Product\_{k >= 1} (1 - x^k)^(-k\*(k+1)/2). | **85** | 1001 |
| [A000295](seq/A000xxx/A000295/) | Eulerian numbers (Euler's triangle: column k=2 of A008292, column k=1… | **30** | 501 |
| [A000296](seq/A000xxx/A000296/) | Set partitions without singletons: number of partitions of an n-set… | **56** | 576 |
| [A000297](seq/A000xxx/A000297/) | a(n) = (n+1)\*(n+3)\*(n+8)/6. | **39** | 1002 |
| [A000298](seq/A000xxx/A000298/) | Number of partitions into non-integral powers. | **177** | 22 |
| [A000299](seq/A000xxx/A000299/) | Number of n-node rooted trees of height 4. | **121** | 1000 |
| [A000300](seq/A000xxx/A000300/) | 4th power of rooted tree enumerator: linear forests of 4 rooted trees. | **107** | 497 |
| [A000301](seq/A000xxx/A000301/) | a(n) = a(n-1)\*a(n-2) with a(0) = 1, a(1) = 2; also a(n) =… | **32** | 19 |
| [A000302](seq/A000xxx/A000302/) | Powers of 4: a(n) = 4^n. | **24** | 101 |
| [A000303](seq/A000xxx/A000303/) | Number of permutations of [n] in which the longest increasing run has… | **81** | 464 |
| [A000304](seq/A000xxx/A000304/) | a(n) = a(n-1)\*a(n-2). | **33** | 17 |
| [A000305](seq/A000xxx/A000305/) | Number of certain rooted planar maps. | **91** | 200 |
| [A000306](seq/A000xxx/A000306/) | Number of trees of diameter 8. | **178** | 2500 |
| [A000307](seq/A000xxx/A000307/) | Number of 4-level labeled rooted trees with n leaves. | **85** | 441 |
| [A000308](seq/A000xxx/A000308/) | a(n) = a(n-1)\*a(n-2)\*a(n-3) with a(1)=1, a(2)=2 and a(3)=3. | **43** | 15 |
| [A000309](seq/A000xxx/A000309/) | Number of rooted planar bridgeless cubic maps with 2n nodes. | **55** | 101 |
| [A000310](seq/A000xxx/A000310/) | Coefficients of iterated exponentials. | **85** | 100 |
| [A000311](seq/A000xxx/A000311/) | Schroeder's fourth problem; also series-reduced rooted trees with n… | **81** | 376 |
| [A000312](seq/A000xxx/A000312/) | a(n) = n^n; number of labeled mappings from n points to themselves… | **27** | 386 |
| [A000313](seq/A000xxx/A000313/) | Number of permutations of length n with 3 consecutive ascending pairs. | **43** | 450 |
| [A000314](seq/A000xxx/A000314/) | Number of mixed Husimi trees with n nodes; or labeled polygonal cacti… | **107** | 101 |
| [A000315](seq/A000xxx/A000315/) | Number of reduced Latin squares of order n; also number of labeled… | **140** | 6 |
| [A000316](seq/A000xxx/A000316/) | Two decks each have n kinds of cards, 2 of each kind. The first deck… | **56** | 101 |
| [A000317](seq/A000xxx/A000317/) | a(n+1) = a(n)^2 - a(n)\*a(n-1) + a(n-1)^2. | **41** | 14 |
| [A000318](seq/A000xxx/A000318/) | Generalized tangent numbers d(4,n). | **73** | 100 |
| [A000319](seq/A000xxx/A000319/) | a(n) = floor(b(n)), where b(n) = tan(b(n-1)), b(0)=1. | **254** | 10001 |
| [A000320](seq/A000xxx/A000320/) | Generalized tangent numbers d(5,n). | **89** | 189 |
| [A000321](seq/A000xxx/A000321/) | H\_n(-1/2), where H\_n(x) is Hermite polynomial of degree n. | **43** | 733 |
| [A000322](seq/A000xxx/A000322/) | Pentanacci numbers: a(n) = a(n-1) + a(n-2) + a(n-3) + a(n-4) + a(n-5)… | **39** | 3403 |
| [A000323](seq/A000xxx/A000323/) | Let A(n) = #{(i,j): i^2 + j^2 <= n}, V(n) = Pi\*n, P(n) = A(n) - V(n);… | **177** | 45 |
| [A000324](seq/A000xxx/A000324/) | A nonlinear recurrence: a(0) = 1, a(1) = 5, a(n) = a(n-1)^2 -… | **32** | 13 |
| [A000325](seq/A000xxx/A000325/) | a(n) = 2^n - n. | **29** | 201 |
| [A000326](seq/A000xxx/A000326/) | Pentagonal numbers: a(n) = n\*(3\*n-1)/2. | **30** | 10001 |
| [A000327](seq/A000xxx/A000327/) | Number of partitions into non-integral powers. | **101** | 40 |
| [A000328](seq/A000xxx/A000328/) | Number of points of norm <= n^2 in square lattice. | **77** | 400 |
| [A000329](seq/A000xxx/A000329/) | Nearest integer to b(n), where b(n) = tan(b(n-1)), b(0) = 1. | **267** | 10001 |
| [A000330](seq/A000xxx/A000330/) | Square pyramidal numbers: a(n) = 0^2 + 1^2 + 2^2 + ... + n^2 =… | **33** | 10001 |
| [A000331](seq/A000xxx/A000331/) | Related to zeros of Bessel function. | **151** | 192 |
| [A000332](seq/A000xxx/A000332/) | Binomial coefficient binomial(n,4) = n\*(n-1)\*(n-2)\*(n-3)/24. | **38** | 1003 |
| [A000333](seq/A000xxx/A000333/) | Number of partitions into non-integral powers. | **154** | 15 |
| [A000334](seq/A000xxx/A000334/) | Number of 4-dimensional partitions of n. | **137** | 11 |
| [A000335](seq/A000xxx/A000335/) | Euler transform of A000292. | **96** | 500 |
| [A000336](seq/A000xxx/A000336/) | a(n) = a(n-1)\*a(n-2)\*a(n-3)\*a(n-4); for n < 5, a(n) = n. | **53** | 15 |
| [A000337](seq/A000xxx/A000337/) | a(n) = (n-1)\*2^n + 1. | **33** | 1001 |
| [A000338](seq/A000xxx/A000338/) | Expansion of x^3\*(5-2\*x)\*(1-x^3)/(1-x)^4. | **38** | 998 |
| [A000339](seq/A000xxx/A000339/) | Number of partitions into non-integral powers. | **62** | 560 |
| [A000340](seq/A000xxx/A000340/) | a(0)=1, a(n) = 3\*a(n-1) + n + 1. | **34** | 1001 |
| [A000341](seq/A000xxx/A000341/) | Number of ways to pair up {1..2n} so sum of each pair is prime. | **144** | 11 |
| [A000342](seq/A000xxx/A000342/) | Number of n-node rooted trees of height 5. | **116** | 200 |
| [A000343](seq/A000xxx/A000343/) | 5th power of rooted tree enumerator; number of linear forests of 5… | **107** | 746 |
| [A000344](seq/A000xxx/A000344/) | a(n) = 5\*binomial(2n, n-2)/(n+3). | **52** | 299 |
| [A000345](seq/A000xxx/A000345/) | Number of partitions into non-integral powers. | **141** | 15 |
| [A000346](seq/A000xxx/A000346/) | a(n) = 2^(2\*n+1) - binomial(2\*n+1, n+1). | **49** | 501 |
| [A000347](seq/A000xxx/A000347/) | Number of partitions into non-integral powers. | **166** | 17 |
| [A000348](seq/A000xxx/A000348/) | Number of ways to pair up {1^2, 2^2, ..., (2n)^2 } so sum of each… | **157** | 12 |
| [A000349](seq/A000xxx/A000349/) | One-half the number of permutations of length n with exactly 2 rising… | **129** | 201 |
| [A000350](seq/A000xxx/A000350/) | Numbers m such that Fibonacci(m) ends with m. | **62** | 370 |
| [A000351](seq/A000xxx/A000351/) | Powers of 5: a(n) = 5^n. | **24** | 101 |
| [A000352](seq/A000xxx/A000352/) | One half of the number of permutations of [n] such that the… | **42** | 397 |
| [A000353](seq/A000xxx/A000353/) | Primes p == 7, 19, 23 (mod 40) such that (p-1)/2 is also prime. | **74** | 230 |
| [A000354](seq/A000xxx/A000354/) | Expansion of e.g.f. exp(-x)/(1-2\*x). | **36** | 101 |
| [A000355](seq/A000xxx/A000355/) | Primes p == 3, 9, 11 (mod 20) such that 2p+1 is also prime. | **77** | 230 |
| [A000356](seq/A000xxx/A000356/) | Number of rooted cubic maps with 2n nodes and a distinguished… | **53** | 800 |
| [A000357](seq/A000xxx/A000357/) | Number of 5-level labeled rooted trees with n leaves. | **85** | 401 |
| [A000358](seq/A000xxx/A000358/) | Number of binary necklaces of length n with no subsequence 00,… | **99** | 1000 |
| [A000359](seq/A000xxx/A000359/) | Coefficients of iterated exponentials. | **85** | 100 |
| [A000360](seq/A000xxx/A000360/) | Distribution of nonempty triangles inside a fractal rep-4-tile. | **47** | 10001 |
| [A000361](seq/A000xxx/A000361/) | Binary encodings of the successive columns of the Gosper-Lafitte… | **81** | 10000 |
| [A000362](seq/A000xxx/A000362/) | Generalized class numbers c\_(n,2). | **129** | 4700 |
| [A000363](seq/A000xxx/A000363/) | Number of permutations of [n] with exactly 2 increasing runs of… | **49** | 997 |
| [A000364](seq/A000xxx/A000364/) | Euler (or secant or "Zig") numbers: e.g.f. (even powers only) sec(x)… | **65** | 243 |
| [A000365](seq/A000xxx/A000365/) | Number of genus 0 rooted planar maps with 4 faces and n vertices. | **78** | 198 |
| [A000366](seq/A000xxx/A000366/) | Genocchi numbers of second kind (A005439) divided by 2^(n-1). | **81** | 100 |
| [A000367](seq/A000xxx/A000367/) | Numerators of Bernoulli numbers B\_2n. | **138** | 250 |
| [A000368](seq/A000xxx/A000368/) | Number of connected graphs with one cycle of length 4. | **169** | 1997 |
| [A000369](seq/A000xxx/A000369/) | Triangle of numbers related to triangle A049213; generalization of… | **76** | 1275 |
| [A000370](seq/A000xxx/A000370/) | Number of NPN-equivalence classes of Boolean functions of n or fewer… | **226** | 7 |
| [A000371](seq/A000xxx/A000371/) | a(n) = Sum\_{k=0..n} (-1)^(n-k)\*binomial(n,k)\*2^(2^k). | **59** | 9 |
| [A000372](seq/A000xxx/A000372/) | Dedekind numbers or Dedekind's problem: number of monotone Boolean… | **72** | 7 |
| [A000373](seq/A000xxx/A000373/) | Conjectured dimension of a module associated with the free… | **182** | 200 |
| [A000374](seq/A000xxx/A000374/) | Number of cycles (mod n) under doubling map. | **75** | 480 |
| [A000375](seq/A000xxx/A000375/) | Topswops (1): start by shuffling n cards labeled 1..n. If top card is… | **125** | 10 |
| [A000376](seq/A000xxx/A000376/) | Topswops (2): start by shuffling n cards labeled 1..n. If the top… | **101** | 12 |
| [A000377](seq/A000xxx/A000377/) | Expansion of f(-q^3) \* f(-q^8) \* chi(-q^12) / chi(-q) in powers of q… | **73** | 10001 |
| [A000378](seq/A000xxx/A000378/) | Sums of three squares: numbers of the form x^2 + y^2 + z^2. | **52** | 10000 |
| [A000379](seq/A000xxx/A000379/) | Numbers where total number of 1-bits in the exponents of their prime… | **88** | 8000 |
| [A000380](seq/A000xxx/A000380/) | Number of permutations of an n-sequence discordant with three given… | **116** | 6 |
| [A000382](seq/A000xxx/A000382/) | Restricted permutations. | **49** | 997 |
| [A000383](seq/A000xxx/A000383/) | Hexanacci numbers with a(0) = ... = a(5) = 1. | **39** | 3359 |
| [A000384](seq/A000xxx/A000384/) | Hexagonal numbers: a(n) = n\*(2\*n-1). | **29** | 10001 |
| [A000385](seq/A000xxx/A000385/) | Convolution of A000203 with itself. | **75** | 10000 |
| [A000386](seq/A000xxx/A000386/) | a(n) = A058057(n,n-3). | **107** | 451 |
| [A000387](seq/A000xxx/A000387/) | Rencontres numbers: number of permutations of [n] with exactly two… | **41** | 201 |
| [A000388](seq/A000xxx/A000388/) | Number of permutations of an n-sequence discordant with three given… | **116** | 5 |
| [A000389](seq/A000xxx/A000389/) | Binomial coefficients C(n,5). | **44** | 1001 |
| [A000390](seq/A000xxx/A000390/) | Number of 5-dimensional partitions of n. | **137** | 10 |
| [A000391](seq/A000xxx/A000391/) | Euler transform of A000332. | **103** | 500 |
| [A000392](seq/A000xxx/A000392/) | Stirling numbers of second kind S(n,3). | **38** | 201 |
| [A000393](seq/A000xxx/A000393/) | Number of n-node rooted trees of height 6. | **124** | 200 |
| [A000394](seq/A000xxx/A000394/) | Numbers of form x^2 + y^2 + 7z^2. | **75** | 60 |
| [A000395](seq/A000xxx/A000395/) | 6th power of rooted tree enumerator; number of linear forests of 6… | **107** | 995 |
| [A000396](seq/A000xxx/A000396/) | Perfect numbers k: k is equal to the sum of the proper divisors of k. | **62** | 4 |
| [A000397](seq/A000xxx/A000397/) | Number of partitions into non-integral powers. | **137** | 13 |
| [A000398](seq/A000xxx/A000398/) | Numbers of form x^2 + 2y^2 + 2yz + 4z^2. | **79** | 450 |
| [A000399](seq/A000xxx/A000399/) | Unsigned Stirling numbers of first kind s(n,3). | **54** | 410 |
| [A000400](seq/A000xxx/A000400/) | Powers of 6: a(n) = 6^n. | **24** | 101 |
| [A000401](seq/A000xxx/A000401/) | Numbers of form x^2 + y^2 + 2\*z^2. | **48** | 1000 |
| [A000402](seq/A000xxx/A000402/) | Number of permutations of [n] in which the longest increasing run has… | **126** | 452 |
| [A000404](seq/A000xxx/A000404/) | Numbers that are the sum of 2 nonzero squares. | **73** | 10000 |
| [A000405](seq/A000xxx/A000405/) | Number of 6-level labeled rooted trees with n leaves. | **85** | 151 |
| [A000406](seq/A000xxx/A000406/) | Coefficients of iterated exponentials. | **85** | 100 |
| [A000407](seq/A000xxx/A000407/) | a(n) = (2\*n+1)! / n!. | **33** | 101 |
| [A000408](seq/A000xxx/A000408/) | Numbers that are the sum of three nonzero squares. | **88** | 10000 |
| [A000409](seq/A000xxx/A000409/) | Singular n X n (0,1)-matrices: the number of n X n (0,1)-matrices… | **129** | 14 |
| [A000410](seq/A000xxx/A000410/) | Number of singular n X n rational (0,1)-matrices. | **214** | 5 |
| [A000411](seq/A000xxx/A000411/) | Generalized tangent numbers d(6,n). | **90** | 184 |
| [A000412](seq/A000xxx/A000412/) | Number of bipartite partitions of n white objects and 3 black ones. | **149** | 10001 |
| [A000413](seq/A000xxx/A000413/) | Let A(n) = #{(i,j,k): i^2 + j^2 + k^2 <= n}, V(n) = (4/3)\*Pi\*n^(3/2),… | **298** | 31 |
| [A000414](seq/A000xxx/A000414/) | Numbers that are the sum of 4 nonzero squares. | **71** | 10000 |
| [A000415](seq/A000xxx/A000415/) | Numbers that are the sum of 2 but no fewer nonzero squares. | **82** | 10000 |
| [A000416](seq/A000xxx/A000416/) | Number of 6-dimensional partitions of n. | **143** | 7 |
| [A000417](seq/A000xxx/A000417/) | Euler transform of A000389. | **108** | 1000 |
| [A000418](seq/A000xxx/A000418/) | Number of n-node rooted trees of height 7. | **116** | 200 |
| [A000419](seq/A000xxx/A000419/) | Numbers that are the sum of 3 but no fewer nonzero squares. | **110** | 10000 |
| [A000420](seq/A000xxx/A000420/) | Powers of 7: a(n) = 7^n. | **24** | 101 |
| [A000421](seq/A000xxx/A000421/) | Number of isomorphism classes of connected 3-regular (trivalent,… | **247** | 3 |
| [A000422](seq/A000xxx/A000422/) | Concatenation of numbers from n down to 1. | **38** | 150 |
| [A000423](seq/A000xxx/A000423/) | a(n) is smallest number > a(n-1) of form a(i)\*a(j), i < j < n. | **44** | 49 |
| [A000424](seq/A000xxx/A000424/) | Differences of reciprocals of unity. | **56** | 16 |
| [A000425](seq/A000xxx/A000425/) | Coefficients of ménage hit polynomials. | **57** | 22 |
| [A000426](seq/A000xxx/A000426/) | Coefficients of ménage hit polynomials. | **63** | 100 |
| [A000427](seq/A000xxx/A000427/) | Number of 7-dimensional partitions of n. | **147** | 7 |
| [A000428](seq/A000xxx/A000428/) | Euler transform of A000579. | **108** | 1000 |
| [A000429](seq/A000xxx/A000429/) | Number of n-node rooted trees of height 8. | **116** | 200 |
| [A000430](seq/A000xxx/A000430/) | Primes and squares of primes. | **60** | 1000 |
| [A000431](seq/A000xxx/A000431/) | Expansion of 2\*x^3/((1-2\*x)^2\*(1-4\*x)). | **37** | 201 |
| [A000432](seq/A000xxx/A000432/) | Series-parallel numbers. | **165** | 38 |
| [A000433](seq/A000xxx/A000433/) | n written in base where place values are positive cubes. | **69** | 10001 |
| [A000434](seq/A000xxx/A000434/) | Number of permutations of [n] in which the longest increasing run has… | **126** | 450 |
| [A000435](seq/A000xxx/A000435/) | Normalized total height of all nodes in all rooted trees with n… | **72** | 1000 |
| [A000436](seq/A000xxx/A000436/) | Generalized Euler numbers c(3,n). | **75** | 101 |
| [A000437](seq/A000xxx/A000437/) | Smallest nonnegative number that is the sum of 3 squares in exactly n… | **135** | 43 |
| [A000438](seq/A000xxx/A000438/) | Number of 1-factorizations of complete graph K\_{2n}. | **169** | 4 |
| [A000439](seq/A000xxx/A000439/) | Powers of rooted tree enumerator. | **45** | 43 |
| [A000440](seq/A000xxx/A000440/) | Number of permutations of an n-sequence discordant with three given… | **150** | 19 |
| [A000441](seq/A000xxx/A000441/) | a(n) = Sum\_{k=1..n-1} k\*sigma(k)\*sigma(n-k). | **77** | 1000 |
| [A000442](seq/A000xxx/A000442/) | a(n) = (n!)^3. | **34** | 101 |
| [A000443](seq/A000xxx/A000443/) | Numbers that are the sum of 2 squares in exactly 3 ways. | **99** | 10000 |
| [A000444](seq/A000xxx/A000444/) | Number of partially labeled rooted trees with n nodes (3 of which are… | **169** | 100 |
| [A000445](seq/A000xxx/A000445/) | Latest possible occurrence of the first consecutive pair of n-th… | **311** | 2 |
| [A000446](seq/A000xxx/A000446/) | Smallest number that is the sum of 2 squares (allowing zeros) in… | **193** | 1458 |
| [A000447](seq/A000xxx/A000447/) | a(n) = 1^2 + 3^2 + 5^2 + 7^2 + ... + (2\*n-1)^2 = n\*(4\*n^2 - 1)/3. | **34** | 1001 |
| [A000448](seq/A000xxx/A000448/) | Smallest number that is the sum of 2 squares in at least n ways. | **219** | 10000 |
| [A000449](seq/A000xxx/A000449/) | Rencontres numbers: number of permutations of [n] with exactly 3… | **51** | 98 |
| [A000450](seq/A000xxx/A000450/) | a(n) = A058057(n,n-4). | **86** | 447 |
| [A000451](seq/A000xxx/A000451/) | Smallest number that is the sum of 3 squares in at least n ways. | **145** | 200 |
| [A000452](seq/A000xxx/A000452/) | The greedy sequence of integers which avoids 3-term geometric… | **83** | 10000 |
| [A000453](seq/A000xxx/A000453/) | Stirling numbers of the second kind, S(n,4). | **45** | 197 |
| [A000454](seq/A000xxx/A000454/) | Unsigned Stirling numbers of first kind s(n,4). | **66** | 97 |
| [A000455](seq/A000xxx/A000455/) | Digits of powers of 2. | **34** | 10000 |
| [A000456](seq/A000xxx/A000456/) | Number of permutations of [n] in which the longest increasing run has… | **144** | 450 |
| [A000457](seq/A000xxx/A000457/) | Exponential generating function: (1+3\*x)/(1-2\*x)^(7/2). | **37** | 201 |
| [A000458](seq/A000xxx/A000458/) | a(0) = a(1) = 1; thereafter a(n) = sigma(a(n-1)) + sigma(a(n-2)). | **134** | 40 |
| [A000459](seq/A000xxx/A000459/) | Number of multiset permutations of {1, 1, 2, 2, ..., n, n} with no… | **55** | 101 |
| [A000460](seq/A000xxx/A000460/) | Eulerian numbers (Euler's triangle: column k=3 of A008292, column k=2… | **44** | 998 |
| [A000461](seq/A000xxx/A000461/) | Concatenate n n times. | **31** | 333 |
| [A000462](seq/A000xxx/A000462/) | Numbers written in base of triangular numbers. | **65** | 10000 |
| [A000463](seq/A000xxx/A000463/) | n followed by n^2. | **35** | 10000 |
| [A000464](seq/A000xxx/A000464/) | Expansion of e.g.f. sin(x)/cos(2\*x). | **77** | 216 |
| [A000465](seq/A000xxx/A000465/) | Number of bipartite partitions of n white objects and 4 black ones. | **138** | 5001 |
| [A000466](seq/A000xxx/A000466/) | a(n) = 4\*n^2 - 1. | **28** | 901 |
| [A000467](seq/A000xxx/A000467/) | Number of permutations of [n] in which the longest increasing run has… | **144** | 450 |
| [A000468](seq/A000xxx/A000468/) | Powers of ten written in base 8. | **30** | 101 |
| [A000469](seq/A000xxx/A000469/) | 1 together with products of 2 or more distinct primes. | **54** | 10000 |
| [A000470](seq/A000xxx/A000470/) | Number of permutations of an n-sequence discordant with three given… | **150** | 19 |
| [A000471](seq/A000xxx/A000471/) | a(n) = floor(sinh(n)). | **86** | 201 |
| [A000472](seq/A000xxx/A000472/) | a(n) = a(n-1)^2 + (a(n-2) + 1)\*(a(n-1) - a(n-2)^2). | **39** | 14 |
| [A000473](seq/A000xxx/A000473/) | Number of genus 0 rooted maps with 5 faces and n vertices. | **98** | 497 |
| [A000474](seq/A000xxx/A000474/) | Number of nonisomorphic 1-factorizations of complete graph K\_{2n}. | **308** | 4 |
| [A000475](seq/A000xxx/A000475/) | Rencontres numbers: number of permutations of [n] with exactly 4… | **51** | 97 |
| [A000476](seq/A000xxx/A000476/) | Number of permutations of an n-sequence discordant with three given… | **147** | 19 |
| [A000477](seq/A000xxx/A000477/) | a(n) = Sum\_{k=1..n-1} k^2\*sigma(k)\*sigma(n-k). | **78** | 10000 |
| [A000478](seq/A000xxx/A000478/) | Number of ways of placing n labeled balls into 3 indistinguishable… | **47** | 195 |
| [A000479](seq/A000xxx/A000479/) | Number of 1-factorizations of K\_{n,n}. | **167** | 6 |
| [A000480](seq/A000xxx/A000480/) | a(n) = floor(cos(n)). | **86** | 80 |
| [A000481](seq/A000xxx/A000481/) | Stirling numbers of the second kind, S(n,5). | **55** | 196 |
| [A000482](seq/A000xxx/A000482/) | Unsigned Stirling numbers of first kind s(n,5). | **69** | 96 |
| [A000483](seq/A000xxx/A000483/) | Associated Stirling numbers: second-order reciprocal Stirling numbers… | **73** | 195 |
| [A000484](seq/A000xxx/A000484/) | a(n) = round(cos(n)). | **89** | 1001 |
| [A000485](seq/A000xxx/A000485/) | Number of partially labeled trees with n nodes (4 of which are… | **163** | 100 |
| [A000486](seq/A000xxx/A000486/) | One half of the number of permutations of [n] such that the… | **52** | 996 |
| [A000487](seq/A000xxx/A000487/) | Number of permutations of length n with exactly two valleys. | **51** | 196 |
| [A000488](seq/A000xxx/A000488/) | Generalized tangent numbers d\_(n,3). | **129** | 1000 |
| [A000489](seq/A000xxx/A000489/) | Card matching: Coefficients B[n,3] of t^3 in the reduced hit… | **132** | 100 |
| [A000490](seq/A000xxx/A000490/) | Generalized Euler numbers c(4,n). | **71** | 195 |
| [A000491](seq/A000xxx/A000491/) | Number of bipartite partitions of n white objects and 5 black ones. | **171** | 1001 |
| [A000492](seq/A000xxx/A000492/) | Number of permutations of an n-sequence discordant with three given… | **150** | 18 |
| [A000493](seq/A000xxx/A000493/) | a(n) = floor(sin(n)). | **126** | 10001 |
| [A000494](seq/A000xxx/A000494/) | Nearest integer to sin(n). | **95** | 1001 |
| [A000495](seq/A000xxx/A000495/) | Nearest integer to sinh(n). | **88** | 251 |
| [A000496](seq/A000xxx/A000496/) | Restricted permutations. | **57** | 1001 |
| [A000497](seq/A000xxx/A000497/) | S2(j,2j+2) where S2(n,k) is a 2-associated Stirling number of the… | **44** | 100 |
| [A000498](seq/A000xxx/A000498/) | Eulerian numbers (Euler's triangle: column k=4 of A008292, column k=3… | **57** | 197 |
| [A000499](seq/A000xxx/A000499/) | a(n) = Sum\_{k=1..n-1} k^3\*sigma(k)\*sigma(n-k). | **79** | 10000 |
| [A000500](seq/A000xxx/A000500/) | Number of permutations of an n-sequence discordant with three given… | **150** | 18 |
| [A000501](seq/A000xxx/A000501/) | a(n) = floor(cosh(n)). | **83** | 30 |
| [A000502](seq/A000xxx/A000502/) | Number of genus 0 rooted maps with 6 faces and n vertices. | **103** | 496 |
| [A000503](seq/A000xxx/A000503/) | a(n) = floor(tan(n)). | **121** | 100 |
| [A000504](seq/A000xxx/A000504/) | S2(j,2j+3) where S2(n,k) is a 2-associated Stirling number of the… | **60** | 17 |
| [A000505](seq/A000xxx/A000505/) | Eulerian numbers (Euler's triangle: column k=5 of A008292, column k=4… | **87** | 996 |
| [A000506](seq/A000xxx/A000506/) | One half of the number of permutations of [n] such that the… | **94** | 18 |
| [A000507](seq/A000xxx/A000507/) | Number of permutations of [n] with exactly 3 increasing runs of… | **71** | 18 |
| [A000508](seq/A000xxx/A000508/) | Generalized class numbers c\_(n,3). | **135** | 21 |
| [A000509](seq/A000xxx/A000509/) | Size of second largest n-arc in PG(2,q), where q runs through the… | **447** | 2 |
| [A000510](seq/A000xxx/A000510/) | Maximal number of points in PG(2,q) with at most 3 on a line (next… | **367** | 3 |
| [A000511](seq/A000xxx/A000511/) | Number of n-step spiral self-avoiding walks on hexagonal lattice,… | **125** | 20 |
| [A000512](seq/A000xxx/A000512/) | Number of equivalence classes of n X n matrices over {0,1} with rows… | **436** | 8 |
| [A000513](seq/A000xxx/A000513/) | Number of equivalence classes of n X n matrices over {0,1} with rows… | **436** | 8 |
| [A000514](seq/A000xxx/A000514/) | Eulerian numbers (Euler's triangle: column k=6 of A008292, column k=5… | **91** | 995 |
| [A000515](seq/A000xxx/A000515/) | a(n) = (2n)!(2n+1)!/n!^4, or equally (2n+1)\*binomial(2n,n)^2. | **43** | 101 |
| [A000516](seq/A000xxx/A000516/) | Number of equivalence classes of n X n matrices over {0,1} with rows… | **436** | 8 |
| [A000517](seq/A000xxx/A000517/) | Number of permutations of length n with exactly three valleys. | **71** | 194 |
| [A000518](seq/A000xxx/A000518/) | Generalized tangent numbers d\_(n,4). | **151** | 1000 |
| [A000519](seq/A000xxx/A000519/) | Number of equivalence classes of nonzero regular 0-1 matrices of… | **457** | 7 |
| [A000520](seq/A000xxx/A000520/) | Nearest integer to log\_10(n). | **39** | 1000 |
| [A000521](seq/A000xxx/A000521/) | Coefficients of modular function j as power series in q = e^(2 Pi i… | **116** | 150 |
| [A000522](seq/A000xxx/A000522/) | Total number of ordered k-tuples (k=0..n) of distinct elements from… | **33** | 451 |
| [A000523](seq/A000xxx/A000523/) | a(n) = floor(log\_2(n)). | **36** | 105 |
| [A000524](seq/A000xxx/A000524/) | Number of rooted trees with n nodes, 2 of which are labeled. | **153** | 30 |
| [A000525](seq/A000xxx/A000525/) | Number of partially labeled rooted trees with n nodes (4 of which are… | **185** | 21 |
| [A000526](seq/A000xxx/A000526/) | Number of partially labeled trees with n nodes (5 of which are… | **186** | 30 |
| [A000527](seq/A000xxx/A000527/) | Series-parallel numbers. | **169** | 15 |
| [A000528](seq/A000xxx/A000528/) | Number of types of Latin squares of order n. Equivalently, number of… | **270** | 5 |
| [A000529](seq/A000xxx/A000529/) | Powers of rooted tree enumerator. | **56** | 50 |
| [A000530](seq/A000xxx/A000530/) | Let p(n, s, x) be predicate that number of occurrences of s's in x >=… | **103** | 8 |
| [A000531](seq/A000xxx/A000531/) | From area of cyclic polygon of 2n + 1 sides. | **48** | 100 |
| [A000532](seq/A000xxx/A000532/) | Number of Hamiltonian paths from NW to SW corners in an n X n grid. | **125** | 5 |
| [A000533](seq/A000xxx/A000533/) | a(0)=1; a(n) = 10^n + 1, n >= 1. | **27** | 101 |
| [A000534](seq/A000xxx/A000534/) | Numbers that are not the sum of 4 nonzero squares. | **62** | 100 |
| [A000535](seq/A000xxx/A000535/) | Card matching: coefficients B[n,2] of t^2 in the reduced hit… | **123** | 20 |
| [A000536](seq/A000xxx/A000536/) | Number of 3-line Latin rectangles. | **57** | 15 |
| [A000537](seq/A000xxx/A000537/) | Sum of first n cubes; or n-th triangular number squared. | **33** | 1001 |
| [A000538](seq/A000xxx/A000538/) | Sum of fourth powers: 0^4 + 1^4 + ... + n^4. | **34** | 1001 |
| [A000539](seq/A000xxx/A000539/) | Sum of 5th powers: 0^5 + 1^5 + 2^5 + ... + n^5. | **34** | 1001 |
| [A000540](seq/A000xxx/A000540/) | Sum of 6th powers: 0^6 + 1^6 + 2^6 + ... + n^6. | **34** | 1001 |
| [A000541](seq/A000xxx/A000541/) | Sum of 7th powers: 1^7 + 2^7 + ... + n^7. | **34** | 1001 |
| [A000542](seq/A000xxx/A000542/) | Sum of 8th powers: 1^8 + 2^8 + ... + n^8. | **34** | 24 |
| [A000543](seq/A000xxx/A000543/) | Number of inequivalent ways to color vertices of a cube using at most… | **46** | 25 |
| [A000544](seq/A000xxx/A000544/) | One-half of the number of permutations p of [n] having exactly two… | **165** | 447 |
| [A000545](seq/A000xxx/A000545/) | Number of ways of n-coloring a dodecahedron. | **48** | 1000 |
| [A000546](seq/A000xxx/A000546/) | First occurrence of n consecutive numbers that take same number of… | **121** | 20 |
| [A000547](seq/A000xxx/A000547/) | Number of steps to reach 1 in sequence A000546. | **132** | 20 |
| [A000548](seq/A000xxx/A000548/) | Squares that are not the sum of 2 nonzero squares. | **63** | 300 |
| [A000549](seq/A000xxx/A000549/) | Numbers that are the sum of 2 squares but not sum of 3 nonzero… | **99** | 30 |
| [A000550](seq/A000xxx/A000550/) | Number of trees of diameter 7. | **177** | 50 |
| [A000551](seq/A000xxx/A000551/) | Number of labeled rooted trees of height 2 with n nodes. | **81** | 198 |
| [A000552](seq/A000xxx/A000552/) | Number of labeled rooted trees of height 3 with n nodes. | **128** | 16 |
| [A000553](seq/A000xxx/A000553/) | Number of labeled rooted trees of height 4 with n nodes. | **128** | 15 |
| [A000554](seq/A000xxx/A000554/) | Number of labeled trees of diameter 3 with n nodes. | **38** | 997 |
| [A000555](seq/A000xxx/A000555/) | Number of labeled trees of diameter 4 with n nodes. | **85** | 24 |
| [A000556](seq/A000xxx/A000556/) | Expansion of exp(-x) / (1 - exp(x) + exp(-x)). | **85** | 20 |
| [A000557](seq/A000xxx/A000557/) | Expansion of e.g.f. 1/(1 - 2\*sinh(x)). | **85** | 201 |
| [A000558](seq/A000xxx/A000558/) | Generalized Stirling numbers of second kind. | **76** | 557 |
| [A000559](seq/A000xxx/A000559/) | Generalized Stirling numbers of second kind. | **91** | 20 |
| [A000560](seq/A000xxx/A000560/) | Number of symmetric ways of folding a strip of n labeled stamps. | **158** | 8 |
| [A000561](seq/A000xxx/A000561/) | Number of discordant permutations. | **40** | 998 |
| [A000562](seq/A000xxx/A000562/) | Number of discordant permutations. | **55** | 36 |
| [A000563](seq/A000xxx/A000563/) | Number of discordant permutations. | **62** | 29 |
| [A000564](seq/A000xxx/A000564/) | Number of discordant permutations. | **81** | 25 |
| [A000565](seq/A000xxx/A000565/) | Number of discordant permutations. | **88** | 24 |
| [A000566](seq/A000xxx/A000566/) | Heptagonal numbers (or 7-gonal numbers): n\*(5\*n-3)/2. | **31** | 10001 |
| [A000567](seq/A000xxx/A000567/) | Octagonal numbers: n\*(3\*n-2). Also called star numbers. | **29** | 1001 |
| [A000568](seq/A000xxx/A000568/) | Number of outcomes of unlabeled n-team round-robin tournaments. | **171** | 35 |
| [A000569](seq/A000xxx/A000569/) | Number of graphical partitions of 2n. | **166** | 12 |
| [A000570](seq/A000xxx/A000570/) | Number of tournaments on n nodes determined by their score vectors. | **48** | 500 |
| [A000571](seq/A000xxx/A000571/) | Number of different score sequences that are possible in an n-team… | **144** | 1000 |
| [A000572](seq/A000xxx/A000572/) | A Beatty sequence: [ n(e+1) ]. | **46** | 59 |
| [A000573](seq/A000xxx/A000573/) | Number of 4 X n normalized Latin rectangles. | **157** | 3 |
| [A000574](seq/A000xxx/A000574/) | Coefficient of x^5 in expansion of (1 + x + x^2)^n. | **48** | 998 |
| [A000575](seq/A000xxx/A000575/) | Tenth column of quintinomial coefficients. | **66** | 1001 |
| [A000576](seq/A000xxx/A000576/) | a(n) is the number of (n-2) X n normalized Latin rectangles. | **163** | 3 |
| [A000577](seq/A000xxx/A000577/) | Number of triangular polyominoes (or triangular polyforms, or… | **246** | 10 |
| [A000578](seq/A000xxx/A000578/) | The cubes: a(n) = n^3. | **27** | 10001 |
| [A000579](seq/A000xxx/A000579/) | Figurate numbers or binomial coefficients C(n,6). | **46** | 1001 |
| [A000580](seq/A000xxx/A000580/) | a(n) = binomial coefficient C(n,7). | **36** | 994 |
| [A000581](seq/A000xxx/A000581/) | a(n) = binomial coefficient C(n,8). | **36** | 993 |
| [A000582](seq/A000xxx/A000582/) | a(n) = binomial coefficient C(n,9). | **36** | 992 |
| [A000583](seq/A000xxx/A000583/) | Fourth powers: a(n) = n^4. | **27** | 1001 |
| [A000584](seq/A000xxx/A000584/) | Fifth powers: a(n) = n^5. | **27** | 501 |
| [A000585](seq/A000xxx/A000585/) | Number of equivalence classes of Boolean functions of n variables… | **193** | 4 |
| [A000586](seq/A000xxx/A000586/) | Number of partitions of n into distinct primes. | **119** | 10001 |
| [A000587](seq/A000xxx/A000587/) | Rao Uppuluri-Carpenter numbers (or complementary Bell numbers):… | **55** | 596 |
| [A000588](seq/A000xxx/A000588/) | a(n) = 7\*binomial(2n,n-3)/(n+4). | **59** | 201 |
| [A000589](seq/A000xxx/A000589/) | a(n) = 11\*binomial(2n,n-5)/(n+6). | **54** | 196 |
| [A000590](seq/A000xxx/A000590/) | a(n) = 13\*binomial(2n,n-6)/(n+7). | **54** | 195 |
| [A000591](seq/A000xxx/A000591/) | Number of n-state 2-input 1-output automata with one initial and one… | **189** | 13 |
| [A000592](seq/A000xxx/A000592/) | Number of nonnegative solutions of x^2 + y^2 = z in first n shells. | **75** | 2750 |
| [A000593](seq/A000xxx/A000593/) | Sum of odd divisors of n. | **60** | 10000 |
| [A000594](seq/A000xxx/A000594/) | Ramanujan's tau function (or Ramanujan numbers, or tau numbers). | **83** | 5000 |
| [A000595](seq/A000xxx/A000595/) | Number of binary relations on n unlabeled points. | **171** | 25 |
| [A000596](seq/A000xxx/A000596/) | Central factorial numbers: A008955(n,2). | **47** | 9998 |
| [A000597](seq/A000xxx/A000597/) | Central factorial numbers: A008955(n,3). | **61** | 997 |
| [A000598](seq/A000xxx/A000598/) | Number of rooted ternary trees with n nodes; number of n-carbon alkyl… | **127** | 1001 |
| [A000599](seq/A000xxx/A000599/) | Number of secondary alcohols (alkanols or alkyl alcohols C\_n H\_{2n+1}… | **149** | 1001 |
| [A000600](seq/A000xxx/A000600/) | Number of tertiary alcohols (alkanols or alkyl alcohols C\_n H\_{2n+1}… | **145** | 1001 |
| [A000601](seq/A000xxx/A000601/) | Expansion of 1/((1-x)^2\*(1-x^2)\*(1-x^3)). | **42** | 10001 |
| [A000602](seq/A000xxx/A000602/) | Number of n-node unrooted quartic trees; number of n-carbon alkanes… | **185** | 35 |
| [A000603](seq/A000xxx/A000603/) | Number of nonnegative solutions to x^2 + y^2 <= n^2. | **75** | 540 |
| [A000604](seq/A000xxx/A000604/) | Number of nonnegative solutions to x^2 + y^2 + z^2 <= n^2. | **90** | 105 |
| [A000605](seq/A000xxx/A000605/) | Number of points of norm <= n in cubic lattice. | **92** | 64 |
| [A000606](seq/A000xxx/A000606/) | Number of nonnegative solutions to x^2 + y^2 + z^2 <= n. | **89** | 110 |
| [A000607](seq/A000xxx/A000607/) | Number of partitions of n into prime parts. | **97** | 13000 |
| [A000608](seq/A000xxx/A000608/) | Number of connected partially ordered sets with n unlabeled elements. | **285** | 7 |
| [A000609](seq/A000xxx/A000609/) | Number of threshold functions of n or fewer variables. | **247** | 6 |
| [A000610](seq/A000xxx/A000610/) | Number of self-complementary Boolean functions of n variables: see… | **224** | 10 |
| [A000611](seq/A000xxx/A000611/) | Number of normalized Latin squares of order n containing no 2 X 2… | **192** | 7 |
| [A000612](seq/A000xxx/A000612/) | Number of P-equivalence classes of switching functions of n or fewer… | **175** | 13 |
| [A000613](seq/A000xxx/A000613/) | Number of Boolean functions of n variables. | **192** | 4 |
| [A000614](seq/A000xxx/A000614/) | Number of complemented types of Boolean functions of n variables… | **217** | 4 |
| [A000615](seq/A000xxx/A000615/) | Number of threshold functions of exactly n variables. | **258** | 6 |
| [A000616](seq/A000xxx/A000616/) | a(-1)=1 by convention; for n >= 0, a(n) = number of irreducible… | **219** | 12 |
| [A000617](seq/A000xxx/A000617/) | Number of NP-equivalence classes of threshold functions of n or fewer… | **203** | 7 |
| [A000618](seq/A000xxx/A000618/) | Number of nondegenerate Boolean functions of n variables: For n > 0,… | **221** | 9 |
| [A000619](seq/A000xxx/A000619/) | NP-equivalence classes of threshold functions of exactly n variables. | **213** | 7 |
| [A000620](seq/A000xxx/A000620/) | Number of monosubstituted alkanes C(n-1)H(2n-1)-X with n-1 carbon… | **156** | 1930 |
| [A000621](seq/A000xxx/A000621/) | Number of monosubstituted alkanes C(n-1)H(2n-1)-X with n-1 carbon… | **60** | 3000 |
| [A000622](seq/A000xxx/A000622/) | Number of monosubstituted alkanes C(n)H(2n+1)-X of the form shown in… | **170** | 1930 |
| [A000623](seq/A000xxx/A000623/) | Number of monosubstituted alkanes C(n)H(2n+1)-X of the form shown in… | **186** | 1930 |
| [A000624](seq/A000xxx/A000624/) | Number of monosubstituted alkanes C(n)H(2n+1)-X of the form shown in… | **93** | 3000 |
| [A000625](seq/A000xxx/A000625/) | Number of n-node steric rooted ternary trees; number of n carbon… | **118** | 1931 |
| [A000626](seq/A000xxx/A000626/) | Number of stereoisomeric paraffins with n carbon atoms. | **232** | 36 |
| [A000627](seq/A000xxx/A000627/) | Number of non-stereoisomeric paraffins with n carbon atoms. | **102** | 42 |
| [A000628](seq/A000xxx/A000628/) | Number of n-node unrooted steric quartic trees; number of n-carbon… | **160** | 39 |
| [A000629](seq/A000xxx/A000629/) | Number of necklaces of partitions of n+1 labeled beads. | **56** | 425 |
| [A000630](seq/A000xxx/A000630/) | Number of ways to represent n using the binary operator a \* b = 2^a +… | **76** | 36 |
| [A000631](seq/A000xxx/A000631/) | Number of ethylene derivatives with n carbon atoms. | **167** | 499 |
| [A000632](seq/A000xxx/A000632/) | Number of esters with n carbon atoms up to structural isomerism. | **138** | 98 |
| [A000633](seq/A000xxx/A000633/) | Number of acyclic quaternary ammonium ions with n carbon atoms. | **194** | 31 |
| [A000634](seq/A000xxx/A000634/) | Number of glycols with n carbon atoms. | **215** | 29 |
| [A000635](seq/A000xxx/A000635/) | Number of paraffins C\_n H\_{2n} X Y with n carbon atoms. | **172** | 40 |
| [A000636](seq/A000xxx/A000636/) | Number of paraffins C\_n H\_{2n} X\_2 with n carbon atoms. | **213** | 30 |
| [A000637](seq/A000xxx/A000637/) | Number of fixed-point-free permutation groups of degree n. | **292** | 6 |
| [A000638](seq/A000xxx/A000638/) | Number of permutation groups of degree n; also number of conjugacy… | **282** | 6 |
| [A000639](seq/A000xxx/A000639/) | Number of alkyl benzenes with n carbon atoms: C(n)H(2n-6). | **197** | 40 |
| [A000640](seq/A000xxx/A000640/) | Number of paraffins C\_n H\_{2n-1} XYZ with n carbon atoms. | **175** | 40 |
| [A000641](seq/A000xxx/A000641/) | Number of paraffins C\_n H\_{2n-1} X\_3 with n carbon atoms. | **223** | 28 |
| [A000642](seq/A000xxx/A000642/) | a(n) = number of isomeric hydrocarbons of the acetylene series with… | **137** | 201 |
| [A000643](seq/A000xxx/A000643/) | a(n) = a(n-1) + 2^a(n-2). | **34** | 10 |
| [A000644](seq/A000xxx/A000644/) | Number of loops of length 4n on square grid that turn at each step… | **202** | 5 |
| [A000645](seq/A000xxx/A000645/) | Number of alkyls X^{II} C\_n H\_{2n+1} Y with n carbon atoms. | **175** | 28 |
| [A000646](seq/A000xxx/A000646/) | Number of alkyls Y^{II} C\_n H\_{2n+2} with n carbon atoms. | **144** | 30 |
| [A000647](seq/A000xxx/A000647/) | Alkyl naphthalenes C\_{n+10} H\_{2n+8} with n+10 carbon atoms. | **159** | 27 |
| [A000648](seq/A000xxx/A000648/) | Number of alkyls C\_{n+15} H\_{2n+10} (Anthr.) with n carbon atoms. | **173** | 26 |
| [A000649](seq/A000xxx/A000649/) | Number of alkyls C\_{n+15} H\_{2n+10} (Phenan) with n carbon atoms. | **158** | 26 |
| [A000650](seq/A000xxx/A000650/) | Number of alkyls S C\_{n+4} H\_{2n+4} with n carbon atoms. | **157** | 40 |
| [A000651](seq/A000xxx/A000651/) | Running time of Takeuchi function. | **124** | 571 |
| [A000652](seq/A000xxx/A000652/) | Invertible Boolean functions of n variables. | **71** | 7 |
| [A000653](seq/A000xxx/A000653/) | Invertible Boolean functions of n variables. | **291** | 8 |
| [A000654](seq/A000xxx/A000654/) | Invertible Boolean functions of n variables. | **306** | 6 |
| [A000655](seq/A000xxx/A000655/) | a(n) = number of letters in a(n-1), a(1) = 1 (in English). | **28** | 80 |
| [A000656](seq/A000xxx/A000656/) | Invertible Boolean functions of n variables with S(n) acting on the… | **325** | 4 |
| [A000657](seq/A000xxx/A000657/) | Median Euler numbers (the middle numbers of Arnold's shuttle… | **78** | 201 |
| [A000658](seq/A000xxx/A000658/) | Strehl's sequence "C\_n^(3)". | **105** | 596 |
| [A000659](seq/A000xxx/A000659/) | a(n) = 2^a(n-1) + a(n-2). | **37** | 7 |
| [A000660](seq/A000xxx/A000660/) | Boustrophedon transform of 1,1,2,3,4,5,... | **62** | 401 |
| [A000661](seq/A000xxx/A000661/) | Shifts 2 places left under boustrophedon transform. | **63** | 481 |
| [A000662](seq/A000xxx/A000662/) | Number of relations with 3 arguments on n nodes. | **159** | 15 |
| [A000663](seq/A000xxx/A000663/) | Number of binary relations on an infinite set, each with exactly n… | **182** | 7 |
| [A000664](seq/A000xxx/A000664/) | Number of graphs with n edges. | **216** | 8 |
| [A000665](seq/A000xxx/A000665/) | Number of 3-uniform hypergraphs on n unlabeled nodes, or equivalently… | **188** | 15 |
| [A000666](seq/A000xxx/A000666/) | Number of symmetric relations on n nodes. | **135** | 18 |
| [A000667](seq/A000xxx/A000667/) | Boustrophedon transform of all-1's sequence. | **57** | 486 |
| [A000668](seq/A000xxx/A000668/) | Mersenne primes (primes of the form 2^n - 1). | **66** | 15 |
| [A000669](seq/A000xxx/A000669/) | Number of series-reduced planted trees with n leaves. Also the number… | **96** | 1001 |
| [A000670](seq/A000xxx/A000670/) | Fubini numbers: number of preferential arrangements of n labeled… | **59** | 425 |
| [A000671](seq/A000xxx/A000671/) | Number of boron trees with n nodes, i.e. n-node rooted trees with… | **154** | 50 |
| [A000672](seq/A000xxx/A000672/) | Number of 3-valent trees (= boron trees or binary trees) with n nodes. | **151** | 52 |
| [A000673](seq/A000xxx/A000673/) | Number of bicentered 3-valent (or boron, or binary) trees with n… | **147** | 36 |
| [A000674](seq/A000xxx/A000674/) | Boustrophedon transform of 1, 2, 2, 2, 2, ... | **57** | 401 |
| [A000675](seq/A000xxx/A000675/) | Number of centered 3-valent (or boron, or binary) trees with n nodes. | **165** | 36 |
| [A000676](seq/A000xxx/A000676/) | Number of centered trees with n nodes. | **155** | 38 |
| [A000677](seq/A000xxx/A000677/) | Number of bicentered trees with n nodes. | **172** | 38 |
| [A000678](seq/A000xxx/A000678/) | Number of carbon (rooted) trees with n carbon atoms = unordered… | **185** | 44 |
| [A000679](seq/A000xxx/A000679/) | Number of groups of order 2^n. | **473** | 5 |
| [A000680](seq/A000xxx/A000680/) | a(n) = (2n)!/2^n. | **37** | 101 |
| [A000681](seq/A000xxx/A000681/) | Number of n X n matrices with nonnegative entries and every row and… | **50** | 251 |
| [A000682](seq/A000xxx/A000682/) | Semi-meanders: number of ways a semi-infinite directed curve can… | **140** | 12 |
| [A000683](seq/A000xxx/A000683/) | Number of colorings of labeled graphs on n nodes using exactly 2… | **78** | 20 |
| [A000684](seq/A000xxx/A000684/) | Number of colored labeled n-node graphs with 2 interchangeable colors. | **77** | 20 |
| [A000685](seq/A000xxx/A000685/) | Number of 3-colored labeled graphs on n nodes, divided by 3. | **109** | 12 |
| [A000686](seq/A000xxx/A000686/) | Number of 4-colored labeled graphs on n nodes, divided by 4. | **109** | 9 |
| [A000687](seq/A000xxx/A000687/) | Boustrophedon transform (first version) of Fibonacci numbers… | **71** | 483 |
| [A000688](seq/A000xxx/A000688/) | Number of Abelian groups of order n; number of factorizations of n… | **97** | 10000 |
| [A000689](seq/A000xxx/A000689/) | Final decimal digit of 2^n. | **27** | 81 |
| [A000690](seq/A000xxx/A000690/) | Landau's approximation to population of x^2 + y^2 <= 2^n. | **294** | 400 |
| [A000691](seq/A000xxx/A000691/) | Ramanujan's approximation to population of x^2 + y^2 <= 2^n. | **375** | 34 |
| [A000693](seq/A000xxx/A000693/) | Related to population of numbers of form x^2 + y^2. | **93** | 21 |
| [A000694](seq/A000xxx/A000694/) | Related to population of numbers of form x^2 + y^2. | **370** | 33 |
| [A000695](seq/A000xxx/A000695/) | Moser-de Bruijn sequence: sums of distinct powers of 4. | **38** | 1024 |
| [A000696](seq/A000xxx/A000696/) | Numbers k such that (1,k) is "good". | **79** | 17 |
| [A000697](seq/A000xxx/A000697/) | Boustrophedon transform of 1, 1, 4, 9, 16, ... | **65** | 401 |
| [A000698](seq/A000xxx/A000698/) | A problem of configurations: a(0) = 1; for n>0, a(n) = (2n-1)!! -… | **78** | 201 |
| [A000699](seq/A000xxx/A000699/) | Number of irreducible chord diagrams with 2n nodes. | **75** | 405 |
| [A000700](seq/A000xxx/A000700/) | Expansion of Product\_{k>=0} (1 + x^(2k+1)); number of partitions of n… | **71** | 600 |
| [A000701](seq/A000xxx/A000701/) | One half of number of non-self-conjugate partitions; also half of… | **79** | 1900 |
| [A000702](seq/A000xxx/A000702/) | a(n) is the number of conjugacy classes in the alternating group A\_n. | **92** | 1000 |
| [A000703](seq/A000xxx/A000703/) | Chromatic number (or Heawood number) of nonorientable surface with n… | **55** | 1001 |
| [A000704](seq/A000xxx/A000704/) | Number of degree-n even permutations of order dividing 2. | **58** | 201 |
| [A000705](seq/A000xxx/A000705/) | n-th superior highly composite number A002201(n) is product of first… | **288** | 5000 |
| [A000706](seq/A000xxx/A000706/) | Expansion of modular function 1/E\_3 (cf. A013973). | **81** | 361 |
| [A000707](seq/A000xxx/A000707/) | Number of permutations of [1,2,...,n] with n-1 inversions. | **83** | 420 |
| [A000708](seq/A000xxx/A000708/) | a(n) = E(n+1) - 2\*E(n), where E(i) is the Euler number A000111(i). | **65** | 483 |
| [A000709](seq/A000xxx/A000709/) | Related to population of numbers of form x^2 + y^2. | **197** | 500 |
| [A000710](seq/A000xxx/A000710/) | Number of partitions of n, with two kinds of 1, 2, 3 and 4. | **87** | 1001 |
| [A000711](seq/A000xxx/A000711/) | Number of partitions of n, with three kinds of 1,2,3 and 4 and two… | **90** | 1001 |
| [A000712](seq/A000xxx/A000712/) | a(n) = number of partitions of n into parts of 2 kinds. | **81** | 7000 |
| [A000713](seq/A000xxx/A000713/) | EULER transform of 3, 2, 2, 2, 2, 2, 2, 2, ... | **82** | 1001 |
| [A000714](seq/A000xxx/A000714/) | Number of partitions of n, with three kinds of 1 and 2 and two kinds… | **90** | 7000 |
| [A000715](seq/A000xxx/A000715/) | Number of partitions of n, with three kinds of 1,2 and 3 and two… | **90** | 6500 |
| [A000716](seq/A000xxx/A000716/) | Number of partitions of n into parts of 3 kinds. | **81** | 6500 |
| [A000717](seq/A000xxx/A000717/) | Number of graphs with n nodes and floor(n(n-1)/4) edges. | **214** | 13 |
| [A000718](seq/A000xxx/A000718/) | Boustrophedon transform of triangular numbers 1,1,3,6,10,... | **70** | 401 |
| [A000719](seq/A000xxx/A000719/) | Number of disconnected graphs with n nodes. | **213** | 18 |
| [A000720](seq/A000xxx/A000720/) | pi(n), the number of primes <= n. Sometimes called PrimePi(n) to… | **44** | 70000 |
| [A000721](seq/A000xxx/A000721/) | Number of NP-equivalence classes of balanced Boolean functions of n… | **263** | 6 |
| [A000722](seq/A000xxx/A000722/) | Number of invertible Boolean functions of n variables: a(n) = (2^n)!. | **42** | 9 |
| [A000723](seq/A000xxx/A000723/) | Invertible Boolean functions of n variables. | **56** | 8 |
| [A000724](seq/A000xxx/A000724/) | Invertible Boolean functions of n variables. | **139** | 6 |
| [A000725](seq/A000xxx/A000725/) | Invertible Boolean functions of n variables. | **320** | 6 |
| [A000726](seq/A000xxx/A000726/) | Number of partitions of n in which no parts are multiples of 3. | **85** | 5001 |
| [A000727](seq/A000xxx/A000727/) | Expansion of Product\_{k >= 1} (1 - x^k)^4. | **82** | 8500 |
| [A000728](seq/A000xxx/A000728/) | Expansion of Product\_{n>=1} (1-x^n)^5. | **82** | 8500 |
| [A000729](seq/A000xxx/A000729/) | Expansion of Product\_{k >= 1} (1 - x^k)^6. | **82** | 8500 |
| [A000730](seq/A000xxx/A000730/) | Expansion of Product\_{n>=1} (1 - x^n)^7. | **82** | 8500 |
| [A000731](seq/A000xxx/A000731/) | Expansion of Product (1 - x^k)^8 in powers of x. | **82** | 8500 |
| [A000732](seq/A000xxx/A000732/) | Boustrophedon transform of 1 & primes: 1,2,3,5,7,... | **79** | 401 |
| [A000733](seq/A000xxx/A000733/) | Boustrophedon transform of partition numbers 1, 1, 1, 2, 3, 5, 7, ... | **118** | 483 |
| [A000734](seq/A000xxx/A000734/) | Boustrophedon transform of 1,1,2,4,8,16,32,... | **65** | 401 |
| [A000735](seq/A000xxx/A000735/) | Expansion of Product\_{k>=1} (1 - x^k)^12. | **83** | 7000 |
| [A000736](seq/A000xxx/A000736/) | Boustrophedon transform of Catalan numbers 1, 1, 1, 2, 5, 14, ... | **78** | 401 |
| [A000737](seq/A000xxx/A000737/) | Boustrophedon transform of natural numbers, cf. A000027. | **62** | 401 |
| [A000738](seq/A000xxx/A000738/) | Boustrophedon transform (first version) of Fibonacci numbers… | **70** | 401 |
| [A000739](seq/A000xxx/A000739/) | Expansion of Product\_{k>=1} (1 - x^k)^16. | **83** | 7000 |
| [A000740](seq/A000xxx/A000740/) | Number of 2n-bead balanced binary necklaces of fundamental period 2n,… | **82** | 3322 |
| [A000741](seq/A000xxx/A000741/) | Number of compositions of n into 3 ordered relatively prime parts. | **84** | 10000 |
| [A000742](seq/A000xxx/A000742/) | Number of compositions of n into 4 ordered relatively prime parts. | **93** | 9997 |
| [A000743](seq/A000xxx/A000743/) | Number of compositions of n into 5 ordered relatively prime parts. | **100** | 9996 |
| [A000744](seq/A000xxx/A000744/) | Boustrophedon transform (second version) of Fibonacci numbers… | **68** | 401 |
| [A000745](seq/A000xxx/A000745/) | Boustrophedon transform of squares. | **67** | 401 |
| [A000746](seq/A000xxx/A000746/) | Boustrophedon transform of triangular numbers. | **68** | 401 |
| [A000747](seq/A000xxx/A000747/) | Boustrophedon transform of primes. | **80** | 401 |
| [A000748](seq/A000xxx/A000748/) | Expansion of bracket function. | **35** | 1001 |
| [A000749](seq/A000xxx/A000749/) | a(n) = 4\*a(n-1) - 6\*a(n-2) + 4\*a(n-3), n > 3, with a(0)=a(1)=a(2)=0,… | **44** | 201 |
| [A000750](seq/A000xxx/A000750/) | Expansion of bracket function. | **55** | 3001 |
| [A000751](seq/A000xxx/A000751/) | Boustrophedon transform of partition numbers. | **117** | 483 |
| [A000752](seq/A000xxx/A000752/) | Boustrophedon transform of powers of 2. | **62** | 401 |
| [A000753](seq/A000xxx/A000753/) | Boustrophedon transform of Catalan numbers. | **78** | 401 |
| [A000754](seq/A000xxx/A000754/) | Boustrophedon transform of odd numbers. | **62** | 401 |
| [A000755](seq/A000xxx/A000755/) | No-3-in-line problem on n X n grid: total number of ways of placing… | **172** | 7 |
| [A000756](seq/A000xxx/A000756/) | Boustrophedon transform of sequence 1,1,0,0,0,0,... | **60** | 401 |
| [A000757](seq/A000xxx/A000757/) | Number of cyclic permutations of [n] with no i -> i+1 (mod n). | **43** | 201 |
| [A000758](seq/A000xxx/A000758/) | Sum over rooted plane trees with n edges of (height - 1); height =… | **114** | 600 |
| [A000759](seq/A000xxx/A000759/) | Number of n-step self-avoiding walks on cubic lattice ending at point… | **119** | 11 |
| [A000760](seq/A000xxx/A000760/) | Number of n-step self-avoiding walks on cubic lattice ending at point… | **120** | 10 |
| [A000761](seq/A000xxx/A000761/) | Number of n-step self-avoiding walks on cubic lattice ending at point… | **120** | 9 |
| [A000762](seq/A000xxx/A000762/) | Number of n-step self-avoiding walks on cubic lattice ending at point… | **120** | 8 |
| [A000763](seq/A000xxx/A000763/) | Number of interval orders constructed from n intervals of generic… | **178** | 100 |
| [A000764](seq/A000xxx/A000764/) | Boustrophedon transform of Bell numbers. | **83** | 483 |
| [A000765](seq/A000xxx/A000765/) | Number of n-step self-avoiding walks on f.c.c. lattice ending at… | **133** | 7 |
| [A000766](seq/A000xxx/A000766/) | Number of n-step self-avoiding walks on f.c.c. lattice ending at… | **135** | 6 |
| [A000767](seq/A000xxx/A000767/) | Number of n-step self-avoiding walks on f.c.c. lattice ending at… | **135** | 5 |
| [A000768](seq/A000xxx/A000768/) | Number of n-step self-avoiding walks on f.c.c. lattice ending at… | **135** | 4 |
| [A000769](seq/A000xxx/A000769/) | No-3-in-line problem: number of inequivalent ways of placing 2n… | **256** | 7 |
| [A000770](seq/A000xxx/A000770/) | Stirling numbers of the second kind, S(n,6). | **63** | 195 |
| [A000771](seq/A000xxx/A000771/) | Stirling numbers of second kind, S(n,7). | **63** | 194 |
| [A000772](seq/A000xxx/A000772/) | E.g.f. exp(tan(x) + sec(x) - 1). | **83** | 479 |
| [A000773](seq/A000xxx/A000773/) | Number of numbers == 0 (mod 3) in range 2^n to 2^(n+1) with odd… | **46** | 501 |
| [A000774](seq/A000xxx/A000774/) | a(n) = n!\*(1 + Sum\_{i=1..n} 1/i). | **41** | 251 |
| [A000775](seq/A000xxx/A000775/) | a(n) = n! \* (n + 1 + 2\*Sum\_{k=1...n} 1/k). | **46** | 101 |
| [A000776](seq/A000xxx/A000776/) | a(n) = n! \* (1 + 2\*Sum\_{k=1..n} 1/k). | **43** | 251 |
| [A000777](seq/A000xxx/A000777/) | a(n) = (n+2)\*Catalan(n) - 1. | **44** | 201 |
| [A000778](seq/A000xxx/A000778/) | a(n) = Catalan(n) + Catalan(n+1) - 1. | **45** | 201 |
| [A000779](seq/A000xxx/A000779/) | a(n) = 2\*(2n-1)!!-(n-1)!\*2^(n-1), where (2n-1)!! is A001147(n). | **43** | 250 |
| [A000780](seq/A000xxx/A000780/) | a(n) = (n+1)!/2 + (n-1)(n-1)!. | **41** | 200 |
| [A000781](seq/A000xxx/A000781/) | a(n) = 3\*Catalan(n) - Catalan(n-1) - 1. | **46** | 1657 |
| [A000782](seq/A000xxx/A000782/) | a(n) = 2\*Catalan(n) - Catalan(n-1). | **46** | 1000 |
| [A000784](seq/A000xxx/A000784/) | Number of symmetrical planar partitions of n (planar partitions… | **230** | 150 |
| [A000785](seq/A000xxx/A000785/) | Number of asymmetrical planar partitions of n: planar partitions… | **297** | 150 |
| [A000786](seq/A000xxx/A000786/) | Number of inequivalent planar partitions of n, when considering them… | **153** | 151 |
| [A000787](seq/A000xxx/A000787/) | Strobogrammatic numbers: the same upside down. | **72** | 510 |
| [A000788](seq/A000xxx/A000788/) | Total number of 1's in binary expansions of 0, ..., n. | **43** | 10001 |
| [A000789](seq/A000xxx/A000789/) | Maximal order of a triangle-free cyclic graph with no independent set… | **201** | 6 |
| [A000790](seq/A000xxx/A000790/) | Primary pretenders: least composite c such that n^c == n (mod c). | **66** | 10001 |
| [A000791](seq/A000xxx/A000791/) | Ramsey numbers R(3,n). | **125** | 4 |
| [A000792](seq/A000xxx/A000792/) | a(n) = max{(n - i)\*a(i) : i < n}; a(0) = 1. | **47** | 6288 |
| [A000793](seq/A000xxx/A000793/) | Landau's function g(n): largest order of permutation of n elements.… | **116** | 80 |
| [A000794](seq/A000xxx/A000794/) | Permanent of the Desarguesian projective plane PG(2,n), or 0 if such… | **419** | 5 |
| [A000795](seq/A000xxx/A000795/) | Salié numbers: expansion of cosh x / cos x = Sum\_{n >= 0}… | **70** | 101 |
| [A000796](seq/A000xxx/A000796/) | Decimal expansion of Pi (or digits of Pi). | **85** | 20000 |
| [A000797](seq/A000xxx/A000797/) | Numbers that are not the sum of 4 tetrahedral numbers. | **121** | 241 |
| [A000798](seq/A000xxx/A000798/) | Number of different quasi-orders (or topologies, or transitive… | **168** | 6 |
| [A000799](seq/A000xxx/A000799/) | a(n) = floor(2^n / n). | **31** | 300 |
| [A000800](seq/A000xxx/A000800/) | Sum of upward diagonals of Eulerian triangle. | **84** | 601 |
| [A000801](seq/A000xxx/A000801/) | a(n) = Sum\_{k = 1..n} floor(2^k / k). | **38** | 500 |
| [A000802](seq/A000xxx/A000802/) | Maximal number of states in the minimal deterministic finite… | **74** | 3301 |
| [A000803](seq/A000xxx/A000803/) | a(n+3) = a(n+2) + a(n+1) + a(n) - 4. | **43** | 401 |
| [A000804](seq/A000xxx/A000804/) | Permanent of a certain cyclic n X n (0,1) matrix. | **142** | 1001 |
| [A000805](seq/A000xxx/A000805/) | Permanent of a certain cyclic n X n (0,1) matrix. | **146** | 1002 |
| [A000806](seq/A000xxx/A000806/) | Bessel polynomial y\_n(-1). | **40** | 405 |
| [A000807](seq/A000xxx/A000807/) | Quadratic invariants. | **69** | 289 |
| [A000808](seq/A000xxx/A000808/) | Number of switching networks (see Harrison reference for precise… | **39** | 12 |
| [A000809](seq/A000xxx/A000809/) | Number of switching networks (see Harrison reference for precise… | **42** | 9 |
| [A000810](seq/A000xxx/A000810/) | Expansion of e.g.f. (sin x + cos x)/cos 3x. | **71** | 201 |
| [A000811](seq/A000xxx/A000811/) | Number of switching networks (see Harrison reference for precise… | **160** | 7 |
| [A000812](seq/A000xxx/A000812/) | Number of switching networks (see Harrison reference for precise… | **160** | 6 |
| [A000813](seq/A000xxx/A000813/) | Expansion of (sin x + cos x)/cos 4x. | **71** | 201 |
| [A000814](seq/A000xxx/A000814/) | Number of switching networks (see Harrison reference for precise… | **213** | 7 |
| [A000815](seq/A000xxx/A000815/) | Number of switching networks (see Harrison reference for precise… | **213** | 6 |
| [A000816](seq/A000xxx/A000816/) | E.g.f.: Sum\_{n >= 0} a(n) \* x^(2\*n) / (2\*n)! = sin(x)^2 / cos(2\*x). | **71** | 201 |
| [A000817](seq/A000xxx/A000817/) | Number of switching networks under action of GL\_n(Z\_2) acting on 2… | **192** | 4 |
| [A000818](seq/A000xxx/A000818/) | Number of switching networks under action of GL\_n(Z\_2) acting on 3… | **193** | 4 |
| [A000819](seq/A000xxx/A000819/) | E.g.f.: cos(x)^2 / cos(2x) = Sum\_{n >= 0} a(n) \* x^(2n) / (2n)!. | **70** | 201 |
| [A000820](seq/A000xxx/A000820/) | Number of switching networks under action of AG\_n(Z\_2) acting on 2… | **199** | 4 |
| [A000821](seq/A000xxx/A000821/) | Number of switching networks under action of AG\_n(Z\_2) acting on 3… | **200** | 4 |
| [A000822](seq/A000xxx/A000822/) | Expansion of (sin^2 x + sin x) /cos 2x. | **85** | 178 |
| [A000823](seq/A000xxx/A000823/) | Number of switching networks (see Harrison reference for precise… | **42** | 7 |
| [A000824](seq/A000xxx/A000824/) | Number of switching networks (see Harrison reference for precise… | **67** | 6 |
| [A000825](seq/A000xxx/A000825/) | Expansion of cos x (1 + sin x ) /cos 2x. | **83** | 201 |
| [A000826](seq/A000xxx/A000826/) | Number of switching networks (see Harrison reference for precise… | **187** | 8 |
| [A000827](seq/A000xxx/A000827/) | Number of switching networks (see Harrison reference for precise… | **206** | 6 |
| [A000828](seq/A000xxx/A000828/) | E.g.f. cos(x)/(cos(x) - sin(x)). | **59** | 201 |
| [A000829](seq/A000xxx/A000829/) | Number of switching networks (see Harrison reference for precise… | **224** | 7 |
| [A000830](seq/A000xxx/A000830/) | Number of switching networks (see Harrison reference for precise… | **251** | 6 |
| [A000831](seq/A000xxx/A000831/) | Expansion of e.g.f. (1 + tan(x))/(1 - tan(x)). | **60** | 433 |
| [A000832](seq/A000xxx/A000832/) | Number of switching networks (see Harrison reference for precise… | **217** | 4 |
| [A000833](seq/A000xxx/A000833/) | Number of switching networks (see Harrison reference for precise… | **243** | 4 |
| [A000834](seq/A000xxx/A000834/) | Expansion of e.g.f. exp(x)\*(1 + tan(x))/(1 - tan(x)). | **61** | 162 |
| [A000835](seq/A000xxx/A000835/) | Number of switching networks (see Harrison reference for precise… | **236** | 4 |
| [A000836](seq/A000xxx/A000836/) | Number of switching networks (see Harrison reference for precise… | **270** | 4 |
| [A000837](seq/A000xxx/A000837/) | Number of partitions of n into relatively prime parts. Also aperiodic… | **131** | 6500 |
| [A000838](seq/A000xxx/A000838/) | Number of n-input 2-output switching networks under action of… | **42** | 7 |
| [A000839](seq/A000xxx/A000839/) | Number of n-input 3-output switching networks under action of… | **47** | 6 |
| [A000840](seq/A000xxx/A000840/) | Number of cubic bicolored graphs on n unlabeled nodes admitting an… | **388** | 20 |
| [A000841](seq/A000xxx/A000841/) | Number of n-input 2-output switching networks under action of… | **162** | 7 |
| [A000842](seq/A000xxx/A000842/) | Number of n-input 3-output switching networks under action of… | **162** | 6 |
| [A000843](seq/A000xxx/A000843/) | Number of quartic bicolored graphs on n unlabeled nodes admitting an… | **388** | 16 |
| [A000844](seq/A000xxx/A000844/) | Number of switching networks (see Harrison reference for precise… | **225** | 7 |
| [A000845](seq/A000xxx/A000845/) | Number of switching networks (see Harrison reference for precise… | **225** | 7 |
| [A000846](seq/A000xxx/A000846/) | a(n) = C(3n,n) - C(2n,n). | **64** | 201 |
| [A000847](seq/A000xxx/A000847/) | Number of n-input 2-output switching networks under action of GL(n,2)… | **194** | 4 |
| [A000848](seq/A000xxx/A000848/) | Number of n-input 3-output switching networks under action of GL(n,2)… | **195** | 4 |
| [A000849](seq/A000xxx/A000849/) | Number of primes <= product of first n primes, A002110(n). | **75** | 7 |
| [A000850](seq/A000xxx/A000850/) | Number of n-input 2-output switching networks under action of AG(n,2)… | **224** | 4 |
| [A000851](seq/A000xxx/A000851/) | Number of n-input 3-output switching networks under action of AG(n,2)… | **225** | 4 |
| [A000852](seq/A000xxx/A000852/) | Numbers beginning with a vowel in English. | **61** | 10000 |
| [A000853](seq/A000xxx/A000853/) | Number of n-input 2-output switching networks under action of… | **44** | 10 |
| [A000854](seq/A000xxx/A000854/) | Number of n-input 3-output switching networks under action of… | **69** | 10 |
| [A000855](seq/A000xxx/A000855/) | Final two digits of 2^n. | **28** | 1001 |
| [A000856](seq/A000xxx/A000856/) | Number of n-input 2-output switching networks under the action of… | **189** | 7 |
| [A000857](seq/A000xxx/A000857/) | Number of n-input 3-output switching networks under the action of… | **210** | 6 |
| [A000859](seq/A000xxx/A000859/) | Number of n-input 2-output switching networks under action of S(n)… | **252** | 7 |
| [A000860](seq/A000xxx/A000860/) | Number of n-input 3-output switching networks under action of S(n)… | **265** | 6 |
| [A000861](seq/A000xxx/A000861/) | Numbers ending with a vowel in American English. | **63** | 1000 |
| [A000862](seq/A000xxx/A000862/) | Number of n-input 2-output switching networks under action of AG(n,2)… | **268** | 4 |
| [A000863](seq/A000xxx/A000863/) | Number of n-input 3-output switching networks under action of AG(n,2)… | **295** | 4 |
| [A000864](seq/A000xxx/A000864/) | Deceptive nonprimes: composite numbers k that divide the repunit… | **55** | 58 |
| [A000865](seq/A000xxx/A000865/) | Numbers beginning with letter 'o' in English. | **46** | 10000 |
| [A000866](seq/A000xxx/A000866/) | 2^n written in base 5. | **59** | 301 |
| [A000867](seq/A000xxx/A000867/) | Numbers beginning with letter 'f' in English. | **61** | 10000 |
| [A000868](seq/A000xxx/A000868/) | Number of switching networks with C(2,n) acting on domain and… | **46** | 10 |
| [A000869](seq/A000xxx/A000869/) | Number of switching networks with C(2,n) acting on domain and… | **84** | 10 |
| [A000870](seq/A000xxx/A000870/) | Numbers beginning with letter 's' in English. | **61** | 10000 |
| [A000871](seq/A000xxx/A000871/) | Number of switching networks with S(n) acting on the domain and… | **211** | 7 |
| [A000872](seq/A000xxx/A000872/) | Number of switching networks with S(n) acting on the domain and… | **263** | 6 |
| [A000873](seq/A000xxx/A000873/) | Numbers beginning with letter 'e' in English. | **67** | 10000 |
| [A000874](seq/A000xxx/A000874/) | Number of switching networks with S(n) and C(2,2) acting on the… | **252** | 7 |
| [A000875](seq/A000xxx/A000875/) | Number of switching networks with S(n) and C(2,2) acting on the… | **295** | 6 |
| [A000877](seq/A000xxx/A000877/) | Number of switching networks with GL(n,2) acting on the domain and… | **239** | 4 |
| [A000878](seq/A000xxx/A000878/) | Number of switching networks with GL(n,2) acting on the domain and… | **287** | 4 |
| [A000879](seq/A000xxx/A000879/) | Number of primes < prime(n)^2. | **68** | 48 |
| [A000880](seq/A000xxx/A000880/) | Number of switching networks with AG(n,2) acting on the domain and… | **266** | 4 |
| [A000881](seq/A000xxx/A000881/) | Number of switching networks with AG(n,2) acting on the domain and… | **294** | 4 |
| [A000882](seq/A000xxx/A000882/) | Number of twin prime pairs <= product of first n primes. | **91** | 6 |
| [A000883](seq/A000xxx/A000883/) | Number of switching networks with C(2,n) acting on the domain and… | **48** | 10 |
| [A000884](seq/A000xxx/A000884/) | Number of switching networks with C(2,n) acting on the domain and… | **87** | 10 |
| [A000885](seq/A000xxx/A000885/) | Number of twin prime pairs < square of n-th prime. | **86** | 44 |
| [A000886](seq/A000xxx/A000886/) | Number of switching networks with S(n,2) acting on the domain and… | **215** | 7 |
| [A000887](seq/A000xxx/A000887/) | Number of switching networks with S(n,2) acting on the domain and… | **265** | 6 |
| [A000888](seq/A000xxx/A000888/) | a(n) = (2\*n)!^2 / ((n+1)!\*n!^3). | **44** | 101 |
| [A000889](seq/A000xxx/A000889/) | Number of switching networks with S(n) and C(2,2) acting on the… | **266** | 7 |
| [A000890](seq/A000xxx/A000890/) | Number of switching networks with S(n) and C(2,2) acting on the… | **317** | 7 |
| [A000891](seq/A000xxx/A000891/) | a(n) = (2\*n)!\*(2\*n+1)! / (n! \* (n+1)!)^2. | **45** | 101 |
| [A000892](seq/A000xxx/A000892/) | Number of switching networks with GL(n,2) acting on the domain and… | **240** | 4 |
| [A000893](seq/A000xxx/A000893/) | Number of switching networks with GL(n,2) acting on the domain and… | **290** | 4 |
| [A000894](seq/A000xxx/A000894/) | a(n) = (2\*n)!\*(2\*n+1)! / ((n+1)! \* n!^3). | **45** | 181 |
| [A000895](seq/A000xxx/A000895/) | Number of switching networks with AG(n,2) acting on the domain and… | **290** | 4 |
| [A000896](seq/A000xxx/A000896/) | Number of switching networks with AG(n,2) acting on the domain and… | **323** | 4 |
| [A000897](seq/A000xxx/A000897/) | a(n) = (4\*n)! / ((2\*n)!\*n!^2). | **51** | 201 |
| [A000898](seq/A000xxx/A000898/) | a(n) = 2\*(a(n-1) + (n-1)\*a(n-2)) for n >= 2 with a(0) = 1. | **44** | 201 |
| [A000899](seq/A000xxx/A000899/) | Number of solutions to the rook problem on an n X n board having a… | **97** | 200 |
| [A000900](seq/A000xxx/A000900/) | Number of solutions to the rook problem on an n X n board having a… | **77** | 201 |
| [A000901](seq/A000xxx/A000901/) | Number of solutions to the rook problem on a 2n X 2n board having a… | **73** | 403 |
| [A000902](seq/A000xxx/A000902/) | Expansion of e.g.f. (1/2)\*(exp(2\*x + x^2) + 1). | **49** | 201 |
| [A000903](seq/A000xxx/A000903/) | Number of inequivalent ways of placing n nonattacking rooks on n X n… | **97** | 451 |
| [A000904](seq/A000xxx/A000904/) | a(n) = (n+1)\*a(n-1) + (n+2)\*a(n-2) + a(n-3); a(1)=0, a(2)=3, a(3)=13. | **52** | 100 |
| [A000905](seq/A000xxx/A000905/) | Hamilton numbers. | **92** | 14 |
| [A000906](seq/A000xxx/A000906/) | Exponential generating function: 2\*(1+3\*x)/(1-2\*x)^(7/2). | **37** | 201 |
| [A000907](seq/A000xxx/A000907/) | Second-order reciprocal Stirling number (Fekete) a(n) = [[2n+2, n]].… | **51** | 16 |
| [A000908](seq/A000xxx/A000908/) | Atom-rooted polyenoids with n edges with symmetry class C\_s. | **117** | 27 |
| [A000909](seq/A000xxx/A000909/) | a(n) = (2\*n)!\*(2\*n+1)! / n!^2. | **37** | 101 |
| [A000910](seq/A000xxx/A000910/) | a(n) = 5\*binomial(n, 6). | **49** | 900 |
| [A000911](seq/A000xxx/A000911/) | a(n) = (2n+3)! /( n! \* (n+1)! ). | **41** | 201 |
| [A000912](seq/A000xxx/A000912/) | Expansion of (sqrt(1-4x^2) - sqrt(1-4x))/(2x). | **58** | 201 |
| [A000913](seq/A000xxx/A000913/) | Number of bond-rooted polyenoids with n edges. | **107** | 25 |
| [A000914](seq/A000xxx/A000914/) | Stirling numbers of the first kind: s(n+2, n). | **40** | 1001 |
| [A000915](seq/A000xxx/A000915/) | Stirling numbers of first kind s(n+4, n). | **63** | 1000 |
| [A000916](seq/A000xxx/A000916/) | a(2n) = n+2, a(2n-1) = smallest number requiring n+2 letters in… | **256** | 56 |
| [A000917](seq/A000xxx/A000917/) | a(n) = (2n+3)!/(n!\*(n+2)!). | **44** | 201 |
| [A000918](seq/A000xxx/A000918/) | a(n) = 2^n - 2. | **26** | 1001 |
| [A000919](seq/A000xxx/A000919/) | a(n) = 4^n - C(4,3)\*3^n + C(4,2)\*2^n - C(4,1). | **42** | 201 |
| [A000920](seq/A000xxx/A000920/) | Differences of 0: 6!\*Stirling2(n,6). | **58** | 1000 |
| [A000921](seq/A000xxx/A000921/) | Primes p of the form 3k+1 such that Sum\_{x=1..p} cos(2\*Pi\*x^3/p) >… | **236** | 175 |
| [A000922](seq/A000xxx/A000922/) | Primes p of the form 3k+1 such that -sqrt(p) < Sum\_{x=1..p}… | **229** | 130 |
| [A000923](seq/A000xxx/A000923/) | Primes p of the form 3k+1 such that Sum\_{x=1..p} cos(2\*Pi\*x^3/p) <… | **236** | 90 |
| [A000924](seq/A000xxx/A000924/) | Class number of Q(sqrt(-n)), n squarefree. | **161** | 180 |
| [A000925](seq/A000xxx/A000925/) | Number of ordered ways of writing n as a sum of 2 squares of… | **60** | 10001 |
| [A000926](seq/A000xxx/A000926/) | Euler's "numerus idoneus" (or "numeri idonei", or idoneal, or… | **115** | 65 |
| [A000927](seq/A000xxx/A000927/) | "First factor" (or relative class number) h- for cyclotomic field Q(… | **227** | 75 |
| [A000928](seq/A000xxx/A000928/) | Irregular primes: primes p such that at least one of the numerators… | **99** | 45 |
| [A000929](seq/A000xxx/A000929/) | Dimension of the n-th graded piece of the mod-2 Steenrod algebra A\_2. | **77** | 210 |
| [A000930](seq/A000xxx/A000930/) | Narayana's cows sequence: a(0) = a(1) = a(2) = 1; thereafter a(n) =… | **37** | 5001 |
| [A000931](seq/A000xxx/A000931/) | Padovan sequence (or Padovan numbers): a(n) = a(n-2) + a(n-3) with… | **39** | 8181 |
| [A000932](seq/A000xxx/A000932/) | a(n) = a(n-1) + n\*a(n-2); a(0) = a(1) = 1. | **40** | 800 |
| [A000933](seq/A000xxx/A000933/) | Genus of complete graph on n nodes. | **40** | 1000 |
| [A000934](seq/A000xxx/A000934/) | Chromatic number (or Heawood number) Chi(n) of a closed orientable… | **54** | 10001 |
| [A000935](seq/A000xxx/A000935/) | Number of free planar polyenoids with 2n nodes and symmetry point… | **284** | 6 |
| [A000936](seq/A000xxx/A000936/) | Number of free planar polyenoids with n nodes and symmetry point… | **278** | 11 |
| [A000937](seq/A000xxx/A000937/) | Length of longest simple cycle without chords in the n-dimensional… | **144** | 6 |
| [A000938](seq/A000xxx/A000938/) | Number of collinear point-triples in an n X n grid. | **109** | 500 |
| [A000939](seq/A000xxx/A000939/) | Number of inequivalent n-gons. | **155** | 450 |
| [A000940](seq/A000xxx/A000940/) | Number of n-gons with n vertices. | **162** | 498 |
| [A000941](seq/A000xxx/A000941/) | Number of free planar polyenoids with n nodes and symmetry point… | **279** | 11 |
| [A000942](seq/A000xxx/A000942/) | Number of free planar polyenoids with n nodes. | **236** | 11 |
| [A000943](seq/A000xxx/A000943/) | Number of combinatorial types of simplicial n-dimensional polytopes… | **104** | 34 |
| [A000944](seq/A000xxx/A000944/) | Number of polyhedra (or 3-connected simple planar graphs) with n… | **473** | 6 |
| [A000945](seq/A000xxx/A000945/) | Euclid-Mullin sequence: a(1) = 2, a(n+1) is smallest prime factor of… | **60** | 14 |
| [A000946](seq/A000xxx/A000946/) | Euclid-Mullin sequence: a(1) = 2, a(n+1) is the largest prime factor… | **75** | 8 |
| [A000947](seq/A000xxx/A000947/) | Number of free nonplanar polyenoids with n nodes and symmetry point… | **283** | 6 |
| [A000948](seq/A000xxx/A000948/) | Number of free nonplanar polyenoids with n nodes and symmetry point… | **284** | 6 |
| [A000949](seq/A000xxx/A000949/) | Number of forests with n nodes and height at most 2. | **113** | 101 |
| [A000950](seq/A000xxx/A000950/) | Number of forests with n nodes and height at most 3. | **112** | 64 |
| [A000951](seq/A000xxx/A000951/) | Number of forests with n nodes and height at most 4. | **112** | 41 |
| [A000952](seq/A000xxx/A000952/) | Numbers k == 2 (mod 4) that are the orders of conference matrices. | **203** | 5 |
| [A000953](seq/A000xxx/A000953/) | Number of free nonplanar polyenoids with n nodes. | **250** | 6 |
| [A000955](seq/A000xxx/A000955/) | A sequence satisfying (a(2n+1) + 1)^3 = Sum\_{k=1..2n+1} a(k)^3. | **60** | 10 |
| [A000956](seq/A000xxx/A000956/) | A sequence satisfying (a(2n+1) + 1)^3 = Sum\_{k=1..2n+1} a(k)^3. | **60** | 14 |
| [A000957](seq/A000xxx/A000957/) | Fine's sequence (or Fine numbers): number of relations of valence >=… | **54** | 1671 |
| [A000958](seq/A000xxx/A000958/) | Number of ordered rooted trees with n edges having root of odd degree. | **55** | 1000 |
| [A000959](seq/A000xxx/A000959/) | Lucky numbers. | **83** | 14000 |
| [A000960](seq/A000xxx/A000960/) | Flavius Josephus's sieve: Start with the natural numbers; at the k-th… | **57** | 10000 |
| [A000961](seq/A000xxx/A000961/) | Powers of primes. Alternatively, 1 and the prime powers (p^k, p… | **65** | 10000 |
| [A000962](seq/A000xxx/A000962/) | The convergent sequence A\_n for the ternary continued fraction… | **56** | 1001 |
| [A000963](seq/A000xxx/A000963/) | The convergent sequence B\_n for the ternary continued fraction… | **56** | 1001 |
| [A000964](seq/A000xxx/A000964/) | The convergent sequence C\_n for the ternary continued fraction… | **56** | 1001 |
| [A000965](seq/A000xxx/A000965/) | Numerators of expansion of e.g.f. sinh(x) / sin(x) (even powers only). | **134** | 101 |
| [A000966](seq/A000xxx/A000966/) | n! never ends in this many 0's. | **48** | 10000 |
| [A000967](seq/A000xxx/A000967/) | Sum of Fermat coefficients. | **56** | 1000 |
| [A000968](seq/A000xxx/A000968/) | Sum of odd Fermat coefficients rounded to nearest integer. | **54** | 500 |
| [A000969](seq/A000xxx/A000969/) | Expansion of g.f. (1 + x + 2\*x^2)/((1 - x)^2\*(1 - x^3)). | **30** | 10001 |
| [A000970](seq/A000xxx/A000970/) | Fermat coefficients. | **39** | 996 |
| [A000971](seq/A000xxx/A000971/) | Fermat coefficients. | **47** | 995 |
| [A000972](seq/A000xxx/A000972/) | Fermat coefficients. | **52** | 994 |
| [A000973](seq/A000xxx/A000973/) | Fermat coefficients. | **52** | 993 |
| [A000975](seq/A000xxx/A000975/) | a(2n) = 2\*a(2n-1), a(2n+1) = 2\*a(2n)+1 (also a(n) is the n-th number… | **27** | 3301 |
| [A000976](seq/A000xxx/A000976/) | Period of 1/n! in base 10. | **78** | 200 |
| [A000977](seq/A000xxx/A000977/) | Numbers that are divisible by at least three different primes. | **69** | 10000 |
| [A000978](seq/A000xxx/A000978/) | Wagstaff numbers: numbers k such that (2^k + 1)/3 is prime. | **66** | 10 |
| [A000979](seq/A000xxx/A000979/) | Wagstaff primes: primes of form (2^p + 1)/3. | **68** | 10 |
| [A000980](seq/A000xxx/A000980/) | Number of ways of writing 0 as Sum\_{k=-n..n} e(k)\*k, where e(k) is 0… | **73** | 520 |
| [A000981](seq/A000xxx/A000981/) | Numbers beginning with letter 'n' in English. | **59** | 10000 |
| [A000982](seq/A000xxx/A000982/) | a(n) = ceiling(n^2/2). | **31** | 3001 |
| [A000983](seq/A000xxx/A000983/) | Size of minimal binary covering code of length n and covering radius… | **180** | 7 |
| [A000984](seq/A000xxx/A000984/) | Central binomial coefficients: binomial(2\*n,n) = (2\*n)!/(n!)^2. | **39** | 1501 |
| [A000985](seq/A000xxx/A000985/) | Number of n X n symmetric matrices with nonnegative entries and all… | **75** | 101 |
| [A000986](seq/A000xxx/A000986/) | Number of n X n symmetric matrices with (0,1) entries and all row… | **75** | 446 |
| [A000987](seq/A000xxx/A000987/) | Number of stochastic matrices of integers. | **74** | 446 |
| [A000988](seq/A000xxx/A000988/) | Number of one-sided polyominoes with n cells. | **174** | 12 |
| [A000989](seq/A000xxx/A000989/) | 3-adic valuation of binomial(2\*n, n): largest k such that 3^k divides… | **54** | 2001 |
| [A000990](seq/A000xxx/A000990/) | Number of plane partitions of n with at most two rows. | **87** | 6500 |
| [A000991](seq/A000xxx/A000991/) | Number of 3-line partitions of n. | **89** | 6001 |
| [A000992](seq/A000xxx/A000992/) | "Half-Catalan numbers": a(n) = Sum\_{k=1..floor(n/2)} a(k)\*a(n-k) with… | **72** | 2500 |
| [A000993](seq/A000xxx/A000993/) | Number of distinct quadratic residues mod 10^n; also number of… | **49** | 1001 |
| [A000994](seq/A000xxx/A000994/) | Shifts 2 places left under binomial transform. | **59** | 651 |
| [A000995](seq/A000xxx/A000995/) | Shifts left two terms under the binomial transform. | **59** | 101 |
| [A000996](seq/A000xxx/A000996/) | Shifts 3 places left under binomial transform. | **64** | 301 |
| [A000997](seq/A000xxx/A000997/) | From a differential equation. | **64** | 31 |
| [A000998](seq/A000xxx/A000998/) | From a differential equation. | **67** | 696 |
| [A000999](seq/A000xxx/A000999/) | 5-adic valuation of binomial(2\*n,n): largest k such that 5^k divides… | **54** | 1001 |
| [A001000](seq/A001xxx/A001000/) | a(n) = least m such that if a/b < c/d where a,b,c,d are integers in… | **52** | 1000 |
| [A001001](seq/A001xxx/A001001/) | Number of sublattices of index n in generic 3-dimensional lattice. | **78** | 7500 |
| [A001002](seq/A001xxx/A001002/) | Number of dissections of a convex (n+2)-gon into triangles and… | **62** | 210 |
| [A001003](seq/A001xxx/A001003/) | Schroeder's second problem (generalized parentheses); also called… | **55** | 1313 |
| [A001004](seq/A001xxx/A001004/) | Number of nonequivalent dissections of an (n+2)-gon by… | **168** | 201 |
| [A001005](seq/A001xxx/A001005/) | Number of ways of partitioning n points on a circle into subsets only… | **58** | 201 |
| [A001006](seq/A001xxx/A001006/) | Motzkin numbers: number of ways of drawing any number of… | **51** | 2107 |
| [A001007](seq/A001xxx/A001007/) | a(n) = ( Sum C(p,i); i=1,...,floor(2p/3) ) / p^2, where p = prime(n). | **77** | 198 |
| [A001008](seq/A001xxx/A001008/) | a(n) = numerator of harmonic number H(n) = Sum\_{i=1..n} 1/i. | **69** | 2296 |
| [A001009](seq/A001xxx/A001009/) | Triangle giving number L(n,k) of normalized k X n Latin rectangles. | **152** | 21 |
| [A001010](seq/A001xxx/A001010/) | Number of symmetric foldings of a strip of n labeled stamps. | **185** | 17 |
| [A001011](seq/A001xxx/A001011/) | Number of ways to fold a strip of n blank stamps. | **203** | 10 |
| [A001013](seq/A001xxx/A001013/) | Jordan-Polya numbers: products of factorial numbers A000142. | **80** | 8000 |
| [A001014](seq/A001xxx/A001014/) | Sixth powers: a(n) = n^6. | **27** | 501 |
| [A001015](seq/A001xxx/A001015/) | Seventh powers: a(n) = n^7. | **27** | 1001 |
| [A001016](seq/A001xxx/A001016/) | Eighth powers: a(n) = n^8. | **27** | 1001 |
| [A001017](seq/A001xxx/A001017/) | Ninth powers: a(n) = n^9. | **27** | 10001 |
| [A001018](seq/A001xxx/A001018/) | Powers of 8: a(n) = 8^n. | **24** | 101 |
| [A001019](seq/A001xxx/A001019/) | Powers of 9: a(n) = 9^n. | **24** | 101 |
| [A001020](seq/A001xxx/A001020/) | Powers of 11: a(n) = 11^n. | **25** | 101 |
| [A001021](seq/A001xxx/A001021/) | Powers of 12: a(n) = 12^n. | **25** | 101 |
| [A001022](seq/A001xxx/A001022/) | Powers of 13: a(n) = 13^n. | **25** | 101 |
| [A001023](seq/A001xxx/A001023/) | Powers of 14: a(n) = 14^n. | **25** | 101 |
| [A001024](seq/A001xxx/A001024/) | Powers of 15: a(n) = 15^n. | **25** | 101 |
| [A001025](seq/A001xxx/A001025/) | Powers of 16: a(n) = 16^n. | **25** | 821 |
| [A001026](seq/A001xxx/A001026/) | Powers of 17: a(n) = 17^n. | **25** | 101 |
| [A001027](seq/A001xxx/A001027/) | Powers of 18: a(n) = 18^n. | **25** | 101 |
| [A001028](seq/A001xxx/A001028/) | E.g.f. A(x) satisfies A'(x) = 1 + A(A(x)), with A(0) = 0. | **153** | 300 |
| [A001029](seq/A001xxx/A001029/) | Powers of 19: a(n) = 19^n. | **25** | 101 |
| [A001030](seq/A001xxx/A001030/) | Fixed under 1 -> 21, 2 -> 211. | **37** | 8119 |
| [A001031](seq/A001xxx/A001031/) | Goldbach conjecture: a(n) = number of decompositions of 2n into sum… | **84** | 10000 |
| [A001032](seq/A001xxx/A001032/) | Numbers k such that sum of squares of k consecutive integers >= 1 is… | **495** | 380 |
| [A001033](seq/A001xxx/A001033/) | Numbers n such that the sum of the squares of n consecutive positive… | **493** | 250 |
| [A001034](seq/A001xxx/A001034/) | Orders of noncyclic simple groups (without repetition). | **945** | 10000 |
| [A001035](seq/A001xxx/A001035/) | Number of partially ordered sets ("posets") with n labeled elements… | **168** | 6 |
| [A001036](seq/A001xxx/A001036/) | Partial sums of A001037, omitting A001037(1). | **90** | 34 |
| [A001037](seq/A001xxx/A001037/) | Number of degree-n irreducible polynomials over GF(2); number of… | **90** | 3334 |
| [A001038](seq/A001xxx/A001038/) | Invertible Boolean functions with GL(n,2) acting on the domain and… | **274** | 4 |
| [A001039](seq/A001xxx/A001039/) | a(n) = (p^p-1)/(p-1) where p = prime(n). | **50** | 26 |
| [A001040](seq/A001xxx/A001040/) | a(n+1) = n\*a(n) + a(n-1) with a(0)=0, a(1)=1. | **40** | 451 |
| [A001041](seq/A001xxx/A001041/) | a(0)=12; thereafter a(n) = 12 times the product of the first n primes. | **54** | 101 |
| [A001042](seq/A001xxx/A001042/) | a(n) = a(n-1)^2 - a(n-2)^2. | **37** | 14 |
| [A001043](seq/A001xxx/A001043/) | Numbers that are the sum of 2 successive primes. | **49** | 10000 |
| [A001044](seq/A001xxx/A001044/) | a(n) = (n!)^2. | **33** | 101 |
| [A001045](seq/A001xxx/A001045/) | Jacobsthal sequence (or Jacobsthal numbers): a(n) = a(n-1) +… | **29** | 3317 |
| [A001046](seq/A001xxx/A001046/) | a(n) = n\*(n-1)\*a(n-1)/2 + a(n-2), a(0) = a(1) = 1. | **47** | 101 |
| [A001047](seq/A001xxx/A001047/) | a(n) = 3^n - 2^n. | **32** | 201 |
| [A001048](seq/A001xxx/A001048/) | a(n) = n! + (n-1)!. | **35** | 100 |
| [A001049](seq/A001xxx/A001049/) | Numbered stops in Manhattan on the Lexington Avenue subway. | **36** | 16 |
| [A001050](seq/A001xxx/A001050/) | Number of letters in n (in Finnish). | **226** | 20001 |
| [A001051](seq/A001xxx/A001051/) | Number of subgroups of order n in orthogonal group O(3). | **65** | 10000 |
| [A001052](seq/A001xxx/A001052/) | a(n) = n\*(n-1)\*a(n-1)/2 + a(n-2), a(0) = 1, a(1) = 2. | **49** | 101 |
| [A001053](seq/A001xxx/A001053/) | a(n+1) = n\*a(n) + a(n-1) with a(0)=1, a(1)=0. | **41** | 101 |
| [A001054](seq/A001xxx/A001054/) | a(n) = a(n-1)\*a(n-2) - 1. | **35** | 22 |
| [A001055](seq/A001xxx/A001055/) | The multiplicative partition function: number of ways of factoring n… | **92** | 10000 |
| [A001056](seq/A001xxx/A001056/) | a(n) = a(n-1)\*a(n-2) + 1, a(0) = 1, a(1) = 3. | **35** | 18 |
| [A001057](seq/A001xxx/A001057/) | Canonical enumeration of integers: interleaved positive and negative… | **29** | 1001 |
| [A001058](seq/A001xxx/A001058/) | 1-digit numbers in reverse alphabetical order, then 2-digit numbers,… | **395** | 10000 |
| [A001059](seq/A001xxx/A001059/) | Number of doubly labeled heap-ordered trees. | **100** | 101 |
| [A001060](seq/A001xxx/A001060/) | a(n) = a(n-1) + a(n-2) with a(0)=2, a(1)=5. Sometimes called the… | **33** | 1001 |
| [A001061](seq/A001xxx/A001061/) | 1-, 2-, 3-, ... digit numbers in alphabetical order in German. | **250** | 10000 |
| [A001063](seq/A001xxx/A001063/) | E.g.f. satisfies A'(x) = A(x/(1-x)). | **63** | 301 |
| [A001064](seq/A001xxx/A001064/) | a(n) = a(n-1)\*a(n-2) + a(n-3). | **41** | 23 |
| [A001065](seq/A001xxx/A001065/) | Sum of proper divisors (or aliquot parts) of n: sum of divisors of n… | **56** | 10000 |
| [A001066](seq/A001xxx/A001066/) | Dimensions (sorted, with duplicates removed) of real simple Lie… | **117** | 10000 |
| [A001067](seq/A001xxx/A001067/) | Numerator of Bernoulli(2\*n)/(2\*n). | **122** | 314 |
| [A001068](seq/A001xxx/A001068/) | a(n) = floor(5\*n/4), numbers that are congruent to {0, 1, 2, 3} mod 5. | **27** | 10001 |
| [A001069](seq/A001xxx/A001069/) | Log2\*(n) (version 2): take log\_2 of n this many times to get a number… | **54** | 1000 |
| [A001070](seq/A001xxx/A001070/) | Number of normalized Latin squares with second row even. | **191** | 6 |
| [A001071](seq/A001xxx/A001071/) | Number of one-sided chessboard polyominoes with n cells. | **271** | 9 |
| [A001072](seq/A001xxx/A001072/) | Number of minimally 2-edge-connected non-isomorphic graphs with n… | **351** | 5 |
| [A001073](seq/A001xxx/A001073/) | Label a 1-cm ruler with digits 1 cm wide. | **40** | 10001 |
| [A001074](seq/A001xxx/A001074/) | Numbers m such that Sum\_{k=0..m-1} exp(2\*Pi\*i\*k^3/m) != 0. | **107** | 1000 |
| [A001075](seq/A001xxx/A001075/) | a(0) = 1, a(1) = 2, a(n) = 4\*a(n-1) - a(n-2). | **33** | 1746 |
| [A001076](seq/A001xxx/A001076/) | Denominators of continued fraction convergents to sqrt(5). | **33** | 1001 |
| [A001077](seq/A001xxx/A001077/) | Numerators of continued fraction convergents to sqrt(5). | **34** | 1001 |
| [A001078](seq/A001xxx/A001078/) | a(n) = 10\*a(n-1) - a(n-2) with a(0) = 0, a(1) = 2. | **34** | 1001 |
| [A001079](seq/A001xxx/A001079/) | a(n) = 10\*a(n-1) - a(n-2); a(0) = 1, a(1) = 5. | **35** | 201 |
| [A001080](seq/A001xxx/A001080/) | a(n) = 16\*a(n-1) - a(n-2) with a(0) = 0, a(1) = 3. | **35** | 201 |
| [A001081](seq/A001xxx/A001081/) | a(n) = 16\*a(n-1) - a(n-2). | **35** | 201 |
| [A001082](seq/A001xxx/A001082/) | Generalized octagonal numbers: k\*(3\*k-2), k=0, +- 1, +- 2, +-3, ... | **31** | 1000 |
| [A001083](seq/A001xxx/A001083/) | Length of one version of Kolakoski sequence {A000002(i)} at n-th… | **73** | 32 |
| [A001084](seq/A001xxx/A001084/) | a(n) = 20\*a(n-1) - a(n-2) with a(0) = 0, a(1) = 3. | **35** | 201 |
| [A001085](seq/A001xxx/A001085/) | a(n) = 20\*a(n-1) - a(n-2). | **35** | 201 |
| [A001086](seq/A001xxx/A001086/) | Continued fraction associated with y(y+1) = x(x^2 -1). | **415** | 73 |
| [A001087](seq/A001xxx/A001087/) | Related to S(n), the number of self-dual monotone Boolean functions… | **96** | 32 |
| [A001088](seq/A001xxx/A001088/) | Product of totient function: a(n) = Product\_{k=1..n} phi(k) (cf.… | **74** | 497 |
| [A001089](seq/A001xxx/A001089/) | Number of permutations of [n] containing exactly 2 increasing… | **92** | 1001 |
| [A001090](seq/A001xxx/A001090/) | a(n) = 8\*a(n-1) - a(n-2); a(0) = 0, a(1) = 1. | **34** | 1001 |
| [A001091](seq/A001xxx/A001091/) | a(n) = 8\*a(n-1) - a(n-2); a(0) = 1, a(1) = 4. | **35** | 201 |
| [A001092](seq/A001xxx/A001092/) | Union of all numbers {p, q} where p and q are both primes or powers… | **79** | 900 |
| [A001093](seq/A001xxx/A001093/) | a(n) = n^3 + 1. | **30** | 10002 |
| [A001094](seq/A001xxx/A001094/) | a(n) = n + n\*(n-1)\*(n-2)\*(n-3). | **39** | 1001 |
| [A001095](seq/A001xxx/A001095/) | a(n) = n + n\*(n-1)\*(n-2)\*(n-3)\*(n-4). | **39** | 1001 |
| [A001096](seq/A001xxx/A001096/) | a(n) = n + n\*(n-1)\*(n-2)\*(n-3)\*(n-4)\*(n-5). | **49** | 1001 |
| [A001097](seq/A001xxx/A001097/) | Twin primes. | **61** | 1700 |
| [A001098](seq/A001xxx/A001098/) | Multiply previous term by 2 and write in binary. | **36** | 7 |
| [A001099](seq/A001xxx/A001099/) | a(n) = n^n - a(n-1), with a(1) = 1. | **35** | 100 |
| [A001100](seq/A001xxx/A001100/) | Triangle read by rows: T(n,k) = number of permutations of length n… | **139** | 40 |
| [A001101](seq/A001xxx/A001101/) | Moran numbers: k such that k/(sum of digits of k) is prime. | **86** | 1300 |
| [A001102](seq/A001xxx/A001102/) | Numbers k such that k / (sum of digits of k) is a square. | **87** | 220 |
| [A001103](seq/A001xxx/A001103/) | Numbers k such that (k / product of digits of k) is 1 or a prime. | **93** | 90 |
| [A001104](seq/A001xxx/A001104/) | Numbers k such that k / product of digits of k is a square. | **93** | 31 |
| [A001105](seq/A001xxx/A001105/) | a(n) = 2\*n^2. | **28** | 1001 |
| [A001106](seq/A001xxx/A001106/) | 9-gonal (or enneagonal or nonagonal) numbers: a(n) = n\*(7\*n-5)/2. | **31** | 10001 |
| [A001107](seq/A001xxx/A001107/) | 10-gonal (or decagonal) numbers: a(n) = n\*(4\*n-3). | **29** | 1001 |
| [A001108](seq/A001xxx/A001108/) | a(n)-th triangular number is a square: a(n+1) = 6\*a(n) - a(n-1) + 2,… | **35** | 1305 |
| [A001109](seq/A001xxx/A001109/) | a(n)^2 is a triangular number: a(n) = 6\*a(n-1) - a(n-2) with a(0)=0,… | **34** | 1305 |
| [A001110](seq/A001xxx/A001110/) | Square triangular numbers: numbers that are both triangular and… | **36** | 601 |
| [A001111](seq/A001xxx/A001111/) | Number of inequivalent Hadamard designs of order 4n. | **423** | 5 |
| [A001112](seq/A001xxx/A001112/) | A continued fraction. | **63** | 201 |
| [A001113](seq/A001xxx/A001113/) | Decimal expansion of e. | **76** | 50000 |
| [A001114](seq/A001xxx/A001114/) | Increasing blocks of digits of e. | **117** | 430 |
| [A001115](seq/A001xxx/A001115/) | Maximal number of pairwise relatively prime polynomials of degree n… | **103** | 41 |
| [A001116](seq/A001xxx/A001116/) | Maximal kissing number of an n-dimensional lattice. | **1447** | 6 |
| [A001117](seq/A001xxx/A001117/) | a(n) = 3^n - 3\*2^n + 3. | **36** | 201 |
| [A001118](seq/A001xxx/A001118/) | Number of labeled ordered set partitions into 5 parts for n>=1,… | **51** | 1001 |
| [A001119](seq/A001xxx/A001119/) | Number of skew-symmetric Hadamard matrices of order 4n. | **1063** | 4 |
| [A001120](seq/A001xxx/A001120/) | a(0) = a(1) = 1; for n > 1, a(n) = n\*a(n-1) + (-1)^n. | **36** | 451 |
| [A001121](seq/A001xxx/A001121/) | Number of doubly-regular tournaments of order 4n-1. | **788** | 5 |
| [A001122](seq/A001xxx/A001122/) | Primes with primitive root 2. | **65** | 450 |
| [A001123](seq/A001xxx/A001123/) | Primes with 3 as smallest primitive root. | **87** | 190 |
| [A001124](seq/A001xxx/A001124/) | Primes with 5 as smallest primitive root. | **91** | 100 |
| [A001125](seq/A001xxx/A001125/) | Primes with 6 as smallest primitive root. | **95** | 38 |
| [A001126](seq/A001xxx/A001126/) | Primes with 7 as smallest primitive root. | **97** | 38 |
| [A001127](seq/A001xxx/A001127/) | Trajectory of 1 under map x->x + (x-with-digits-reversed). | **40** | 1001 |
| [A001128](seq/A001xxx/A001128/) | Reverse digits of previous term and multiply by previous term. | **40** | 12 |
| [A001129](seq/A001xxx/A001129/) | Iccanobif numbers: reverse digits of two previous terms and add. | **65** | 1001 |
| [A001130](seq/A001xxx/A001130/) | Number of graphical basis partitions of 2n. | **203** | 100 |
| [A001131](seq/A001xxx/A001131/) | Number of red-black rooted trees with n-1 internal nodes. | **82** | 34 |
| [A001132](seq/A001xxx/A001132/) | Primes == +-1 (mod 8). | **46** | 4500 |
| [A001133](seq/A001xxx/A001133/) | Primes p such that the multiplicative order of 2 modulo p is (p-1)/3. | **71** | 80 |
| [A001134](seq/A001xxx/A001134/) | Primes p such that the multiplicative order of 2 modulo p is (p-1)/4. | **71** | 56 |
| [A001135](seq/A001xxx/A001135/) | Primes p such that the multiplicative order of 2 modulo p is (p-1)/5. | **71** | 24 |
| [A001136](seq/A001xxx/A001136/) | Primes p such that the multiplicative order of 2 modulo p is (p-1)/6. | **72** | 62 |
| [A001137](seq/A001xxx/A001137/) | Number of black-rooted red-black trees with n internal nodes. | **78** | 220 |
| [A001138](seq/A001xxx/A001138/) | Number of red rooted red-black trees with n internal nodes. | **82** | 35 |
| [A001139](seq/A001xxx/A001139/) | Number of stable feedback shift registers with n stages. | **117** | 5 |
| [A001140](seq/A001xxx/A001140/) | Describe the previous term! (method A - initial term is 4). | **82** | 20 |
| [A001141](seq/A001xxx/A001141/) | Describe the previous term! (method A - initial term is 5). | **82** | 20 |
| [A001142](seq/A001xxx/A001142/) | a(n) = Product\_{k=1..n} k^(2k - 1 - n). | **45** | 51 |
| [A001143](seq/A001xxx/A001143/) | Describe the previous term! (method A - initial term is 6). | **82** | 20 |
| [A001144](seq/A001xxx/A001144/) | An exponential function on partitions (next term is 2^512). | **50** | 8 |
| [A001145](seq/A001xxx/A001145/) | Describe the previous term! (method A - initial term is 7). | **82** | 20 |
| [A001146](seq/A001xxx/A001146/) | a(n) = 2^(2^n). | **24** | 12 |
| [A001147](seq/A001xxx/A001147/) | Double factorial of odd numbers: a(n) = (2\*n-1)!! = 1\*3\*5\*...\*(2\*n-1). | **31** | 401 |
| [A001148](seq/A001xxx/A001148/) | Final digit of 3^n. | **27** | 81 |
| [A001149](seq/A001xxx/A001149/) | A self-generating sequence: a(1)=1, a(2)=2, a(n+1) chosen so that… | **73** | 2000 |
| [A001150](seq/A001xxx/A001150/) | Number of n-input 2-output switching networks with GL(n,2) acting on… | **219** | 4 |
| [A001151](seq/A001xxx/A001151/) | Describe the previous term! (method A - initial term is 8). | **82** | 20 |
| [A001152](seq/A001xxx/A001152/) | Number of n-input 3-output switching networks with GL(n,2) acting on… | **255** | 4 |
| [A001153](seq/A001xxx/A001153/) | Degrees of primitive irreducible trinomials: n such that 2^n - 1 is a… | **186** | 11 |
| [A001154](seq/A001xxx/A001154/) | Describe the previous term! (method A - initial term is 9). | **82** | 20 |
| [A001155](seq/A001xxx/A001155/) | Describe the previous term! (method A - initial term is 0). | **82** | 20 |
| [A001156](seq/A001xxx/A001156/) | Number of partitions of n into squares. | **88** | 8000 |
| [A001157](seq/A001xxx/A001157/) | a(n) = sigma\_2(n): sum of squares of divisors of n. | **58** | 10000 |
| [A001158](seq/A001xxx/A001158/) | sigma\_3(n): sum of cubes of divisors of n. | **59** | 10000 |
| [A001159](seq/A001xxx/A001159/) | sigma\_4(n): sum of 4th powers of divisors of n. | **59** | 10000 |
| [A001160](seq/A001xxx/A001160/) | sigma\_5(n), the sum of the 5th powers of the divisors of n. | **59** | 10000 |
| [A001161](seq/A001xxx/A001161/) | Numbers containing an even number of letters. | **171** | 50 |
| [A001162](seq/A001xxx/A001162/) | Numbers containing an odd number of letters. | **172** | 50 |
| [A001163](seq/A001xxx/A001163/) | Stirling's formula: numerators of asymptotic series for Gamma… | **170** | 228 |
| [A001164](seq/A001xxx/A001164/) | Stirling's formula: denominators of asymptotic series for Gamma… | **172** | 296 |
| [A001165](seq/A001xxx/A001165/) | Position of first even digit after decimal point in sqrt(n). | **79** | 1000 |
| [A001166](seq/A001xxx/A001166/) | Smallest natural number requiring n letters in English. | **247** | 55 |
| [A001167](seq/A001xxx/A001167/) | Smallest natural number requiring n words in English (as spoken in… | **186** | 25 |
| [A001168](seq/A001xxx/A001168/) | Number of fixed polyominoes with n cells. | **152** | 15 |
| [A001169](seq/A001xxx/A001169/) | Number of board-pile polyominoes with n cells. | **60** | 200 |
| [A001170](seq/A001xxx/A001170/) | Number of board-pair-pile polyominoes with n cells. | **229** | 13 |
| [A001171](seq/A001xxx/A001171/) | From least significant term in expansion of E( tr (X'\*X)^n ), X… | **219** | 100 |
| [A001172](seq/A001xxx/A001172/) | Smallest even number that is an unordered sum of two odd primes in… | **121** | 55 |
| [A001173](seq/A001xxx/A001173/) | Half the number of binary relations on n unlabeled points. | **135** | 21 |
| [A001174](seq/A001xxx/A001174/) | Number of oriented graphs (i.e., digraphs with no bidirected edges)… | **138** | 21 |
| [A001175](seq/A001xxx/A001175/) | Pisano periods (or Pisano numbers): period of Fibonacci numbers mod n. | **68** | 5000 |
| [A001176](seq/A001xxx/A001176/) | Number of zeros in fundamental period of Fibonacci numbers mod n. | **74** | 1000 |
| [A001177](seq/A001xxx/A001177/) | Fibonacci entry points: a(n) = least k >= 1 such that n divides… | **62** | 10000 |
| [A001178](seq/A001xxx/A001178/) | Fibonacci frequency of n. | **103** | 4000 |
| [A001179](seq/A001xxx/A001179/) | Leonardo logarithm of n. | **118** | 4000 |
| [A001181](seq/A001xxx/A001181/) | Number of Baxter permutations of length n (also called Baxter… | **75** | 1120 |
| [A001182](seq/A001xxx/A001182/) | Number of cells of square lattice of edge 1/n inside quadrant of unit… | **79** | 10000 |
| [A001183](seq/A001xxx/A001183/) | Number of nontrivial Baxter permutations of length 2n-1. | **148** | 9 |
| [A001184](seq/A001xxx/A001184/) | Number of simple Hamiltonian paths connecting opposite corners of a… | **245** | 6 |
| [A001185](seq/A001xxx/A001185/) | Number of nontrivial Baxter permutations of length 2n-1. | **181** | 9 |
| [A001186](seq/A001xxx/A001186/) | Number of cubic Hamiltonian graphs with 2n nodes. | **325** | 6 |
| [A001187](seq/A001xxx/A001187/) | Number of connected labeled graphs with n nodes. | **121** | 51 |
| [A001188](seq/A001xxx/A001188/) | Number of even graphs with n edges. | **158** | 50 |
| [A001189](seq/A001xxx/A001189/) | Number of degree-n permutations of order exactly 2. | **42** | 800 |
| [A001190](seq/A001xxx/A001190/) | Wedderburn-Etherington numbers: unlabeled binary rooted trees (every… | **95** | 2546 |
| [A001191](seq/A001xxx/A001191/) | Digits of positive squares. | **41** | 5500 |
| [A001192](seq/A001xxx/A001192/) | Number of full sets of size n. | **108** | 51 |
| [A001193](seq/A001xxx/A001193/) | a(n) = (n+1)\*(2\*n)!/(2^n\*n!) = (n+1)\*(2n-1)!!. | **37** | 101 |
| [A001194](seq/A001xxx/A001194/) | a(n) = A059366(n,n-2) = A059366(n,2) for n >= 2, where the triangle… | **48** | 18 |
| [A001195](seq/A001xxx/A001195/) | a(n) = floor(n\*log((14/11)\*n^(10/9))). | **144** | 58 |
| [A001196](seq/A001xxx/A001196/) | Double-bitters: only even length runs in binary expansion. | **40** | 10001 |
| [A001197](seq/A001xxx/A001197/) | Zarankiewicz's problem k\_2(n). | **249** | 17 |
| [A001198](seq/A001xxx/A001198/) | Zarankiewicz's problem k\_3(n). | **275** | 9 |
| [A001200](seq/A001xxx/A001200/) | Number of linear geometries on n (unlabeled) points. | **338** | 9 |
| [A001201](seq/A001xxx/A001201/) | Number of Steiner triple systems (STS's) on 6n+1 or 6n+3 elements. | **195** | 5 |
| [A001202](seq/A001xxx/A001202/) | a(1)=0, a(2n) = a(n)+1, a(2n+1) = 10\*a(n+1). | **46** | 8192 |
| [A001203](seq/A001xxx/A001203/) | Simple continued fraction expansion of Pi. | **116** | 10000 |
| [A001204](seq/A001xxx/A001204/) | Continued fraction for e^2. | **52** | 20001 |
| [A001205](seq/A001xxx/A001205/) | Number of clouds with n points; number of undirected 2-regular… | **57** | 101 |
| [A001206](seq/A001xxx/A001206/) | Number of self-dual monotone Boolean functions of n variables. | **141** | 8 | 
| [A001207](seq/A001xxx/A001207/) | Number of fixed hexagonal polyominoes with n cells. | **154** | 12 |
| [A001208](seq/A001xxx/A001208/) | a(n) = solution to the postage stamp problem with 3 denominations and… | **208** | 1000 |
| [A001217](seq/A001xxx/A001217/) | Sorted list of orders of Weyl groups of types A\_n, B\_n, D\_n, E\_n,… | **118** | 34 |
| [A001218](seq/A001xxx/A001218/) | a(n) = 3^n mod 100. | **29** | 1001 |
| [A001219](seq/A001xxx/A001219/) | Triangular numbers of form a\*(a+1)\*(a+2). | **45** | 7 |
| [A001220](seq/A001xxx/A001220/) | Wieferich primes: primes p such that p^2 divides 2^(p-1) - 1. | **55** | 2 |
| [A005150](seq/A005xxx/A005150/) | Look and Say sequence: describe the previous term! (method A -… | **82** | 25 |
| [A034851](seq/A034xxx/A034851/) | Rows of Losanitsch's triangle T(n, k), n >= 0, 0 <= k <= n. | **92** | 5050 |
| [A035513](seq/A035xxx/A035513/) | Wythoff array read by falling antidiagonals. | **89** | 5151 |
| [A139569](seq/A139xxx/A139569/) | A triangle of coefficients of a Chebyshev T(x,n) polynomials to make… | **86** | 66 |
| [A228129](seq/A228xxx/A228129/) | a(n) = number of semistandard Young tableau families, headed by a… | **91** | 36 |
| [A228444](seq/A228xxx/A228444/) | Primes expressible as concatenation of phi(sigma(n)) and… | **127** | 16 |
| [A276805](seq/A276xxx/A276805/) | a(n) = numerator((n^2 + 3\*n + 2)/n^3). | **41** | 1000 |
| [A300000](seq/A300xxx/A300000/) | The sum of the first n terms of the sequence is the concatenation of… | **65** | 1001 |
| [A300001](seq/A300xxx/A300001/) | Side length of the smallest equilateral triangle that can be… | **71** | 100 |
| [A300002](seq/A300xxx/A300002/) | Lexicographically earliest sequence of positive integers such that no… | **208** | 10 |
| [A334244](seq/A334xxx/A334244/) | Decimal representation of n-th iteration of the one-dimensional… | **46** | 1000 |
| [A335332](seq/A335xxx/A335332/) | Decimal representation of n-th iteration of the one-dimensional… | **42** | 22 |
| [A384128](seq/A384xxx/A384128/) | Number of iterations for the circular absolute first-difference on… | **118** | 106 |
| [A386929](seq/A386xxx/A386929/) | a(n) is the least base b in {2,...,10} such that the base-b expansion… | **131** | 200 |
| [A401762](seq/A401xxx/A401762/) | Number of distinct traces of length n of Wolfram's 2-state 3-symbol… | **144** | 18 |

<!-- records:end -->

## Short-bar records

Programs that follow every rule but only have to print the first few terms
(the "Its terms" column) within the time limit; the main record next to them
clears the full bar. Each sequence has at most one, and each one is read by a
person before it lands ([rules](CONTRIBUTING.md#short-bar-records)).

<!-- short:start -->

| Sequence | Name | Short record | Its terms | Python 3 | Terms checked |
|---|---|---|---|---|---|
| [A000001](seq/A000xxx/A000001/) | Number of groups of order n. | **194** | 5 | 221 | 6 |

<!-- short:end -->

## Rules in short

- Print the sequence from its OEIS offset, one term per line, forever.
- CPython 3.12, no flags, no input. Size = file bytes, trailing newline free.
- Plain Python 3, standard library only; one program per sequence, plus
  optionally a [short-bar record](#short-bar-records).
- Correct for every n, with exact arithmetic; hard-coding only with a proof on
  the page.

Full rules and how to send a record: [CONTRIBUTING.md](CONTRIBUTING.md).

## Verify locally

```bash
python tools/verify.py
```

## Why "shortest known"

No record here is proved minimal, and in general none can be:

- A function that returns the length of the shortest program for any output
  cannot exist (the Berry paradox argument behind Kolmogorov complexity).
- Even deciding whether a given program prints a given infinite sequence is
  undecidable (Rice's theorem): a program that prints the sequence but switches
  to 0 once some machine halts prints it exactly when that machine never halts.
- For one specific record of, say, 66 bytes, ruling out every shorter program
  means about 96⁶⁵ ≈ 10¹²⁸ candidates, each needing a proof about its infinite
  output.

So a record stands until someone finds a shorter program.

## Related

- [LODA](https://loda-lang.org/) mines programs for OEIS sequences in its own
  assembly-like language, at a much larger scale and without byte golfing.
- The `%o` lines of each OEIS entry hold readable reference programs.

## License

Programs and tools: [MIT](LICENSE). Sequence names, b-files and other data
come from [The On-Line Encyclopedia of Integer Sequences](https://oeis.org/)
under [CC BY-SA 4.0](https://oeis.org/LICENSE); the pages that quote them are
under CC BY-SA 4.0 too.
