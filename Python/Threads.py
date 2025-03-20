from threading import Thread, current_thread, Lock

class RideQueue:
    def __init__(self, tickets_available):
        self.tickets_available = tickets_available
        self.lock = Lock()  # Создаем объект блокировки для синхронизации

    def take_ticket(self, tickets_requested):
        with self.lock:  # Гарантируем, что одновременно только один поток выполняет этот блок кода
            print(f"{self.tickets_available} ticket(s) available before request.")
            name = current_thread().name
            if tickets_requested <= self.tickets_available:
                self.tickets_available -= tickets_requested
                print(f"{tickets_requested} ticket(s) assigned to {name}. Enjoy the ride!")
            else:
                print(f"Sorry {name}, not enough tickets available.")

ride = RideQueue(1)

# Создаем два потока
visitor1 = Thread(target=ride.take_ticket, kwargs={"tickets_requested": 1}, name="Alice")
visitor2 = Thread(target=ride.take_ticket, kwargs={"tickets_requested": 1}, name="Bob")

# Запускаем потоки
visitor1.start()
visitor2.start()

# Ожидаем завершения потоков
visitor1.join()
visitor2.join()