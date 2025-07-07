
# bb84_gui_app.py

import random
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# BB84 Functions

def generate_bits(n):
    return [random.randint(0, 1) for _ in range(n)]

def generate_bases(n):
    return [random.choice(['+', 'x']) for _ in range(n)]

def encode_qubits(bits, bases):
    qubits = []
    for bit, basis in zip(bits, bases):
        if basis == '+':
            qubits.append('|' if bit == 0 else '—')
        else:
            qubits.append('\'' if bit == 0 else '/')
    return qubits

def eve_intercept(qubits, eve_bases):
    eve_measured = []
    for photon, e_basis in zip(qubits, eve_bases):
        if e_basis == '+':
            eve_measured.append(0 if photon == '|' or photon == '—' else 1)
        else:
            eve_measured.append(0 if photon == '\'' or photon == '/' else 1)
    return eve_measured

def resend_qubits(eve_bits, eve_bases):
    return encode_qubits(eve_bits, eve_bases)

def measure_qubits(qubits, bob_bases):
    measured = []
    for photon, basis in zip(qubits, bob_bases):
        if basis == '+':
            measured.append(0 if photon == '|' else 1)
        else:
            measured.append(0 if photon == '\'' else 1)
    return measured

def extract_key(alice_bits, bob_bits, alice_bases, bob_bases):
    key = []
    errors = 0
    count = 0
    for a_bit, b_bit, a_basis, b_basis in zip(alice_bits, bob_bits, alice_bases, bob_bases):
        if a_basis == b_basis:
            key.append(b_bit)
            if a_bit != b_bit:
                errors += 1
            count += 1
    error_rate = (errors / count * 100) if count != 0 else 0
    return key, round(error_rate, 2), count

def text_to_bits(text):
    return [int(bit) for b in bytearray(text, 'utf-8') for bit in format(b, '08b')]

def bits_to_text(bits):
    chars = [chr(int(''.join(map(str, bits[i:i+8])), 2)) for i in range(0, len(bits), 8)]
    return ''.join(chars)

def xor_encrypt_decrypt(bits, key):
    key = key * (len(bits) // len(key)) + key[:len(bits) % len(key)]
    return [b ^ k for b, k in zip(bits, key)]

# GUI Functions

def run_simulation():
    message = message_entry.get()
    if not message:
        messagebox.showerror("Error", "Please enter a message.")
        return

    n = 100
    alice_bits = generate_bits(n)
    alice_bases = generate_bases(n)
    qubits = encode_qubits(alice_bits, alice_bases)

    eve_bases = generate_bases(n)
    eve_bits = eve_intercept(qubits, eve_bases)
    intercepted_qubits = resend_qubits(eve_bits, eve_bases)

    bob_bases = generate_bases(n)
    bob_bits = measure_qubits(intercepted_qubits, bob_bases)

    final_key, error_rate, key_length = extract_key(alice_bits, bob_bits, alice_bases, bob_bases)

    msg_bits = text_to_bits(message)
    cipher_bits = xor_encrypt_decrypt(msg_bits, final_key)
    decrypted_bits = xor_encrypt_decrypt(cipher_bits, final_key)
    decrypted_message = bits_to_text(decrypted_bits)

    result_text.set(f"Error Rate: {error_rate}%\nKey Length: {key_length}\nDecrypted Message: {decrypted_message}")
    plot_summary(error_rate, key_length)

def plot_summary(error_rate, key_length):
    labels = ['Error Rate (%)', 'Shared Key Length']
    values = [error_rate, key_length]
    colors = ['red' if error_rate > 20 else 'green', 'blue']

    plt.figure(figsize=(6, 4))
    plt.bar(labels, values, color=colors)
    plt.title('Quantum Key Distribution Summary')
    plt.ylabel('Value')
    plt.ylim(0, max(100, key_length + 10))
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

# GUI Setup

root = tk.Tk()
root.title("Quantum Key Encryption - BB84 Simulation")
root.geometry("450x300")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

message_label = tk.Label(frame, text="Enter Message:")
message_label.grid(row=0, column=0, sticky="w")

message_entry = tk.Entry(frame, width=40)
message_entry.grid(row=0, column=1)

run_button = tk.Button(frame, text="Encrypt using BB84 Key", command=run_simulation)
run_button.grid(row=1, columnspan=2, pady=10)

result_text = tk.StringVar()
result_label = tk.Label(frame, textvariable=result_text, justify="left", fg="blue")
result_label.grid(row=2, columnspan=2)

root.mainloop()
