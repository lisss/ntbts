#include <iostream>
#include <cmath>
#include <numeric>
#include <list>
#include "containers.h"

using namespace std;

double square(double x)
{
    return x * x;
};

double sort(vector<double> &v){};
double sum(const vector<double> &v){};

constexpr double square_2(double x) { return x * x; }

struct Vector0
{
    int size;
    double *elem;
};

class Vector1
{
public:
    Vector1(int s) : elem{new double[s]}, sz{s} {}
    double &operator[](int i) { return elem[i]; }
    int size() { return sz; }

private:
    double *elem;
    int sz;
};

void init_vector(Vector0 &v, int s)
{
    v.elem = new double[s];
    v.size = s;
};

template <typename T>
Vector<T>::Vector(int s)
{
    if (s < 0)
        throw length_error{""};
    elem = new double[s];
    sz = s;

    for (int i = 0; i != s; ++i)
        elem[i] = 0;
}
template <typename T>
Vector<T>::Vector(const Vector &a) : elem{new double[a.sz]}, sz{a.sz}
{
    for (int i = 0; i != sz; ++i)
        elem[i] = a.elem[i];
}
template <typename T>
Vector<T>::Vector(Vector &&a) : elem{new double[a.sz]}, sz{a.sz}
{
    a.elem = nullptr;
    a.sz = 0;
}
template <typename T>
Vector<T>::~Vector() { delete[] elem; } // destructor

template <typename T>
T &Vector<T>::operator[](int i)
{
    if (i < 0 || sz <= i)
        throw out_of_range{"Vector::operator[]"};
    return elem[i];
}

template <typename T>
Vector<T> &Vector<T>::operator=(const Vector &a)
{
    double *p = new double[a.sz];
    for (int i = 0; i != a.sz; ++i)
    {
        p[i] = a.elem[i];
        delete[] elem;
        elem = p;
        sz = a.sz;
        return *this;
    }
}
template <typename T>
int Vector<T>::size() { return sz; }

template <typename T>
T *begin(Vector<T> &v)
{
    return v.size() ? &v[0] : nullptr;
}

template <typename T>
T *end(Vector<T> &v)
{
    return begin(v) + &v.size();
}

class Vector2
{
    double *elem;
    int sz;

public:
    Vector2(initializer_list<double> lst)
        : elem{new double[lst.size()]},
          sz{static_cast<int>(lst.size())}
    {
        copy(lst.begin(), lst.end(), elem);
    }
    void push_back(double v){};
};

class Vector_container : public Container
{
    Vector<double> v;

public:
    Vector_container(int s) : v(s) {}
    ~Vector_container() {}
    double &operator[](int i) { return v[i]; }
    int size() { return v.size(); }
};

class List_container : public Container
{
    list<double> ld;

public:
    List_container(){};
    List_container(initializer_list<double> lst) : ld{lst} {}
    ~List_container(){};

    double &operator[](int i)
    {
        for (auto &x : ld)
        {
            if (i == 0)
                return x;
            --i;
        }
        throw out_of_range("List_container");
    }
    int size() { return ld.size(); }
};

Vector2 read(istream &is)
{
    Vector2 v = {1, 2};

    for (double d; is >> d;)
        v.push_back(d);
    return v;
}

double read_and_sum(int s) // read s integers from cin and return their sum; s is assumed to be positive
{
    Vector0 v;
    init_vector(v, s); // allocate s elements
    for (int i = 0; i != s; ++i)
        cin >> v.elem[i]; // read into elements
    double sum = 0;
    for (int i = 0; i != s; ++i)
        sum += v.elem[i]; // take the sum of the elements
    return sum;
};

double read_and_sum_2(int s) // read s integers from cin and return their sum; s is assumed to be positive
{
    Vector1 v(s);
    for (int i = 0; i != v.size(); ++i)
        cin >> v[i];
    double sum = 0;
    for (int i = 0; i != v.size(); ++i)
        sum += v[i];
    return sum;
};

