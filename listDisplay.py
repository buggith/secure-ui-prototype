def countries(countries_dict):
    result = ""
    # Iterate through key and value items in the dictionary
    for continent, country_list in countries_dict.items():
        # Use the string format method to append the formatted list followed by a newline
        result += "{}\n".format(country_list)
    return result


print(countries({
    "Africa": ["Kenya", "Egypt", "Nigeria"],
    "Asia": ["China", "India", "Thailand"],
    "South America": ["Ecuador", "Bolivia", "Brazil"]
}))
