#!/usr/bin/env python3
# ======================================================
# CTF-Coach | Educational CTF Walkthrough Simulator
# Graduation Project - Single File Version
# ======================================================

import time
import sys
import re

# ---------- Utilities ----------
def slow_print(text, delay=0.015):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(delay)
    print()

def banner():
    print("=" * 60)
    print("🧠 CTF-Coach | Educational CTF Simulator")
    print("🎓 Graduation Project Edition")
    print("⚠️  Simulation Only | No Real Exploitation")
    print("=" * 60)
    print()

def detect_target_type(target):
    if target.startswith("http://") or target.startswith("https://"):
        return "LAB_URL"
    ip_regex = r"^\d{1,3}(\.\d{1,3}){3}$"
    if re.match(ip_regex, target):
        return "IP"
    return "UNKNOWN"

# ---------- Simulation Phases ----------
def phase_recon():
    slow_print("[Phase 1] Reconnaissance")
    slow_print("• Objective: Identify open ports and services")
    slow_print("• Tool: Nmap")
    slow_print("• Command:")
    slow_print("  nmap -sC -sV -A <TARGET>")
    slow_print("\n[Simulated Output]")
    slow_print("  22/tcp  open  ssh")
    slow_print("  80/tcp  open  http")
    slow_print("\n• Analysis: Web service detected → proceed with web enumeration.\n")
    time.sleep(0.8)

def phase_web_enum():
    slow_print("[Phase 2] Web Enumeration")
    slow_print("• Objective: Discover hidden directories and endpoints")
    slow_print("• Tool: Gobuster")
    slow_print("• Command:")
    slow_print("  gobuster dir -u http://<TARGET> -w /usr/share/wordlists/dirb/common.txt")
    slow_print("\n[Simulated Discovery]")
    slow_print("  /login")
    slow_print("  /admin")
    slow_print("  /uploads")
    slow_print("\n• Analysis: Login + Upload functionality → potential initial access.\n")
    time.sleep(0.8)

def phase_exploitation():
    slow_print("[Phase 3] Initial Access (Simulation)")
    slow_print("• Objective: Gain low-privilege shell")
    slow_print("• Technique: Authentication bypass")
    slow_print("• Payload Example:")
    slow_print("  ' OR 1=1 --")
    slow_print("\n[Simulated Result]")
    slow_print("  ✔ Authentication bypass successful")
    slow_print("  ✔ File upload abused to deploy PHP reverse shell")
    slow_print("  ✔ Shell obtained as user: www-data\n")
    time.sleep(0.8)

def phase_user_flag():
    slow_print("[Phase 4] User Flag (Simulated)")
    slow_print("• Objective: Locate user-level flag")
    slow_print("• Typical Location:")
    slow_print("  /home/user/user.txt")
    slow_print("\n[Simulated Flag]")
    slow_print("  CTF{user_flag_simulated}\n")
    time.sleep(0.8)

def phase_privesc():
    slow_print("[Phase 5] Privilege Escalation")
    slow_print("• Objective: Escalate privileges to root")
    slow_print("• Check sudo permissions")
    slow_print("• Command:")
    slow_print("  sudo -l")
    slow_print("\n[Simulated Finding]")
    slow_print("  User can run /usr/bin/python3 as root (NOPASSWD)")
    slow_print("\n• Exploitation:")
    slow_print("  sudo python3 -c 'import os; os.system(\"/bin/bash\")'\n")
    time.sleep(0.8)

def phase_root_flag():
    slow_print("[Phase 6] Root Flag (Simulated)")
    slow_print("• Objective: Confirm full system compromise")
    slow_print("• Typical Location:")
    slow_print("  /root/root.txt")
    slow_print("\n[Simulated Flag]")
    slow_print("  CTF{root_flag_simulated}\n")
    time.sleep(0.8)

def summary():
    slow_print("=" * 60)
    slow_print("✔ Reconnaissance completed")
    slow_print("✔ Initial access achieved")
    slow_print("✔ User flag identified")
    slow_print("✔ Privilege escalation successful")
    slow_print("✔ Root access achieved")
    slow_print("=" * 60)
    slow_print("🎉 Simulation Finished — Educational Walkthrough Complete")

# ---------- Main ----------
def main():
    banner()
    target = input("[+] Enter Target IP or Lab URL: ").strip()
    ttype = detect_target_type(target)

    if ttype == "UNKNOWN":
        slow_print("[-] Invalid input. Please enter a valid IP or Lab URL.")
        sys.exit(1)

    slow_print(f"\n[+] Target accepted ({ttype})")
    slow_print("[+] Starting educational CTF simulation...\n")
    time.sleep(0.8)

    phase_recon()
    phase_web_enum()
    phase_exploitation()
    phase_user_flag()
    phase_privesc()
    phase_root_flag()
    summary()

if __name__ == "__main__":
    main()
