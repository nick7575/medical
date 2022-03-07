import model


#指定圖片網址
url = "https://c.readmop.com/photos/15/e6/ced85ade888fb6552b0ed1c0b9d37dfd.jpg"
#呼叫方法
result= model.predict(url)
#輸出結果
print(result)