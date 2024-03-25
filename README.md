# MIPS Assembly Compiler, Machine Code Converter, and Simulator

This repository contains a comprehensive set of Python scripts designed for educational purposes, to demonstrate the MIPS architecture and instruction set. These tools include an Assembly to Machine Language Converter, a Single Cycle Data Processor, and a Cache Simulator, providing insights into the assembly language compilation, the execution of instructions in a simulated MIPS environment, and caching mechanisms.

## Components

- `assembly_to_machine_converter.py`: Converts MIPS assembly instructions into machine code by parsing the assembly instructions, categorizing them into R-type and I-type, and generating the corresponding machine code output.

- `single_cycle_data_processor.py`: Simulates the execution of MIPS machine code in a single-cycle data processor model. It supports basic arithmetic operations, memory access, and branching instructions, showcasing how a CPU might execute these instructions in a single cycle.

- `cache_simulator.py`: Simulates a cache memory interacting with the single cycle data processor. It demonstrates basic cache operations such as cache hits, misses, and the replacement policies in the context of MIPS instruction execution.

## Requirements

- Python 3.x
- \`bitstring\` Python package (for \`simulator.py\`)

## Setup

1. Clone the repository to your local machine.
2. Ensure Python 3.x is installed on your system.
3. Install the \`bitstring\` package using pip:

```
pip install bitstring
```

## Usage

### Assembly to Machine Language Converter

To convert MIPS assembly instructions into machine code:

```
python assembly_to_machine_converter.py --input <path_to_assembly_file>
```

### Single Cycle Data Processor Simulator

To simulate the execution of MIPS machine code in a single-cycle model:

```
python single_cycle_data_processor.py <path_to_machine_code_file> <path_to_memory_initialization_file>
```

### Cache Simulator

To run the cache simulator along with the data processor:

```
python cache_simulator.py <path_to_configuration_file> <path_to_trace_file>
```

Replace \`<path_to_configuration_file>\` and \`<path_to_trace_file>\` with the path to your cache configuration and instruction trace files, respectively.


