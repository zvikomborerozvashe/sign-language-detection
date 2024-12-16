import splitfolders

dr = 'C:\\Users\\Neha Nandiki\\OneDrive\\Desktop\\Sign language detection\\aslsigndataset-main\\splitdataset48x48'
splitfolders.ratio(dr, "splitdataset48x48", ratio=(0.8, 0.2))  # 0.8 == train , 0.2 == validate, test

