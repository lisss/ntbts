// chain of responsibility
class Employee {
  constructor(name, level) {
    this.name = name;
    this.level = level;
  }
}

class EmployeeChain {
  setNextEmp(handler) {}
  assignWork(emp) {}
  assignWorkInternal(emp, level) {
    if (emp.level === level) {
      console.log(`${level} work assigned to: ${emp.name}`);
    } else {
      this.nextHandler.assignWork(emp);
    }
  }
}

class EasyLevelWorkHandler extends EmployeeChain {
  constructor() {
    super();
    this.nextHandler = new EmployeeChain();
  }

  setNextEmp(handler) {
    this.nextHandler = handler;
  }
  assignWork(emp) {
    this.assignWorkInternal(emp, "Easy");
  }
}

class MediumLevelWorkHandler extends EmployeeChain {
  constructor() {
    super();
    this.nextHandler = new EmployeeChain();
  }

  setNextEmp(handler) {
    this.nextHandler = handler;
  }
  assignWork(emp) {
    this.assignWorkInternal(emp, "Medium");
  }
}

class HardLevelWorkHandler extends EmployeeChain {
  constructor() {
    super();
    this.nextHandler = new EmployeeChain();
  }

  setNextEmp(handler) {
    this.nextHandler = handler;
  }
  assignWork(emp) {
    this.assignWorkInternal(emp, "Hard");
  }
}

// const w1 = new EasyLevelWorkHandler();
// const w2 = new MediumLevelWorkHandler();
// const w3 = new HardLevelWorkHandler();
// w1.setNextEmp(w2);
// w2.setNextEmp(w3);

// const emp1 = new Employee("Joe", "Easy");
// const emp2 = new Employee("Anne", "Medium");
// const emp3 = new Employee("Shawn", "Hard");

// w1.assignWork(emp1);
// w1.assignWork(emp2);
// w1.assignWork(emp3);

// command pattern
class BankAccount {
  constructor(amount) {
    this.amount = amount;
  }

  checkAmount() {
    console.log(this.amount);
  }

  withdrawMoney(withdrawamount) {
    if (withdrawamount > this.amount) {
      console.log("Not enough money");
    } else {
      this.amount -= withdrawamount;
    }
  }
  depositAmount(money) {
    this.amount += money;
  }
}

class Command {
  execute(args) {}
}

class AccountManager {
  request(account, rest) {
    account.execute(rest);
  }
}

class CheckAmount extends Command {
  constructor(account) {
    super();
    this.account = account;
  }

  execute(args) {
    return this.account.checkAmount(args);
  }
}

class WithDrawAmount extends Command {
  constructor(account) {
    super();
    this.account = account;
  }
  execute(args) {
    return this.account.withdrawMoney(args);
  }
}

class DepositAmount extends Command {
  constructor(account) {
    super();
    this.account = account;
  }
  execute(args) {
    return this.account.depositAmount(args);
  }
}

// const manager = new AccountManager();
// const account = new BankAccount(100);
// const check = new CheckAmount(account);
// manager.request(check);
// const withdraw = new WithDrawAmount(account);
// const deposit = new DepositAmount(account);
// manager.request(withdraw, 10);
// manager.request(check);
// manager.request(deposit, 50);
// manager.request(check);

// iterator

class ReverseIterator {
  constructor(elements) {
    this.keys = Object.keys(elements);
    this.index = this.keys.length - 1;
    this.elements = elements;
  }

  hasprevElement() {
    return this.index >= 0;
  }

  last() {
    this.index = this.keys.length - 1;
    return this.elements[this.keys[this.index]];
  }

  previous() {
    if (this.index >= 0) {
      return this.elements[this.keys[--this.index]];
    } else {
      return null;
    }
  }
}

function reverseIterate(items) {
  const iter = new ReverseIterator(items);

  for (let i = iter.last(); iter.hasprevElement(); i = iter.previous()) {
    console.log(i);
  }
}

