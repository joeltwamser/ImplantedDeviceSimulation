import grpc
import connect_pb2
import connect_pb2_grpc
import matplotlib.pyplot as plt

#I initially did this (made a generic function that took a string input) instead of
#having 2 different functions "TextChangePhase" and "TextChangeFrequency" because
#they were so similar, but there must be a better way to do it than this.
def TextChangeCosineFunction(prompt):
    while True:
        try:
            user_input = float(input("Enter new desired " + prompt + ": "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    return user_input

def PlotData(graph_samples_object):
    x_array = []
    y_array = []
    for point in graph_samples_object:
        x_array.append(point.x)
        y_array.append(point.y)
    #tune this plot
    plt.plot(x_array,y_array)
    plt.show()

#reorganize this code more elegantly
if __name__ == '__main__':
    with grpc.insecure_channel('localhost:5146') as channel:
        stub = connect_pb2_grpc.ConnectionStub(channel)
        graph_samples = (stub.Initialization(connect_pb2.Initialize(init_message='BeginInit'))).samples
        PlotData(graph_samples)

        #This is very primitive I know, but I'm simply out of time to implement a UI using something
        #like PySimpleGUI, though that is of course but one of many options.
        while True:
            print("To change FREQUENCY, press 1")
            print("To change PHASE, press 2")
            print("To exit, press 0")
            user_input = input("Enter input: ")
            if user_input == "0":
                break
            elif user_input == "1":
                new_freq = TextChangeCosineFunction("Frequency")
                graph_samples = (stub.FrequencyChange(connect_pb2.Frequency(cycles_per_second=new_freq))).samples
                PlotData(graph_samples)
            elif user_input == "2":
                new_phase = TextChangeCosineFunction("Phase")
                graph_samples = (stub.PhaseChange(connect_pb2.Phase(number=new_phase))).samples
                PlotData(graph_samples)
            else:
                print("Invalid Input")