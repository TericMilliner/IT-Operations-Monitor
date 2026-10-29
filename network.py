import socket 
import time
import psutil

def check_connection():
    """Check connectivity and measure TCP connection time."""
    host = "1.1.1.1"
    port = 443

    start = time.perf_counter()

    try: 
        with socket.create_connection(
            (host, port), timeout=3
        ):
            response_time = (
                time.perf_counter() - start
            ) * 1000
        return {
            "status": "Online",
            "response_time": round(response_time, 2)
        }
    except OSError:
        return {
            "status": "Offline",
            "response_time": None
        }


def network_traffic():
    """Get total network data sent and recieved."""
    traffic = psutil.net_io_counters()

    return {
        "sent_mb": round(
            traffic.bytes_sent / (1024 ** 2), 2
        ),
        "received_mb": round(
            traffic.bytes_recv / (1024 ** 2), 2
        )
    }

if __name__ == "__main__":
    print("NETWORK MONITOR")
    print(check_connection())
    print(network_traffic())
