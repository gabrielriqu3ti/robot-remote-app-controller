
import logging
import grpc
from guicomponent_pb2 import Component, ComponentEditor, GuiResponse
from guicomponent_pb2_grpc import RobotStub

def run():
    print("Will try to control remote app...")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = RobotStub(channel)
        new_text = "New text"

        type_text(stub, new_text)
        click(stub)
        text = get_text(stub)

        assert text == new_text

        new_text = "New text again"

        type_text(stub, new_text)
        click(stub)
        text = get_text(stub)

        assert text == new_text


def type_text(stub: RobotStub, new_text: str) -> str:
    print(f"Trying to type '{new_text}'...")
    text_field_name = '.'.join(("App", "JTextField", "inputText"))
    response = stub.setText(ComponentEditor(component=Component(name=text_field_name), text=new_text))
    if isinstance(response, GuiResponse):
        print(f"Received status {response.status} with message '{response.message}'")
        return response.message
    else:
        print(f"ERROR: response of type {type(response)}")
        return ""


def click(stub: RobotStub):
    print("Trying to click button...")
    button_name = '.'.join(("App", "JButton", "copyText"))
    response = stub.click(Component(name=button_name))
    if isinstance(response, GuiResponse):
        print(f"Received status {response.status} with message '{response.message}'")
    else:
        print(f"ERROR: response of type {type(response)}")


def get_text(stub: RobotStub) -> str:
    print("Trying to get label text...")
    label_name = '.'.join(("App", "JLabel", "copiedText"))
    response = stub.getText(Component(name=label_name))
    if isinstance(response, GuiResponse):
        print(f"Received status {response.status} with message '{response.message}'")
        return response.message
    else:
        print(f"ERROR: response of type {type(response)}")
        return ""


if __name__ == "__main__":
    logging.basicConfig()
    run()
