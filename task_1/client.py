import asyncio
import json


# some request examples
REQ_1 = {
    "request_id": "01",
    "data": "Hub&&name&&qwe&&id&&123&&%%Device&&name&&wqe&&id&&234&&"
}

REQ_2 = {
    "request_id": "02",
    "data": "Hub&&name&&qwerty&&id&&&&%%Device&&name&&wqefv&&id&&214&&"
}


class Client:
    def __init__(self, loop, host, port):
        self.loop = loop
        self.host = host
        self.port = port

    async def tcp_echo_client(self, REQ):
        """
        Клиент:
        1) Шлёт реквест
        2) Ожидает респонс от сервера

        Parameters:
        REQ -- request (dict)
        """
        reader, writer = await asyncio.open_connection(self.host, self.port, loop=self.loop)

        print(f'Send: {REQ}\n')
        writer.write(self.convert_request(REQ))

        response = await reader.read(100)
        print(f"Received: {self.convert_response(response)}")

        print("Close the socket\n")
        writer.close()

    @staticmethod
    def convert_request(REQ):
        """
        Converts REQ into encoded JSON order to send it ot hte server

        Parameters:
        REQ -- request (dict)

        Returns:
        REQ (bytes)
        """
        return json.dumps(REQ).encode()

    @staticmethod
    def convert_response(RESP):
        """
        Decodes response RESP from server

        Parameters:
        RESP -- response (bytes)

        Returns:
        RESP in JSON (str)
        """
        return RESP.decode()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    client = Client(loop, "127.0.0.1", 8888)

    try:
        asyncio.ensure_future(client.tcp_echo_client(REQ_1))
        asyncio.ensure_future(client.tcp_echo_client(REQ_2))
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()
        print('Loop closed')
