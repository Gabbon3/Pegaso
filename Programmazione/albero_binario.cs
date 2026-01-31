public class Main
{
    public static void Main(string[] args)
    {
        int input = -1;
        int tree = new BinaryTree();
        while (input > 0)
        {
            input = (int)Console.ReadLine("Inserisci un numero da mettere nell'albero");
            tree.Insert();
        }
    }
}

public class Node
{
    public int Value;
    public Node Left;
    public Node Right;

    public Node(int value)
    {
        Value = value;
        Left = null;
        Right = null;
    }
}

public class BinaryTree
{
    public Node Root;

    public void Insert(int value)
    {
        if (Root == null)
        {
            Root = new Node(value);
        }
        else
        {
            InsertRecursive(Root, value);
        }
    }

    private void InsertRecursive(Node current, int value)
    {
        if (value < current.Value)
        {
            if (current.Left == null)
            {
                current.Left = new Node(value);
            }
            else
            {
                InsertRecursive(current.Left, value);
            }
        }
        else
        {
            if (current.Right == null)
            {
                current.Right = new Node(value);
            }
            else
            {
                InsertRecursive(current.Right, value);
            }
        }
    }

    /// <summary>
    /// Restituisce la profondità massima dell'albero
    /// </summary>
    /// <returns></returns>
    public int Deep()
    {
        int leftDeep = Root.Left == null ? 0 : DeepRecursive(Root.Left);
        int rightDeep = Root.Right == null ? 0 : DeepRecursive(Root.Right);
        return leftDeep > rightDeep ? leftDeep : rightDeep;
    }

    private int DeepRecursive(Node current)
    {
        int leftDeep = current.Left == null ? 0 : DeepRecursive(current.Left);
        int rightDeep = current.Right == null ? 0 : DeepRecursive(current.Right);
        return (leftDeep > rightDeep ? leftDeep : rightDeep) + 1;
    }
}