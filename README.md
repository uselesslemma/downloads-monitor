# Downloads Monitor

A Python package to monitor your downloads folder and remove duplicate files.

## Directory Structure

```tree
downloads-monitor/
├── monitor
│   ├── __init__.py
│   ├── monitor.py
│   └── config.py
├── setup.py
└── README.md
```

## Command-Line Installation

### Prerequisites

- Python 3.6 or higher
- `pip` (Python package installer)

### Instructions

1. Clone the repository (or download the source code).

```bash
git clone https://github.com/uselesslemma/downloads-monitor.git
```

2. Navigate to the main directory (containing `setup.py`).

```bash
cd downloads-monitor
```

3. Install the package.

```bash
pip install .
```

## Usage

To run the script, simply execute:

```bash
downloads-monitor
```

The script will announce which folder it's monitoring for downloads, which downloaded files have been detected, and what actions were taken (if any).

## Configuration

The configuration file is stored at `~/.downloads_monitor_config.json`. By default, it monitors the `~/Downloads` folder. You can modify this file to change the monitored directory.

```json
{
    "download_folder": "/path/to/your/download/folder"
}
```

## Automating the Script on Startup

### Windows

1. Navigate to the Startup folder by opening the Run menu and typing `shell:startup`.
2. Within the Startup folder, right-click and create a shortcut to the `downloads-monitor` command, which is typically installed in the `Scripts` directory of your Python environment. Common locations include:

- `C:\Users\<YourUsername>\AppData\Local\Programs\Python\Python39\Scripts`
- `C:\Python39\Scripts`

### Linux/MacOS

Add the following line to your `~/.bashrc` or `~/.bash_profile` to run the script on startup:

```bash
echo 'downloads-monitor &' >> ~/.bashrc
source ~/.bashrc
```

Alternatively, you can create a `systemd` service for more robust startup management on Linux.

## Contributing

Contributions are welcome! Please create a pull request with a clear description of your changes.

## License

This project is licensed under the MIT License.
