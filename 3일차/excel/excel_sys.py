
import pandas as pd
from glob import glob
import sys

# sys 모듈을 사용하여 사용자에게 값을 입력받는다
# input() 함수와 같다
# sys.argv[0]은 현재 작성중인 스크립트 파일을 의미한다.
# 사용법
# cmd창에서 실행한다
# cmd> python 스크립트파일명 사용자입력값

input_dirs = sys.argv[1]

excel_data_files = glob(input_dirs)

total_data2 = pd.DataFrame()

for i in excel_data_files :
    df = pd.read_excel(i)
    total_data2 = total_data2.append(df,
                                    ignore_index=True)
print(total_data2)

# 엑셀파일로 저장하기

total_data2.to_excel('데이터_통합.xlsx', index=False)
print()
print("파일이 저장되었습니다")
