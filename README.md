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

Arguments
--type (required): Specifies the cache type. Use d for direct-mapped cache and s for set associative cache.
--nway (optional for s type): The number of ways for a set associative cache. This parameter is required if the --type is set to s.
--cache_size (required): Total cache size in bytes. The value must be a power of two.
--block_size (required): Block size in bytes. The value must be a power of two.
--memfile (required): Path to the input file containing memory addresses in hexadecimal format. Each address should be on a separate line.
