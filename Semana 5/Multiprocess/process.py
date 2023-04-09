import time
import concurrent.futures

start = time.perf_counter() 
def do_something(seconds): 
    print(f'Sleeping {seconds} second(s)...') 
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}' 

with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1] #testa para outros segundos
    results = executor.map(do_something, secs) 

finish = time.perf_counter() #calcula o tempo final
print(f'Finished in {round(finish-start, 2)} second(s)') 
