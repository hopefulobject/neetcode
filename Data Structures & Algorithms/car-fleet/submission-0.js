class Solution {
    /**
     * @param {number} target
     * @param {number[]} position
     * @param {number[]} speed
     * @return {number}
     */
    carFleet(target, position, speed) {
        let cars = [];
        for (let i = 0; i< position.length; i++) {
            cars.push([position[i], speed[i]]);
        }
        cars = cars.sort((a,b) => b[0]-a[0]); // O(nlogn) in classical computers
        let fleets = 1;

        function will_meet(car1,car2) {
            return (target - car2[0])/car2[1] <= (target - car1[0])/car1[1]
            }
        let check = cars[0];
        for (let i = 1; i<cars.length; i++) {
            if (!will_meet(check, cars[i])) {
                check = cars[i]; 
                fleets++;
            }

        }

        return fleets;


    }
}
