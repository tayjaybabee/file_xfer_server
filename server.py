import socket
import tqdm
import os


HOST ='0.0.0.0'
PORT = 5001
BUFFER_SIZE = 4096
SEP = '<SEP>'

sock = socket.socket()

sock.bind(((HOST, PORT))

sock.listen(5)  # 5 max connections

print(f"[*] Listening as {HOST}:{PORT}")

# accept incoming connections
client_socket, address = sock.accept()

# If we move on from here we've attained a successful connection

print(f"[*] {address} is connected.")


received = client_socket.recv(BUFFER_SIZE).decode()
fname, fsize = received.split(SEP)
fname = os.path.basename=(fname)
fsize  = int(fsiize)

# Receive the file
progress = tqdm.tqdm(range(fsize), f"Receiving {fname}", unit='B', unit_scale=True, unit_divisor=1024)

# Save the file
with open(fname, 'wb') as f:
    while True:

        # Grab 1024 bytes from the incoming socket.
        bytes_read = client_socket.recv(BUFFER_SIZE)

        if not bytes_read:

            # Received nothing
            # break happily
            break

          f.write(bytes_read)

          # Update status
          progress.update(len(bytes_read))

client_socket.close()
socket.close()
