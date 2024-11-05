# Lab 5: Modular Arithmetic

- [Lab 5: Modular Arithmetic](#lab-5-modular-arithmetic)
  - [Objectives](#objectives)
  - [Part I: Algebraic Structures](#part-1-algebraic-structures)
    - [Part I's implementation](#part-is-implementation)
  - [Part II: Galois Field](#part-ii-galois-field)
    - [Part II's implementation](#part-iis-implementation)
  - [Part III: Generate tables](#part-iii-generate-tables)
    - [Part III's workings](#part-iiis-workings)

## Objectives

* Implement a class to do computation in GF(2<sup>n</sup>)

## Part I: Algebraic Structures

Create a class `Polynomial2` where:
- An instance of the class is a polunomial of any arbitrary degree
- Each coefficient is in GF(2) - it can only be 0 or 1
- The constructor takes in a list containing the values of coefficient of a polynomial, starting from the lowest power to the highest power

#### Polynomial2 Methods

##### `add()` and `sub()`

- For addition, coefficient of the same powers are `XOR`-ed
- Addition and subtraction on polynomials are the same operation
- It should return a new `Polynomial2` object

#### `mul()`

- It takes in another polynomial `p2` to be multiplied and the modulus polynomial `modp` and returns a new `Polynomial2` object

<p align="center">
  <img src="https://raw.githubusercontent.com/DarrenPea/50.042-Foundations-of-Cybersecurity/refs/heads/main/lab_5/images/mult.jpg" />
</p>

#### Euclidean Division with `div()`

- The method should return two polynomials, one for quotient and one for remainder

<p align="center">
  <img src="https://raw.githubusercontent.com/DarrenPea/50.042-Foundations-of-Cybersecurity/refs/heads/main/lab_5/images/div.png" />
</p>

### Part I's implementation

Solution file: `gf2ntemplate.py`

I implemented a bitwise `XOR` for the `add()` and `sub()` after ensuring they are padded to the same degree.

For `mul()`, I found the result using partial results. Following the logic of how multiplication workings came about, I proceeded with the following steps:

For each coefficient index `i` of the polynomial, from the lowest power:
1. Initialise the result to be a polynomial of 0's
2. Copy the polynomial into `working` (to do workings on)
3. Shift `working` left by 1 bit
4. Let `x_max` be the degree of the irreducible polynomial
5. Check if the coefficient of `working` at degree `x_max` is 1
6. If it is, subtract the irreducible polynomial from it and only keep the polynomial till degree `x_max`
7. If the coefficient of the original polynomial at index `i` is 1, add the result from step 5 to the final result.
8. Repeat steps 2 to 6 until the multiplication process is complete

For `div()`, I implemented the Euclidean division, whose pseudocode can be seen above.

## Part II: Galois Field

- Create a class `GF2N` that implements Galois Field (a finite field with number of elements equals to 2<sup>n</sup>)
- The constructor takes in x, n, and ip
	- x is the number to be represented in Galois Field
	- n is the power, 2<sup>n</sup>
	- ip is the irreducible polynomial
  - The default polynomial is P(x) = x<sup>8</sup> + x<sup>4</sup> + x<sup>3</sup> + x + 1

Methods to implement:
- Addition, subtraction, multiplication and division
- `getPolynomial2()` that returns the polynomial representation of the number
- `getInt()` that returns the integer value
- Overwrite `__str__()` to print the integer value

### Part II's implementation

Solution file: `gf2ntemplate.py`

To implement these methods, I used the methods that I have already created in Part I.

## Part III: Generate Tables

### Part III's workings

I have created a table for addition and multiplication for GF(2<sup>4</sup>), using (x<sup>4</sup> + x<sup>3</sup> + 1) as the modulus and saved it in `table1.txt`.