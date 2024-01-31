datalogger.onLogFull(function () {
    start = 0
})
let start = 0
let num = 1
let num2 = 1
datalogger.deleteLog()
datalogger.mirrorToSerial(true)
start = 1
basic.forever(function () {
    while (0 == Math.sqrt(num2) - Math.round(Math.sqrt(num2))) {
    	
    }
})
basic.forever(function () {
    if (start == 1) {
        let Páratlanszám: number[] = []
        let Négyzetszám: number[] = []
        Négyzetszám.push(num * num)
        Páratlanszám.push(num2)
        datalogger.log(datalogger.createCV("Négyzetszám", num * num))
        datalogger.log(datalogger.createCV("Páratlanszám", num2))
        num += 1
        num2 += 2
        basic.pause(200)
    }
})
