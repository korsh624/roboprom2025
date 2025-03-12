import socket
import time

def udp_server(host='192.168.100.167', port=8888):
    # Создаем UDP сокет
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        # Привязываем сокет к адресу и порту
        sock.bind((host, port))
        print(f"Сервер запущен и слушает на {host}:{port}")

        while True:
            # Ожидаем получение данных
            data, addr = sock.recvfrom(1024)  # Буфер размером 1024 байта
            print(f"Получено сообщение от {addr}: {data.decode()}")
            #p:х:y:z:v#
            message=data.decode()
            if message[1]=="p":
                message=message[3:-1]
                message=message.split(':')
                print(f'Moving manipulator to point x={message[0]}, y={message[1]},z={message[2]}')
                time.sleep(5)
                # Отправляем обратно сообщение "Done"
                sock.sendto(b"done", addr)

if __name__ == "__main__":
    udp_server()