// reverseIterate({
//   name: "Anne",
//   age: "23",
//   gender: "Female",
//   Occupation: "Engineer",
// });

// mediator

class HR {
  constructor() {
    this.employees = [];
  }

  registerEmployee(employee) {
    this.employees[employee.name] = employee;
  }

  scheduleRaise(raise, worker, manager) {
    manager.receiveMessage(worker, raise);
    const approved = manager.finalizeRaise(worker, raise);
    if (approved) {
      worker.receiveRaise(raise);
    }
  }
}

class Employee1 {
  constructor(hr, name, position, pay) {
    this.hr = hr;
    this.name = name;
    this.position = position;
    this.pay = pay;
  }
}

class Manager extends Employee1 {
  constructor(hr, name, position, pay) {
    super(hr, name, position, pay);
    this.hr.registerEmployee(this);
  }
  receiveMessage(worker, raise) {
    console.log(`${worker.name} should get ${raise} dollar raise`);
  }
  finalizeRaise(worker, raise) {
    console.log(`${worker.name}'s ${raise} dollar raise is approved`);
    return true;
  }
}

class Worker extends Employee1 {
  constructor(hr, name, position, pay) {
    super(hr, name, position, pay);
    this.hr.registerEmployee(this);
  }
  receiveRaise(raise) {
    this.pay += raise;
    console.log(`My new pay is ${this.pay} dollars`);
  }
}

// const hr = new HR();
// const employee = new Worker(hr, "Joe", "Developer", 1400);
// const manager = new Manager(hr, "Allen", "Team Lead", 3000);
// hr.scheduleRaise(200, employee, manager);

// observer

class Auctioneer {
  constructor() {
    this.bidders = [];
  }
  registerBidder(bidder) {
    this.bidders.push(bidder);
  }
  announceNewBidderPrice() {
    this.notifyBidders();
  }
  notifyBidders() {
    this.bidders.forEach((b) => b.update());
  }
}

class Bidder {
  constructor(name) {
    this.name = name;
    this.bidPrice = null;
  }
  update() {
    console.log(`${this.name} is offering ${this.bidPrice} dollars`);
    if (this.bidPrice > 500) {
      console.log(`Sold to ${this.name}`);
    }
  }
  giveNewPrice(price) {
    this.bidPrice = price;
  }
}

// const auctioner = new Auctioneer();
// const bidder1 = new Bidder("Ross");
// auctioner.registerBidder(bidder1);
// const bidder2 = new Bidder("Joey");
// auctioner.registerBidder(bidder2);
// bidder1.giveNewPrice(200);
// bidder2.giveNewPrice(350);
// auctioner.announceNewBidderPrice();
// bidder1.giveNewPrice(400);
// bidder2.giveNewPrice(550);
// auctioner.announceNewBidderPrice();

// visitor
class RockMusicVisitor {
  visit(musicLibrary) {
    return musicLibrary.songs
      .filter((x) => x.genre === "Rock")
      .map((x) => x.name);
  }
}

class Song {
  constructor(name, genre) {
    this.name = name;
    this.genre = genre;
  }
  getName() {
    return this.name;
  }
  getGenre() {
    return this.genre;
  }
}

class MusicLibrary {
  constructor() {
    this.songs = [];
  }
  addSong(song) {
    this.songs.push(song);
  }
  accept(visitor) {
    return visitor.visit(this);
  }
}

const rockMusicVisitor = new RockMusicVisitor();
const song1 = new Song("Bohemian Rhapsody", "Rock");
const song2 = new Song("Stairway to Heaven", "Rock");
const song3 = new Song("Oops I did it again", "Pop");
const song4 = new Song("Crazy", "Country");
const musicLibrary = new MusicLibrary();
musicLibrary.addSong(song1);
musicLibrary.addSong(song2);
musicLibrary.addSong(song3);
musicLibrary.addSong(song4);
console.log(musicLibrary.accept(rockMusicVisitor));
