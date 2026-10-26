import socket

def check_eligibility(roll_no: str, marks: float, attendance: float) -> str:
 
    try:
        r_val = int(roll_no.split("-")[-1])
    except (ValueError, IndexError):
        r_val = 0
    
    attendance_threshold = 70.0 if (r_val % 2 != 0) else 75.0
    
    if attendance >= attendance_threshold and marks >= 50.0:
        return f"[SERVER SUCCESS] Roll No {roll_no} is ELIGIBLE for the exam. (Required Attendance: {attendance_threshold}%)"
    elif attendance < attendance_threshold and marks < 50.0:
        return f"[SERVER REJECTED] Roll No {roll_no} is INELIGIBLE due to low attendance ({attendance}%) AND low marks ({marks}%)."
    elif attendance < attendance_threshold:
        return f"[SERVER REJECTED] Roll No {roll_no} is INELIGIBLE due to low attendance ({attendance}% < {attendance_threshold}%)."
    else:
        return f"[SERVER REJECTED] Roll No {roll_no} is INELIGIBLE due to low marks ({marks}% < 50%)."

def start_server(host='127.0.0.1', port=65432):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Allow socket address reuse
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"[*] Server listening on {host}:{port}...")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"[*] Accepted connection from {client_address}")

            try:
                data = client_socket.recv(1024).decode('utf-8')
                if not data:
                    print("[-] No data received. Closing connection.")
                    client_socket.close()
                    continue

                print(f"[+] Received payload from client: {data}")
                
              
                parts = data.strip().split(",")
                if len(parts) != 3:
                    response = "[SERVER ERROR] Invalid input format. Expected: ROLL_NUMBER,MARKS,ATTENDANCE"
                else:
                    roll_no = parts[0].strip()
                    marks = float(parts[1].strip())
                    attendance = float(parts[2].strip())
                    
                   
                    response = check_eligibility(roll_no, marks, attendance)

            except ValueError:
                response = "[SERVER ERROR] Invalid numeric values for marks or attendance."
            except Exception as e:
                response = f"[SERVER ERROR] Exception encountered: {str(e)}"

            client_socket.sendall(response.encode('utf-8'))
            client_socket.close()
            print("[-] Connection closed with client.\n")

    except KeyboardInterrupt:
        print("\n[*] Server shutting down gracefully.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()
