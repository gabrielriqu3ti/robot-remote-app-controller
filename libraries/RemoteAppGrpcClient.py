
import logging
import grpc
from guicomponent_pb2 import Component, ComponentEditor, GuiResponse
from guicomponent_pb2_grpc import RobotStub


class RemoteAppGrpcClient:

    def __init__(self):
        self.channel = None
        self.stub = None


    def connect(self, ip: str, port: int):
        if self.stub is not None:
            raise ValueError(f"Already connected to remote controlled app")

        print(f"Trying to connect to server {ip}:{port}")
        self.channel = grpc.insecure_channel(f"{ip}:{port}")
        self.stub = RobotStub(self.channel)
        print("Successfully connected")


    def disconnect(self):
        if self.stub is None:
            raise ValueError(f"Disconnected from remote controlled app")

        print(f"Trying to disconnect from server")
        self.channel.close()
        self.channel = None
        self.stub = None
        print("Successfully disconnected")


    def type_text(self, text_field_name: str, new_text: str) -> str:
        if self.stub is None:
            raise ValueError(f"Disconnected from remote controlled app")

        print(f"Trying to type '{new_text}'...")
        response = self.stub.setText(ComponentEditor(component=Component(name=text_field_name), text=new_text))
        if isinstance(response, GuiResponse):
            print(f"Received status {response.status} with message '{response.message}'")
            return response.message
        else:
            print(f"ERROR: response of type {type(response)}")
            return ""


    def click(self, button_name: str):
        if self.stub is None:
            raise ValueError(f"Disconnected from remote controlled app")

        print("Trying to click button...")
        response = self.stub.click(Component(name=button_name))
        if isinstance(response, GuiResponse):
            print(f"Received status {response.status} with message '{response.message}'")
        else:
            print(f"ERROR: response of type {type(response)}")


    def get_text(self, label_name: str) -> str:
        if self.stub is None:
            raise ValueError(f"Disconnected from remote controlled app")

        print("Trying to get label text...")
        response = self.stub.getText(Component(name=label_name))
        if isinstance(response, GuiResponse):
            print(f"Received status {response.status} with message '{response.message}'")
            return response.message
        else:
            print(f"ERROR: response of type {type(response)}")
            return ""



def main():
    print("Will try to control remote app...")
    robot = RemoteAppGrpcClient()
    try:
        robot.connect("localhost", 50051)

        new_text = "New text"
        text_field_name = '.'.join(("App", "JTextField", "inputText"))
        button_name = '.'.join(("App", "JButton", "copyText"))
        label_name = '.'.join(("App", "JLabel", "copiedText"))

        robot.type_text(new_text, text_field_name)
        robot.click(button_name)
        text = robot.get_text(label_name)

        assert text == new_text

        new_text = "New text again"

        robot.type_text(new_text, text_field_name)
        robot.click(button_name)
        text = robot.get_text(label_name)

        assert text == new_text
    finally:
        robot.disconnect()


if __name__ == "__main__":
    logging.basicConfig()
    main()
