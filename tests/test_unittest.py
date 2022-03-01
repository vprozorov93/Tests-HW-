import unittest.mock
from secretary import check_document_existance, add_new_doc, delete_doc


class MyTestCase(unittest.TestCase):
    # def setUp(self):
    #     print('setUp')
    #
    # def tearDown(self) -> None:
    #     print('tearDown')

    def test_check_document_existance(self):
        self.assertTrue(check_document_existance('11-2'))
        self.assertFalse(check_document_existance('5'))

    @unittest.mock.patch('builtins.input', side_effect=[1, 2, 3, 4])
    def test_add_new_doc(self, mock_inputs):
        result = add_new_doc()
        self.assertEqual(result, 4)

    @unittest.mock.patch('builtins.input', lambda *args: '11-2')
    def test_delete_doc(self):
        self.assertEqual(delete_doc(), ('11-2', True))

    @unittest.mock.patch('builtins.input', lambda *args: '500')
    def test_delete_doc2(self):
        self.assertEqual(delete_doc(), None)


if __name__ == '__main__':
    unittest.main()
