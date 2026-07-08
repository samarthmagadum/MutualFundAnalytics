"""
ETL Pipeline Script

Runs the complete ETL workflow for
Mutual Fund Analytics.
"""

import subprocess


def run_script(script_name):
    """
    Executes a Python script.
    """

    print(f"\nRunning {script_name}...")

    try:
        subprocess.run(
            ["python", script_name],
            check=True
        )

        print(f"{script_name} completed successfully.")

    except subprocess.CalledProcessError:
        print(f"Error while running {script_name}")


def main():

    print("=" * 50)
    print("Bluestock Mutual Fund ETL Pipeline")
    print("=" * 50)

    run_script("data_ingestion.py")

    run_script("clean_data.py")

    run_script("load_to_sqlite.py")

    # Optional
    # run_script("live_nav_fetch.py")

    print("\nETL Pipeline Completed Successfully")


if __name__ == "__main__":
    main()