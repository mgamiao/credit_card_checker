while True:
    # ask user for their credit card number, reprompt user if number inputted is not int or negatives
    while True:
        try:
            number = int(input("Enter your credit card number: "))
        except:
            print("Input error: letters or special characters are not accepted. Please Try again.\n")
            continue
        if number < 0:
            print("Input error: letters or special characters are not accepted. Please Try again.\n")
            continue
        
        else:
            break

  
    # get first digit for checking card type
    firstdigit = number
    while firstdigit >= 10:
        firstdigit = firstdigit // 10
        if firstdigit < 10:
            # uncomment print to check the result
            #print("firstdigit = " + str(firstdigit))
            break 

    # get first and second digit for checking card type
    seconddigit = number 
    while seconddigit >= 100:
        seconddigit = seconddigit // 10
        if seconddigit < 100:
            # uncomment print to check the result
            #print("secondigit = " + str(seconddigit))
            break 


    # calculating checksum:
    # get length of inputted number
    count = 0 
    numbercheck = number 
    while numbercheck > 0:
        numbercheck = numbercheck // 10
        # uncomment print to check the result
        #print("number check = " + str(numbercheck))
        count += 1
        # uncomment print to check the result
        #print("count = " + str(count))
        if numbercheck <= 0:
            break
        

    #process of selecting every other digits
    sum1 = 0
    digits2 = 0
    sum2 = 0
    while number > 0:
        sum1 = sum1 + (number % 10)  #select first digit
        # uncomment print to check the result
        #print("sum1 = " + str(sum1))
        number = number // 10 
        digits2 = (2 * (number % 10))  #select second digit
        number = number // 10 
        if digits2 > 9: # if the digit is double digit, add then together
            a = 0
            b = 0
            c = digits2 
            d = 0
            a = c % 10 
            c = c / 10 
            d = a + c 
            sum2 = d + sum2
        elif digits2 < 10:
            sum2 = sum2 + digits2 
            # uncomment print to check the result
            #print("sum2 = " + str(sum2))
        elif number < 0:
            break
    # end of process of selecting every other digits    


    checksum = sum1 + sum2 
    last_digit_checksum = checksum % 10
    # uncomment print to check the result
    #print("checksum = " + str(checksum))
    #print("last_digit_checksum = " + str(last_digit_checksum))
    # end of calculating check sum


    # check card length and starting digits:
    # if checksum's sum's last digit is 0, the credit card is valid. Else invalid
    if last_digit_checksum == 0:
        # if number is 13 or 16 digits and starting number is 4, print VISA
        if ((count == 13 or count == 16) and firstdigit == 4):
            print("Your credit card is VISA\n") 

        # if number is 16 digits and starting number is 5, print MASTERCARD
        elif (count == 16 and firstdigit == 5):
             print("Your credit card is MASTERCARD\n") 

        # if number inputted satisfy checksum but doesn't satisfy conditions of card number length and starting digit
        else:
             print("Your credit card is INVALID\n") 

    # if checksum's sum's last digit is not 0
    else:
         print("Your credit card is INVALID\n") 
    # end of card length and starting digits checker