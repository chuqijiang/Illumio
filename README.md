# FlowTagger - Network Flow Analysis Tool

## Overview

`FlowTagger` is a Python tool for analyzing network flow logs, tagging traffic based on port-protocol combinations using a lookup table, and providing insights into traffic patterns.

## Files

- `flow_logs.txt`: Network flow logs with fields such as `id`, `source_ip`, `dest_ip`, `source_port`, `dest_port`, `protocol`, `packets`, `bytes`, `start_time`, `end_time`, `action`, and `status`.
- `lookup.csv`: Lookup table for mapping `port` and `protocol` to `service_name`.
- `tag_counts.csv`: Tracks counts of specific network tags.
- `port_protocol_counts.csv`: Lists occurrences of port/protocol combinations.
- `FlowTagger.py`: Main script for tagging and analyzing flows.

