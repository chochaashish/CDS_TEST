import sys
import subprocess


def main():
    try:
        subprocess.Popen([sys.executable, 'file_monitor.py'])
        subprocess.Popen([sys.executable, 'file_writer.py'])
    except Exception as e:
        return e


if __name__ == "__main__":
    main()
