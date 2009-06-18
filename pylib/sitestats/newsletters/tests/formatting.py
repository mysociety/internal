import unittest
from sitestats.newsletters import formatting

class FormattingTests(unittest.TestCase):
    
    def testFormatHTMLCellValueWithLink(self):
        info = {'link'           : 'http://test.host', 
                'current_value'  : '34',
                'percent_change' : '+12%', 
                'unit'           : 's'}
        formatted = formatting.format_cell_value('html', info)
        expected_formatted  = "<a href='http://test.host'>34s</a> (+12%)"
        self.assertEqual(expected_formatted, formatted, 'format_cell_value formats html example with units and link correctly')
      
     
    def testFormatHTMLCellValueWithoutLink(self):
        info = {'current_value'  : '34', 
                'percent_change' : '-3%', 
                'unit'           : '%'}
        formatted = formatting.format_cell_value('html', info)
        expected_formatted = "34% (-3%)"
        self.assertEqual(expected_formatted, formatted, 'format_cell_value formats html example without link correctly')  

    def testFormatTextCellValue(self):
        info = {'link'           : 'http://test.host', 
                'current_value'  : '34',
                'percent_change' : '+12%', 
                'unit'           : 's'}
        formatted = formatting.format_cell_value('text', info)
        expected_formatted  = "34s (+12%)"    
        self.assertEqual(expected_formatted, formatted, 'format_cell_value formats text example without link correctly')
        
def main():

    unittest.main()

if __name__ == '__main__':
    main()