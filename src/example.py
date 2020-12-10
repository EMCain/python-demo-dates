from date_functions import DEFAULT_FORMAT, first_sunday, this_year_info


def this_year_info_string():
    info = this_year_info()
    days_list = '\n'.join([
        d.strftime(DEFAULT_FORMAT)
        for d in info["first_sundays"]
        ])
    result = f"""Today is {info["today"].strftime(DEFAULT_FORMAT)}
The first Sundays for {info["year"]} are: 
{days_list}
"""
    return result



if __name__ == "__main__":
    print(this_year_info_string())
