# Redis Python Integration

A plug-and-play Redis integration library for Python frameworks like FastAPI, designed to simplify caching, session management, and data operations.

## Features

- **Easy Integration**: Drop-in Redis support for FastAPI and other Python frameworks
- **Connection Pooling**: Efficient connection management for production environments
- **Type Safety**: Built with Python 3.7+ type hints for better IDE support
- **Async Support**: Compatible with async/await patterns in modern Python frameworks
- **Plug-and-Play**: Minimal configuration required to get started

# Prerequisites

- Python 3.7+
- Redis
- `uv` package manager
- `just` command runner (optional, for task automation)
## Installation

### 1. Install uv (if not already installed)

**macOS and Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Verify installation:**

```bash
uv --version
```

### 2. Clone and Setup

```bash
git clone https://github.com/Motssembillahmahin/redis-python-integration.git
cd redis-python-integration
```

### 3. Install Dependencies

```bash
uv pip install redis uvicorn fastapi alembic sqlmodel psycopg2-binary
```
or
```bash
uv sync
```

This command will automatically:
- Detect or download the appropriate Python version
- Create a virtual environment in `.venv`
- Install all project dependencies from `pyproject.toml`
- Generate/update the `uv.lock` lockfile

### 4. Activate Virtual Environment (Optional)

**Linux/macOS**
```bash
.venv\bin\activate
```
**Windows**
```bash
.venv\Scripts\activate
```

### 5. Configure Environment Variables

Create a `.env` file in your project root with the following variables:

```env
# Redis Connection
REDIS_HOST=localhost
REDIS_PORT=14921
REDIS_DB=DB
REDIS_PASSWORD=PASSWORD
REDIS_URL=URL

# Cache TTL Settings (in seconds)
CACHE_TTL=300              # Default cache: 5 minutes
PRODUCT_CACHE_TTL=3600     # Product cache: 1 hour
SESSION_TTL=86400          # Session: 24 hours
```
or
``` cp .env.example .env```

### 6. Run the Application

**Using just**
```bash
just run
```

The API will be available at `http://localhost:8000`


## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Code Style

This project uses:
- `just` for task automation
- Python 3.7+ type hints
- Black for code formatting

## Support

- **Issues**: [GitHub Issues](https://github.com/Motssembillahmahin/redis-python-integration/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Motssembillahmahin/redis-python-integration/discussions)

## Acknowledgments

- Built with [redis-py](https://github.com/redis/redis-py)
- Designed for [FastAPI](https://fastapi.tiangolo.com/)
- Inspired by modern Python development practices
