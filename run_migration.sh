
# run sh run_migration.sh to run test and coverage report

echo "****************************** Running migrations ***********************************************"
cd server
python3 manage.py makemigrations
python3 manage.py migrate

echo "****************************** Running migrations finished **************************************"