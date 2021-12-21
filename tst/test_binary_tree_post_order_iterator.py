import unittest
from binary_tree_post_order_iterator import TreeNode, PostOrderIterator


class MyTestCase(unittest.TestCase):
    def test_iterator_with_all_left_not_none(self):
        n1 = TreeNode(1)
        n2 = TreeNode(2)
        n3 = TreeNode(3)
        n4 = TreeNode(4)
        n5 = TreeNode(5)
        n6 = TreeNode(6)

        n1.left = n2
        n1.right = n3
        n2.left = n4
        n2.right = n5
        n3.left = n6

        itr = PostOrderIterator(n1)
        for expected_vals in [4, 5, 2, 6, 3, 1]:
            self.assertTrue(itr.hasNext())
            self.assertEqual(itr.next(), expected_vals)
        self.assertFalse(itr.hasNext())

    def test_iterator_with_all_left_is_none(self):
        n1 = TreeNode(1)
        n2 = TreeNode(2)
        n3 = TreeNode(3)
        n4 = TreeNode(4)
        n5 = TreeNode(5)
        n6 = TreeNode(6)

        n1.left = n2
        n1.right = n3
        n2.left = n4
        n2.right = n5
        n3.right = n6

        itr = PostOrderIterator(n1)
        for expected_vals in [4, 5, 2, 6, 3, 1]:
            self.assertTrue(itr.hasNext())
            self.assertEqual(itr.next(), expected_vals)
        self.assertFalse(itr.hasNext())


if __name__ == '__main__':
    unittest.main()
