BB84 Quantum Key Distribution — GUI-Based Python Simulation

🔐 Project Overview

In a world where future quantum computers may break today's strongest encryptions, this project presents a defense-grade alternative:
BB84 Quantum Key Distribution Protocol, simulated entirely using pure Python and built-in libraries.

This app demonstrates how photons — the smallest particles of light — can be used to share encryption keys securely.
If an attacker tries to intercept the communication, the system detects it automatically using quantum error thresholds.


---

💡 Key Highlights

🧠 No quantum libraries used — Only core Python logic

🖥️ Fully functional GUI application using Tkinter

🔐 Supports real-time encryption and decryption of messages

⚠️ Eavesdropping detection using error-rate analysis

📊 Matplotlib graphs to show key metrics visually

🚫 No external dependencies — works on any basic Python setup



---

🛠 Technology Stack

Language: Python (pure)

GUI: Tkinter

Graph Plotting: Matplotlib

Encryption Logic: XOR-based using shared quantum key

Protocol Simulated: BB84



---

📊 How It Works (The Logic)

1. Alice generates random bits and random bases.


2. Bits are encoded as qubits (simulated photons).


3. Eve (optional attacker) tries to intercept the photons using random bases.


4. Intercepted photons are measured again by Bob.


5. Only matching-basis photons are kept → shared key generated.


6. Original message is encrypted using XOR with this key.


7. Error rate is calculated. If it exceeds 20%,
a message is shown: “Eavesdropping Detected!”



(Based on the real BB84 protocol where 25% is the theoretical threshold.)


---

🔬 Why This Matters (For DRDO/ISRO & Beyond)

Conventional encryption methods may become obsolete in quantum era.

India needs quantum-resilient communication systems.

This simulation provides a blueprint to develop future-grade secure channels.

Applicable for:

Secure satellite communication (ISRO use case)

Defense-level secure message exchange (DRDO use case)

Quantum network training and awareness




---

🧪 Features Breakdown

✔️ Quantum key generation (BB84 logic)
✔️ Message encryption using XOR
✔️ Message decryption with shared key
✔️ Error rate detection for spy attacks
✔️ Graphical stats with Matplotlib
✔️ Clean GUI built in Tkinter
✔️ No need for external libraries or simulators


---

🖼 Screenshots

📸 GUI View
📈 Error Rate & Key Length Chart
🔐 Encrypted + Decrypted Message Display

🧑‍💻 Author

Atharva Dubey
B.Tech Student — Shri G.S. Institute of Technology and Science (SGSITS), Indore
B.S. in Data Science — IIT Madras
🔭 Passionate about National Defense, Quantum Security & Cyber Warfare
🔗 LinkedIn


---

🇮🇳 Vision Behind This Project

This project is part of a broader goal:

> Building quantum-secure systems that can serve India's space, defense, and cyber infrastructure.



It is not just a simulation — it's a signal that the next generation of developers are ready to contribute to India’s quantum-secure future.


---

🔗 Connect, Collaborate, Contribute

This project is open for learning, innovation, and feedback — especially from organizations like DRDO, ISRO, SAC, and IN-SPACe.

If you're from a national agency or research org, feel free to connect — I'd love to contribute further to India’s secure tech initiatives.
