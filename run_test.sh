
# run sh run_test.sh to run test and coverage report

echo "****************************** Running test ***********************************************"
cd server
python3 manage.py test tests -v 2
coverage report

echo "****************************** Running test finished **************************************"