# Cache Simulator

## Overview

This project provides a Python-based cache simulator for educational and experimental purposes. It supports both direct-mapped and set associative caches, offering insights into cache operations such as hits, misses, and evictions based on given memory access patterns.

## Features

- Support for direct-mapped and set associative caches.
- Configuration options for cache size, block size, and associativity.
- Input via text files containing memory addresses in hexadecimal format.
- Output includes detailed cache access results and hit rate.

## Requirements

- Python 3.x

## Usage

1. Clone the repository or download the Python script.
2. Prepare a text file with hexadecimal memory addresses, one per line.
3. Run the script with the required arguments. For example:

```sh
python cache_simulator.py --type d --cache_size 2048 --block_size 64 --memfile memory_addresses.txt

