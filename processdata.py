import os
train_path = r'C:\Users\Downloads\traindgrl'
xml_list = [os.path.join(train_path, i) for i in os.listdir(train_path) if i.endswith('.dgrl')]
print(len(xml_list))
print(xml_list[0])
