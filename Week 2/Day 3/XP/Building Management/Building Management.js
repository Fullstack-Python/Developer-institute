let building = {
    numberOfFloors : 4,
    numberOfAptByFloor : {
        firstFloor : 3,
        secondFloor : 4,
        thirdFloor : 9,
        fourthFloor : 2,
    },
    nameOfTenants : ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan :  [4, 1000],
        david : [1, 500],
    },
}
    console.log(building.numberOfFloors);
    let numberOfAptByFloor = {
        firstFloor : 3,
        secondFloor : 4,
        thirdFloor : 9,
        fourthFloor : 2,
    };
    console.log(numberOfAptByFloor.firstFloor + numberOfAptByFloor.thirdFloor);
    let nameOfTenants = ["Sarah", "Dan", "David"];
    let numberOfRoomsAndRent = {
        sarah: [3, 990],
        dan :  [4, 1000],
        david : [1, 500],
    };
    console.log(nameOfTenants[1]+` ${numberOfRoomsAndRent.dan[0]}`);

        if(numberOfRoomsAndRent.sarah[1]+numberOfRoomsAndRent.david[1] > numberOfRoomsAndRent.dan[1]){
            console.log(numberOfRoomsAndRent.dan[1]+1200)
            } else {
                console.log(numberOfRoomsAndRent.dan[1])
            }
