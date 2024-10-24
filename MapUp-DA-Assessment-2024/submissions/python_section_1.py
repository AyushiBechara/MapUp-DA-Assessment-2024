from typing import Dict, List

import pandas as pd


def reverse_by_n_elements(lst: List[int], n: int) -> List[int]:
    """
    Reverses the input list by groups of n elements.
    """
    # Your code goes here.
    for i in range(0,len(lst),n):
        start=i
        end=min(i+n-1,len(lst)-1) 
        while start<end:
            lst[start], lst[end]=lst[end],lst[start]
            start+=1
            end-=1
    return lst
print(reverse_by_n_elements([1, 2, 3, 4, 5, 6, 7, 8], 3)) 
print(reverse_by_n_elements([1, 2, 3, 4, 5], 2)) 
print(reverse_by_n_elements([10, 20, 30, 40, 50, 60, 70], 4)) 


def group_by_length(lst: List[str]) -> Dict[int, List[str]]:
    length_dict={}
    for i in lst:
        length=len(i)
        if length not in length_dict:
            length_dict[length]=[] 
        length_dict[length].append(i)
    
    sorted_length_dict=dict(sorted(length_dict.items()))
    result_dict=sorted_length_dict   
    return result_dict 
print(group_by_length(["apple", "bat", "car", "elephant", "dog", "bear"]))
print(group_by_length([["one", "two", "three", "four"]]))

def flatten_dict(nested_dict: dict, sep: str = '.') -> dict:
    flattened={} 
    def _flatten(current, parent_key):
        if isinstance(current, dict):
            for k in current:
                new_key=f"{parent_key}{sep}{k}" if parent_key else k
                _flatten(current[k], new_key) 
        elif isinstance(current, list): 
            for i in range(len(current)):
                new_key=f"{parent_key}[{i}]"
                _flatten(current[i],new_key)
        else:  
            flattened[parent_key]=current  

    _flatten(nested_dict, '')
    return flattened 
nested_dict={
    "road": {
        "name": "Highway 1",
        "length": 350,
        "sections": [
            {
                "id": 1,
                "condition": {
                    "pavement": "good",
                    "traffic": "moderate"
                }
            }
        ]
    }
}

print(flatten_dict(nested_dict))



def unique_permutations(nums: List[int]) -> List[List[int]]:
    result=[] 
    nums.sort() 
    def backtrack(path, used):
        if len(path)==len(nums): 
            result.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue 
            if i>0 and nums[i]==nums[i - 1] and not used[i - 1]:
                continue
            used[i]=True 
            path.append(nums[i]) 
            backtrack(path, used)
            path.pop()
            used[i]=False
    used = [False]*len(nums)
    backtrack([], used)
    return result
print(unique_permutations([1, 1, 2]))


def find_all_dates(text: str) -> List[str]:
    def is_valid_date(date_str: str) -> bool:
        if len(date_str)==10 and date_str[2]=='-' and date_str[5]=='-':
            day=int(date_str[:2])
            month=int(date_str[3:5])
            year=int(date_str[6:])
            return 1<=day<=31 and 1<=month<= 12 and year>0
        if len(date_str)==10 and date_str[2]=='/' and date_str[5]=='/':
            month=int(date_str[:2])
            day=int(date_str[3:5])
            year=int(date_str[6:])
            return 1<=day<=31 and 1<=month<=12 and year>0
        if len(date_str)==10 and date_str[4]=='.' and date_str[7]=='.':
            year=int(date_str[:4])
            month=int(date_str[5:7])
            day=int(date_str[8:])
            return 1<=day<=31 and 1<=month<=12 and year>0
        return False
    words=text.split()
    valid_dates=[]
    for word in words:
        cleaned_word=word.strip(",.") 
        if is_valid_date(cleaned_word): 
            valid_dates.append(cleaned_word)
    return valid_dates
text="I was born on 23-08-1994, my friend on 08/23/1994, and another one on 1994.08.23."
print(find_all_dates(text))



def polyline_to_dataframe(polyline_str: str) -> pd.DataFrame:
    """
    Converts a polyline string into a DataFrame with latitude, longitude, and distance between consecutive points.
    
    Args:
        polyline_str (str): The encoded polyline string.

    Returns:
        pd.DataFrame: A DataFrame containing latitude, longitude, and distance in meters.
    """
    return pd.Dataframe()


def rotate_and_multiply_matrix(matrix: List[List[int]]) -> List[List[int]]:
    n=len(matrix)
    rotated_matrix=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated_matrix[j][n - 1 - i]=matrix[i][j]
    final_matrix=[[0]*n for _ in range(n)]   
    for i in range(n):
        for j in range(n):
            row_sum=sum(rotated_matrix[i]) 
            col_sum=sum(rotated_matrix[k][j] for k in range(n))  
            final_matrix[i][j]=row_sum+col_sum-rotated_matrix[i][j]     
    return final_matrix


def time_check(df: pd.DataFrame) -> pd.Series:
    df['timestamp']=pd.to_datetime(df['timestamp'])
    results=[]
    grouped=df.groupby(['id', 'id_2'])
    for (id_val, id_2_val),group in grouped:
        days_covered=group['timestamp'].dt.dayofweek.unique()
        full_week_check=len(days_covered)==7  
        time_range=group['timestamp'].min(), group['timestamp'].max()
        full_day_check=(time_range[1]-time_range[0])>=pd.Timedelta(days=1)
        results.append(((id_val, id_2_val),not (full_week_check and full_day_check))) 
    results_series=pd.Series(dict(results))    
    return results_series
