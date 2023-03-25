#Python Tutorial: File Objects - Reading and Writing to Files

with open('texto.txt', 'r') as f:
    f_contents = f.read(100)
    print(f_contents, end='')
    
    f_contents = f.read(100)
    print(f_contents, end='')
    
    f_contents = f.read(100)
    print(f_contents, end='')
    
    while len(f_contents) > 0:
        print(f_contents, end='')
        f_contents = f.read(100)
        
        

with open("test.txt", "r") as rf:
	with open("test_copy.txt", "w") as wf:
		for line in rf:
			wf.write(line)


with open("bronx.jpg", "r") as rf:
	with open("bronx_copy.jpg", "w") as wf:
		for line in rf:
			wf.write(line)


with open("bronx.jpg", "rb") as rf:
	with open("bronx_copy.jpg", "wb") as wf:
		for line in rf:
		  wf.write(line)


with open("bronx.jpg", "rb") as rf:
	with open("bronx_copy.jpg", "wb") as wf:
    		chunk_size = 4096
            rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
