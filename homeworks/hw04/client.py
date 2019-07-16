import socket
import threading
import time

# Логические флаги, об отключении и подключении клиента
shutdown = False
join = False


def receiving(name, sock):
    """ Функция, для приема сообщений с сервера """
    while not shutdown:
        try:
            while True:
                # Получаем сообщения
                data, addr = sock.recvfrom(1024)
                # Обязательно декодируем сообщение
                print(data.decode("utf-8"))
                # Ждем 0.2 секунды, на всякий случай :)
                time.sleep(0.2)
        except:
            pass


server = ("http://vladislavlubomski.pythonanywhere.com", 9090)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('localhost', 0))

name = input("Name: ")

# отдельный поток для получения сообщений
rT = threading.Thread(target=receiving, args=("RecvThread", s))
rT.start()

while not shutdown:
    if not join:
        s.sendto(("[" + name + "] => join chat ").encode("utf-8"), server)
        join = True
    else:
        try:
            message = input()

            if message != "":
                # Обязательно кодируем сообщение
                # указываем само сообщение и кому его отправить
                s.sendto(("[" + name + "] :: " + message).encode("utf-8"), server)

            time.sleep(0.2)
        except Exception as ex:
            print(ex)
            s.sendto(("[" + name + "] <= left chat ").encode("utf-8"), server)
            shutdown = True

rT.join()
s.close()
