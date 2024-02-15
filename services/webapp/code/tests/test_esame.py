import unittest
from esame import CSVTimeSeriesFile, compute_increments, ExamException

score = 0

class TestComputeIncrements(unittest.TestCase):
    
    def test_get_data(self):
        file = CSVTimeSeriesFile('/data/data.csv')
        data = file.get_data()
        self.assertEqual(len(data), 3) 
        self.assertEqual(data[0], ['1947-01', 90])
        self.assertEqual(data[-1], ['1951-11', 100])
        
        global score
        score += 2
    
    def test_get_data_missing_file(self):
        file = CSVTimeSeriesFile('/data/missing.csv')
        with self.assertRaises(ExamException):
            file.get_data()
        
        global score
        score += 1
    
    def test_get_data_invalid_rows(self):
        file = CSVTimeSeriesFile('/data/invalid_rows.csv')
        actual = file.get_data()
        expected = [['1949-01', 90], ['1950-11', 100]]
        self.assertEqual(expected, actual)
            
        global score
        score += 1
        
    def test_get_data_out_of_order(self):
        file = CSVTimeSeriesFile('/data/dates_out_of_order.csv')
        with self.assertRaises(ExamException):
            file.get_data()
            
        global score
        score += 1
        
    def test_get_data_dates_incorrect_format(self):
        file = CSVTimeSeriesFile('/data/dates_incorrect_format.csv')
        data = file.get_data()
        self.assertEqual( len(data), 2)
            
        global score
        score += 1
        
    def test_get_data_months_range(self):
        file = CSVTimeSeriesFile('/data/months_range.csv')
        data = file.get_data()
        self.assertEqual( len(data), 12)
            
        global score
        score += 1
        
    def test_get_data_duplicate_dates(self):
        file = CSVTimeSeriesFile('/data/duplicate_dates.csv')
        with self.assertRaises(ExamException):
            file.get_data()
            
        global score
        score += 1
    
    def test_get_data_months_out_of_order(self):
        file = CSVTimeSeriesFile('/data/months_out_of_order.csv')
        with self.assertRaises(ExamException):
            file.get_data()
            
        global score
        score += 1
        
    def test_get_data_passengers_string(self):
        file = CSVTimeSeriesFile('/data/passengers_string.csv')
        data = file.get_data()
        self.assertEqual( len(data), 11)
            
        global score
        score += 1
        
    def test_get_data_passengers_float(self):
        file = CSVTimeSeriesFile('/data/passengers_float.csv')
        data = file.get_data()
        self.assertEqual( len(data), 11)
            
        global score
        score += 1
    
    def test_get_data_passengers_negative(self):
        file = CSVTimeSeriesFile('/data/passengers_negative.csv')
        data = file.get_data()
        self.assertEqual( len(data), 11)
            
        global score
        score += 1
    
    def test_get_data_passengers_zero(self):
        file = CSVTimeSeriesFile('/data/passengers_zero.csv')
        data = file.get_data()
        self.assertEqual( len(data), 11)
            
        global score
        score += 1
        
    def test_get_data_other(self):
        file = CSVTimeSeriesFile('/data/other.csv')
        data = file.get_data()
        self.assertEqual( len(data), 2)
            
        global score
        score += 1

    def test_normal(self):
        time_series = [['2020-01', 100], ['2020-02', 120], ['2021-01', 130], ['2021-02', 140]]
        first_year = '2020' 
        last_year = '2021'
        expected = {'2020-2021': 25.0}
        actual = compute_increments(time_series, first_year, last_year)
        self.assertEqual(expected, actual)
        
        global score
        score += 3
        
    def test_first_last_four_digits(self):
        time_series = [['2020-01', 100], ['2020-02', 120], ['2021-01', 130], ['2021-02', 140]]
        first_year = '2020' 
        last_year = '921'
        with self.assertRaises(ExamException):
            compute_increments(time_series, first_year, last_year)
        
        global score
        score += 1
        
    def test_first_last_not_digits(self):
        time_series = [['2020-01', 100], ['2020-02', 120], ['2021-01', 130], ['2021-02', 140]]
        first_year = '2020' 
        last_year = 'test'
        with self.assertRaises(ExamException):
            compute_increments(time_series, first_year, last_year)
        
        global score
        score += 1

    def test_missing_year(self):
        time_series = [['2020-01', 100], ['2020-02', 120], ['2022-01', 140], ['2022-02', 150]] 
        first_year = '2020'
        last_year = '2022'
        expected = {'2020-2022': 35.0}
        actual = compute_increments(time_series, first_year, last_year)
        self.assertEqual(expected, actual)
        
        global score
        score += 1
        
    def test_missing_years(self):
        time_series = [['2020-01', 100], ['2020-02', 120], ['2023-01', 140], ['2023-02', 150]] 
        first_year = '2020'
        last_year = '2023'
        expected = {'2020-2023': 35.0}
        actual = compute_increments(time_series, first_year, last_year)
        self.assertEqual(expected, actual)
        
        global score
        score += 1

    def test_empty_result(self):
        time_series = [['2020-01', 100], ['2022-01', 120]]
        first_year = '2020'
        last_year = '2021' 
        expected = []
        actual = compute_increments(time_series, first_year, last_year)
        self.assertEqual(expected, actual)
        
        global score
        score += 1

    def test_invalid_years(self):
        time_series = [['2020-01', 100], ['2020-02', 120]]
        first_year = '2019'
        last_year = '2020'
        expected = []
        actual = compute_increments(time_series, first_year, last_year)
        self.assertEqual(expected, actual)
        
        global score
        score += 1

    def test_years_not_in_order(self):
        time_series = [['2020-01', 100], ['2021-02', 120]]
        first_year = '2021'
        last_year = '2020'
        with self.assertRaises(ExamException):
            compute_increments(time_series, first_year, last_year)

        global score
        score += 1

    def test_years_not_in_data(self):
        time_series = [['2020-01', 100], ['2020-02', 120]]
        first_year = '2018'
        last_year = '2020'
        with self.assertRaises(ExamException):
            compute_increments(time_series, first_year, last_year)
            
        global score
        score += 1
        
    def test_missing_first_year(self):
        time_series = [['2020-01', 100], ['2020-02', 120], ['2021-01', 130], ['2021-02', 140]]
        first_year = '2019'
        last_year = '2021'
        with self.assertRaises(ExamException):
            compute_increments(time_series, first_year, last_year)

        global score
        score += 1
    
    def test_holes(self):
        time_series = [['2020-01', 100], ['2022-02', 120], ['2024-01', 130], ['2026-02', 140]]
        first_year = '2020'
        last_year = '2026'
        expected = {'2020-2022': 20.0, '2022-2024': 10.0, '2024-2026': 10.0}
        actual = compute_increments(time_series, first_year, last_year)
        self.assertEqual(expected, actual)
        
        global score
        score += 1
    
    def test_holes_hard(self):
        time_series = [['2020-01', 100], ['2030-02', 120], ['2050-01', 130], ['2051-02', 140]]
        first_year = '2020'
        last_year = '2051'
        expected = {'2020-2030': 20.0, '2030-2050': 10.0, '2050-2051': 10.0}
        actual = compute_increments(time_series, first_year, last_year)
        self.assertEqual(expected, actual)
        
        global score
        score += 1
        
    def test_same_year(self):
        time_series = [['2020-01', 100], ['2020-02', 120], ['2020-01', 130], ['2020-02', 140]]
        first_year = '2020'
        last_year = '2020'
        with self.assertRaises(ExamException):
            compute_increments(time_series, first_year, last_year)
        
        global score
        score += 1
        
    def test_negative_years(self):
        time_series = [['1999-01', 100], ['1999-02', 120], ['2020-01', 130], ['2020-02', 140]]
        first_year = '-999'
        last_year = '2020'
        with self.assertRaises(ExamException):
            compute_increments(time_series, first_year, last_year)
        
        global score
        score += 1

    @classmethod
    def tearDownClass(cls):
        global score
        print('\n\n-------------')
        print('| Voto: {}  |'.format(score))
        print('-------------\n')

