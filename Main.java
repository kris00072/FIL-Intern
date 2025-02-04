// Parent class
class Car {
    String brand;
    String model;

    // Constructor of Car
    Car(String brand, String model) {
        this.brand = brand;
        this.model = model;
        System.out.println("Car Constructor: " + brand + " " + model);
    }

    // Method in parent class
    void displayDetails() {
        System.out.println("Brand: " + brand);
        System.out.println("Model: " + model);
    }
}

// Child class inheriting from Car
class SportsCar extends Car {
    int topSpeed;

    // Constructor of SportsCar
    SportsCar(String brand, String model, int topSpeed) {
         // Calls the parent class constructor
        this.topSpeed = topSpeed;
        super(brand, model); 
        System.out.println("SportsCar Constructor: " + brand + " " + model + " with top speed " + topSpeed + " km/h");
    }

    // Overriding method and using super to call parent method
    @Override
    void displayDetails() {
        super.displayDetails();  // Calls the displayDetails() from Car class
        System.out.println("Top Speed: " + topSpeed + " km/h");
    }
}

// Main class to test
public class Main {
    public static void main(String[] args) {
        SportsCar sc = new SportsCar("Porsche", "911", 320);
        sc.displayDetails();
    }
}
