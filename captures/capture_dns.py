import pyshark

def print_live_dns():
    capture = pyshark.LiveCapture("wlp0s20f3", bpf_filter="udp port 53", display_filter="dns")

    for packet in capture:
        # print(packet)
        if "DNS" in packet and not packet.dns.flags_response.int_value:
            print(packet.dns.qry_name)

        # break

if __name__ == "__main__":
    print_live_dns()