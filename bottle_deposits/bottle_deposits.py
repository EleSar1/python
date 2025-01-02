def refund(small_container, big_container):
    deposit_small = 0.10
    deposit_big = 0.25
    if small_container >= 1:
        refund_small_cont = small_container * deposit_small
    if big_container > 1:
        refund_big_cont = big_container * deposit_big
    
    final_refund = refund_small_cont + refund_big_cont

    return f"Your refund is ${final_refund:.2f}"


def main():
    small = int(input("Please enter the number of containers containing one liter or less: "))
    big = int(input("Please enter the number of containers containing more than one liter: "))
    ref = refund(small,big)
    print(ref)


if __name__ == "__main__":
    main()