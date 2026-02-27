# Chat Share

Chat Share is a Model Context Protocol (MCP) server that enables efficient searching and retrieval of conversation summaries stored in markdown format. It's designed to work with AI assistants like Claude Desktop to provide contextual information from past conversations.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Development](#development)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

- **Search Functionality**: Search through markdown files containing conversation summaries using keyword matching
- **Content Retrieval**: Read and retrieve the full content of specific chat summary files
- **MCP Integration**: Works seamlessly with Model Context Protocol compatible clients
- **Fast Search**: Utilizes ripgrep for high-performance text searching
- **Flexible Filtering**: Search specifically within markdown files in designated directories

## Installation

### Prerequisites

- Python 3.12 or higher
- [uv](https://github.com/astral-sh/uv) (recommended for dependency management)

### Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd chat-share
   ```

2. Install dependencies using uv:
   ```bash
   uv sync
   ```

   Alternatively, you can use pip:
   ```bash
   pip install -e .
   ```

## Usage

### Running the Server

To start the chat summary server:

```bash
python server.py
```

The server will run and listen for MCP requests through stdio transport.

### Integration with Claude Desktop

To use with Claude Desktop, you'll need to configure the MCP server in your Claude settings. Add the chat-share server as a configured tool in your Claude Desktop configuration.

### Available Tools

The server exposes two main tools:

1. **search_mdfiles**: Search for keywords in markdown files
   - Parameters: `keyword` (string)
   - Returns: List of file paths matching the keyword

2. **read_mdfile**: Read the content of a specific file
   - Parameters: `file_path` (string)
   - Returns: Content of the specified file

## Project Structure

```
chat-share/
├── main.py              # Main entry point
├── server.py            # MCP server implementation
├── pyproject.toml       # Project configuration and dependencies
├── uv.lock              # Dependency lock file
├── README.md            # This file
└── md_files/            # Directory containing conversation summaries
```

### Key Files

- `server.py`: Implements the MCP server with search and read tools
- `pyproject.toml`: Defines project metadata and dependencies
- `private-states/lifelogs/`: Contains the markdown files with conversation summaries

## Development

### Dependencies

The project uses the following key dependencies:

- [mcp](https://github.com/modelcontextprotocol/python-sdk): Model Context Protocol SDK for Python
- [ripgrep-rs](https://github.com/nathom/ripgrep-rs): Python bindings for ripgrep

### Adding New Features

1. Fork the repository
2. Create a new branch for your feature
3. Make your changes
4. Test your changes
5. Submit a pull request

### Testing

Currently, the project doesn't have formal tests. To test functionality:

1. Run the server locally
2. Use an MCP-compatible client to interact with the tools
3. Verify that search and read operations work as expected

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Thanks to the Model Context Protocol team for creating the specification
- Thanks to the ripgrep project for providing fast search capabilities
- Inspired by the need to maintain and retrieve context from AI-assisted conversations
-
