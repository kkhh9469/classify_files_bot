import os
import shutil



def extract_tags(file_list):
  tag_list = []
  for file_name in file_list:
    tag = file_name.split("#")[1:]
    if tag != []:
      for tag in tag:
        tag_list.append(tag)
  tag_list = list(set(tag_list))
  return tag_list

def create_tag_name_files(file_list, tag_list):
  for tag in tag_list:
    for file in file_list:
      try:
        if tag != file:
          os.mkdir(f"./{tag}")
          print(f"{tag} 폴더 생성")
      except FileExistsError:
        # print(f"{tag} 파일이 이미 존제합니다")
        pass

def classify_files(file_list, tag_list):
  for file in file_list:
    file_name_file_tag = file.split("#")
    if file_name_file_tag[1:] != []:
      file_tag = file_name_file_tag[1]
      for tag in tag_list:
        if file_tag == tag:
          shutil.move(file, tag)
          print(f"{file} 이(가) {tag}로 이동")
    



# 분류
file_list = os.listdir("./")
tag_list = extract_tags(file_list)

create_tag_name_files(file_list, tag_list)
classify_files(file_list, tag_list)



  #   pass 1잘가, 2안녕, 1어제 1다음





