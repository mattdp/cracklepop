#Write a program that prints out the numbers 1 to 100 (inclusive). 
#If the number is divisible by 3, print Crackle instead of the number. 
#If it's divisible by 5, print Pop. If it's divisible by both 3 and 5, print CracklePop. 
#You can use any language.

# COPY FROM HERE
#!/usr/bin/env python3

def main():
    print_number = True
    output_string = ""

    for i in range(1,101):
        if(i % 3 == 0):
            output_string += "Crackle"
            print_number = False
        if(i % 5 == 0):
            output_string += "Pop"
            print_number = False
        if(print_number):
            output_string += str(i)

        print(output_string)
        
        output_string = ""
        print_number = True

main()