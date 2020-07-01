#getdata関数（データの読み込み）
def get_data(e):
    return_list = []
    print(return_list)
    f = open("data24.txt", "r")
    for line in f:
        print("入力データ（文字列）")
        print(line)
        a = line.split()
        print(a, "要素１",a[0], "要素2",a[1])#文字列を分割できた
        numbers = [int(a[0]),int(a[1])]
        print("数字に変換後格納")
        return_list.insert(len(return_list), numbers)
        print(return_list)
    f.close()
    print("end_loop")
    n_of_e = len(return_list)
    return(n_of_e,return_list)
