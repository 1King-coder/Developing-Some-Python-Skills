import subprocess

output = subprocess.run(
    ['netsh', 'wlan', 'show', 'profile', 'Fibernet', 'key=clear'],
    capture_output=True).stdout.decode('ISO-8859-1')
print(output)
