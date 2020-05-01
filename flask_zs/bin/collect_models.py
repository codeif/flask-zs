import argparse
import inspect
import sys

from werkzeug.utils import find_modules, import_string

from .. import BaseModel


def find_classes(modname, import_path):
    cls_names = []
    mod = import_string(modname)
    for cls_name, cls_ in inspect.getmembers(mod, inspect.isclass):
        if issubclass(cls_, BaseModel):
            cls_names.append(cls_name)
    import_line = (
        f'from {modname.replace(import_path, "")} import {", ".join(cls_names)}'
    )
    return import_line, cls_names


def stdout_result(import_path):
    all_imports = []
    all_names = []
    for modname in find_modules(import_path):
        import_line, cls_names = find_classes(modname, import_path)
        if not cls_names:
            continue
        all_imports.append(import_line)
        all_names.extend(cls_names)
        import_str = "\n".join(all_imports)

    all_str = "\n    ".join([f'"{x}",' for x in sorted(all_names)])

    sys.stdout.write(
        f"""{import_str}

__all__ = [
    {all_str}
]
"""
    )


def main():
    parser = argparse.ArgumentParser(description="Collect all models to single file.")
    parser.add_argument(
        "project_name", help="current project name(package name), eg. zsdemo"
    )
    parsed_args = parser.parse_args()
    import_path = f"{parsed_args.project_name}.models"
    stdout_result(import_path)
