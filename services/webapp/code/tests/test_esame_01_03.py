import unittest

from esame import CSVTimeSeriesFile, find_min_max, ExamException

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
        time_series = [['2012-01', 100], ['2012-02', 120], ['2012-03', 140], ['2012-04', 150], ['2012-05', 160], ['2012-06', 170], ['2012-07', 180], ['2012-08', 190], ['2012-09', 200], ['2012-10', 210], ['2012-11', 220], ['2012-12', 230]]
        
        expected = {'2012' : {'min' : ['01'], 'max' : ['12']}}
        actual = find_min_max(time_series)
        self.assertEqual(expected, actual)
        
        global score
        score += 10

    def test_empty_result(self):
        time_series = []
        expected = {}
        actual = find_min_max(time_series)
        self.assertEqual(expected, actual)
        
        global score
        score += 1
        
    def test_multiple_years(self):
        time_series = [['2012-01', 100], ['2012-02', 120], ['2012-03', 140], ['2012-04', 150], ['2012-05', 160], ['2012-06', 170], ['2012-07', 180], ['2012-08', 190], ['2012-09', 200], ['2012-10', 210], ['2012-11', 220], ['2012-12', 230], ['2013-01', 100], ['2013-02', 120], ['2013-03', 140], ['2013-04', 150], ['2013-05', 160], ['2013-06', 170], ['2013-07', 180], ['2013-08', 190], ['2013-09', 200], ['2013-10', 210], ['2013-11', 220], ['2013-12', 230]]
        
        expected = {'2012' : {'min' : ['01'], 'max' : ['12']}, '2013' : {'min' : ['01'], 'max' : ['12']}}
        actual = find_min_max(time_series)
        self.assertEqual(expected, actual)
        
        global score
        score += 1
        
    def test_multiple_min_and_max(self):
        time_series = [['1999-01', 1], ['1999-02', 1], ['1999-03', 1], ['1999-04', 2], ['1999-05', 1], ['1999-06', 4], ['1999-07', 3], ['1999-08', 3], ['1999-09', 1], ['1999-10', 4], ['1999-11', 4], ['1999-12', 4]]
        
        expected = {'1999' : {'min' : ['01', '02', '03', '05', '09'], 'max' : ['06', '10', '11', '12']}}
        actual = find_min_max(time_series)
        self.assertEqual(expected, actual)
        
        global score
        score += 2
        
    def test_only_one_month(self):
        time_series = [['1999-01', 1], ['1999-02', 1], ['2000-01', 1]]
        expected = {'1999' : {'min' : ['01', '02'], 'max' : ['01', '02']}, '2000' : {}}
        actual = find_min_max(time_series)
        self.assertEqual(expected, actual)

        global score
        score += 2
        
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