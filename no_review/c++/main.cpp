#include <iostream>
#include <cmath>
#include <numeric>
#include "Vector.h"

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

Vector::Vector(int s)
{
    if (s < 0)
        throw length_error{""};
    elem = new double[s];
    sz = s;

    for (int i = 0; i != s; ++i)
        elem[i] = 0;
}
Vector::~Vector() { delete[] elem; } // destructor

double &Vector::operator[](int i)
{
    if (i < 0 || sz <= i)
        throw out_of_range{"Vector::operator[]"};
    return elem[i];
}
int Vector::size() { return sz; }

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
}

void user(int sz) noexcept
{
    Vector v(sz);
    iota(&v[0], &v[sz], 1);
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

    user(3);

    static_assert(sizeof(int) >= 4, "int too small");
}
