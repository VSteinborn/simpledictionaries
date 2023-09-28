export FLASK_APP=app.py
alias setuppy="source ./env/bin/activate"
alias setupdb="flask db init"
alias dbmigrate='flask db migrate -m "update goods and prices"'
alias dbupgrade='flask db upgrade'