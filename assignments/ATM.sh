#Initial Balance
balance=10000

while true
do
	echo "========================="
	echo "1. Check Balance"
	echo "2. Deposit"
	echo "3. Withdraw"
	echo "4. Exit"
	echo "========================="

	echo -n "Enter your choice: "
	read choice

	case $choice in
		1)
			echo "Current Balance: $balance"
			;;
		2)
			echo "Enter Deposit Amount: "
			read amount
			if [[ $amount -gt 0 ]]; then
				balance=$((balance+amount))
				echo "Amount Debited Successfully"
				echo "Updated Account Balance: $balance"
			else
				echo "Invalid Amount"
               		fi
;;
		3)
			echo "Enter WIthdrawl Amount"
			read withdraw
			if [[ $withdraw -le 0 ]]; then
				echo "Invalid Withdrawl Amount"
			elif [[ $withdraw -gt $balance ]]; then
				echo "Insufficient Balance"
			else
				balance = $((balance-withdraw))
				echo "Amount Withdrawl Successfully"
				echo "Updated Balance: $balance"
			fi
;;
		4)
			echo "Thank you for using our Application."
			break
			;;
		*)
			echo "Invalid Choice Chosen, Please select a valid option"
			;;
esac
done
