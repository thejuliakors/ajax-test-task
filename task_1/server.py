import asyncio
import random
import json


HOST = "127.0.0.1"
PORT = 8888


class Server:
    async def handle_echo(self, reader, writer):
        """
        Сервер:
        1) Ожидает любой входящий пакет и превращает его в ожидаемую репрезентацию
        2) Ожидает случайный таймаут от 1 до 5 секунд
        3) Реквесты принимаются и обрабатываются асинхронно.

        Parameters:
        reader -- (StreamReader)
        writer -- (StreamWriter)
        """
        REQ = await reader.read(100)
        RESP = self.translate_request(REQ)
        request_id = self.get_request_id(REQ)
        addr = writer.get_extra_info('peername')
        print(f"Received REQ with request_id = {request_id} from {addr}")

        timeout = random.randint(1, 5)
        print(f"Random timeout is {timeout} seconds\n")
        await asyncio.sleep(timeout)

        print(f"Send: {RESP}")
        writer.write(RESP)
        await writer.drain()

        print("Close the client socket\n")
        writer.close()

    @staticmethod
    def translate_request(REQ):
        """
        Translates request REQ to RESP representation

        Parameters:
        REQ -- request (bytes)

        Returns:
        RESP - response (bytes)
        """
        print(type(REQ))
        request_dict = json.loads(REQ.decode())
        request_id = request_dict["request_id"]
        request_data = request_dict["data"]
        request_entities = [rd for rd in request_data.split("%%") if rd]
        response_data = {}
        for request_entity in request_entities:
            request_parameters = request_entity.split('&&')
            response_data[request_parameters[0]] = {
                request_parameters[i]: request_parameters[i + 1] 
                for i in range(1, len(request_parameters) - 1, 2)
                if request_parameters[i + 1]
            }
        RESP = {
            "request_id": request_id,
            "data": response_data
        }
        return json.dumps(RESP).encode()

    @staticmethod
    def get_request_id(REQ):
        """
        Returns request_id in REQ

        Parameters:
        REQ -- request (bytes)

        Returns:
        request_id (str)
        """
        return json.loads(REQ.decode())["request_id"]


if __name__ == '__main__':
    server = Server()

    loop = asyncio.get_event_loop()
    coro = asyncio.start_server(server.handle_echo, HOST, PORT, loop=loop)
    server_ = loop.run_until_complete(coro)

    print(f"Serving on {server_.sockets[0].getsockname()}\n")
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server_.close()
        loop.run_until_complete(server_.wait_closed())
        loop.close()
