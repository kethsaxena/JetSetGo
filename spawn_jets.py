import subprocess
import argparse

def start_instances(n: int):
    processes = []

    # Start N processes
    for i in range(n):
        p = subprocess.Popen(
            ["jetsetgo"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        processes.append((i + 1, p))

    # Collect outputs
    for idx, p in processes:
        out, err = p.communicate()
        print(f"Started JetSetGo instance {idx} with PID: {p.pid}")
        if out.strip():
            print(f"Identity: {out.strip()}")
        if err.strip():
            print(f"Error: {err.strip()}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Launch multiple JetSetGo instances")
    parser.add_argument("num_jets", type=int, help="Number of JetSetGo instances to start")
    args = parser.parse_args()

    start_instances(args.num_jets)
   