void f(Vector0 v, Vector0 &rv, Vector0 *pv)
{
    int i1 = v.size;   // access through name
    int i2 = rv.size;  // access through reference
    int i4 = pv->size; // access through pointer
}

enum Type
{
    str,
    num
};

enum class Traffic_light
{
    green,
    yellow,
    red
};

Traffic_light &operator++(Traffic_light &t)
{
    switch (t)
    {
    case Traffic_light::green:
        return t = Traffic_light::yellow;
    case Traffic_light::yellow:
        return t = Traffic_light::red;
    case Traffic_light::red:
        return t = Traffic_light::green;
    }
}

Traffic_light tl = Traffic_light::green;
Traffic_light next = ++tl;

union Value
{
    char *s;
    int i;
};

struct Entry
{
    char *name;
    Type t;
    Value v;
};

void f(Entry *p)
{
    if (p->t == str)
        cout << p->v.s << endl;
    else
        cout << p->v.i << endl;
}

namespace My_code
{
    class complex
    {
        double re, im;

    public:
        complex(double r, double i) : re{r}, im{i} {}
        complex(double r) : re{r}, im{0} {}
        complex() : re{0}, im{0} {}

        double real() const { return re; }
        void real(double r) { re = r; }
        double imag() const { return im; }
        void imag(double i) { im = i; }

        complex &operator+=(complex z)
        {
            re += z.re;
            im += z.im;
        }
        complex &operator-=(complex z)
        {
            re -= z.re;
            im -= z.im;
            return *this;
        }
    };

    complex sqrt(complex){};
    complex operator+(complex a, complex b) { return a += b; }
    int main();
} // namespace My_code

int My_code::main()
{
    complex z{1.2};
    auto z2 = sqrt(z);
    cout << '{' << z2.real() << ',' << z2.imag() << "}\n";
    auto z3 = z + z2;
    return 0;
}

void user(int sz) noexcept
{
    Vector<double> v(sz);
    iota(&v[0], &v[sz], 1);
}

void use(Container &c)
{
    int sz = c.size();

    for (int i = 0; i != sz; ++i)
        cout << typeid(c).name() << ": " << c[i] << endl;
}

class Shape
{
public:
    Shape() {}
    ~Shape(){};
    virtual void draw() = 0;
};

class Smiley : public Shape
{
};

Shape *read_shape(istream &is)
{
}

void check_hier_type()
{
    Shape *ps{read_shape(cin)};
    { // nullptr if ps is not of type Smiley
        if (Smiley *p = dynamic_cast<Smiley *>(ps))
        {
            // call Smiley specific method
        }
    };
    Smiley &r{dynamic_cast<Smiley &>(*ps)}; // bad_cast exception if ps is not of type Smiley
}

// unique_ptr to avoid resourse leaks
unique_ptr<Shape> read_shape_safe(istream &is)
{
}
void use_shape_safe()
{
    // vector<unique_ptr<Shape>> v;
}

void bad_copy(Vector<double>::Vector v1)
{
    Vector<double>::Vector v2 = v1;
    v1[0] = 2; // v2[0] is also 2!
    v2[1] = 3; // v1[1] is also 3!
}

// explicit notion of using default copy & move
class Y
{
public:
    Y(int);
    Y(const Y &) = default;
    Y(Y &&) = default;
};

// explicit notion of no default copy & move
class Y1
{
public:
    Y1(int);
    Y1(const Y &) = delete;
    Y1(Y &&) = delete;
};

class Z
{
public:
    Z(int);
};

Z z1(3);
Z z1{3};
Z z1 = 3;

class Z1
{
public:
    explicit Z1(int);
};

Z1 z1(3);
Z1 z1{3};
// Z1 z1 = 3; // not allowed

vector<thread> my_threads;
Vector<double>::Vector init(int n)
{
    thread t();
    // my_threads.push_back(move(t));

    Vector<double>::Vector vec(n);

    for (int i = 0; i != vec.size(); ++i)
        vec[i] = 777;

    return vec;
}

