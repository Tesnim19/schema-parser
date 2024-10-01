# YAML Schema Processor

## Overview

This repository contains a Python script designed to process YAML schemas. The script parses a given schema, extracts nodes and edges based on defined relationships, and generates an adjacency list. The output is stored in a JSON file for further analysis or integration into other systems.

## Features

- Parses YAML schemas to identify nodes and relationships (edges) between them.
- Generates an adjacency list from the schema.
- Saves the adjacency list in a JSON format for easy access and usage.
- Processes the schema from the same directory as the script for simplicity during the initial trial.

## Files

- `schema_parser.py`: The main Python script that processes the YAML schema and generates the adjacency list.
- `adjacency_list.json`: The JSON output generated from the YAML schema, containing the adjacency list.
- `schema_config.yaml`: Example YAML file containing the schema that the script processes.

## How It Works

1. The script reads a YAML schema file (`schema_config.yaml`).
2. It identifies:
   - **Nodes**: Entities such as `gene`, `snp`, `pathway`, etc., represented as `"node"`.
   - **Edges**: Relationships between the nodes, represented as `"edge"`, with defined `source` and `target`.
3. The script creates an adjacency list, where:
   - Each node is a key.
   - The value of each key is a dictionary of other connected nodes and their relationship types (edges).
4. The resulting adjacency list is saved in a JSON file (`adjacency_list.json`).

## Usage

### Prerequisites

Ensure you have Python installed on your system. You also need the `PyYAML` library.

To install the required libraries, run the following command:

```bash
pip install pyyaml
```

## Running the Script

### Clone this repository:

```bash
git clone <repository-url>
```

### Navigate to the project directory and install:
```bash
cd schema-parser
pip install -r requirements.txt
```

Place the YAML schema you want to process in the same directory as schema_parser.py. By default, the script reads schema_config.yaml.

### Run script:
```bash
python schema_parser.py
```

The adjacency list will be saved as adjacency_list.json in the same directory.

