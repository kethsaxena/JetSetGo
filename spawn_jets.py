import subprocess


if __name__ == "__main__":
    # Start two independent JetSetGo instances and capture their output
    p1 = subprocess.Popen(['jetsetgo'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    p2 = subprocess.Popen(['jetsetgo'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    out1, err1 = p1.communicate()
    out2, err2 = p2.communicate()

    print(f"Started JetSetGo instance 1 with PID: {p1.pid}")
    print(f"Identity: {out1.strip()}")
    print(f"Started JetSetGo instance 2 with PID: {p2.pid}")
    print(f"Identity: {out2.strip()}")
