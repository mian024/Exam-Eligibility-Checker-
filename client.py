import socket

def send_request(roll_no: str, marks: float, attendance: float, host='127.0.0.1', port=65432):
    """Connects to server, sends formatted input, and prints response."""
    payload = f"{roll_no},{marks},{attendance}"
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))
        print(f"\n[CLIENT] Sending data: '{payload}'")
        client_socket.sendall(payload.encode('utf-8'))
        
        response = client_socket.recv(1024).decode('utf-8')
        print(f"[SERVER RESPONSE]\n{response}\n")
    except ConnectionRefusedError:
        print("\n[CLIENT ERROR] Unable to connect. Make sure 'server.py' is running first.\n")
    finally:
        client_socket.close()

def main():
    print("=" * 45)
    print("      EXAM ELIGIBILITY CHECKER CLIENT      ")
    print("=" * 45)

    # 1. Take Roll Number input
    roll_no = input("Enter your Roll Number (e.g., BCS-23-042): ").strip()
    
    # 2. Take Marks input with validation
    while True:
        try:
            marks = float(input("Enter your Marks percentage (0 - 100): "))
            if 0 <= marks <= 100:
                break
            print("Invalid input. Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numerical value for marks.")

    # 3. Take Attendance input with validation
    while True:
        try:
            attendance = float(input("Enter your Attendance percentage (0 - 100): "))
            if 0 <= attendance <= 100:
                break
            print("Invalid input. Attendance must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numerical value for attendance.")

    # Send data to server
    send_request(roll_no, marks, attendance)

if __name__ == "__main__":
    main()
