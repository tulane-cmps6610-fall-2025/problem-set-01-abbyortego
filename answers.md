# CMPS 6610 Problem Set 01
## Answers

**Name:** Abby Ortego

Place all written answers from `assignment-01.md` here for easier grading.

1. **Asymptotic notation**
  - 1a. $2^{n+1} \in \mathcal{O}(2^{n})$ iff there exists $c>0, n_0>0$ such that $2^{n+1} \leq c2^{n}$ $\forall n>n_0$
    - $2^{n+1} \leq c2^n$, Let $c=2, n_0=1$
    - $2^{1+1} \leq (2)2^1$
    - $4 \leq 4$
    - Thus, $2^{n+1} \in \mathcal{O}(2^{n})$.
  <br>

  - 1b. $2^{2^{n}} \in \mathcal{O}(2^{n})$  iff there exists $c>0, n_0>0$ such that $2^{2^{n}} \leq c2^{n}$ $\forall n>n_0$
    - $2^{2^{n}} \leq c2^n$, Let $c=2, n_0=1$
    - $2^{2^{1}} \leq (2)2^1$
    - $4 \leq 4$
    - Thus, $2^{2^{n}} \in \mathcal{O}(2^{n})$. 
  <br>
 
  - 1c. $n^{1.01} \in \mathcal{O}(\log^2{n})$  iff there exists $c>0, n_0>0$ such that $n^{1.01} \leq \log^2{n}$ $\forall n>n_0$
    - $n^{1.01} \leq c\log^2{n}$
  <br>

  - 1d. $n^{1.01} \in \mathcal{\Omega}(\log^2{n})$ iff there exists $c>0, n_0>0$ such that $n^{1.01} \geq \log^2{n}$ $\forall n>n_0$
    - $n^{1.01} \geq c\log^2{n}$, Let $c=1, n_0=1$
    - $1^{1.01} \geq 1 \log^2{1}$
    - $1 \geq 1 (0)^2$
    - $1 \geq 0$
    - Thus, $n^{1.01} \in \mathcal{\Omega}(\log^2{n})$.
    <br>

  - 1e. $\sqrt{n} \in \mathcal{O}(\log^3{n}) \texttt{ iff } \exists$ $c>0, n_0>0 \ni \sqrt{n} \leq \log^3{n}$ $\forall n>n_0$
    - $\sqrt{n} \leq c\log^3{n}$
  <br>

  - 1f. $\sqrt{n} \in \mathcal{\Omega}(\log^3{n})$ iff there exists $c>0, n_0>0$ such that $\sqrt{n} \geq \log^3{n}$ $\forall n>n_0$
    - $\sqrt{n} \geq c\log^3{n}$, Let $c=1, n_0=1$
    - $\sqrt{1} \geq 1\log^3{1}$
    - $1 \geq 1(0)^3$
    - $1 \geq 0$
    - Thus, $\sqrt{n} \in \mathcal{\Omega}(\log^3{n})$.
  <br>

  - 1g. Assume $\mathcal{o}(g(n)) \cap \mathcal{\Omega}(g(n)) \neq \mathcal{\empty}$ 
    - $\mathcal{o}(g(n)) \coloneqq f(n) < cg(n), c>0, n_0>0$
    - $\mathcal{\omega}(g(n)) \coloneqq f(n) > cg(n), c>0, n_0>0$
    - $cg(n) < f(n) < cg(n)$ which cannot be true.
    - As $n \rightarrow \infty$, $f(n)$ cannot be both less than $cg(n)$ and greater than $cg(n)$. Therefore, $\mathcal{o}(g(n)) \cap \mathcal{\Omega}(g(n)) = \mathcal{\empty}$

2. **SPARC to Python**

  - 2b. It does a remainder calculation but seems to always return the maximum out of the two inputs given.

3. **Parallelism and recursion**
*The superscripts refer to the lines of code in `main.py`!*

  - 3b. 
    - $W = c_{30}n + c_{31}n + c_{33}n + c_{34}n + c_{35}n + c_{38} = \mathcal{O}(n)$
    - No parallelization so $S = \mathcal{O}(n)$
  <br>

  - 3d.
    - $W = \mathcal{O}(n)$
    - No parallelization so $S = \mathcal{O}(n)$
  <br>

  - 3e.
    - $W = \mathcal{O}(n)$
    - $S = \mathcal{O}(\log{n})$
  
4. **GCD**
