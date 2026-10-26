# Exam-Eligibility-Checker
# Smart Client-Server Application: Exam Eligibility Checker

A Python-based socket programming project developed for the **Computer Networks Lab** 

This application implements a custom TCP client-server architecture where a client gathers user inputs, transmits them to a central server, and receives an evaluated decision based on personalized rules.

---

## 📌 Project Overview

- **Task Assigned:**  Exam Eligibility Checker
- **Architecture:** Client-Server model using TCP Sockets (`socket.AF_INET`, `socket.SOCK_STREAM`)
- **Key Feature:** Strict separation of concerns — the client handles user input gathering and socket streaming, while all decision-making, evaluation, and personalization logic reside strictly on the server.

---

## ⚙️ How It Works

1. **Client Side:** 
   - Takes input for **Roll Number**, **Marks (%)**, and **Attendance (%)** from the user with input validation.
   - Formats the inputs into a delimited payload (`ROLL,MARKS,ATTENDANCE`).
   - Establishes a TCP connection to the server on host `127.0.0.1` and port `65432`.
   - Sends the payload and waits for the server's verdict.

2. **Server Side:**
   - Binds to the specified port and listens for incoming connections.
   - Parses the payload and extracts the last two digits of the roll number ($R$).
   - Dynamically applies personalized eligibility criteria based on $R$ (e.g., dynamic attendance thresholds).
   - Returns a detailed pass/fail response string back to the client.

---

## 🚀 How to Run

### Prerequisites
- Python 3.x installed on your system.

### Steps


1. **Start the Server:**
   Open a terminal window and run:
   ```bash
   python server.py
   ```

2. **Run the Client:**
   Open a **second** terminal window and run:
   ```bash
   python client.py
   ```

3. **Follow the Prompts:** Enter your roll number, marks percentage, and attendance percentage when prompted.

---

## 🧪 Test Cases & Results

| Test Case | Inputs (`Roll No`, `Marks`, `Attendance`) | Server Verdict | Result |
| :--- | :--- | :--- | :--- |
| **1. Eligible** | `BCS-23-042`, `78.5%`, `82.0%` | `[SERVER SUCCESS] Roll No BCS-23-042 is ELIGIBLE for the exam.` | PASSED ✅ |
| **2. Low Attendance** | `BCS-23-042`, `85.0%`, `60.0%` | `[SERVER REJECTED] Ineligible due to low attendance (60.0% < 75.0%).` | REJECTED ❌ |
| **3. Low Marks** | `BCS-23-042`, `42.0%`, `90.0%` | `[SERVER REJECTED] Ineligible due to low marks (42.0% < 50.0%).` | REJECTED ❌ |

---

## 🛠 Tech Stack

- **Language:** Python 3
- **Networking Library:** `socket` (Standard Library)
- **Protocol:** TCP/IP
