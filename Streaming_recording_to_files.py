
import threading
import time

def write_words(word_count, file_name):
    words = [str(i) for i in range(word_count)]
    with open(file_name, 'a', encoding='utf-8') as file:
        for i in words:
            file.write(i + " ")
            time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

arguments_for_working_directly = [(10, "example1.txt"), (30, "example2.txt"), (200, "example3.txt"), (100, "example4.txt")]
arguments_for_working_through_threads = [(10, "example5.txt"), (30, "example6.txt"), (200, "example7.txt"), (100, "example8.txt")]

start_time = time.time()

for word_count, file_name in arguments_for_working_directly:
    write_words(word_count, file_name)

end_time = time.time()
print(f"Работа потоков: {end_time - start_time:.4f}")



start_time = time.time()
threads = []

for word_count, file_name in arguments_for_working_through_threads:
    thread = threading.Thread(target=write_words, args=(word_count, file_name))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time()
print(f"Работа потоков: {end_time - start_time:.4f}")

