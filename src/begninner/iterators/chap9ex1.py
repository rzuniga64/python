def main():
    square = {(10, 8), (10, 23), (25, 23), (25, 8)}
    for points in square:
        print(points)
    
    square_it = iter(square)
    print(next(square_it))
    print(next(square_it))
    print(next(square_it))
    print(next(square_it))
                
main()