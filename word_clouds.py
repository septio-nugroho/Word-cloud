from string import punctuation     # punctuation berisi tanda baca
from collections import Counter    # modul counter untuk menghitung banyak kata
from html_functions import make_HTML_word, make_HTML_box, print_HTML_file

print(''' 
Program untuk membuat word cloud dari text file
---------------------------------------------
hasilnya disimpan sebagai file html,
yang bisa ditampilkan di browser.
''')

file_input_name = input("Silakan masukkan nama file: ")
print("")
print(file_input_name, ":")

file_input = open(file_input_name, "r", encoding="utf-8") # file input dibuka dengan mode "r", hanya dibaca
file_input_read = file_input.read()         # isi file akan dimasukkan ke variable
file_input_read = file_input_read.split()   # teks file akan dipisah dengan split() menjadi per kata semua     kata dipisah dengan spasi dan dimasukkan ke dalam list
                                            
stop_words = open("stopwords.txt", "r") 
stop_words = stop_words.read()
stop_words = stop_words.split()

# fungsi untuk menghilangkan tanda baca
def remove_punc(strings):
    for i in strings:       # setiap huruf dalam kata akan di-loop dan dicek ada atau tidaknya tanda baca
        if i in punctuation:
            strings = strings.replace(i, "") # jika ada bagian yang termasuk tanda baca, akan diganti(replace) dengan string kosong ""
    return strings

# fungsi remove_punc dipanggil dengan argumen setiap kata dari loop isi file
file_input_read = [remove_punc(words) for words in file_input_read]
# semua huruf dibuat lower case
low_case = [k.lower() for k in file_input_read]

# setelah lower case semua, kata yang termasuk stop_words dihapus dengan method remove
for word in list(low_case):
    if word in stop_words:
        low_case.remove(word)

# modul counter untuk menghitung jumlah kata sama yang muncul
counts = Counter(low_case)
frequent_word = counts.most_common(56) # hanya mengambil 56 kata dengan jumlah terbanyak
print("56 kata diurutkan berdasarkan jumlah kemunculan dalam pasangan (jumlah:kata)\n")

# list untuk mengambil kata dari frequent_word
table = []
for x, y in frequent_word:
    a = x           # frequent_word me-return list[tuple(kata, banyak kata)]
    table.append(a)

# fungsi untuk mengambil kata terpanjang
def get_max(my_list):
    return max(my_list, key=len)
    
longest = len(get_max(table))

# print kata terbanyak dengan format 4 kolom
urutan = 0
for x, y in frequent_word:
    urutan +=1
    if urutan % 4 != 0:
        print("{:>2}:{:<{widht}}\t".format(y,x, widht = longest), end="")
    else:
        print("{:>2}:{:<{widht}}\t".format(y,x, widht = longest))
            
# fungsi untuk mensortir list berdasarkan abjad
def abjad(datum):
    return datum[0]
frequent_word.sort(key=abjad)

# fungsi untuk me-return banyak kata dari list[tuple(kata, banyak kata)] dan
# menentukan nilai maksimal dan minimal
def word_count(datum):
    return datum[1]

highest_word = max(frequent_word, key=word_count)[1]
lowest_word = min(frequent_word, key=word_count)[1]

# menggunakan fungsi dari html_function.py
def main():
    pairs = frequent_word
    high_count = highest_word
    low_count = lowest_word
    body = ''
    for word, cnt in pairs:
        body = body + " " + make_HTML_word(word, cnt, high_count, low_count)
    box = make_HTML_box(body)
    print_HTML_file(box, file_input_name)
    
if __name__ == '__main__':
    main()
    
input("\nTekan Enter untuk keluar...")
