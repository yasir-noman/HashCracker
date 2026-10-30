# Hash Cracker

A powerful, multi-core Hash Cracker built in Python. It performs a brute-force attack for 8-digit numeric passwords and utilizes multiprocessing to significantly speed up the cracking process.

Features:
- Supports MD5, SHA1, SHA256: Cracks common cryptographic hashes.
- Multiprocessing: Uses all available CPU cores for maximum performance.
- Fast Execution: Utilizes optimized loops instead of heavy itertools.
- Clean CLI UI: Color-coded hacker-style terminal output.

Technologies Used:
- Python 3
- hashlib (For hash generation)
- multiprocessing (For parallel processing)

How to Install and Run:
1. Open terminal in the project folder.
2. Run the script: python cracker.py (No external libraries required)
3. Enter the target hash (e.g., 25d55ad283aa400af464c76d713c07ad).
4. Enter the hash type (e.g., md5).
5. Wait for the script to find the 8-digit numeric password.

Disclaimer:
This tool is for educational purposes only. Do not use it to crack passwords or hashes that you do not own.

Developed by YASIR ARAFAT NOMAN