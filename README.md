# Python example code for the ACM/IEEE Quantum Computing for Drug Discovery Challenge at ICCAD 2023

## What's in this repository?

This repository contains a simple example to illustrate how to train the variational quantum eigensolver in qiskit platform and evaluate the comprehensive performances in terms of accuracy, quantum resource cost and classical computation resource cost. 

For this example, we implemented a UCCSD ansatz with Hartree-fork initial state. You can use different techniques to construct the ansatz and find the initial state for your implementation. We required all participant read the [Example_Code](https://github.com/qccontest/QC-Contest-Demo/blob/main/examplecode.ipynb), as we describe detailes in the .ipynb file, with the example of implementation, how to calculate the accuracy, how to obtain the circuit duration. Please noticed that since participants may use different optimizers, so we 
require all participant self-report their optimization iterations directly from optimizer output, which will be detailed in the submission requirement that will release soon.


## How do I find the dataset?

You can find the hamiltonian for the target molecule at [Hamiltonian](https://github.com/qccontest/QC-Contest-Demo/tree/main/Hamiltonian). And we also require participant to fix the seed for algorithmic, transpiling, and measurement in qiskit, the final results should be the average of 10 different seeds in [Seeds](https://github.com/qccontest/QC-Contest-Demo/blob/main/algorithm_seeds/requiredseeds.txt).