// MVC
class ShoppingCartModel {
  constructor(itemNumber, itemName, itemQuantity, itemPrice) {
    this.itemNumber = itemNumber;
    this.itemName = itemName;
    this.itemQuantity = itemQuantity;
    this.itemPrice = itemPrice;
  }

  getItemNumber() {
    return this.itemNumber;
  }
  getItemName() {
    return this.itemName;
  }
  getItemQuantity() {
    return this.itemQuantity;
  }
  setItemQuantity(qty) {
    this.itemQuantity = qty;
  }
  getItemPrice() {
    return this.itemPrice;
  }
}

class ShoppingCartView {
  constructor() {
    this.controller = null;
  }
  registerWith(controller) {
    this.controller = controller;
    this.controller.addView(this);
  }

  displayItem({ itemNumber, itemName, itemQuantity, itemPrice }) {
    console.log(
      `Item Number: ${itemNumber}\nItem: ${itemName}\nQuantity: ${itemQuantity}\nPrice: ${itemPrice}`
    );
  }

  buyItem(name, quantity, price) {
    this.controller.buyItem(name, quantity, price);
  }

  changeItemQuantity(itemNumber, newQuantity) {
    this.controller.changeItemQuantity(itemNumber, newQuantity);
  }
}

class ShoppingCartController {
  constructor() {
    this.itemNum = 0;
    this.model = null;
    this.view = null;
    this.itemList = [];
  }

  addView(view) {
    this.view = view;
  }
  addModel(model) {
    this.itemList.push(model);
  }

  buyItem(name, quantity, price) {
    this.addModel(new ShoppingCartModel(this.itemNum, name, quantity, price));
    this.itemNum += 1;
    this.updateView();
  }

  changeItemQuantity(itemNumber, newQuantity) {
    const item = this.itemList.find((x) => x.itemNumber === itemNumber);
    if (item) {
      item.setItemQuantity(newQuantity);
      this.updateView();
    }
  }

  updateView() {
    this.itemList.forEach((it) => this.view.displayItem(it));
  }
}

// const view = new ShoppingCartView();
// const controller = new ShoppingCartController();
// view.registerWith(controller);
// view.buyItem("Popcorn", 3, 2.5);
// view.buyItem("Soap", 5, 10.0);
// view.changeItemQuantity(0, 6);

// MVP
class Model {
  constructor() {
    this.sender = "";
    this.reciever = "";
    this.emailTitle = "";
  }

  setSender(sender) {
    this.sender = sender;
  }
  setReciever(recever) {
    this.recever = recever;
  }
  setEmailTitle(emailTitle) {
    this.emailTitle = emailTitle;
  }

  getSender() {
    return this.sender;
  }
  getReciever() {
    return this.recever;
  }
  getEmailTitle() {
    return this.emailTitle;
  }
}

class View {
  constructor() {
    this.presenter = null;
  }

  registerWith(presenter) {
    this.presenter = presenter;
  }

  sendEmail(to, fromWhom, emailTitle) {
    this.presenter.sendEmail(to, fromWhom, emailTitle);
  }

  displayEmailInfo(senderName, recieverName, emailTitle) {
    console.log(
      "Email From: " +
        senderName +
        " To: " +
        recieverName +
        " Title: " +
        emailTitle
    );
  }
}

class Presenter {
  constructor(view) {
    this.view = view;
    this.model = null;
  }

  setModel(model) {
    this.model = model;
  }

  getView() {
    return this.view;
  }

  sendEmail(to, fromWhom, emailTitle) {
    this.model.setSender(fromWhom);
    this.model.setReciever(to);
    this.model.setEmailTitle(emailTitle);
    this.view.displayEmailInfo(
      this.model.getSender(),
      this.model.getReciever(),
      this.model.getEmailTitle()
    );
  }
}

// const model = new Model();
// const view = new View();
// const presenter = new Presenter(view);
// presenter.setModel(model);
// view.registerWith(presenter);
// presenter.getView().sendEmail("Rachel", "Joey", "Rent Discussion");
// presenter.getView().sendEmail("Monica", "Phoebe", "Smelly Cat Draft");

// MVVM
class Model {
  constructor() {
    this.model = { color: "red" };
    this.observers = [];
  }
  subscribe(observer) {
    this.observers.push(observer);
  }

  notifyObservers(attrNm, newVal) {
    this.observers.forEach((obs) => obs(attrNm, newVal));
  }

  getValue(key) {
    return this.model[key];
  }

  setValue(key, value) {
    this.model[key] = value;
    this.notifyObservers(key, value);
  }
}

class ViewModel {
  constructor(model) {
    this.bind = (viewElement, modelElement) => {
      viewElement.style.color = model.getValue(modelElement);

      model.subscribe((attrNm, newVal) => {
        const elem = document.getElementById(attrNm);
        if (newVal === "green") {
          elem.style.color = "red";
        } else if (newVal === "red") {
          elem.style.color = "blue";
        } else {
          elem.style.color = "green";
        }
      });
      viewElement.addEventListener("input", () => {
        model.setValue(viewElement.name, viewElement.value);
      });
    };
  }
}

{
  /* <html>
	<head>
	</head>
	<body>
		Color: <input type="text" name = "color" id="color">
	</body>
</html> */
}

const colorInput = document.getElementById("color");
const model = new Model();
const viewModel = new ViewModel(model);
viewModel.bind(colorInput, "color");
