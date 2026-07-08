#!/bin/bash

employee_count=0

calculate_tax() {
    salary=$1
    echo $((salary * 10 / 100))
}

calculate_bonus() {
    salary=$1
    echo $((salary * 5 / 100))
}

echo "Enter Employee File:"
read empfile

if [[ ! -f "$empfile" ]]
then
    echo "File does not exist"
    exit 1
fi

{
echo "=================================================="
echo "           EMPLOYEE PAYROLL REPORT"
echo "=================================================="
echo ""
} > payroll_report.txt

while read -r id name salary
do
    tax=$(calculate_tax "$salary")
    bonus=$(calculate_bonus "$salary")
    netsalary=$((salary - tax + bonus))

    {
    echo "ID: $id | Name: $name"
    echo "Salary: $salary"
    echo "Tax: $tax"
    echo "Bonus: $bonus"
    echo "Net Salary: $netsalary"
    echo ""
    echo "--------------------------------------------------"
    echo ""
    } >> payroll_report.txt

    employee_count=$((employee_count + 1))

done < "$empfile"

{
echo "Total Employees Processed : $employee_count"
echo "=================================================="
} >> payroll_report.txt

echo "Report Generated: payroll_report.txt"
