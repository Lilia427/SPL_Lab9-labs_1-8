import os
import subprocess

def generate_docs(modules):
    """
    Generates HTML documentation for the provided modules using pydoc.
    
    Args:
        modules (list): A list of module paths to document.
    """
    for module in modules:
        print(f"Generating documentation for {module}...")
        subprocess.run(["pydoc", "-w", module], check=True)

if __name__ == "__main__":
    modules = [
        "runner",
        "shared_lib.logger",
        "shared_lib.file_manager",
        "shared_lib.data_parser",
        "shared_lib.input_validator",
        "shared_lib.ascii_art_generator",
    ]
    generate_docs(modules)
