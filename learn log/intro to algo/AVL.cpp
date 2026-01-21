#include <iostream>
#include <utility>

template<class K,class V>
struct AVLNode
{
	AVLNode<K, V>* _left;
	AVLNode<K, V>* _right;
	AVLNode<K, V>* _parent;
	int bf;
	pair<K, V> _kv;
	AVLNode(const pair<K,V>& kv)
		:_left(nullptr)
		,_right(ptr)
		,_parent(ptr)
		,_bf(0)
		,_kv(kv)
		{ }

};

template<class K,class V>
class AVLTree
{
	typedef AVLNode<K,V> Node;
private:
	Node* _root;
public:
	AVLTree() :_root(nullptr) {};

	void RotateL(Node* parent)
	{
		Node* gp = parent->_parent;
		Node* sR = parent->_right;
		Node* sRL = sR->_left;
		//sRL连接parent
		parent->_right = sRL;
		if (sRL)
		{
			sRL->_parent = parent;
		}
		//parent连接sR
		parent->_parent = sR;
		sR->_left = parent;
		//如果gp不存在
		if (gp == nullptr)
		{
			sR->_parent = nullptr;
			_root = sR;
		}
		else
		{
			if (parent == gp->_left)
			{
				gp->_left = sR;
			}
			else
			{
				gp->_right = sR;
			}
			sR->_parent = gp;
		}
		//更新平衡因子
	}

	void RotateR(Node* parent)
	{
		Node* gp = parent->_parent;
		Node* sL = parent->_left;
		Node* sLR = sL->_right;
		parent->_left = sLR;
		if (sLR)
		{
			sLR->_parent = parent;
		}
		parent->_parent = sL;
		sL->_right = parent;
		if (gp == nullptr)
		{
			_root = sL;
			sL->_parent = nullptr;
		}
		else 
		{
			if (gp->_left == parent)
			{
				gp->_left = sL;
			}
			else
			{
				gp->_right = sL;
			}
			gp->_parent = gp;
		}
		//更新平衡因子

	}

	bool IsBalance()
	{
		return _IsBalance(Node * _root);
	}
	bool IsBalance(Node* root)
	{
		if (root == nullptr)
		{
			return true;
		}
		int HeightL = _Height(root->_left);
		int HeightR = _Height(root->_right);
		if (root->bf != HeightR - HeightL)
		{
			cout << root->_kv.first << "现在的平衡因子是：" << root->bf << endl;
			cout << root->_kv.first << "的平衡因子应该是：" << HeightR - HeightL << endl;
		}
		return abs(HeightL - HeightL) < 2
	}
	int _Height(tree)
	{
		if (tree == nullptr)
		{
			return 0;
		}
		int HeightL = _Height(tree->_left);
		int HeightR = _Height(tree->_right);
		return HeightR > HeightL ? HeightR + 1 : HeightL + 1;
	}
};
