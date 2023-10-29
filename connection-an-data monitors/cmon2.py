import time
from blessings import Terminal
from psutil import net_io_counters
from asciichartpy import plot

def main():
    term = Terminal()
    last_stats = net_io_counters(pernic=False)

    data = {'incoming': [], 'outgoing': []}
    max_data_points = 50  # Number of data points to keep for the graph
    graph_width = 60
    graph_height = 20

    while True:
        current_stats = net_io_counters(pernic=False)
        incoming_kb = (current_stats.bytes_recv - last_stats.bytes_recv) / 1024
        outgoing_kb = (current_stats.bytes_sent - last_stats.bytes_sent) / 1024

        data['incoming'].append(incoming_kb)
        data['outgoing'].append(outgoing_kb)

        if len(data['incoming']) > max_data_points:
            data['incoming'].pop(0)
            data['outgoing'].pop(0)

        incoming_plot = plot(data['incoming'], {'height': 5, 'width': 60, 'offset': 5, 'legend': 'Incoming', 'color': term.green})
        outgoing_plot = plot(data['outgoing'], {'height': 5, 'width': 60, 'offset': 5, 'legend': 'Outgoing', 'color': term.red})

        with term.fullscreen():
            term.clear()
            print(f"{term.bold('Network Traffic')}")
            print(f"Incoming: {incoming_kb:.2f} KB")
            print(f"Outgoing: {outgoing_kb:.2f} KB")

            print(f"{term.bold('Traffic Graph')}")
            print(incoming_plot)
            print(outgoing_plot)

        last_stats = current_stats
        time.sleep(1)

if name == "main":
    main()