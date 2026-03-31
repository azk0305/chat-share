# import glob
import os

import ripgrep_rs
from fastmcp import FastMCP

mcp = FastMCP("chat-share")
MARKDOWN_FILES = "md_files/lifelogs"


# @mcp.tool
# def greet(name: str) -> str:
#     return f"Hello, {name}!"


# @mcp.tool
# def search_mdfiles(keyword: str) -> list:
#     """Search for keyword in MD files and return list of full paths of matching files."""
#     md_files = glob.glob(os.path.join(MARKDOWN_FILES, "*.md"))
#     matching_files = []

#     for file_path in md_files:
#         try:
#             with open(file_path, "r", encoding="utf-8") as file:
#                 content = file.read()
#                 if keyword in content:
#                     matching_files.append(os.path.abspath(file_path))
#         except Exception as e:
#             print(f"Error reading file {file_path}: {e}")

#     return matching_files


@mcp.tool
def search_mdfiles(keyword: str) -> list:
    """Ripgrep search for keyword in MD files and return list of full paths of matching files."""
    result = ripgrep_rs.search(
        patterns=[keyword],
        paths=[MARKDOWN_FILES],
        globs=["*.md"],
        line_number=False,
        multiline=True,
        case_sensitive=False,
        smart_case=False,
    )

    result_array = []
    for item in result:
        result_array.append(item.split(":")[0])

    return result_array


@mcp.tool
def read_mdfile(file_path: str) -> str:
    """Read the content of a specified file."""
    try:
        # Security check to ensure the file is within the allowed directory
        abs_file_path = os.path.abspath(MARKDOWN_FILES + "/" + file_path)
        abs_mdfiles_dir = os.path.abspath(MARKDOWN_FILES)

        if not abs_file_path.startswith(abs_mdfiles_dir):
            return (
                "Error: Access to files outside the lifelogs directory is not allowed."
            )

        with open(abs_file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: File '{abs_file_path}' not found."
    except Exception as e:
        return f"Error reading file '{file_path}': {str(e)}"


if __name__ == "__main__":
    mcp.run()