auto v = init(10000);

void write(Vector<string> &vs)
{
    for (int i = 0; i != vs.size(); ++i)
    {
        cout << vs[i] << endl;
    }
}

void write2(Vector<string> &vs)
{
    for (auto &s : vs)
    {
        cout << s << endl;
    }
}

template <typename T, int N>
struct Buffer
{
    using value_type = T; // type alias
    constexpr int size() { return N; }
    T[N];
};

template <typename Container, typename Value>
Value sum(Container &c, Value v)
{
    for (auto x : c)
        v += x return v
}

void user(Vector<int> &vi, list<double> &ld)
{
    auto x = sum(vi, 0);
    auto d = sum(vi, 0.0);

    double dd = sum(ld, 0.0);
}

// aliases
template <typename C>
using Element_type = C::value_type; // the type of C's elements

template <typename Containter_gen>
void algo(Containter_gen &c)
{
    Vector<Element_type<Containter_gen>> vec;
}

template <typename Key, typename Value>
class Map
{
};

template <typename Value>
using String_map = Map<string, Value>;

String_map<int> m;
// ----

// FUNCTOR
template <typename T>
class Less_than
{
    const T val; // value to compare against

public:
    Less_than(const T &v) : val(v){};
    bool operator()(const T &x) const {return x < val};
};

template <typename C, typename P>
int count(const C &c, P pred)
{
    int cnt = 0;
    for (auto &x : c)
        if (pred(x))
            ++cnt;
    return cnt;
}

void f(const Vector<int> &vec, const list<string> &lst, int x, const string &s)
{
    cout << "number of values less than " << x << ": "
         << count(vec, Less_than{x}) << endl;
    cout << "number of values less than " << s << ": "
         << count(lst, Less_than{s}) << endl;
}

// generating function objects implicitly (lambda expression)
void f(const Vector<int> &vec, const list<string> &lst, int x, const string &s)
{
    cout << "number of values less than " << x << ": "
         << count(vec, [&](int a) { return a < x; }) << endl;
    cout << "number of values less than " << s << ": "
         << count(lst, [&](string &a) { return a < s; }) << endl;
}

// variadic templates
template <typename T, typename... Tail>
void f_var(T head, Tail... tail)
{
    g(head);
    f_var(... tail);
}

int main()
{
    cout << "Hello, world!\n";
    // double num = 1.56;
    // cout << "the square of " << num << " is " << square(num) << "\n";
    cout << "size of char: " << sizeof(char) << "\n";
    cout << "size of int: " << sizeof(int) << "\n";
    cout << "size of double: " << sizeof(double) << "\n";
    cout << "size of uint: " << sizeof(unsigned) << "\n";

    // int a = 2.3;
    // int b = {2.3};
    // cout << a << "\n";
    // cout << b << "\n";

    const int v1 = 42;
    const auto v2 = 42;
    auto v3 = 42;
    constexpr int v4 = v1 * 3;
    const int v5 = v3 * 3;

    // vector<double> &v6 = {1.2,
    //                      3.4};
    // const auto s1 = sum(v6);
    constexpr auto s2 = square_2(v4);

    double *pd = nullptr;

    // cout << "enter numbers" << endl;
    // auto s = read_and_sum(4);
    // cout << "The sum is: " << s << endl;

    Vector1 v(6);
    auto yy = v[4];
    auto ss = v.size();

    Entry e1;
    e1.t = str;
    e1.v.i = 666;
    e1.v.s = "Hell";

    Entry e2;
    e2.t = num;
    e2.v.i = 777;
    e2.v.s = "Sev";

    // f(&e1);
    // f(&e2);

    // My_code::main();

    // user(3);

    static_assert(sizeof(int) >= 4, "int too small");

    Vector_container vc{1};
    use(vc);

    List_container lc{1, 2, 3};
    use(lc);

    Vector<list<int>> vli(45);

    Buffer<char, 1024> bf;

    Less_than lti{42};
    lti(4); // true
}
