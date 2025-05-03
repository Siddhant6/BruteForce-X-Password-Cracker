 💣 BruteForce-X – Python Password Cracking Tool

**BruteForce-X** is a Python-based password cracking utility that uses brute-force logic to guess a given password by generating every possible character combination. It showcases the weaknesses of short or simple passwords and emphasizes the importance of password complexity and length.

---

   📌 Features

- 🔁 Brute-force every password up to 10 characters
- ⌛ Measures time taken to crack the password
- 🔤 Uses all lowercase characters (a-z)
- 🖥️ Real-time feedback: shows each attempt in terminal
- 📈 Teaches password entropy concepts via code

---

   🛠️ Tech Stack & Tools

| Technology | Purpose                          |
|------------|----------------------------------|
| Python 3   | Core programming language        |
| `itertools` | Generating all combinations     |
| `string`   | Charset configuration            |
| `time`     | Measuring cracking performance   |

---

   📂 File Structure
   BruteForce-X-Password-Cracker/
├── Bruteforce-X.py # Brute-force script
├── README.md # Project documentation

---

   ▶️ How to Run

1. **Make sure Python 3 is installed**

2. Run the script:
     🪟 On Windows
Open CMD or PowerShell

Navigate to project folder:
cd path\to\BruteForce-X-Password-Cracker

Run it:
python3 bruteforce.py

🐧 On Linux
Open Terminal

Navigate to folder:
cd /path/to/BruteForce-X-Password-Cracker

Run it:
python3 bruteforce.py

You’ll see each attempt printed to the console. Time taken will be shown when the password is found.

4. Modify the target_password in the script to test your own examples

---

   Sample Output

Trying password: a
Trying password: b
...
Trying password: abc
Password cracked: abc
Time taken: 1.8329 seconds

---

