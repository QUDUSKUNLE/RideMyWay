
# run sh run_test.sh to run test and coverage report

echo "****************************** Running test ***********************************************"
cd server
coverage run manage.py test tests -v 2
coverage report
coveralls

echo "****************************** Running test finished **************************************"