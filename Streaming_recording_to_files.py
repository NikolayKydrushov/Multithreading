"""
import threading
import time



def wite_words(word_count, file_name):

    words = [str(i) for i in range(word_count)]
    with open(file_name, 'a', encoding='utf-8') as file:
        time.sleep(0.1)
        for i in words:
            file.write(i + " ")

    print(f"Завершилась запись в файл {file_name}")




word_count = (10, 30, 200, 100)
file_name = ("example1.txt", "example2.txt", "example3.txt", "example4.txt",
             "example5.txt", "example6.txt", "example7.txt", "example8.txt" )
function = {file_name[i]: word_count[i % len(word_count)] for i in range(len(file_name))}

items = list(function.items()) # Преобразуем элементы словаря в список
half_length = len(items) // 2

start_time = time.time()
for file_name, word_count in items[:half_length]:
    wite_words(word_count, file_name)

end_time = time.time()
execution_time = end_time - start_time
print(f"Работа потоков {execution_time}")


start_time = time.time()
for file_name, word_count in items[half_length:]:
    thread = threading.Thread(target=wite_words, args=(word_count, file_name))
    thread.start()

end_time = time.time()
execution_time = end_time - start_time
print(f"Работа потоков {execution_time}")


for word_count, file_name in function.items():
    wite_words(word_count, file_name)



start_time = time.time()
wite_words(10, "example1.txt")
wite_words(30, "example2.txt")
wite_words(200, "example3.txt")
wite_words(100, "example4.txt")
end_time = time.time()
print(f"Работа потоков {end_time - start_time : .4f}")


start_time = time.time()
thread0 = threading.Thread(target=wite_words, args = (10, "example5.txt"))
thread0.start()
thread0.join()
thread1 = threading.Thread(target=wite_words, args = (30, "example6.txt"))
thread1.start()
thread2 = threading.Thread(target=wite_words, args = (200, "example7.txt"))
thread2.start()
thread3 = threading.Thread(target=wite_words, args = (100, "example8.txt"))
thread3.start()


end_time = time.time()
print(f"Работа потоков {end_time - start_time : .4f}")


print(threading.enumerate())

"""









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

