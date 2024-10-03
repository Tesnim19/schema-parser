import yaml
import json
from collections import defaultdict

# Parse the YAML schema and generate nodes and edges
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
                    relationship = value.get('relationship', key)

                    # Add the relationship from source to target only (no reverse or extra modifications)
                    edges[source][target].append(relationship)

    return nodes, edges

# Create an adjacency list from nodes and edges
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
