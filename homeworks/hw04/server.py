import socket
import time

# настройки хоста и порта
host = 'localhost'
port = 9090
# список подключенных клиентов
clients = []

# создаем сокет
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))
quit = False
print("[ Server Started ]")
# создаем сокет

while not quit:
    try:
        # принимаем данные с клиентов: данные, адрес клиента
        data, address = sock.recvfrom(1024)

        # если клиент "новый", добавляем его в наш список
        if address not in clients:
            clients.append(address)
        # текущее время
        current_time = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())

        print("[" + address[0] + "]=[" + str(address[1]) + "]=[" + current_time + "]/", end="")
        print(data.decode("utf-8"))
        for client in clients:
            if address != client:
                sock.sendto(data, client)
    except Exception as ex:
        print(ex)
        print("\n[ Server Stopped ]")
        quit = True

sock.close()
