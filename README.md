# Python example code for the ACM/IEEE Quantum Computing for Drug Discovery Challenge at ICCAD 2023

## What's in this repository?

This repository contains a simple example to illustrate how to train the variational quantum eigensolver on the Qiskit platform and evaluate the comprehensive performances in terms of accuracy, quantum resource cost, and classical computation resource cost.

For this example, we implemented a UCCSD ansatz with a Hartree-fork initial state. You can use different techniques to construct the ansatz and find the initial state for your implementation. We required all participants to read the [Example_Code](https://github.com/qccontest/QC-Contest-Demo/blob/main/examplecode.ipynb), as we describe details in the .ipynb file, with examples of implementation, how to calculate the accuracy, and how to obtain the circuit duration. 

And we release the noise model and system model, we require participant to follow the topology map from FakeMontreal. And we provide three noise models extracted from FakeCairo, FakeMontreal, and FakeKolkata. Please refer to the [NoiseModel and SystemModel](https://github.com/qccontest/QC-Contest-Demo/blob/main/NoiseModel_and_SystemModel.ipynb).


## How do I find the dataset?

You can find the Hamiltonian for the target molecule at [Hamiltonian](https://github.com/qccontest/QC-Contest-Demo/tree/main/Hamiltonian). And we also recommend participants some seeds for algorithmic, transpiling, and measurement in Qiskit; the final results should be the average of 10 different seeds: 5 in [Seeds](https://github.com/qccontest/QC-Contest-Demo/blob/main/algorithm_seeds/requiredseeds.txt), and other 5 will be selected from hidden test seeds set. You can find the noise models at [NoiseModel](https://github.com/qccontest/QC-Contest-Demo/tree/main/NoiseModel).

## Convert given Hamiltonian to compatible with pennylane:

You can find the example code to convert the given Hamiltonian to compatible with pennylane at [converter](https://github.com/qccontest/QC-Contest-Demo/blob/main/Hamiltonian_to_pennylane.py).