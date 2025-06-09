import json
import sys
from datetime import datetime
import base64
import binascii
from mdutils.mdutils import MdUtils


# Modified from: https://github.com/marksowell/caldera-report-generator

# Generate a simple markdown file for each report.

def is_base64(s):
    """
    Checks if a string is Base64 encoded.
    """
    try:
        base64.b64decode(s, validate=True)
        return True
    except binascii.Error:
        return False

def decode_base64(s):
    """
    Decodes a Base64 encoded string.
    """
    if is_base64(s):
        return base64.b64decode(s).decode('utf-8')
    else:
        return "The provided string is not Base64 encoded."

def hosts(data, markdown):
    # Iterate through host groups
    # Things get from here:
    # the C2 IP Node
    # the C2 5-tuples, with date range(?)
    # the beachhead PID/parent PID
    # Map of "paw" to hostname. paw is a Caldera unique host id and is used in other parts of the report.
    hostmap = {}
    hosts = ["Host","User","Beachhead Command","PID","Parent PID","IP","C2 Server"]
    num_hosts = 0
    markdown.new_header(level=1, title="Hosts Attacked")
    for host in data['host_group']:
        # There *should* only be 1 c2 server, so save values in a map and dump out after iterating over hosts.
        # Build a table of host info
        hosts.extend([host['host'],host['username'],host['exe_name'],host['pid'],host['ppid'],', '.join(host['host_ip_addrs']),host['server']])
        hostmap[host['paw']] = host['host']
        num_hosts += 1
    # Output the table now so its at the top.
    markdown.new_table(columns=7, rows=num_hosts+1, text=hosts)

    # Now iterate thru the links for each host.
    # Links executed
    markdown.new_header(level=1, title="Links")
    markdown.new_line("(what exactly is a link? seems to be a command executed when initializing the beachhead?)")
    for host in data['host_group']:
        links(host, hostmap, markdown)

    return hostmap

def links(host, hostmap, markdown):
    markdown.new_header(level=2, title=f"Host: {host['host']}")
    for link in host['links']:
        cmd=link['plaintext_command']
        if is_base64(cmd):
            cmd=decode_base64(cmd)
        markdown.new_paragraph(f"  Technique: {link['ability']['technique_name']}")
        markdown.new_paragraph(f"  PID: {link['pid']}")
        markdown.new_paragraph(f"  Status: {'Success' if link['status'] == 0 else 'Failed'}")
        markdown.new_paragraph(f"  Start: {link['collect']}")
        markdown.new_paragraph(f"  Finish: {link['finish']}")
        markdown.new_paragraph(f"  Command: \n```powershell\n{cmd}\n```")
        markdown.new_paragraph("")

def steps(data, hostmap, markdown):
    markdown.new_header(level=1, title="Steps")
    for host_key, host_steps in data.get("steps", {}).items():
        markdown.new_header(level=2, title=f"Host: {hostmap[host_key]} (paw: {host_key})")
        for step in host_steps.get("steps", []):
            cmd=step.get('plaintext_command')
            if is_base64(cmd):
                cmd=decode_base64(cmd)
            markdown.new_header(level=3, title=f"  Description: {step.get('description')}")
            markdown.new_paragraph(f"  Attack: {step.get('attack')}")
            markdown.new_paragraph(f"  Status: {'Success' if step.get('status') == 0 else 'Failed'}")
            markdown.new_paragraph(f"  PID: {step.get('pid')}")
            markdown.new_paragraph(f"  Start: {step.get('run')}")
            markdown.new_paragraph(f"  Command: \n```powershell\n{cmd}\n```")
            markdown.new_paragraph("")

def main():
    # Check if a file path is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python extract_ids_from_reports.py <path_to_json_file>")
        sys.exit(1)

    json_file_path = sys.argv[1]

    # Load JSON data from the provided file path
    try:
        with open(json_file_path, 'r') as file:
            data = json.load(file)
    except Exception as e:
        print(f"Failed to load JSON file: {e}")
        sys.exit(1)

    # Get the operation name, sanitize it, and convert to lowercase
    operation_name = data['name'].replace(' ', '_').replace('/', '_').replace('\\', '_').lower()

    # Create an Everest TKP file with the operation name and a formatted timestamp in the filename
    tkp = f"{operation_name}_caldera_report.tkp"
    markdown = MdUtils(file_name=f"reports/{operation_name}_caldera_report.md",title=data['name'])
    hostmap = hosts(data, markdown)
    steps(data, hostmap, markdown)
    markdown.new_table_of_contents(table_title='Contents', depth=3)
    markdown.create_md_file()


if __name__ == "__main__":
    main()




