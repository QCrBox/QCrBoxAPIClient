import os
import shutil


def generate_rst_files(module_base: str, source_dir: str, output_dir: str, index_content: list, no_index=False):
    for root, _, files in os.walk(source_dir):
        for f in files:
            if f.endswith(".py") and f != "__init__.py":
                full_path = os.path.join(root, f)
                rel_path = os.path.relpath(full_path, source_dir)
                module_path = f"{module_base}.{rel_path[:-3].replace(os.sep, '.')}"
                rst_path = os.path.join(output_dir, rel_path[:-3] + ".rst")

                os.makedirs(os.path.dirname(rst_path), exist_ok=True)
                with open(rst_path, "w") as rst:
                    rst.write(f"{module_path}\n{'=' * len(module_path)}\n\n")
                    rst.write(f".. automodule:: {module_path}\n")
                    rst.write("   :members:\n   :undoc-members:\n   :show-inheritance:\n")
                    if no_index:
                        rst.write("   :no-index:\n")

                index_content.append(f"   {rel_path[:-3]}")


# API Reference index
output_dir = "docs/source/api"
shutil.rmtree(output_dir)
os.makedirs(output_dir, exist_ok=True)
api_index = ["API Reference", "=============", "", ".. toctree::", "   :maxdepth: 2", ""]
generate_rst_files("qcrboxapiclient.api", "qcrboxapiclient/api", output_dir, api_index)
with open(os.path.join(output_dir, "api_reference.rst"), "w") as f:
    f.write("\n".join(api_index))

# Model Reference index
output_dir = "docs/source/models"
shutil.rmtree(output_dir)
os.makedirs(output_dir, exist_ok=True)
model_index = ["Model Reference", "===============", "", ".. toctree::", "   :maxdepth: 2", ""]
generate_rst_files("qcrboxapiclient.models", "qcrboxapiclient/models", output_dir, model_index, no_index=True)
with open(os.path.join(output_dir, "model_reference.rst"), "w") as f:
    f.write("\n".join(model_index))
