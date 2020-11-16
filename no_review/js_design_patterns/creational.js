// factory pattern

function ToyFactory() {
  this.toy = ToyDuck;
  this.createToy = ({ toyType, color, price, name }) => {
    switch (toyType) {
      case "car":
        this.toy = ToyCar;
        break;
      case "duck":
        this.toy = ToyDuck;
        break;
    }
    return new this.toy({ toyType, color, price, name });
  };
}

function ToyDuck({ color, price }) {
  this.color = color;
  this.price = price;
}

function ToyCar({ color, price, name }) {
  this.color = color;
  this.price = price;
  this.name = name;
}

const toyFact = new ToyFactory();
const car = toyFact.createToy({
  toyType: "car",
  name: "honda",
  color: "blue",
  price: 40,
});

const duck = toyFact.createToy({
  toyType: "duck",
  color: "red",
  price: 4,
});

// builder pattern

class Assignment {
  constructor() {
    this.make = (builder) => {
      builder.step1();
      builder.step2();
      builder.step3();
      builder.step4();
      return builder.get();
    };
  }
}

class AssignmentBuilder {
  constructor(subject, level, dueDate) {
    this.unit = null;

    this.step1 = () => (this.unit = new AssignmentUnit());
    this.step2 = () => this.unit.addSubject(subject);
    this.step3 = () => this.unit.addLevel(level);
    this.step4 = () => this.unit.addDueDate(dueDate);

    this.get = () => {
      return this.unit;
    };
  }
}

class AssignmentUnit {
  constructor() {
    this.subject = null;
    this.level = null;
    this.dueDate = null;

    this.addSubject = (subj) => {
      this.subject = subj;
    };
    this.addLevel = (level) => (this.level = level);
    this.addDueDate = (date) => (this.dueDate = date);

    this.announcement = () => {
      console.log(
        `Your ${this.subject} assignment's difficulty level is: ${this.level}. It is due on ${this.dueDate}.`
      );
    };
  }
}

// const assignment = new Assignment();
// const assignmentBuilder = new AssignmentBuilder(
//   "Math",
//   "Hard",
//   "12th June, 2020"
// );
// const mathAssignment = assignment.make(assignmentBuilder);
// mathAssignment.announcement();

// prototype pattern

class Ninja {
  constructor(name) {
    this.name = name;
    this.points = 100;
  }
}

Ninja.prototype.punch = function (ninja) {
  if (this.points && ninja.points) {
    ninja.points -= 20;
    return `${ninja.name}'s points are ${ninja.points}`;
  } else {
    return `Can't punch ${ninja.name}`;
  }
};

Ninja.prototype.kick = function (ninja) {
  if (this.points && ninja.points) {
    ninja.points -= 50;
    return `${ninja.name}'s points are ${ninja.points}`;
  } else {
    return `Can't kick ${ninja.name}`;
  }
};

const ninja1 = new Ninja("Ninja1");
const ninja2 = new Ninja("Ninja2");

ninja1.kick(ninja2);
ninja2.punch(ninja1);
ninja1.kick(ninja2);
ninja1.punch(ninja2);
ninja2.kick(ninja1);

// abstract pattern

const calculateInterest = (amount, interest, duration) =>
  amount * interest * duration;

class HomeLoan {
  constructor({ amount, duration }) {
    this.amount = amount;
    this.duration = duration;
    this.interest = 0.08;
    this.calculateInterest = () =>
      calculateInterest(amount, this.interest, duration);
  }
}

class StudentLoan {
  constructor({ amount, duration }) {
    this.amount = amount;
    this.duration = duration;
    this.interest = 0.03;
    this.calculateInterest = () =>
      calculateInterest(amount, this.interest, duration);
  }
}

class PersonalLoan {
  constructor({ amount, duration }) {
    this.amount = amount;
    this.duration = duration;
    this.interest = 0.05;
    this.calculateInterest = () =>
      calculateInterest(amount, this.interest, duration);
  }
}

class Loans {
  constructor() {
    this.getloan = (type, amount, duration) => {
      switch (type) {
        case "home":
          return new HomeLoan({ amount, duration });
        case "student":
          return new StudentLoan({ amount, duration });
        case "personal":
          return new PersonalLoan({ amount, duration });
      }
    };
  }
}

// const loan = new Loans();

// const homeLoan = loan.getloan("home", 3200, 5);
// homeLoan.calculateInterest();

// const studentLoan = loan.getloan("student", 1800, 4);
// studentLoan.calculateInterest();

// const personalLoan = loan.getloan("personal", 1200, 2);
// personalLoan.calculateInterest();
