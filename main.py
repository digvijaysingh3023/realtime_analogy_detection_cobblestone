
from ewma_detector import EWMAAnomalyDetector

from data_stream import DataStreamSimulator

from real_time_plotter import RealTimePlotter

def main():
    # Main function to run the real-time data stream visualization with anomaly detection.
    try:
        stream_simulator = DataStreamSimulator()

        # Alpha and threshold can be adjusted from here
        ewma_detector = EWMAAnomalyDetector(alpha=0.1, threshold=3)

        plotter = RealTimePlotter(detector=ewma_detector, stream=stream_simulator)

        # Start the real-time plot
        plotter.start_animation()

    except KeyboardInterrupt:

        print("Execution interrupted.")


    except Exception as e:

        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()