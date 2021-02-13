class Container
{
public:
    virtual double &operator[](int) = 0;
    virtual int size() = 0;
    virtual ~Container() {}
};

class Vector
{
public:
    Vector(int s);
    ~Vector();
    double &operator[](int i);
    int size();

private:
    double *elem;
    int sz;
};
