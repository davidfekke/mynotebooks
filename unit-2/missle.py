import usb.core
import usb.util
import time

# Find the device (Dream Cheeky Vendor ID is usually 0x2123 or 0x0a81)
dev = usb.core.find(idVendor=0x1941, idProduct=0x8021)

if dev is None:
    raise ValueError("Launcher not found!")

# On Mac, you may need to detach the kernel driver if it's "claimed"
if dev.is_kernel_driver_active(0):
    dev.detach_kernel_driver(0)

def command(dev, com):
    table = {
        "Stop":[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
        "Up":[0x01, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
        "Down":[0x02, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
        "Left":[0x04, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
        "Right":[0x08, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
        "Fire":[0x10, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
    }
    try:
        if com == "Fire":
            dev.ctrl_transfer(0x21, 0x09, 0, 0, table[com])
            time.sleep(3)
        else:
            dev.ctrl_transfer(0x21, 0x09, 0, 0, table[com])
    except usb.core.USBError as e:
        if e.errno == 32:
            print("Pipe error detected. Resetting device...")
            dev.reset()
            # On Mac, you might need to re-claim the interface after a reset
            usb.util.claim_interface(dev, 0)
        else:
            print(f"USB error #: {e.errno}")
            raise e


# Example: Here are some tests
command(dev, "Up")

time.sleep(1) # Move for 1 second

command(dev, "Down")

time.sleep(1)

command(dev, "Left")

time.sleep(1)

command(dev, "Right")

time.sleep(1)

command(dev, "Stop")

# time.sleep(1)

command(dev, "Fire")

# time.sleep(5)

command(dev, "Stop")
