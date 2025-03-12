import socket
kvu=('192.168.100.223',8888)
knu=('192.168.100.49',8888)
kmr=('192.168.100.167',8888)
points=['#p:200:0:200:1#',
        '#p:200:100:200:1#',
        '#p:100:100:200:1#',
        '#p:100:0:200:1#' ]
pointer=0

def udp_server(host='192.168.100.223', port=8888):
    global pointer
    # Создаем UDP сокет
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        # Привязываем сокет к адресу и порту
        sock.bind((host, port))
        print(f"Сервер запущен и слушает на {host}:{port}")
        sock.sendto(b"whating", knu)
        while True:
            # Ожидаем получение данных
            data, addr = sock.recvfrom(1024)  # Буфер размером 1024 байта
            #print(f"Получено сообщение от {addr}: {data.decode()}")
            message=data.decode()
            print(message)
            if addr==knu and '1' in message:
                response=points[pointer]
                print(response)
                sock.sendto(b'worck', knu)
                sock.sendto(response.encode(), kmr)
                pointer+=1
                message=''
                print(pointer)
                if pointer>len(points)-1:
                    pointer=0
                    sock.sendto(b'whating', knu)

            if message=='done':
                message=''
                if pointer==0:
                    sock.sendto(b'whating', knu)
                else:
                    sock.sendto(b'done', knu)
                

if __name__ == "__main__":
    udp_server()