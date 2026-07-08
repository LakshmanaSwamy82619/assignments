ile="books.txt"

while true
do
    echo "=============================="
    echo "     BOOK MANAGEMENT SYSTEM"
    echo "=============================="
    echo "1. View All Books"
    echo "2. Search for a Book"
    echo "3. Count Books Out of Stock"
    echo "4. Update Stock Status"
    echo "5. Calculate Total Inventory Value"
    echo "6. Display Books by Category"
    echo "7. Find the Costliest Book"
    echo "8. Exit"
    echo "Enter Your Choice:"
    read choice

    case $choice in

        1)
            echo "----- All Books -----"
            cat "$file"
            ;;

        2)
            echo "Enter Book Name:"
            read book
            grep -i "$book" "$file"
            ;;

        3)
            count=$(grep -c "OutOfStock" "$file")
            echo "Books Out of Stock: $count"
            ;;

        4)
            echo "Enter Book ID:"
            read id

            if grep -q "^$id," "$file"
            then
                sed -i "/^$id,/ s/OutofStock/Available/" "$file"
                echo "Stock Updated Successfully."
            else
                echo "Book ID Not Found."
            fi
            ;;

        5)
            total=$(awk -F',' '
            $4=="Available" {
                sum += $5
            }
            END {
                print sum
            }' "$file")

            echo "Total Inventory Value: Rs. $total"
            ;;

        6)
            echo "Enter Category:"
            read category

            echo "Books in Category: $category"
            awk -F',' -v cat="$category" '
            $3==cat {
                print $0
            }' "$file"
            ;;

        7)
            awk -F',' '
            {
                if ($5 > max) {
                    max = $5
                    book = $2
                }
            }
            END {
                print "Costliest Book :", book
                print "Price :", max
            }' "$file"
            ;;

        8)
            echo "Thank You!"
            exit 0
            ;;

        *)
            echo "Invalid Choice"
            ;;
    esac

    echo
done
