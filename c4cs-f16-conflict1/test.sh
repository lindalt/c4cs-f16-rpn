<<<<<<< HEAD
diff <(python main.py) golden.txt

=======
diff <(python main.py) - <<< $(cat << EOF
Welcome to the simple test program

According to current estimates, the diag construction will be done:
Summer 2017.
EOF
)
>>>>>>> remotes/origin/merge_me
if [ $? -eq 0 ]; then
	echo "Success"
else
	echo "Fail. Did not match output"
fi
