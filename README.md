# Remote App Robot

This project consists of a robot that interacts with a GUI application using a gRPC service.
Its intended purpose is to automate GUI tests of a remote application.

## Set up environment

This application uses the conda environment to manage python dependencies. So, execute the following command to set up
the project's dependencies:

```[bash]
conda env create -f remote-app-robot.yml
```

## Execution

Run the GUI app to be tested and start its gRPC server on the port 50051. To communicate with it, the gRPC client shall implement the protobuff protos\guicomponent.proto.

The graphical user interface of the application should be displayed.

Execute the following command to run this application:

```[bash]
python -m robot tests
```

A robot should start to interact with the GUI of the application. At the end of the tests, a report and a log shall be saved. 
