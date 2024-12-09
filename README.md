# LLMinfer

LLMinfer is a VS Code extension that helps Python developers by automatically inferring variable types in Python code using LLM (Large Language Model) technology.

## Features

- **Whole File Type Inference**: Analyze all variables in a Python file and show their inferred types
- **Single Variable Type Inference**: Right-click on any variable to see its inferred type
- **Type Caching**: Results are cached to provide instant type information for previously analyzed variables
- **JSON Output**: Type inference results are displayed in a clean JSON format

![Type Inference Demo](images/demo.gif)

## Requirements

- Python 3.x installed and available in PATH
- Ollama installed with llama3.1 model
- VS Code 1.95.0 or higher

## Installation

1. Install Python if you haven't already
2. Install Ollama following instructions at [Ollama's official site](https://ollama.ai)
3. Pull the llama3.1 model:
   ```bash
   ollama pull llama3.1
   ```
4. Install this extension from VS Code Marketplace

## Usage

### Analyze Whole File
1. Open a Python file
2. Click the class icon in the editor title bar, or
3. Open Command Palette (Ctrl+Shift+P) and run "TypeInfer: Infer Python Types"

### Analyze Single Variable
1. Select a variable in your Python code
2. Right-click and choose "Infer Variable Type" from the context menu

## Extension Settings

Currently, this extension doesn't require any additional settings.

## Known Issues

- The extension requires an active internet connection for LLM inference
- Initial type inference might take a few seconds depending on file size
- Only Python files are supported at the moment

## Release Notes

### 0.0.1

Initial release of TypeInfer:
- Basic type inference for Python files
- Variable-specific type inference
- Type caching
- JSON output format

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This extension is licensed under the [MIT License](LICENSE).

---

## More Information

- [Source Code](https://github.com/yourusername/typeinfer)
- [Issue Tracker](https://github.com/yourusername/typeinfer/issues)

**Enjoy coding with TypeInfer!**
