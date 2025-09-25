import re

def check_iperf_log(log_file, threshold=900):
    throughput = None
    with open(log_file, 'r') as f:
        for line in f:
            # Case-insensitive search for Mbits/sec
            match = re.search(r'(\d+(?:\.\d+)?)\s*Mbits/sec', line, re.IGNORECASE)
            if match:
                throughput = float(match.group(1))

    if throughput is not None:
        print(f"Measured throughput: {throughput} Mbits/sec")
        if throughput >= threshold:
            print("PASS: Throughput meets requirement")
            return True
        else:
            print("FAIL: Throughput below requirement")
            return False
    else:
        print("No throughput result found in log")
        return False

# Example usage
if __name__ == "__main__":
    check_iperf_log("sample_iperf.log", threshold=900)
