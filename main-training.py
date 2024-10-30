#!/usr/bin/env python3
# main_training.py

import os
import importlib.util

def run_member_scripts():
    members_dir = 'members'

    for filename in os.listdir(members_dir):
        if filename.endswith('.py'):
            file_path = os.path.join(members_dir, filename)
            module_name = filename[:-3]

            spec = importlib.util.spec_from_file_location(module_name, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            print("\n" + "-" * 30)

# Run all member scripts
if __name__ == "__main__":
    run_member_scripts()
