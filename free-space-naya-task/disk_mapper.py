import os
import psutil

def get_disk_info():
  """Get disk information."""
  disks = psutil.disk_partitions()
  for disk in disks:
    print(f"{disk.mountpoint}: {disk.free} / {disk.total}")

if __name__ == "__main__":
  get_disk_info()
