Lab Activity 4: Design Patterns and Unit Testing

This project implements the Builder Design Pattern in Python simulating a custom PC builder application.

Design Pattern: Builder Pattern
Why it fits: It constructs a customized PC step-by-step while maintaining default specifications for unselected parts.

Files:
- main.py: Core program with the PCBuilder class.
- test_main.py: Automated unit tests using unittest.
- README.md: Project description and instructions.

Test Cases:
1. test_default_pc: Verifies PC creation using default specs.
2. test_gaming_pc: Verifies custom PC build with custom CPU, GPU, and RAM.
3. test_ram_upgrade_only: Verifies upgrading only the RAM while keeping other defaults.

Instructions to Run:
1. Open the terminal in the project directory.
2. Run the tests with the following command:
python test_main.py

Author: Lorenzo B. Kollin
