// decorator

class SuperHero {
  constructor(name, power) {
    this.name = name;
    this.power = power;
  }
}

const SuperHeroWithSword = (hero) => {
  hero.sword = true;
  hero.hasSword = () =>
    `${hero.name}'s power is ${hero.power}, and he also has a sword now.`;
  return hero;
};

const SuperHeroWithSuperSpeed = (hero) => {
  hero.superSpeed = true;
  hero.hasSuperSpeed = () =>
    `${hero.name}'s power is ${hero.power}, and he also has the super speed now.`;
  return hero;
};

const SuperHeroWithSpeedandSword = (hero) => {
  hero.speedAndSword = true;
  hero.hasSpeedAndSword = () =>
    `${hero.name}'s power is ${hero.power}, and he also has both super speed and a sword now.`;
  return hero;
};

// var superhero1 = new SuperHero("Fire Man", "Fire");
// console.log(SuperHeroWithSword(superhero1).hasSword());
// console.log(SuperHeroWithSuperSpeed(superhero1).hasSuperSpeed());
// var superhero2 = new SuperHero("Ice Man", "Ice");
// console.log(SuperHeroWithSpeedandSword(superhero2).hasSpeedAndSword());

// facade

class Inventory {
  constructor() {
    this.products = {
      shampoo: 20,
      conditioner: 20,
      hairSerum: 1000,
    };
  }

  checkAvailability({ productName, amount }) {
    return this.products[productName] >= amount;
  }
}

class BuyingProduct extends Inventory {
  buyProduct(product) {
    const isAvailable = this.checkAvailability(product);

    return isAvailable
      ? new BuyProduct().showDetails(product)
      : new PreOrderProduct().showDetails(product);
  }
}

class BuyProduct {
  showDetails({ productName, amount }) {
    console.log(
      `${amount} bottles of ${productName} are available. Click on "buy" to purchase them.`
    );
  }
}

class PreOrderProduct {
  showDetails({ productName, amount }) {
    console.log(
      `${amount} bottles of ${productName} are not available. You can Pre-order them on the next page.`
    );
  }
}

// var customer = new BuyingProduct();
// customer.buyProduct({ productName: "shampoo", amount: 2 });
// customer.buyProduct({ productName: "hair serum", amount: 2000 });

// adapter

// old interface
class TruthAndDare {
  constructor() {
    this.turn = Math.floor(Math.random() * 2) + 1;
  }
  Getturn() {
    if (this.turn == 1) {
      this.turn = 2;
    } else {
      this.turn = 1;
    }
    return this.turn;
  }
  playGame(playerOnename, playerTwoname) {
    if (this.Getturn() == 1) {
      return `${playerOnename}'s turn`;
    } else {
      return `${playerTwoname}'s turn`;
    }
  }
}

// new interface
class NewTruthAndDare {
  constructor(randomValue) {
    this.turn = randomValue;
  }

  newplayGame(playerOnename, playerTwoname) {
    if (this.turn % 2 === 0) {
      return `${playerOnename}'s turn`;
    } else {
      return `${playerTwoname}'s turn`;
    }
  }
}

// Adapter Class
class Adapter {
  constructor(randomValue) {
    const newGame = new NewTruthAndDare(randomValue);

    this.playGame = function (playerOnename, playerTwoname) {
      return newGame.newplayGame(playerOnename, playerTwoname);
    };
  }
}

// const obj = new Adapter(6); //pass even/odd values here to see varying results
// console.log(obj.playGame("Ross", "Chandler"));

// bridge pattern

class Applications {
  constructor(name, type) {
    this.name = name;
    this.type = type;
  }
  setMode(mode) {}
  displayMode() {}
}

class Facebook extends Applications {
  constructor(name, type) {
    super(name, type);
    this.mode = "light";
  }
  setMode(mode) {
    this.mode = mode;
  }
  displayMode() {
    console.log(`You are using facebook in ${this.mode} mode.`);
  }
}

class WhatsApp extends Applications {
  constructor(name, type) {
    super(name, type);
    this.mode = "light";
  }
  setMode(mode) {
    this.mode = mode;
  }
  displayMode() {
    console.log(`You are using whatsapp in ${this.mode} mode.`);
  }
}

class Mode {
  constructor(app) {
    this.app = app;
  }

  darkMode() {
    this.app.setMode("dark");
  }
  lightMode() {
    this.app.setMode("light");
  }
}

