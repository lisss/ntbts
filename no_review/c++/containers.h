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
    Vector(const Vector &a); // copy constructor
    Vector(Vector &&a);      // move constructor
    ~Vector();
    double &operator[](int i);
    const double &operator[](int i) const;
    Vector &operator=(const Vector &a); // copy assignment
    Vector &operator=(Vector &&a);      // move assignment
    int size();

private:
    double *elem;
    int sz;
};
