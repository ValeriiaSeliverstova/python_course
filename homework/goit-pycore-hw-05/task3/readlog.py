#Description: The script is used to read a log file and display the number of lines for each logging level.
from pathlib import Path # Import the Path class from the pathlib module.
from datetime import datetime # Import the datetime class from the datetime module.

def load_logs(path):
    """
    This function reads a log file and yields each line as a dictionary.
    """
    log_lines = []
    file_path = Path(path)
    if  file_path.exists():
        with open(path, "r", encoding = "utf-8") as file:
            for line in file:
                # Split the line into date, time, level, and message using "parse_log_line" function.
                adjusted_line = parse_log_line(line)
                log_lines.append(adjusted_line)
                yield adjusted_line
    else:
        print("File does not exist")
    return log_lines

def parse_log_line(line: str) -> dict:
    """
    This function parses a log line and returns a dictionary with date, time, level, and message.
    """
    parsed_line = line.strip()
    date, time, level, message = parsed_line.split(" ", 3)
    return {"date": date, "time": time, "level": level, "message": message}

def filter_logs_by_level(log_lines: list) -> list:
    """
    This function filters log lines by level and returns a list of lines for each level.
    """
    INFO_list = []
    DEBUG_list = []
    WARNING_list = []
    ERROR_list = []
    for line in log_lines:
        if line["level"] == "INFO":
            INFO_list.append(line)
        elif line["level"] == "DEBUG":
            DEBUG_list.append(line)
        elif line["level"] == "WARNING":
            WARNING_list.append(line)
        elif line["level"] == "ERROR":
            ERROR_list.append(line)
    return INFO_list, DEBUG_list, WARNING_list, ERROR_list

def count_logs_by_level(INFO_list: list, DEBUG_list: list, WARNING_list: list, ERROR_list: list) -> dict:
    """
    This function counts the number of lines for each logging level and returns a dictionary.
    """
    counted_logs = {
        "INFO": len(INFO_list),
        "DEBUG": len(DEBUG_list),
        "WARNING": len(WARNING_list),
        "ERROR": len(ERROR_list)
    }
    return counted_logs

def display_log_counts(counted_logs: dict):
    """
    This function displays the number of lines for each logging level.
    """
    print("Logging level | Number of lines")
    print("_____________ | _______________")
    for level, count in counted_logs.items():
        print(f"{level:<13} | {count:<15}")

def main():
    """
    The main function of the log reader script. Calls all the function in the correct order.
    """
    path = Path('log.txt')
    log_list = load_logs(path)
    filtered_log_list = filter_logs_by_level(log_list)
    result = count_logs_by_level(*filtered_log_list)
    display_log_counts(result)
        
if __name__ == "__main__":
    main()