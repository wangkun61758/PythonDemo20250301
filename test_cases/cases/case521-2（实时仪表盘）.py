#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/3/21 18:08
=================================================='''
from datetime import time, datetime
from rich.console import Console
from rich.table import Table
import psutil
import time
import csv
from datetime import datetime

# 基础监控
class PerformanceMonitor:
    def __init__(self, interval=1, log_file='../../resources/reports/performance_log.csv'):
        self.interval = interval
        self.log_file = log_file
        self.header_written = False

    def get_cpu_usage(self):
        """获取CPU使用率（百分比）"""
        return psutil.cpu_percent(interval=self.interval)

    def get_memory_usage(self):
        """获取内存使用情况（GB）"""
        mem = psutil.virtual_memory()
        return {
            'used': round(mem.used / (1024**3), 2),
            'total': round(mem.total / (1024**3), 2),
            'percent': mem.percent
        }

    def get_disk_usage(self):
        """获取磁盘使用情况（默认监控根目录）"""
        disk = psutil.disk_usage('/')
        return {
            'used': round(disk.used / (1024**3), 2),
            'total': round(disk.total / (1024**3), 2),
            'percent': disk.percent
        }

    def get_network_usage(self):
        """获取网络IO（字节）"""
        net = psutil.net_io_counters()
        return {
            'sent': net.bytes_sent,
            'recv': net.bytes_recv
        }

    def log_to_csv(self, data):
        """记录数据到CSV文件"""
        with open(self.log_file, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=data.keys())
            if not self.header_written:
                writer.writeheader()
                self.header_written = True
            writer.writerow(data)

    def monitor(self, duration=60):
        """执行监控"""
        start_time = time.time()
        while time.time() - start_time < duration:
            timestamp = datetime.now().isoformat()
            cpu = self.get_cpu_usage()
            mem = self.get_memory_usage()
            disk = self.get_disk_usage()
            net = self.get_network_usage()

            log_data = {
                'timestamp': timestamp,
                'cpu_percent': cpu,
                'mem_used_gb': mem['used'],
                'mem_percent': mem['percent'],
                'disk_used_gb': disk['used'],
                'disk_percent': disk['percent'],
                'net_sent_bytes': net['sent'],
                'net_recv_bytes': net['recv']
            }

            self.log_to_csv(log_data)
            time.sleep(self.interval)

# 实时仪表盘
class LiveDashboard(PerformanceMonitor):
    def show_dashboard(self):
        console = Console()
        while True:
            cpu = self.get_cpu_usage()
            mem = self.get_memory_usage()

            table = Table(title="实时系统监控", show_header=True)
            table.add_column("指标", justify="left")
            table.add_column("数值", justify="right")

            table.add_row("CPU使用率", f"{cpu}%")
            table.add_row("内存使用", f"{mem['used']} GB / {mem['total']} GB ({mem['percent']}%)")

            console.clear()
            console.print(table)
            time.sleep(self.interval)

if __name__ == "__main__":
    # 实时仪表盘
    live_monitor = LiveDashboard(interval=1)
    live_monitor.show_dashboard()
