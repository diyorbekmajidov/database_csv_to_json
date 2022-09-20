import csv
def read_csv(filename:str)->list:
    """
    CSV file name is given split by comma and new line,
    then add to list

    Arguments:
        filename(str): parameter
    Returns:
        list: nested list
    """
    f=open(filename)
    data = list(csv.reader(f))
    return data

x=read_csv('specifications.csv')


