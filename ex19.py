# skipped reads ^L
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have %d cheese" % cheese_count)
    print("You have %d boxes of crackers" % boxes_of_crackers)
    print("Man that enoght for a party ")
    print("Get a blancket. \n")


print("we can just give the function dircitly: ")
cheese_and_crackers(20, 30)


print ("Or, we can use variable from our script:  ")
amount_of_cheese = 10
amount_of_crackers= 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("we can do math inside them : ")
cheese_and_crackers (20 + 10, 5+23)

print ("and do math with variblaes and math: ")
cheese_and_crackers(amount_of_cheese + 12, amount_of_crackers + 1200)
