PASSWORD_FILE="passwords.txt"

sort "$PASSWORD_FILE" | while IFS= read -r password; do
    echo "Processing password: $password"
    echo "$password" > "${password}.txt"
done
