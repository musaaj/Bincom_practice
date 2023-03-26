from typing import List, Tuple
import re

def extract_names(filename: str) -> List[Tuple[int, str, str]]:
    """
    Extracts baby names, ranks, and genders 
    from an HTML file containing US baby name data.

    Args:
        filename: A string representing the name of the HTML file.

    Returns:
        A list of tuples, each containing the rank 
        (int), male name (str), and female name (str).
    """
    try:
        with open(filename) as file:
            html = file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f'{filename} does not exists')
    pattern = r'<td>(\d+)<\/td>\s*<td>(?:<.*?>)*([A-Za-z ]+)<\/td>\s*<td>(?:<.*?>)*(.*?)<\/td>'
    matches = re.findall(pattern, html)
    return [
            (int(rank), 
            male_name.strip(),
            female_name.strip()) 
            for rank, male_name,
            female_name in matches
        ]

if __name__ == '__main__':
    names: List[Tuple[int, str, str]] = extract_names('baby2008.html')
    for rank, male, female in names:
        print(f'Rank: {rank}: Male: {male} Female: {female}')
