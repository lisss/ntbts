class Container
{
public:
    virtual double &operator[](int) = 0;
    virtual int size() = 0;
    virtual ~Container() {}
};

template <typename T>
class Container_gen
{
public:
    using value_type = T;
    virtual T &operator[](int) = 0;
    virtual int size() = 0;
    virtual ~Container_gen() {}
};

template <typename T>
class Vector
{
public:
    Vector(int s);
    Vector(const Vector &a); // copy constructor
    Vector(Vector &&a);      // move constructor
    ~Vector();
    T &operator[](int i);
    const T &operator[](int i) const;
    Vector &operator=(const Vector &a); // copy assignment
    Vector &operator=(Vector &&a);      // move assignment
    int size();

private:
    T *elem;
    int sz;
};
