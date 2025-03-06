import socket
points=['#p:200:0:200:1#',
        '#p:200:100:200:1#',
        '#p:100:100:200:1#',
        '#p:100:0:200:1#' ]
pointer=0

def udp_server(host='192.168.33.136', port=8888):
    global pointer
    # Создаем UDP сокет
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        # Привязываем сокет к адресу и порту
        sock.bind((host, port))
        print(f"Сервер запущен и слушает на {host}:{port}")
        sock.sendto(b"start", ('192.168.33.237',8888))
        while True:
            # Ожидаем получение данных
            data, addr = sock.recvfrom(1024)  # Буфер размером 1024 байта
            #print(f"Получено сообщение от {addr}: {data.decode()}")
            message=data.decode()
            if message=='done':
                response=points[pointer]
                sock.sendto(response.encode(), addr)
                pointer+=1
                message=''
                print(pointer)
                if pointer>len(points)-1:
                    break


if __name__ == "__main__":
    udp_server()