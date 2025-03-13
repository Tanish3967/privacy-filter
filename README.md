# Privacy Filter for Windows

This Python script creates a privacy filter effect on Windows, reducing visibility at the edges of the screen while keeping the center clear. When the mouse moves near the edges, a circular area is revealed to improve visibility.

## Features
- Darkens the edges of the screen while keeping the center visible.
- Clears a circular area around the cursor when near screen edges.
- Runs as an overlay without blocking mouse clicks on underlying applications.
- Press `Esc` to exit the application.

## Installation
### Prerequisites
- Ensure you have **Python 3.8+** installed on your system.
- Install the required dependencies using:

```sh
pip install -r requirements.txt
```

## Running the Privacy Filter
Run the script using the following command:

```sh
python privacy_filter.py
```

## Exiting the Application
To close the filter, press the `Esc` key.

## Troubleshooting
- If you encounter module import errors, ensure you have installed dependencies properly with `pip install -r requirements.txt`.
- The script is designed for **Windows**.
- Edit: Now also available for **macOS**

## License
This project is open-source under the MIT License.

## Contributions
Feel free to contribute by submitting pull requests or opening issues for feature suggestions or bug reports.
