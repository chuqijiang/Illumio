import csv

def read_lookup_table(filename):
    lookup = {}
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            port, proto, tag = row
            lookup[(port.strip(), proto.strip().lower())] = tag.strip()
    return lookup


def parse_flow_logs(filename, lookup):
    tag_counts = {}
    port_protocol_counts = {}

    with open(filename, mode='r') as file:
        for line in file:
            parts = line.strip().split()
            dst_port = parts[5]
            protocol = 'tcp' if parts[7] == '6' else 'udp'
            key = (dst_port, protocol)

            tag = lookup.get(key, 'Untagged')
            tag_counts[tag] = tag_counts.get(tag, 0) + 1

            port_proto_key = (dst_port, protocol)
            port_protocol_counts[port_proto_key] = port_protocol_counts.get(port_proto_key, 0) + 1

    return tag_counts, port_protocol_counts


def output_counts(tag_counts, port_protocol_counts):
    with open('tag_counts.csv', mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(['Tag', 'Count'])
        for tag, count in tag_counts.items():
            writer.writerow([tag, count])

    with open('port_protocol_counts.csv', mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(['Port', 'Protocol', 'Count'])
        for (port, proto), count in port_protocol_counts.items():
            writer.writerow([port, proto, count])


def main():
    lookup_table = read_lookup_table('lookup.csv')
    tag_counts, port_protocol_counts = parse_flow_logs('flow_logs.txt', lookup_table)
    output_counts(tag_counts, port_protocol_counts)
    print("Processing complete.")


if __name__ == '__main__':
    main()
