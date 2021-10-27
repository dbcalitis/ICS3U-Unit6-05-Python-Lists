#!/usr/bin/env python3

# Created by: Daria Bernice Calitis
# Created on: Oct 2021
# This program determines the average


def mean(marks):
    # This function calculates the average mark
    average = 0
    for mark in marks:
        average += mark

    average = round(average / len(marks), 1)

    return average


def main():
    # This function is the main function
    user_marks = []
    print("Please enter 1 mark at a time. Enter -1 to end\n")

    # input
    while True:
        user_input = input("What is your mark? (as %): ")
        try:
            # process & output
            user_input = float(user_input)
            if user_input >= 1 and user_input <= 100:
                user_marks.append(user_input)
            elif user_input == -1:
                print("\nThe average is {0}%".format(mean(user_marks)))
                break
            else:
                print("\nInvalid Input.")
                break
        except (Exception):
            print("\nInvalid Input.")
            break

    print("\nDone.")


if __name__ == "__main__":
    main()
