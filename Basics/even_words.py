st = 'Print every word in this sentence that has an even number of letters'
for i in st.split():
    if len(i) % 2 == 0:
        print(i, '-> even !')
