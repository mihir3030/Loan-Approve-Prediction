import os
from pathlib import Path
import yaml
from LoanApproval import log
import json


def read_yam_file(path_to_yaml: Path):
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            log.info(f"yaml file {path_to_yaml} load  successfully")
            return content
    except Exception as e:
        raise e
    
def create_directories(path_to_directories: list, verbose=True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            log.info(f"created directory at {path}")


def save_reports(report: dict, report_path: str, indentation=4):
    with open(report_path, "w") as f:
        json.dump(report, f, indent=indentation)
    log.info("reports are saved")