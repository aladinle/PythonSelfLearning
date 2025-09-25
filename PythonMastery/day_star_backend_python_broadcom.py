# Q1. Write a Python script to parse a build log file 
# and extract all error messages, 
# counting how many times each error type occurs.

def parse_log(file_path):
    summary = {"INFO": 0, "WARNING": 0, "ERROR": 0, "FAIL": 0}
    
    with open(file_path, "r") as f:
        for line in f:
            for key in summary.keys():
                if key in line:
                    summary[key] += 1
    
    # Determine build status
    if summary["ERROR"] > 0 or summary["FAIL"] > 0:
        status = "FAILED"
    else:
        status = "SUCCESS"
    
        # Print a clean summary
    print("===== Build Log Summary =====")
    print(f"INFO    : {summary['INFO']}")
    print(f"WARNING : {summary['WARNING']}")
    print(f"ERROR   : {summary['ERROR']}")
    print(f"FAIL    : {summary['FAIL']}")
    print("-----------------------------")
    print(f"STATUS  : {status}")
    print("=============================")

    return summary

def main():
    print("Parsing build log for errors...")
    print(parse_log("build.log"))

if __name__ == "__main__":
    main()
