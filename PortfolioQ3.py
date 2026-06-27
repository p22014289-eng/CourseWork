import threading
import time

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def compute_factorial(name, number):
    result = factorial(number)
    print(f"{name} completed")

def run_multithreaded():
    t1 = time.perf_counter_ns()

    thread1 = threading.Thread(target=compute_factorial, args=("50!", 50))
    thread2 = threading.Thread(target=compute_factorial, args=("100!", 100))
    thread3 = threading.Thread(target=compute_factorial, args=("200!", 200))

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

    t2 = time.perf_counter_ns()

    return t2 - t1

def run_single_thread():
    t1 = time.perf_counter_ns()

    factorial(50)
    factorial(100)
    factorial(200)

    t2 = time.perf_counter_ns()

    return t2 - t1

def run_tests():
    multi_times = []
    single_times = []

    print("\n========== FACTORIAL PERFORMANCE TEST ==========\n")

    for i in range(10):
        print("=" * 50)
        print(f"ROUND {i + 1}")

        mt = run_multithreaded()
        st = run_single_thread()

        multi_times.append(mt)
        single_times.append(st)

        print(f"Multithreaded Time: {mt} ns")
        print(f"Single Thread Time: {st} ns")

    avg_multi = sum(multi_times) / len(multi_times)
    avg_single = sum(single_times) / len(single_times)

    print("\n========== FINAL AVERAGE RESULTS ==========")
    print(f"Average Multithreaded Time: {avg_multi:.2f} ns")
    print(f"Average Single Thread Time: {avg_single:.2f} ns")


if __name__ == "__main__":
    run_tests()