// const fb = new Facebook("Facebook", "Social Networking");
// const mode = new Mode(fb);
// mode.darkMode();
// fb.displayMode();

// const whatsapp = new WhatsApp("Whatsapp", "Chatting");
// const mode2 = new Mode(whatsapp);
// mode2.lightMode();
// whatsapp.displayMode();

// composite pattern
class Directory {
  constructor(name, lastModified, size) {
    this.name = name;
    this.lastModified = lastModified;
    this.size = size;
  }
  getLastmodified() {}
  getSize() {}
  getName() {}
}

//Leaf subclass
class File extends Directory {
  constructor(name, lastModified, size) {
    super(name, lastModified, size);
  }

  getLastmodified() {
    console.log(this.lastModified);
    return this.lastModified;
  }

  getSize() {
    console.log(this.size);
    return this.size;
  }

  getName() {
    console.log(this.name);
    return this.name;
  }
}

//Composite subclass
class Folder extends Directory {
  constructor(name, lastModified, size) {
    super(name, lastModified, size);

    this.files = [];
  }

  getSize() {
    return this.files.reduce((x, y) => x + y.size, 0);
  }

  getName() {
    return this.files.map((x) => x.getName());
  }

  getLastmodified() {
    const lastMod = this.files.length
      ? Math.min(...this.files.map((x) => x.getLastmodified()))
      : this.lastModified;
    return lastMod;
  }

  addFile(file) {
    this.files.push(file);
  }

  removeFile(file) {
    this.files = this.files.filter((x) => x !== file);
  }
}

// const file = new File("penguiny.png", 6, 12);
// file.getLastmodified();
// file.getName();
// file.getSize();

// const file2 = new File("penguiny2.png", 4, 8);

// const folder = new Folder("my_dir", 3, 40);
// folder.getSize();
// folder.getLastmodified();
// folder.addFile(file);
// folder.addFile(file2);
// folder.getLastmodified();

// flyweight

class Dress {
  constructor(serialNumber, type, color, designer, availability) {
    this.serialNumber = serialNumber;
    this.type = type;
    this.color = color;
    this.designer = designer;
    this.availability = availability;
    this.price = 0;
  }
  dressPrice() {
    switch (this.type) {
      case "maxi":
        this.price = 1000;
        break;
      case "gown":
        this.price = 2000;
        break;
      case "skirt":
        this.price = 500;
        break;
    }
    return this.price;
  }
}

class DressFactory {
  constructor() {
    this.dressMap = new Map();
  }
  createDress(serialNumber, type, color, designer, availability) {
    const existingDress = this.dressMap.get(serialNumber);
    if (existingDress) {
      return existingDress;
    }
    const dress = new Dress(serialNumber, type, color, designer, availability);
    this.dressMap.set(dress.serialNumber, dress);
    return dress;
  }
}

// const factory = new DressFactory();
// const pinkdress1 = factory.createDress("#123", "skirt", "pink", "Zara", "yes");
// const pinkdress2 = factory.createDress("#123", "skirt", "pink", "Zara", "yes");

// console.log(pinkdress1 === pinkdress2);
// console.log(pinkdress1.dressPrice());
// console.log(pinkdress2.dressPrice());

// proxy

class LibraryKiosk {
  open(app) {
    console.log(`Opening ${app}`);
  }
  connectTo(website) {
    console.log("Connecting to " + website);
  }
}

class ProxyLibraryKiosk {
  constructor() {
    this.kiosk = new LibraryKiosk();

    this.blockedApps = ["camera", "photos", "music", "settings"];
    this.blockedResources = [
      "fb.com",
      "instagram.com",
      "snapchat.com",
      "google.com",
      "gmail.com",
    ];
  }

  open(app) {
    if (this.blockedApps.includes(app)) {
      console.log(`You can't access the ${app}`);
    } else {
      this.kiosk.open(app);
    }
  }

  connectTo(website) {
    if (this.blockedResources.includes(website)) {
      console.log(`Access to ${website} denied`);
    } else {
      this.kiosk.connectTo(website);
    }
  }
}

const libraryKiosk = new ProxyLibraryKiosk();
libraryKiosk.open("photos");
libraryKiosk.open("music");
libraryKiosk.open("Chrome");
libraryKiosk.connectTo("booksportal.com");
libraryKiosk.connectTo("google.com");
libraryKiosk.connectTo("fb.com");
