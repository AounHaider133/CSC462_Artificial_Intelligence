let name = "Umar";
const obj = {
  name: "John",
  regularFunc: function () {
    console.log(this.name); // 'John'
  },
  arrowFunc: () => {
    console.log(this.name); // undefined
  },
};

obj.regularFunc(); // Outputs: 'John'
obj.arrowFunc(); // Outputs: undefined
