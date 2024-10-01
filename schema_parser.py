import yaml
import json
from collections import defaultdict

def parse_yaml_schema(yaml_content):
    schema = yaml.safe_load(yaml_content)
    nodes = set()
    edges = defaultdict(lambda: defaultdict(list))

    for key, value in schema.items():
        if isinstance(value, dict) and 'represented_as' in value:
            if value['represented_as'] == 'node':
                nodes.add(key)
            elif value['represented_as'] == 'edge':
                if 'source' in value and 'target' in value:
                    source = value['source']
                    target = value['target']
                    edges[source][target].append(key)
                    # Add reverse relationship
                    edges[target][source].append(f"reverse_{key}")

    return nodes, edges

def create_adjacency_list(nodes, edges):
    adjacency_list = {node: dict(edges[node]) for node in nodes}
    return adjacency_list

# Read the YAML file
with open('schema_config.yaml', 'r') as file:
    yaml_content = file.read()

# Parse the YAML content
nodes, edges = parse_yaml_schema(yaml_content)

# Create the adjacency list
adj_list = create_adjacency_list(nodes, edges)

# Save the adjacency list to a file
with open('adjacency_list.json', 'w') as outfile:
    json.dump(adj_list, outfile, indent=2)


# Print the adjacency list

print(json.dumps(adj_list, indent=2))