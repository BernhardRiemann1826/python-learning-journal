This Python project simulates the RSA encryption and decryption process, and visualizes the operation of RSA exponents on the multiplicative group of integers modulo n. It includes:
A customizable RSA setup using user input
Interactive encryption and decryption
Graph visualization of the RSA exponentiation and decryption process
A circular layout illustrating how each element maps under RSA transformations


Setup: This project requires Python 3.7+ and the following libraries:
matplotlib
networkx
How to Run: 
Save the code into a file named, for example, rsa_simulation.py.
Run the script from the command line or an IDE: python rsa_simulation.py.
Follow the interactive prompts.
Testing:
Verify mod_exp_dp(x, exp) returns the same as pow(x,exp,n).
Verify _EEA(a, b) satisfies Bézout’s identity: a*x + b*y == gcd(a, b).
Verify compute_d(e, phi) returns a modular inverse of e mod phi.
Verify encrypt(msg) encrypts string to integer.
Verify decrypt(ciphertext) reverses encrypt() correctly
Verify all nodes and edges follow RSA logic in the graph built by build_graph()



