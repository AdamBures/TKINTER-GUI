import platform
import psutil
from datetime import datetime
import tkinter as tk
import matplotlib.pyplot as plt

win = tk.Tk()
win.resizable(False,False)
win.title("HW Checker") 
win.geometry("250x250")

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


def sys_info():
    win1 = tk.Tk()
    win1.resizable(False,False)
    win1.title("HW Checker") 
    win1.geometry("400x250")

    sys = platform.uname().system
    node = platform.uname().node
    rel = platform.uname().release
    ver = platform.uname().version
    mach = platform.uname().machine
    proc = platform.uname().processor

    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)

    lbl = tk.Label(win1, text="System information").pack()
    lbl1 = tk.Label(win1, text=f"System: {sys}").pack()
    lbl2 = tk.Label(win1, text=f"Node: {node}" ,height=1).pack()
    lbl3 = tk.Label(win1, text=f"Release: {rel}",height=1).pack()
    lbl4 = tk.Label(win1,text=f"Version: {ver}",height=1).pack()
    lbl5 = tk.Label(win1,text=f"Machine: {mach}",height=1).pack()
    lbl6 = tk.Label(win1,text=f"Processor: {proc}").pack()
    lbl7 = tk.Label(win1, text=f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}").pack()

def cpu_info():
    win2 = tk.Tk()
    win2.resizable(False,False)
    win2.title("HW Checker") 
    win2.geometry("500x300")

    cpufreq = psutil.cpu_freq()

    phy = psutil.cpu_count(logical=False)
    tot = psutil.cpu_count(logical=True)

    precent = psutil.cpu_percent(percpu=True)


    lbl = tk.Label(win2, text="CPU information").pack()
    lbl1 = tk.Label(win2, text=f"Physical cores: {psutil.cpu_count(logical=False)}").pack()
    lbl2 = tk.Label(win2, text=f"Total cores: {psutil.cpu_count(logical=True)}").pack()
    lbl3 = tk.Label(win2, text=f"Max phrequency: {cpufreq.max:.2f}Mhz").pack()
    lbl4 = tk.Label(win2, text=f"Min phrequency: {cpufreq.min:.2f}Mhz").pack()
    lbl5 = tk.Label(win2, text=f"Current phrequency: {cpufreq.current:.2f}Mhz").pack()
    lbl6 = tk.Label(win2, text=f"CPU Usage Per Core: ").pack()
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        tk.Label(win2, text=f"Core {i}: {percentage}").pack()
    lbl7 = tk.Label(win2, text=f"Total CPU Usage: {psutil.cpu_percent()}%").pack()

def disk_info():
    win3 = tk.Tk()
    win3.resizable(False,False)
    win3.title("HW Checker") 
    win3.geometry("500x300")

    partitions = psutil.disk_partitions()


    for partition in partitions:
        tk.Label(win3, text=f"Device: {partition.device}").pack()
        tk.Label(win3, text=f"Mountpoint: {partition.mountpoint}").pack()
        tk.Label(win3, text=f"File system type: {partition.fstype}").pack()
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)

        except PermissionError:
            continue

        lbl = tk.Label(win3, text=f"Total size: {get_size(partition_usage.total)}").pack()
        lbl2 = tk.Label(win3,text=f"Used: {get_size(partition_usage.used)}").pack()
        lbl3 = tk.Label(win3,text=f"Free: {get_size(partition_usage.free)}").pack()
        lbl4 = tk.Label(win3,text=f"Percentage: {get_size(partition_usage.percent)}").pack()

    disk_io = psutil.disk_io_counters()
    lbl5 = tk.Label(win3, text=f"Total read: {get_size(disk_io.read_bytes)}").pack()
    lbl6 = tk.Label(win3, text=f"Total write: {get_size(disk_io.write_bytes)}").pack()

def network_info():
    win4 = tk.Tk()
    win4.resizable(False,False)
    win4.title("HW Checker") 
    win4.geometry("1000x750")

    if_addrs = psutil.net_if_addrs()
    tk.Label(win4,text="Network Information").pack()
    for interface_name, interface_addresses in if_addrs.items():
    	for address in interface_addresses:
    		tk.Label(win4, text=f"Interface: {address}").pack()
    		if str(address.family) == 'AddressFamily.AF_INET':
    			tk.Label(win4, text=f"Address: {address.address}").pack()
    			tk.Label(win4,text=f"Netmask: {address.netmask}").pack()
    			tk.Label(win4,text=f"Broadcast IP: {address.broadcast}").pack()
    		elif str(address.family) == 'AddressFamily.AF_PACKET':
    			tk.Label(win4, text=f"MAC Address: {address.address}").pack()
    			tk.Label(win4,text=f"Netmask: {address.netmask}").pack()
    			tk.Label(win4,text=f"Broadcast IP: {address.broadcast}").pack()

    net_io = psutil.net_io_counters()
    lbl = tk.Label(win4,text=f"Total Bytes Sent: {get_size(net_io.bytes_sent)}").pack()
    lbl2 = tk.Label(win4, text=f"Total Bytes Received: {get_size(net_io.bytes_recv)}").pack()


def mem_info():
    win5 = tk.Tk()
    win5.resizable(False,False)
    win5.title("HW Checker") 
    win5.geometry("500x300")
    

    svmem = psutil.virtual_memory()
    tot = get_size(svmem.total)
    avaiable = get_size(svmem.available)
    used = get_size(svmem.used)
    percent = svmem.percent
    
    edit_avaiable = float(avaiable[:4])
    
    edit_used = float(used[:4])
    edit_tot = float(tot[:4])

    a = round(edit_avaiable / edit_tot * 100)
    b = float(percent)

    swap = psutil.swap_memory()
    sw_tot = get_size(swap.total)
    sw_free = get_size(swap.free)
    sw_used = get_size(swap.used)
    sw_percent = swap.percent

    lbl = tk.Label(win5, text="Memory information").pack()
    lbl2 = tk.Label(win5, text=f"Total:{get_size(svmem.total)}").pack()
    lbl3 = tk.Label(win5, text=f"Available: {get_size(svmem.available)}").pack()
    lbl4 = tk.Label(win5, text=f"Used: {get_size(svmem.used)}").pack()
    lbl5 = tk.Label(win5, text=f"Percent: {svmem.percent}").pack()

    lbl6 = tk.Label(win5, text=f"SWAP Information").pack()
    lbl7 = tk.Label(win5, text=f"SWAP Total: {get_size(swap.total)}").pack()
    lbl8 = tk.Label(win5, text=f"SWAP Free: {get_size(swap.free)}").pack()
    lbl9 = tk.Label(win5, text=f"SWAP Used: {get_size(swap.used)}").pack()
    lbl10 = tk.Label(win5, text=f"SWAP Percent: {swap.percent}").pack()

    percentage_1 = [a,b]
    color = ["blue","red"]
    label = ["Available", "Used"]
    plt.pie(percentage_1,labels=label,colors=color)
    plt.show()

sys_btn = tk.Button(win,text="System information", command=sys_info, width=30).pack()
tk.Label(win, height=1).pack()
cpu_btn = tk.Button(win,text="CPU information", command=cpu_info, width=30).pack()
tk.Label(win, height=1).pack()
mem_btn = tk.Button(win,text="Memory information", command=mem_info, width=30).pack()
tk.Label(win, height=1).pack()
disk_btn = tk.Button(win,text="Disk usage", command=disk_info, width=30).pack()
tk.Label(win, height=1).pack()
network_btn = tk.Button(win,text="Network information",command=network_info, width=30).pack()
tk.Label(win, height=1).pack()

win.mainloop()