# Run the tests
if __name__ == "__main__":
    unittest.main()


#===================================
#  OS shell utility
#===================================

import subprocess
from collections import namedtuple

def sanitize_shell_encoding(text):
    return text.encode("utf-8", errors="ignore").decode("utf-8")


def format_shell_error(stdout, stderr, exit_code):
    
    string  = '\n#---------------------------------'
    string += '\n# Shell exited with exit code {}'.format(exit_code)
    string += '\n#---------------------------------\n'
    string += '\nStandard output: "'
    string += sanitize_shell_encoding(stdout)
    string += '"\n\nStandard error: "'
    string += sanitize_shell_encoding(stderr) +'"\n\n'
    string += '#---------------------------------\n'
    string += '# End Shell output\n'
    string += '#---------------------------------\n'

    return string


def os_shell(command, capture=False, verbose=False, interactive=False, silent=False):
    '''Execute a command in the OS shell. By default prints everything. If the capture switch is set,
    then it returns a namedtuple with stdout, stderr, and exit code.'''
    
    if capture and verbose:
        raise Exception('You cannot ask at the same time for capture and verbose, sorry')

    # Log command
    #logger.debug('Shell executing command: "%s"', command)

    # Execute command in interactive mode    
    if verbose or interactive:
        exit_code = subprocess.call(command, shell=True)
        if exit_code == 0:
            return True
        else:
            return False

    # Execute command getting stdout and stderr
    # http://www.saltycrane.com/blog/2008/09/how-get-stdout-and-stderr-using-python-subprocess-module/
    
    process          = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (stdout, stderr) = process.communicate()
    exit_code        = process.wait()

    # Convert to str (Python 3)
    stdout = stdout.decode(encoding='UTF-8')
    stderr = stderr.decode(encoding='UTF-8')

    # Formatting..
    stdout = stdout[:-1] if (stdout and stdout[-1] == '\n') else stdout
    stderr = stderr[:-1] if (stderr and stderr[-1] == '\n') else stderr

    # Output namedtuple
    Output = namedtuple('Output', 'stdout stderr exit_code')

    if exit_code != 0:
        if capture:
            return Output(stdout, stderr, exit_code)
        else:
            print(format_shell_error(stdout, stderr, exit_code))      
            return False    
    else:
        if capture:
            return Output(stdout, stderr, exit_code)
        elif not silent:
            # Just print stdout and stderr cleanly
            print(stdout)
            print(stderr)
            return True
        else:
            return True