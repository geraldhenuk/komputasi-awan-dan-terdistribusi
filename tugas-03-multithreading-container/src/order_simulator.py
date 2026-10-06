import threading
import time

# Counter global untuk mencatat jumlah pesanan
total_orders_processed = 0

# Lock untuk mencegah race condition
counter_lock = threading.Lock()

def process_order(order_id, use_lock):
    global total_orders_processed
    
    # Simulasi jeda pemrosesan pesanan
    time.sleep(0.001)
    
    if use_lock:
        # Critical section aman menggunakan Lock
        with counter_lock:
            current = total_orders_processed
            time.sleep(0.0001)  # Memperbesar peluang race condition jika tanpa lock
            total_orders_processed = current + 1
    else:
        # Pemicu Race Condition (Tanpa Lock)
        current = total_orders_processed
        time.sleep(0.0001)
        total_orders_processed = current + 1

def run_simulation(num_orders, use_lock):
    global total_orders_processed
    total_orders_processed = 0
    threads = []

    mode_str = "DENGAN Lock" if use_lock else "TANPA Lock"
    print(f"\n=== Simulasi Pesanan ({mode_str}) ===")
    
    for i in range(num_orders):
        t = threading.Thread(target=process_order, args=(i, use_lock))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"Target Pesanan : {num_orders}")
    print(f"Hasil Counter  : {total_orders_processed}")
    if total_orders_processed == num_orders:
        print("Status         : SUKSES (Data Tepat)")
    else:
        print("Status         : RACE CONDITION (Data Korup/Kurang)")

if __name__ == "__main__":
    TOTAL = 100
    # 1. Jalankan tanpa lock untuk membuktikan Race Condition
    run_simulation(TOTAL, use_lock=False)
    
    # 2. Jalankan dengan lock untuk perbaikan
    run_simulation(TOTAL, use_lock=True)