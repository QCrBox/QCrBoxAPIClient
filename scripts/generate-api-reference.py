import os

api_dir = "qcrboxapiclient/api"
output_dir = "docs/source/api"
os.makedirs(output_dir, exist_ok=True)

index_lines = ["API Reference", "=============", "", ".. toctree::", "   :maxdepth: 2", ""]

for root, _, files in os.walk(api_dir):
    for f in files:
        if f.endswith(".py") and f != "__init__.py":
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, api_dir)
            module_path = f"qcrboxapiclient.api.{rel_path[:-3].replace(os.sep, '.')}"
            rst_path = os.path.join(output_dir, rel_path[:-3] + ".rst")

            os.makedirs(os.path.dirname(rst_path), exist_ok=True)
            with open(rst_path, "w") as rst:
                rst.write(f"{module_path}\n{'=' * len(module_path)}\n\n")
                rst.write(f".. automodule:: {module_path}\n")
                rst.write("   :members:\n   :undoc-members:\n   :show-inheritance:\n")

            index_lines.append(f"   {rel_path[:-3]}")

# Write the index
with open(os.path.join(output_dir, "api_reference.rst"), "w") as index_file:
    index_file.write("\n".join(index_lines))
