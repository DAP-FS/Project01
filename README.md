# Project01
Theory of Computation : Best Practices 

## Documentation

This project includes comprehensive Sphinx documentation covering theory of computation concepts and best practices.

### Building the Documentation

To build the documentation locally:

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Build the HTML documentation:
   ```bash
   cd docs
   make html
   ```

3. View the documentation:
   Open `docs/_build/html/index.html` in your web browser.

### Documentation Structure

- **Introduction**: Overview of theory of computation
- **Fundamentals**: Core mathematical concepts and definitions
- **Best Practices**: Recommended approaches and methodologies
- **Examples**: Practical examples and case studies
- **References**: Additional resources and bibliography

### Other Build Targets

- `make latexpdf` - Build PDF documentation
- `make clean` - Clean build files
- `make help` - Show all available build targets
