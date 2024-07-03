'''
    Berkas : h_rerata_bubblesort.py
    Program: Menghitung rerata dan mengurutkan dengan bubble sort
    Created: 02 Juli 2024
'''

from flask import Flask, render_template, request

web = Flask(__name__)

def rata_rata(data):
    jumlahAngka = 0
    banyakAngka = 0
    
    for i in data:
        jumlahAngka += i
        banyakAngka += 1
    
    hasilRerata = jumlahAngka / banyakAngka
    return hasilRerata, jumlahAngka, banyakAngka

def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

@web.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@web.route('/rerata', methods=['GET','POST'])
def rerata():
    jumlahAngka = None
    banyakAngka = None
    hasilRerata = None
    if request.method == 'POST':
        try:
            user_input = request.form['inputData'] # get data
            data = [int(x) for x in user_input.split(',')] # pisahkan data
            
            hasilRerata, jumlahAngka, banyakAngka = rata_rata(data)
            
        except ValueError:
            result = 'Pastikan inputan sudah benar!'
    return render_template('rerata.html', jumlahAngka=jumlahAngka, banyakAngka=banyakAngka, hasil=hasilRerata)

@web.route('/bubblesort', methods=['GET','POST'])
def bubbleSort():
    hasilSorting = None
    if request.method == 'POST':
        try:
            user_input = request.form['inputData'] # get data
            data = [int(x) for x in user_input.split(',')] # pisahkan data
            bubble_sort(data)
            
            hasilSorting = data
        except ValueError:
            result = 'Pastikan inputan sudah benar!'
    return render_template('bubbleSort.html', hasil=hasilSorting)

if __name__ == '__main__':
    web.run()