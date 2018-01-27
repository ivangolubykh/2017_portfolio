python3-coverage run --source='.' manage.py test --debug-mode

if [[ $? = 0 ]]
then
    echo ""
    echo "++++++++++++++++++++++++"
    echo ""
    echo "Ошибок в тестах нет. Процент покрытия тестами:"
    echo ""
    echo "++++++++++++++++++++++++"
    echo ""
    python3-coverage report -m --omit=manage.py,portfolio_django_2017/wsgi.py,app_main/test_models.py
fi

#python3-coverage html --directory=_tests_coverage_html_report
