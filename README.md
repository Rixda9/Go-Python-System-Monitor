# System Monitor Microservices

A lightweight system monitoring solution built with a Go backend worker and Python FastAPI frontend, demonstrating microservices architecture and real-time system metrics collection.

## Architecture

- **Go Worker** (`main.go`): Collects real-time CPU, memory, and platform statistics using `gopsutil`
- **Python API** (`main.py`): FastAPI service that aggregates and serves formatted statistics

## Features

- Real-time CPU usage monitoring (total + per-core)
- Memory usage statistics
- Platform information (OS, version, family)
- RESTful JSON API
- Microservices architecture with service separation

## Prerequisites

- Go 1.21+
- Python 3.9+
- `pip` and `go mod`

## Installation

### Go Worker
```bash
cd go-worker
go mod download
go run main.go
```

### Python API

```bash
cd python-api
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

## API Endpoints

### Python API (Port 8000)

- `GET /` - Health check
- `GET /stats` - Formatted system statistics

### Go Worker (Port 9000)

- `GET /` - Service info
- `GET /rawstats` - Raw system metrics

## Example Response

```json
{
  "os": "linux",
  "cpu_percent": [45.2],
  "core_cpu_percents": [42.1, 48.3, 44.7, 46.0],
  "ram_percent": 67.8
}
```

## Tech Stack

- **Go**: System metrics collection, HTTP server
- **Python**: FastAPI, Pydantic validation
- **Libraries**: gopsutil, requests

## Use Cases

- Learning microservices patterns
- System monitoring dashboards
- Resource usage tracking
- DevOps tool integration

## Future Enhancements

- [ ] Add Docker containerization
- [ ] Implement WebSocket for real-time updates
- [ ] Add disk I/O statistics
- [ ] Create a web dashboard frontend
- [ ] Add authentication
- [ ] Implement metrics history/logging

