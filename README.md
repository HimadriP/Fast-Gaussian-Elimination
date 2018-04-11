# Fast-Gaussian-Elimination
A fast algorithm for Gaussain elimination over GF(2) (The matrix inputs are 0/1s) 

This project implements the algorithm described in this [paper](https://www.cs.umd.edu/%7Egasarch/TOPICS/factoring/fastgauss.pdf).

This algorithm was used in the implementation of the quadratic sieve in :
https://github.com/HimadriP/RSA_attacks/tree/master/attacks/factorization

## Future Work
- Implement the algorithm in parallel architecture
- Compare results

## Usage - Using Testcases given
The Usage is : `python fast_guass.py -path ./testcases/input1.txt`
