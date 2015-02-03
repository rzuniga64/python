# Input: file name containing text to find unique words in
# Output: list of unique words


def process_document(filename):
    try:
        document = open("\\\RGC-FP0\\StudentsHome\\3051102\workspace\\python_workspace\\hw7\\src\\senators.txt", "r")
    except:
        print("File " + filename + " did not open.")
        document = open("senators.txt", "r")

    senators = []
    dem_total = 0
    rep_total = 0
    dem_total_years_of_service = 0
    rep_total_years_of_service = 0
    
    for line in document:
        line = line.strip()
        senator_fields = line.split()
        senators.append(senator_fields)
        years_of_service = 2013 - int(senator_fields[-2])
        if senator_fields[-3] == "(R)":
            rep_total += 1
            rep_total_years_of_service += years_of_service
        if senator_fields[-3] == "(D)":
            dem_total += 1
            dem_total_years_of_service += years_of_service
            
    print("The total number of republicans is ", rep_total)
    print("The total number of democrats is ", dem_total)
    print("The total number of republican years of service is ", format(rep_total_years_of_service, "d"))
    print("The total number of democrat years of service is ", format(dem_total_years_of_service, "d"))
            
        #Watch for divide by zero         
    ave_rep_years_of_service = rep_total_years_of_service/rep_total
    ave_dem_years_of_service = dem_total_years_of_service/dem_total
        
    document.close()
    
    return senators


def main():

    unique = process_document("\\\RGC-FP0\\StudentsHome\\3051102\workspace\\python_workspace\\hw7\\src\\senators.txt")
    unique.sort()
    print(unique)

main()
