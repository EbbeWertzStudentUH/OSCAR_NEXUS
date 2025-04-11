import argparse
import json
from pathlib import Path

from NexDBClient import NexDBClient
import pynng

def send_query(client: NexDBClient, query: str):
    resp_type, data = client.send_and_receive("query", {"query": query})
    if resp_type == "query_name_id_result":
        print("query was succesfully executed")
        print("data:")
        for i, (id, name) in enumerate(data.items()):
            print(f"{i:<3} | {id} | {name}")
    elif resp_type == "query_success":
        print("query was succesfully executed")
        print("[no data]")
    elif resp_type == "query_break_warning":
        print(f"query stopped early (but did not fail): {data}")
        print("[no data]")
    else:
        print(f"❌ {resp_type}: {data}")

def shell_mode(client: NexDBClient):
    print("🔁 Entering NexDB shell. Type your query over multiple lines. Submit with empty line.")
    lines = []
    while True:
        try:
            line = input("\033[32;1mNexQL > \033[0m")
            if line.strip() == "" and lines:
                full_query = "\n".join(lines)
                send_query(client, full_query)
                lines.clear()
            else:
                lines.append(line)
        except (KeyboardInterrupt, EOFError):
            print("\n👋 Exiting shell.")
            break

def handle_query(args, client: NexDBClient):
    if args.string:
        send_query(client, args.string)
    elif args.file:
        query = Path(args.file).read_text()
        send_query(client, query)
    elif args.shell:
        shell_mode(client)
    else:
        print("⚠️ Please provide --string, --file or --shell.")

def handle_ingest(args, client: NexDBClient):
    yaml_text = Path(args.file).read_text()
    resp_type, data = client.send_and_receive("ingest", {"yaml_import_model": yaml_text})
    if resp_type == "ingest_success":
        print("The batch was succesfully ingested")
    else:
        print(f"❌ {resp_type}: {data}")
        
def handle_shutdown(client: NexDBClient):
    resp_type, _ = client.send_and_receive("shutdown", {})
    if resp_type == "bye_bye":
        print("NexDB daemon is stopped")

def main(daemon_executable_path:str):
    parser = argparse.ArgumentParser(description="NexDB CLI")
    parser.add_argument("--socket", default="ipc:///tmp/oscar_nexus_nexdb_daemon", help="IPC socket path")
    parser.add_argument("--daemon", default=daemon_executable_path, help="Path to daemon executable")

    subparsers = parser.add_subparsers(dest="command")

    # Query subcommand
    query_parser = subparsers.add_parser("query", help="Run a query")
    query_group = query_parser.add_mutually_exclusive_group()
    query_group.add_argument("--string", type=str, help="Query string")
    query_group.add_argument("--file", type=str, help="Path to file with query script")
    query_group.add_argument("--shell", action="store_true", help="Enter interactive query shell")

    # Ingest subcommand
    ingest_parser = subparsers.add_parser("ingest", help="Ingest YAML model")
    ingest_parser.add_argument("--file", required=True, help="YAML import model path")
    
    subparsers.add_parser("shutdown", help="Stop the NexDB daemon")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    with pynng.Req0() as socket:
        client = NexDBClient(args.socket, args.daemon)
        if not client.connect():
            return
        client.start_engine_if_needed()

        if args.command == "query":
            handle_query(args, client)
        elif args.command == "ingest":
            handle_ingest(args, client)
        elif args.command == "shutdown":
            handle_shutdown(client)

        client.close()

if __name__ == "__main__":
    daemon_path = "C:\\Users\\ebbew\\Desktop\\OSCAR_NEXUS\\nexTK\\NexDB\\main_NexDB_Daemon.py"
    main(daemon_path)
